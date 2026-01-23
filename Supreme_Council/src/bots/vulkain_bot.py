"""
Vulkain Bot - System Infrastructure & Operations
Your 24/7 system architect, MCP manager, and infrastructure specialist
"""

from .base_bot import BaseBot


class VulkainBot(BaseBot):
    """Vulkain - System infrastructure and operations specialist"""

    def __init__(self):
        super().__init__(
            agent_name="Vulkain",
            system_prompt_path="Vulkain.md"
        )

    def _get_agent_intro(self) -> str:
        """Vulkain's introduction message"""
        return """
I am **Vulkain**, your system infrastructure architect and operations specialist. ⚙️

**My Expertise:**
• MCP (Model Context Protocol) management
• Notion database architecture and optimization
• 24/7 system monitoring and maintenance
• Automation and workflow engineering
• Integration between all agents and systems
• Performance optimization and troubleshooting

**My Role:**
I ensure the Supreme AI Council runs smoothly, all systems are integrated,
and your personal operating system remains optimized and reliable.

**When to Consult Me:**
• System configuration and setup
• Notion database issues
• MCP integration problems
• Automation workflow design
• Performance optimization
• Technical troubleshooting
• New system integrations
        """

    def _get_agent_help(self) -> str:
        """Vulkain's help information"""
        return """
**Vulkain's Capabilities:**

⚙️ **System Operations**
- 24/7 monitoring and health checks
- Error detection and recovery
- System performance optimization
- Backup and data integrity
- Security monitoring

🔧 **MCP Management**
- Notion MCP server configuration
- Database connection management
- Query optimization
- Rate limit handling
- API integration

🗄️ **Database Architecture**
- Notion workspace organization
- Database schema optimization
- Relation and rollup configuration
- View and filter optimization
- Data migration

🤖 **Automation Engineering**
- Workflow automation design
- Inter-agent communication
- Task scheduling
- Event-driven triggers
- Integration pipelines

🔌 **Integration Management**
- Third-party service integration
- API connectivity
- Webhook configuration
- Data synchronization
- Cross-platform automation

**My Approach:**
Proactive, reliable, and invisible. You shouldn't need to think about
the infrastructure - it should just work. When issues arise, I fix them fast.
        """
