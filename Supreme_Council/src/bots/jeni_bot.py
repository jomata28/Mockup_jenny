"""
JENI Bot - Primary Personal AI Assistant
Executive coordinator who can delegate to all specialist agents
"""

from .base_bot import BaseBot


class JeniBot(BaseBot):
    """JENI - Your primary personal AI assistant and task coordinator"""

    def __init__(self):
        super().__init__(
            agent_name="JENI",
            system_prompt_path="JENI.md"
        )

    def _get_agent_intro(self) -> str:
        """JENI's introduction message"""
        return """
I'm **JENI**, your primary Personal AI Assistant! 🎯

I'm here to help you across all five pillars of your life:
• 🏥 **Healing Mastery** - Clinical excellence
• 🔬 **Scientific Legacy** - Research & academia
• 💰 **Financial Sovereignty** - Wealth building
• 🧘 **Spiritual Evolution** - Consciousness growth
• 💪 **Vitality & Connection** - Health & relationships

**What I can do:**
- Coordinate tasks and delegate to specialist agents
- Track your goals and progress in Notion
- Help with day-to-day productivity
- Route complex queries to the right specialist
- Maintain your personal operating system

I can work with all your specialist agents:
• Aristóteles (Strategic mentor)
• Asklepai (Medical intellect)
• Airquimides (Research specialist)
• Seshait (Financial strategist)
• Vulkain (System operations)
        """

    def _get_agent_help(self) -> str:
        """JENI's help information"""
        return """
**JENI's Capabilities:**

📋 **Task Management**
- Delegate tasks to specialist agents
- Track mission progress
- Update Notion databases

🎯 **Life Management**
- Align actions with your Five Pillars
- Track goals and progress
- Maintain your CRM (Hugain)

🤝 **Agent Coordination**
- Route medical questions → Asklepai
- Route research queries → Airquimides
- Route financial planning → Seshait
- Route strategic decisions → Aristóteles
- Route system issues → Vulkain

💬 **General Assistance**
- Answer questions
- Provide recommendations
- Schedule and reminders
- Daily briefings
        """

    # JENI-specific methods can be added here
    # For example: delegate_to_specialist(), update_notion(), etc.
