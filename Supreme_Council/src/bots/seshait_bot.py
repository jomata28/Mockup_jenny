"""
Seshait Bot - Financial Strategist & Wealth Builder
Your financial sovereignty architect, AI business tracker, and wealth strategist
"""

from .base_bot import BaseBot


class SeshaitBot(BaseBot):
    """Seshait - Financial strategist and wealth building specialist"""

    def __init__(self):
        super().__init__(
            agent_name="Seshait",
            system_prompt_path="Seshait.md"
        )

    def _get_agent_intro(self) -> str:
        """Seshait's introduction message"""
        return """
I am **Seshait**, your financial sovereignty architect and wealth strategist. 💰

**My Expertise:**
• Financial planning and wealth building
• AI freelancing business tracking
• Investment strategy and portfolio management
• Tax optimization and financial structures
• Income diversification strategies
• Financial goal tracking and accountability

**Financial Sovereignty Pillar:**
I help you build sustainable wealth, grow your AI consulting business,
and achieve true financial independence.

**When to Consult Me:**
• Financial planning and budgeting
• AI freelancing business growth
• Investment decisions and portfolio review
• Tax strategy and optimization
• Income stream diversification
• Financial goal setting and tracking
        """

    def _get_agent_help(self) -> str:
        """Seshait's help information"""
        return """
**Seshait's Capabilities:**

💼 **AI Business Management**
- Client project tracking
- Pricing and proposal strategy
- Business development
- Income optimization
- Service offering expansion

💰 **Wealth Building**
- Financial goal planning
- Investment strategy
- Asset allocation
- Passive income development
- Net worth tracking

📊 **Financial Analytics**
- Cash flow analysis
- Expense optimization
- ROI calculations
- Financial projections
- Performance tracking

🎯 **Strategic Planning**
- Multiple income stream development
- Business scaling strategies
- Financial independence roadmap
- Risk management
- Legacy wealth planning

📈 **Notion Integration**
- Financial tracking in custom databases
- Goal progress monitoring
- Business metrics dashboards
- Investment portfolio tracking

**My Approach:**
Data-driven, strategic, and focused on building sustainable wealth
that supports your life pillars and long-term vision.
        """
