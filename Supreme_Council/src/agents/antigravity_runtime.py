"""
Antigravity Runtime Manager
Manages agent lifecycle, configuration loading, and message routing
"""

import os
import json
import logging
from typing import Dict, Optional, List, Any
from pathlib import Path
from anthropic import Anthropic, AsyncAnthropic


class AgentConfig:
    """Agent configuration loaded from JSON"""

    def __init__(self, config_path: str):
        """Load agent configuration from JSON file"""
        with open(config_path, 'r') as f:
            data = json.load(f)

        self.name = data['name']
        self.description = data['description']
        self.version = data['version']
        self.model = data['model']
        self.system_prompt_file = data['system_prompt_file']
        self.temperature = data.get('temperature', 0.7)
        self.max_tokens = data.get('max_tokens', 4096)
        self.tools = data.get('tools', [])
        self.capabilities = data.get('capabilities', [])
        self.routing = data.get('routing', {})
        self.metadata = data.get('metadata', {})

        # Load system prompt
        self.system_prompt = self._load_system_prompt(config_path)

    def _load_system_prompt(self, config_path: str) -> str:
        """Load system prompt from markdown file"""
        config_dir = Path(config_path).parent
        prompt_path = config_dir / self.system_prompt_file

        try:
            with open(prompt_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            logging.error(f"Failed to load system prompt for {self.name}: {e}")
            return f"You are {self.name}, a helpful AI assistant."


class AntigravityAgent:
    """
    Antigravity Agent Instance
    Wraps Anthropic Claude API with agent-specific configuration
    """

    def __init__(self, config: AgentConfig, anthropic_client: AsyncAnthropic):
        """
        Initialize agent with configuration

        Args:
            config: AgentConfig instance
            anthropic_client: Async Anthropic client
        """
        self.config = config
        self.client = anthropic_client
        self.logger = logging.getLogger(f"Agent.{config.name}")

        # Conversation history per user (simple in-memory for now)
        self.conversations: Dict[int, List[Dict]] = {}

        self.logger.info(f"Agent '{config.name}' initialized (model: {config.model})")

    async def send_message(
        self,
        user_id: int,
        message: str,
        context: Optional[Dict[str, Any]] = None
    ) -> str:
        """
        Send message to agent and get response

        Args:
            user_id: Telegram user ID (for conversation history)
            message: User's message
            context: Optional context (Notion data, etc.)

        Returns:
            Agent's response
        """
        # Get or create conversation history for this user
        if user_id not in self.conversations:
            self.conversations[user_id] = []

        # Add user message to history
        self.conversations[user_id].append({
            "role": "user",
            "content": message
        })

        # Build system prompt with context if provided
        system_prompt = self.config.system_prompt
        if context:
            system_prompt += f"\n\n## Current Context\n{json.dumps(context, indent=2)}"

        try:
            # Call Claude API
            response = await self.client.messages.create(
                model=self.config.model,
                max_tokens=self.config.max_tokens,
                temperature=self.config.temperature,
                system=system_prompt,
                messages=self.conversations[user_id][-10:]  # Keep last 10 messages for context
            )

            # Extract assistant response
            assistant_message = response.content[0].text

            # Add to conversation history
            self.conversations[user_id].append({
                "role": "assistant",
                "content": assistant_message
            })

            self.logger.info(f"Response generated for user {user_id} ({len(assistant_message)} chars)")

            return assistant_message

        except Exception as e:
            self.logger.error(f"Error generating response: {e}")
            raise

    def clear_history(self, user_id: int):
        """Clear conversation history for a user"""
        if user_id in self.conversations:
            del self.conversations[user_id]
            self.logger.info(f"Cleared conversation history for user {user_id}")

    def get_capabilities(self) -> List[str]:
        """Get agent's capabilities"""
        return self.config.capabilities

    def can_delegate_to(self, agent_name: str) -> bool:
        """Check if this agent can delegate to another agent"""
        delegates = self.config.routing.get('can_delegate_to', [])
        return agent_name.lower() in [a.lower() for a in delegates]


class AntigravityRuntime:
    """
    Antigravity Runtime Manager
    Central orchestrator for all agents
    """

    def __init__(self):
        """Initialize Antigravity runtime"""
        self.logger = logging.getLogger("AntigravityRuntime")

        # Initialize Anthropic client
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY not found in environment")

        self.anthropic = AsyncAnthropic(api_key=api_key)

        # Agent registry
        self.agents: Dict[str, AntigravityAgent] = {}

        self.logger.info("Antigravity Runtime initialized")

    def load_agent(self, config_path: str) -> str:
        """
        Load an agent from configuration file

        Args:
            config_path: Path to agent JSON config

        Returns:
            Agent name
        """
        try:
            # Load configuration
            config = AgentConfig(config_path)

            # Create agent instance
            agent = AntigravityAgent(config, self.anthropic)

            # Register agent
            self.agents[config.name.lower()] = agent

            self.logger.info(f"✅ Loaded agent: {config.name}")

            return config.name

        except Exception as e:
            self.logger.error(f"Failed to load agent from {config_path}: {e}")
            raise

    def load_all_agents(self, agents_dir: str = "agents"):
        """
        Load all agent configurations from directory

        Args:
            agents_dir: Directory containing agent JSON configs
        """
        agents_path = Path(agents_dir)

        if not agents_path.exists():
            self.logger.warning(f"Agents directory not found: {agents_dir}")
            return

        # Load all .agent.json files
        for config_file in agents_path.glob("*.agent.json"):
            try:
                self.load_agent(str(config_file))
            except Exception as e:
                self.logger.error(f"Error loading {config_file}: {e}")

        self.logger.info(f"📊 Loaded {len(self.agents)} agents")

    def get_agent(self, agent_name: str) -> Optional[AntigravityAgent]:
        """
        Get agent by name

        Args:
            agent_name: Name of agent (case-insensitive)

        Returns:
            AntigravityAgent instance or None
        """
        return self.agents.get(agent_name.lower())

    def list_agents(self) -> List[str]:
        """Get list of all loaded agent names"""
        return list(self.agents.keys())

    async def route_message(
        self,
        agent_name: str,
        user_id: int,
        message: str,
        context: Optional[Dict] = None
    ) -> str:
        """
        Route a message to specific agent

        Args:
            agent_name: Target agent name
            user_id: Telegram user ID
            message: User message
            context: Optional context data

        Returns:
            Agent response
        """
        agent = self.get_agent(agent_name)

        if not agent:
            raise ValueError(f"Agent '{agent_name}' not found")

        return await agent.send_message(user_id, message, context)

    def shutdown(self):
        """Shutdown runtime and cleanup"""
        self.logger.info("Shutting down Antigravity Runtime")
        # Cleanup if needed
        self.agents.clear()


# Singleton instance
_runtime: Optional[AntigravityRuntime] = None


def get_runtime() -> AntigravityRuntime:
    """Get or create the global Antigravity runtime"""
    global _runtime
    if _runtime is None:
        _runtime = AntigravityRuntime()
        # Load all agents
        _runtime.load_all_agents()
    return _runtime
