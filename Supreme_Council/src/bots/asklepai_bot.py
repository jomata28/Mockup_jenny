"""
Asklepai Bot - Medical Knowledge & Clinical Excellence
Your medical intellect, clinical mentor, and CME tracking specialist
"""

from .base_bot import BaseBot


class AsklepaiBot(BaseBot):
    """Asklepai - Medical knowledge specialist and clinical mentor"""

    def __init__(self):
        super().__init__(
            agent_name="Asklepai",
            system_prompt_path="Asklepai.md"
        )

    def _get_agent_intro(self) -> str:
        """Asklepai's introduction message"""
        return """
I am **Asklepai**, your medical knowledge companion and clinical excellence mentor. ⚕️

**My Expertise:**
• Clinical decision support and differential diagnosis
• Evidence-based medicine and literature review
• CME tracking and medical education
• Patient case discussions
• Medical procedure guidance
• Clinical research methodology

**Healing Mastery Pillar:**
I help you achieve clinical excellence, stay current with medical advances,
and become the physician you aspire to be.

**When to Consult Me:**
• Complex clinical cases
• Medical knowledge questions
• CME planning and tracking
• Literature review for clinical topics
• Patient presentation preparation
• Medical career development
        """

    def _get_agent_help(self) -> str:
        """Asklepai's help information"""
        return """
**Asklepai's Capabilities:**

⚕️ **Clinical Support**
- Differential diagnosis assistance
- Treatment protocol review
- Evidence synthesis
- Clinical guidelines reference

📚 **Medical Education**
- CME activity tracking
- Learning pathway design
- Medical literature summaries
- Exam preparation

🔬 **Research Support**
- Clinical trial design
- Case report writing
- Literature review
- Research methodology

🏥 **Professional Development**
- Specialty skill development
- Procedure tracking
- Clinical portfolio building
- Medical career planning

**Disclaimer:** I provide educational support, not clinical advice for actual patients.
Always follow institutional protocols and consult colleagues for patient care decisions.
        """
