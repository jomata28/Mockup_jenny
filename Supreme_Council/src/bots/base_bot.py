"""
Base Bot Class - Common functionality for all Supreme Council agents
ANTIGRAVITY VERSION - Uses Antigravity Runtime for agent management
"""

import os
import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes
)

# Import auth module
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from auth.telegram_auth import TelegramAuth

# Import Antigravity Runtime
from src.agents.antigravity_runtime import get_runtime


class BaseBot:
    """Base class for all Supreme Council agent bots - Antigravity powered"""

    def __init__(self, agent_name: str):
        """
        Initialize base bot

        Args:
            agent_name: Name of the agent (e.g., "JENI", "Aristoteles")
        """
        self.agent_name = agent_name
        self.logger = logging.getLogger(f"Bot.{agent_name}")

        # Get Antigravity runtime (singleton)
        self.runtime = get_runtime()

        # Verify agent is loaded in runtime
        self.agent = self.runtime.get_agent(agent_name)
        if not self.agent:
            raise ValueError(f"Agent '{agent_name}' not found in Antigravity runtime")

        # Initialize authentication
        self.auth = TelegramAuth()

        self.logger.info(f"{agent_name} bot initialized with Antigravity")

    def setup_handlers(self, application: Application):
        """Setup Telegram command and message handlers"""

        # Command handlers
        application.add_handler(CommandHandler("start", self.cmd_start))
        application.add_handler(CommandHandler("help", self.cmd_help))
        application.add_handler(CommandHandler("auth", self.cmd_auth))
        application.add_handler(CommandHandler("status", self.cmd_status))

        # Message handler (for regular conversation)
        application.add_handler(
            MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message)
        )

        self.logger.info(f"Handlers registered for {self.agent_name}")

    # ==========================================
    # COMMAND HANDLERS
    # ==========================================

    async def cmd_start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /start command"""
        user_id = update.effective_user.id

        welcome_msg = f"""
🌟 **Welcome to {self.agent_name}** 🌟

{self._get_agent_intro()}

**Quick Start:**
1. Authenticate with `/auth YOUR_PIN`
2. Start chatting naturally!

**Commands:**
/help - Show available commands
/status - Check authentication status
/auth <PIN> - Authenticate yourself

Ready to begin?
        """

        await update.message.reply_text(welcome_msg, parse_mode='Markdown')

    async def cmd_help(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /help command"""
        help_msg = f"""
📚 **{self.agent_name} - Command Reference**

{self._get_agent_help()}

**Common Commands:**
/start - Initialize bot
/help - Show this message
/auth <PIN> - Authenticate (required for full access)
/status - Check your session status

**Usage:**
Just send me a message after authenticating, and I'll respond based on my specialization!
        """

        await update.message.reply_text(help_msg, parse_mode='Markdown')

    async def cmd_auth(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /auth command with PIN"""
        user_id = update.effective_user.id

        # Extract PIN from command
        if not context.args:
            await update.message.reply_text(
                "❌ Please provide your PIN: `/auth YOUR_PIN`",
                parse_mode='Markdown'
            )
            return

        pin = context.args[0]

        # Verify PIN
        is_valid, message = self.auth.verify_pin(user_id, pin)

        if is_valid:
            await update.message.reply_text(f"✅ {message}", parse_mode='Markdown')
        else:
            await update.message.reply_text(f"❌ {message}", parse_mode='Markdown')

    async def cmd_status(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /status command"""
        user_id = update.effective_user.id

        if self.auth.is_authenticated(user_id):
            await update.message.reply_text(
                "✅ **Session Active**\n\nYou are authenticated and ready to chat!",
                parse_mode='Markdown'
            )
        else:
            await update.message.reply_text(
                "⚠️ **Not Authenticated**\n\nUse `/auth YOUR_PIN` to authenticate.",
                parse_mode='Markdown'
            )

    # ==========================================
    # MESSAGE HANDLER
    # ==========================================

    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle incoming text messages"""
        user_id = update.effective_user.id
        user_message = update.message.text

        # Check authentication
        if not self.auth.is_authenticated(user_id):
            await update.message.reply_text(
                "🔒 Please authenticate first using `/auth YOUR_PIN`",
                parse_mode='Markdown'
            )
            return

        # Show typing indicator
        await update.message.chat.send_action("typing")

        try:
            # Get AI response
            response = await self._get_ai_response(user_message, user_id)

            # Send response
            await update.message.reply_text(response, parse_mode='Markdown')

        except Exception as e:
            self.logger.error(f"Error handling message: {e}")
            await update.message.reply_text(
                f"❌ I encountered an error processing your message. Please try again."
            )

    # ==========================================
    # AI RESPONSE GENERATION
    # ==========================================

    async def _get_ai_response(self, user_message: str, user_id: int) -> str:
        """
        Get AI response using Antigravity Runtime

        Args:
            user_message: User's message text
            user_id: Telegram user ID

        Returns:
            AI-generated response from Antigravity agent
        """
        try:
            # Route message through Antigravity runtime
            response_text = await self.runtime.route_message(
                agent_name=self.agent_name,
                user_id=user_id,
                message=user_message,
                context=None  # TODO: Add Notion context if needed
            )

            self.logger.info(f"Generated response for user {user_id} ({len(response_text)} chars)")

            return response_text

        except Exception as e:
            self.logger.error(f"Antigravity runtime error: {e}")
            raise

    # ==========================================
    # AGENT-SPECIFIC METHODS (override in subclasses)
    # ==========================================

    def _get_agent_intro(self) -> str:
        """Get agent-specific introduction (override in subclass)"""
        return f"I am {self.agent_name}, here to assist you."

    def _get_agent_help(self) -> str:
        """Get agent-specific help text (override in subclass)"""
        return "I'm ready to help with your requests!"
