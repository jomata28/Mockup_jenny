#!/usr/bin/env python3
"""
Supreme AI Council - Multi-Agent Telegram Bot System
Main entry point that launches all agent bots
"""

import os
import sys
import asyncio
import logging
from dotenv import load_dotenv
from telegram.ext import Application

# Import bot handlers
from src.bots.jeni_bot import JeniBot
from src.bots.aristoteles_bot import AristotelesBot
from src.bots.asklepai_bot import AsklepaiBot
from src.bots.airquimides_bot import AirquimidesBot
from src.bots.seshait_bot import SeshaitBot
from src.bots.vulkain_bot import VulkainBot

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


class SupremeCouncil:
    """Main orchestrator for all Supreme AI Council bots"""

    def __init__(self):
        # Load environment variables
        load_dotenv()

        self.environment = os.getenv('ENVIRONMENT', 'development')
        self.use_webhook = os.getenv('USE_WEBHOOK', 'false').lower() == 'true'

        # Initialize bot registry
        self.bots = {}
        self.applications = []

        logger.info(f"Initializing Supreme AI Council in {self.environment} mode")

    def register_bot(self, name: str, bot_class, token_env_var: str):
        """Register a bot if its token is available"""
        token = os.getenv(token_env_var)

        if not token or token.startswith('your_'):
            logger.warning(f"⚠️  {name} bot token not configured (skipping)")
            return False

        try:
            bot_instance = bot_class()
            application = Application.builder().token(token).build()

            # Setup handlers for this bot
            bot_instance.setup_handlers(application)

            self.bots[name] = bot_instance
            self.applications.append(application)

            logger.info(f"✅ {name} bot registered successfully")
            return True

        except Exception as e:
            logger.error(f"❌ Failed to register {name} bot: {e}")
            return False

    async def start(self):
        """Start all registered bots"""

        # Register all bots
        logger.info("=" * 60)
        logger.info("🚀 SUPREME AI COUNCIL - INITIALIZATION")
        logger.info("=" * 60)

        self.register_bot("JENI", JeniBot, "JENI_BOT_TOKEN")
        self.register_bot("Aristóteles", AristotelesBot, "ARISTOTELES_BOT_TOKEN")
        self.register_bot("Asklepai", AsklepaiBot, "ASKLEPAI_BOT_TOKEN")
        self.register_bot("Airquimides", AirquimidesBot, "AIRQUIMIDES_BOT_TOKEN")
        self.register_bot("Seshait", SeshaitBot, "SESHAIT_BOT_TOKEN")
        self.register_bot("Vulkain", VulkainBot, "VULKAIN_BOT_TOKEN")

        logger.info("=" * 60)
        logger.info(f"📊 Active Bots: {len(self.bots)}/6")
        logger.info("=" * 60)

        if not self.bots:
            logger.error("❌ No bots configured! Check your .env file")
            sys.exit(1)

        # Initialize all applications
        logger.info("🔧 Initializing bot applications...")
        for app in self.applications:
            await app.initialize()

        # Start polling or webhook mode
        if self.use_webhook:
            await self._start_webhook()
        else:
            await self._start_polling()

    async def _start_polling(self):
        """Start all bots in polling mode (for development)"""
        logger.info("🔄 Starting in POLLING mode...")

        # Start all applications
        for app in self.applications:
            await app.start()

        logger.info("=" * 60)
        logger.info("✨ SUPREME AI COUNCIL IS ONLINE")
        logger.info("=" * 60)

        # Keep running
        try:
            # Run all updaters concurrently
            await asyncio.gather(
                *[app.updater.start_polling() for app in self.applications]
            )

            # Keep alive
            await asyncio.Event().wait()

        except KeyboardInterrupt:
            logger.info("🛑 Shutdown signal received...")
        finally:
            await self.shutdown()

    async def _start_webhook(self):
        """Start all bots in webhook mode (for production)"""
        webhook_url = os.getenv('WEBHOOK_URL')
        webhook_port = int(os.getenv('WEBHOOK_PORT', 8443))

        logger.info(f"🌐 Starting in WEBHOOK mode at {webhook_url}")

        # TODO: Implement webhook mode with FastAPI
        # This requires setting up a web server to receive webhook updates
        logger.warning("⚠️  Webhook mode not fully implemented yet, falling back to polling")
        await self._start_polling()

    async def shutdown(self):
        """Gracefully shutdown all bots"""
        logger.info("🔌 Shutting down all bots...")

        for app in self.applications:
            await app.updater.stop()
            await app.stop()
            await app.shutdown()

        logger.info("✅ Supreme AI Council shutdown complete")


async def main():
    """Main entry point"""
    council = SupremeCouncil()
    await council.start()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("👋 Goodbye!")
        sys.exit(0)
