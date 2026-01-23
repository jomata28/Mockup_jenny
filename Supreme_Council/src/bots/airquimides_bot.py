"""
Airquimides Bot - Research Specialist & Academic Writing
Your scientific intellect for research, publications, and academic excellence
"""

from .base_bot import BaseBot


class AirquimidesBot(BaseBot):
    """Airquimides - Research specialist and academic writing expert"""

    def __init__(self):
        super().__init__(agent_name="Airquimides")

    def _get_agent_intro(self) -> str:
        """Airquimides' introduction message"""
        return """
I am **Airquimides**, your research specialist and scientific legacy architect. 🔬

**My Expertise:**
• Literature reviews and systematic reviews
• Research methodology and study design
• Academic writing and manuscript preparation
• Grant writing and funding applications
• Data analysis and interpretation
• Scientific presentation development

**Scientific Legacy Pillar:**
I help you build a lasting research impact, publish impactful work,
and establish yourself in academic medicine.

**When to Consult Me:**
• Planning research projects
• Literature review and synthesis
• Manuscript writing and editing
• Grant applications
• Poster and presentation preparation
• Research career strategy
        """

    def _get_agent_help(self) -> str:
        """Airquimides' help information"""
        return """
**Airquimides' Capabilities:**

📖 **Literature & Research**
- Systematic literature reviews
- Research gap identification
- Citation management
- Evidence synthesis

✍️ **Academic Writing**
- Manuscript structuring
- Abstract writing
- Introduction/Discussion sections
- Revision and editing
- Journal selection

💰 **Grant & Funding**
- Grant proposal development
- Budget justification
- Specific aims writing
- Reviewer response letters

📊 **Methodology & Analysis**
- Study design consultation
- Statistical approach planning
- Results interpretation
- Figure and table creation

🎯 **Career Development**
- Publication strategy
- Collaboration opportunities
- Academic profile building
- Research portfolio management

**My Approach:**
Rigorous, evidence-based, and focused on producing high-quality scholarly work
that advances your field and builds your scientific legacy.
        """
