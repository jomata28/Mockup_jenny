"""
Notion MCP Integration
Handles all interactions with Notion databases via Model Context Protocol
"""

import os
import logging
from typing import Dict, List, Optional, Any
from notion_client import Client
from datetime import datetime


class NotionMCP:
    """
    Notion MCP Client for Supreme AI Council
    Manages interactions with the 4 main vaults: Hugain, Manai, Odyssai, WuWai
    """

    def __init__(self):
        """Initialize Notion client with API key from environment"""
        self.logger = logging.getLogger("MCP.Notion")

        # Initialize Notion client
        api_key = os.getenv("NOTION_API_KEY")
        if not api_key or api_key.startswith("secret_your"):
            self.logger.warning("⚠️  Notion API key not configured")
            self.client = None
        else:
            self.client = Client(auth=api_key)
            self.logger.info("✅ Notion MCP client initialized")

        # Database IDs from environment
        self.databases = {
            "hugain": os.getenv("NOTION_DATABASE_HUGAIN"),
            "manai": os.getenv("NOTION_DATABASE_MANAI"),
            "odyssai": os.getenv("NOTION_DATABASE_ODYSSAI"),
            "wuwai": os.getenv("NOTION_DATABASE_WUWAI"),
        }

    def is_available(self) -> bool:
        """Check if Notion MCP is properly configured"""
        return self.client is not None

    # ==========================================
    # HUGAIN VAULT - CRM
    # ==========================================

    async def add_contact(self, name: str, category: str, **properties) -> Optional[str]:
        """
        Add a new contact to Hugain CRM

        Args:
            name: Contact name
            category: Contact category (Professional, Personal, etc.)
            **properties: Additional properties

        Returns:
            Page ID if successful, None otherwise
        """
        if not self.is_available():
            self.logger.error("Notion MCP not available")
            return None

        try:
            db_id = self.databases.get("hugain")
            if not db_id:
                self.logger.error("Hugain database ID not configured")
                return None

            # Create page properties
            page_properties = {
                "Name": {"title": [{"text": {"content": name}}]},
                "Category": {"select": {"name": category}},
            }

            # Add custom properties
            for key, value in properties.items():
                # Handle different property types
                if isinstance(value, str):
                    page_properties[key] = {"rich_text": [{"text": {"content": value}}]}

            # Create page
            response = self.client.pages.create(
                parent={"database_id": db_id},
                properties=page_properties
            )

            self.logger.info(f"✅ Added contact '{name}' to Hugain")
            return response["id"]

        except Exception as e:
            self.logger.error(f"Error adding contact: {e}")
            return None

    async def log_interaction(self, contact_id: str, interaction_type: str, notes: str) -> Optional[str]:
        """Log an interaction with a contact in Hugain"""
        # TODO: Implement interaction logging
        self.logger.info(f"Logging interaction with contact {contact_id}")
        return None

    # ==========================================
    # MANAI VAULT - Energy Management
    # ==========================================

    async def log_energy_level(self, energy_score: int, activities: List[str], notes: str = "") -> Optional[str]:
        """
        Log daily energy levels in Manai vault

        Args:
            energy_score: Energy level 1-10
            activities: List of activities performed
            notes: Additional notes

        Returns:
            Page ID if successful
        """
        if not self.is_available():
            return None

        try:
            db_id = self.databases.get("manai")
            if not db_id:
                self.logger.error("Manai database ID not configured")
                return None

            # Create daily energy log
            page_properties = {
                "Date": {"date": {"start": datetime.now().isoformat()}},
                "Energy Score": {"number": energy_score},
                "Notes": {"rich_text": [{"text": {"content": notes}}]},
            }

            response = self.client.pages.create(
                parent={"database_id": db_id},
                properties=page_properties
            )

            self.logger.info(f"✅ Logged energy level: {energy_score}/10")
            return response["id"]

        except Exception as e:
            self.logger.error(f"Error logging energy: {e}")
            return None

    # ==========================================
    # ODYSSAI VAULT - Adventures & Experiences
    # ==========================================

    async def add_adventure(self, title: str, category: str, **properties) -> Optional[str]:
        """Add an adventure or experience to Odyssai vault"""
        if not self.is_available():
            return None

        try:
            db_id = self.databases.get("odyssai")
            if not db_id:
                self.logger.error("Odyssai database ID not configured")
                return None

            page_properties = {
                "Title": {"title": [{"text": {"content": title}}]},
                "Category": {"select": {"name": category}},
            }

            response = self.client.pages.create(
                parent={"database_id": db_id},
                properties=page_properties
            )

            self.logger.info(f"✅ Added adventure: {title}")
            return response["id"]

        except Exception as e:
            self.logger.error(f"Error adding adventure: {e}")
            return None

    # ==========================================
    # WUWAI VAULT - Spiritual Growth
    # ==========================================

    async def log_reflection(self, reflection_text: str, theme: str = "") -> Optional[str]:
        """Log a spiritual reflection or contemplative practice in WuWai vault"""
        if not self.is_available():
            return None

        try:
            db_id = self.databases.get("wuwai")
            if not db_id:
                self.logger.error("WuWai database ID not configured")
                return None

            page_properties = {
                "Date": {"date": {"start": datetime.now().isoformat()}},
                "Reflection": {"rich_text": [{"text": {"content": reflection_text}}]},
            }

            if theme:
                page_properties["Theme"] = {"select": {"name": theme}}

            response = self.client.pages.create(
                parent={"database_id": db_id},
                properties=page_properties
            )

            self.logger.info(f"✅ Logged spiritual reflection")
            return response["id"]

        except Exception as e:
            self.logger.error(f"Error logging reflection: {e}")
            return None

    # ==========================================
    # GENERIC QUERY METHODS
    # ==========================================

    async def query_database(self, vault_name: str, filter_params: Dict = None) -> List[Dict]:
        """
        Query a Notion database with optional filters

        Args:
            vault_name: One of 'hugain', 'manai', 'odyssai', 'wuwai'
            filter_params: Notion API filter parameters

        Returns:
            List of page objects
        """
        if not self.is_available():
            return []

        try:
            db_id = self.databases.get(vault_name.lower())
            if not db_id:
                self.logger.error(f"Database ID for {vault_name} not configured")
                return []

            query_params = {"database_id": db_id}
            if filter_params:
                query_params["filter"] = filter_params

            response = self.client.databases.query(**query_params)
            return response.get("results", [])

        except Exception as e:
            self.logger.error(f"Error querying {vault_name}: {e}")
            return []

    async def update_page(self, page_id: str, properties: Dict) -> bool:
        """Update a Notion page with new properties"""
        if not self.is_available():
            return False

        try:
            self.client.pages.update(page_id=page_id, properties=properties)
            self.logger.info(f"✅ Updated page {page_id}")
            return True

        except Exception as e:
            self.logger.error(f"Error updating page: {e}")
            return False


# Singleton instance
_notion_mcp = None


def get_notion_client() -> NotionMCP:
    """Get or create the global Notion MCP client"""
    global _notion_mcp
    if _notion_mcp is None:
        _notion_mcp = NotionMCP()
    return _notion_mcp
