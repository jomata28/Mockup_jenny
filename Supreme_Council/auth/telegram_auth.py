#!/usr/bin/env python3
"""
Telegram PIN Authentication Module
For Supreme AI Council agent security

This module provides PIN-based authentication for Telegram bot interactions.
Each user must authenticate with a PIN before agents respond.
"""

import os
import time
import hashlib
import json
from datetime import datetime, timedelta
from typing import Optional, Dict
from dataclasses import dataclass, asdict


@dataclass
class Session:
    """Represents an authenticated session"""
    user_id: int
    chat_id: int
    authenticated_at: datetime
    expires_at: datetime
    agent: Optional[str] = None

    def is_expired(self) -> bool:
        """Check if session has expired"""
        return datetime.now() > self.expires_at

    def extend(self, hours: int = 2):
        """Extend session expiration"""
        self.expires_at = datetime.now() + timedelta(hours=hours)


class TelegramAuth:
    """
    Handles PIN-based authentication for Telegram interactions

    Features:
    - PIN verification with rate limiting
    - Session management (2-hour timeout)
    - Failed attempt tracking and lockout
    - Per-agent PINs (optional)
    - Security event logging
    """

    def __init__(
        self,
        pin_hash: str,
        session_timeout_hours: int = 2,
        max_attempts: int = 3,
        lockout_duration_minutes: int = 60,
        session_file: str = "/tmp/council_sessions.json"
    ):
        """
        Initialize authentication system

        Args:
            pin_hash: SHA-256 hash of the user's PIN
            session_timeout_hours: Hours until session expires
            max_attempts: Failed attempts before lockout
            lockout_duration_minutes: Minutes of lockout after max attempts
            session_file: Path to store session data
        """
        self.pin_hash = pin_hash
        self.session_timeout_hours = session_timeout_hours
        self.max_attempts = max_attempts
        self.lockout_duration = timedelta(minutes=lockout_duration_minutes)
        self.session_file = session_file

        # In-memory session storage
        self.sessions: Dict[int, Session] = {}

        # Failed attempt tracking: {user_id: (count, lockout_until)}
        self.failed_attempts: Dict[int, tuple[int, Optional[datetime]]] = {}

        # Load existing sessions if file exists
        self._load_sessions()

    @staticmethod
    def hash_pin(pin: str) -> str:
        """
        Generate SHA-256 hash of PIN

        Args:
            pin: 4-digit PIN string

        Returns:
            Hexadecimal hash string
        """
        return hashlib.sha256(pin.encode()).hexdigest()

    def verify_pin(self, pin: str) -> bool:
        """
        Verify if provided PIN matches stored hash

        Args:
            pin: PIN to verify

        Returns:
            True if PIN is correct
        """
        return self.hash_pin(pin) == self.pin_hash

    def is_locked_out(self, user_id: int) -> tuple[bool, Optional[int]]:
        """
        Check if user is currently locked out

        Args:
            user_id: Telegram user ID

        Returns:
            Tuple of (is_locked_out, minutes_remaining)
        """
        if user_id not in self.failed_attempts:
            return False, None

        attempts, lockout_until = self.failed_attempts[user_id]

        if lockout_until and datetime.now() < lockout_until:
            remaining = (lockout_until - datetime.now()).total_seconds() / 60
            return True, int(remaining)

        # Lockout expired, reset
        if lockout_until:
            self.failed_attempts[user_id] = (0, None)

        return False, None

    def record_failed_attempt(self, user_id: int):
        """
        Record a failed authentication attempt

        Args:
            user_id: Telegram user ID
        """
        if user_id not in self.failed_attempts:
            self.failed_attempts[user_id] = (1, None)
        else:
            attempts, _ = self.failed_attempts[user_id]
            new_attempts = attempts + 1

            if new_attempts >= self.max_attempts:
                # Trigger lockout
                lockout_until = datetime.now() + self.lockout_duration
                self.failed_attempts[user_id] = (new_attempts, lockout_until)
                self._log_security_event(
                    user_id=user_id,
                    event="lockout_triggered",
                    details=f"{new_attempts} failed attempts"
                )
            else:
                self.failed_attempts[user_id] = (new_attempts, None)

    def reset_failed_attempts(self, user_id: int):
        """Reset failed attempts counter for user"""
        if user_id in self.failed_attempts:
            del self.failed_attempts[user_id]

    def authenticate(
        self,
        user_id: int,
        chat_id: int,
        pin: str,
        agent: Optional[str] = None
    ) -> tuple[bool, str]:
        """
        Authenticate user with PIN

        Args:
            user_id: Telegram user ID
            chat_id: Telegram chat ID
            pin: User-provided PIN
            agent: Optional agent name for agent-specific PINs

        Returns:
            Tuple of (success, message)
        """
        # Check if locked out
        is_locked, minutes_remaining = self.is_locked_out(user_id)
        if is_locked:
            return False, f"🔒 Account locked due to failed attempts. Try again in {minutes_remaining} minutes."

        # Verify PIN
        if not self.verify_pin(pin):
            self.record_failed_attempt(user_id)
            attempts_left = self.max_attempts - self.failed_attempts[user_id][0]

            self._log_security_event(
                user_id=user_id,
                event="failed_authentication",
                details=f"Attempts left: {attempts_left}"
            )

            if attempts_left > 0:
                return False, f"❌ Incorrect PIN. {attempts_left} attempts remaining."
            else:
                return False, f"🔒 Account locked for {self.lockout_duration.total_seconds() / 60} minutes."

        # PIN correct - create session
        self.reset_failed_attempts(user_id)

        session = Session(
            user_id=user_id,
            chat_id=chat_id,
            authenticated_at=datetime.now(),
            expires_at=datetime.now() + timedelta(hours=self.session_timeout_hours),
            agent=agent
        )

        self.sessions[user_id] = session
        self._save_sessions()

        self._log_security_event(
            user_id=user_id,
            event="authentication_success",
            details=f"Agent: {agent or 'general'}"
        )

        return True, f"✅ Authenticated. Session expires in {self.session_timeout_hours} hours."

    def is_authenticated(self, user_id: int, agent: Optional[str] = None) -> bool:
        """
        Check if user has valid session

        Args:
            user_id: Telegram user ID
            agent: Optional agent name to check agent-specific session

        Returns:
            True if user has valid, non-expired session
        """
        if user_id not in self.sessions:
            return False

        session = self.sessions[user_id]

        # Check expiration
        if session.is_expired():
            del self.sessions[user_id]
            self._save_sessions()
            return False

        # Check agent-specific session if specified
        if agent and session.agent and session.agent != agent:
            return False

        return True

    def get_session(self, user_id: int) -> Optional[Session]:
        """Get user's current session if it exists and is valid"""
        if self.is_authenticated(user_id):
            return self.sessions[user_id]
        return None

    def extend_session(self, user_id: int):
        """Extend user's session expiration"""
        if user_id in self.sessions:
            self.sessions[user_id].extend(self.session_timeout_hours)
            self._save_sessions()

    def logout(self, user_id: int):
        """End user's session"""
        if user_id in self.sessions:
            del self.sessions[user_id]
            self._save_sessions()
            self._log_security_event(
                user_id=user_id,
                event="logout",
                details="Session ended by user"
            )

    def _save_sessions(self):
        """Persist sessions to disk"""
        try:
            session_data = {
                str(user_id): {
                    'user_id': session.user_id,
                    'chat_id': session.chat_id,
                    'authenticated_at': session.authenticated_at.isoformat(),
                    'expires_at': session.expires_at.isoformat(),
                    'agent': session.agent
                }
                for user_id, session in self.sessions.items()
            }

            with open(self.session_file, 'w') as f:
                json.dump(session_data, f, indent=2)
        except Exception as e:
            print(f"Error saving sessions: {e}")

    def _load_sessions(self):
        """Load sessions from disk"""
        try:
            if os.path.exists(self.session_file):
                with open(self.session_file, 'r') as f:
                    session_data = json.load(f)

                for user_id_str, data in session_data.items():
                    user_id = int(user_id_str)
                    session = Session(
                        user_id=data['user_id'],
                        chat_id=data['chat_id'],
                        authenticated_at=datetime.fromisoformat(data['authenticated_at']),
                        expires_at=datetime.fromisoformat(data['expires_at']),
                        agent=data.get('agent')
                    )

                    # Only load if not expired
                    if not session.is_expired():
                        self.sessions[user_id] = session
        except Exception as e:
            print(f"Error loading sessions: {e}")

    def _log_security_event(self, user_id: int, event: str, details: str = ""):
        """
        Log security events for audit trail

        Args:
            user_id: Telegram user ID
            event: Type of security event
            details: Additional details
        """
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'user_id': user_id,
            'event': event,
            'details': details
        }

        log_file = "/var/log/supreme_council/security.log"

        try:
            # Create directory if it doesn't exist
            os.makedirs(os.path.dirname(log_file), exist_ok=True)

            with open(log_file, 'a') as f:
                f.write(json.dumps(log_entry) + '\n')
        except Exception as e:
            # Fallback to stderr if log file not writable
            print(f"Security event: {log_entry}", file=sys.stderr)

    def get_security_stats(self) -> Dict:
        """Get security statistics for monitoring"""
        return {
            'active_sessions': len(self.sessions),
            'locked_out_users': len([
                user_id for user_id, (_, lockout) in self.failed_attempts.items()
                if lockout and datetime.now() < lockout
            ]),
            'users_with_failed_attempts': len(self.failed_attempts)
        }


# Example usage and setup
def setup_authentication():
    """
    Setup function to generate PIN hash and initialize auth system

    Run this once during setup to get your PIN hash
    """
    print("Supreme AI Council - PIN Setup")
    print("=" * 50)
    pin = input("Enter your 4-digit PIN: ")

    if len(pin) != 4 or not pin.isdigit():
        print("❌ PIN must be exactly 4 digits")
        return

    pin_hash = TelegramAuth.hash_pin(pin)

    print("\n✅ PIN hash generated successfully!")
    print(f"\nAdd this to your environment variables:")
    print(f"export SUPREME_COUNCIL_PIN_HASH='{pin_hash}'")
    print("\nOr add to .env file:")
    print(f"SUPREME_COUNCIL_PIN_HASH={pin_hash}")
    print("\n⚠️  Keep this hash secret!")


if __name__ == "__main__":
    # If run directly, provide setup utility
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "setup":
        setup_authentication()
    else:
        print("Run with 'python telegram_auth.py setup' to generate PIN hash")
        print("\nExample usage in agent code:")
        print("""
from telegram_auth import TelegramAuth

# Initialize with PIN hash from environment
auth = TelegramAuth(
    pin_hash=os.getenv('SUPREME_COUNCIL_PIN_HASH'),
    session_timeout_hours=2,
    max_attempts=3,
    lockout_duration_minutes=60
)

# In message handler
def handle_message(user_id, chat_id, message):
    if not auth.is_authenticated(user_id):
        # Not authenticated - check if this is PIN attempt
        success, msg = auth.authenticate(user_id, chat_id, message)
        send_telegram_message(chat_id, msg)
        return

    # User is authenticated - process message normally
    # Extend session on activity
    auth.extend_session(user_id)

    # Handle user's actual request...
        """)
