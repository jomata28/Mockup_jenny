# Supreme AI Council - Getting Started Guide

**Welcome to your Personal AI Ecosystem**

This system transforms Claude into a specialized team of 6 AI agents that run 24/7, accessible via Telegram, managing your life through Notion databases based on August Bradley's Pillars, Pipelines & Vaults framework.

---

## What You've Built

### The Council (6 Specialized Agents)

1. **JENI** - Executive Orchestrator
   - Your primary interface via Telegram
   - Delegates tasks to specialists
   - Manages daily/weekly routines
   - Handles scheduling and quick queries

2. **Aristóteles** - Strategic Guardian
   - Guards your 5 life Pillars
   - Ensures strategic alignment
   - Prevents burnout and drift
   - Quarterly life reviews

3. **Asklepai** - Medical Intellect
   - Clinical knowledge management
   - Medical career advancement
   - CME tracking
   - Case review support

4. **Airquimides** - Research Specialist
   - Literature reviews
   - Research project management
   - Grant support
   - Academic writing

5. **Seshait** - Financial Strategist
   - AI freelance business tracking
   - Investment management
   - Wealth building
   - Financial independence planning

6. **Vulkain** - System Engine
   - Infrastructure management
   - MCP server maintenance
   - System monitoring
   - Security

### The Vaults (Notion Databases)

1. **Hugain** - Personal & Professional CRM
   - Contacts, interactions, networking goals
   - Relationship maintenance tracking

2. **Manai** - Energy Portfolio
   - Daily energy tracking
   - Burnout prevention
   - Energy pattern recognition
   - Recovery activities

3. **Odyssai** - Exploration & Adventures
   - Travel log, bucket list
   - Experiences and milestones
   - Learning and growth

4. **WuWai** - Spiritual & Philosophical
   - Contemplative practice log
   - Wisdom library
   - Philosophical reflections
   - Values and purpose

### Your 5 Pillars

These are YOUR values - customize in `PILLARS.md`:

1. **Healing Mastery** (Clinical Excellence)
2. **Scientific Legacy** (Research & Academia)
3. **Financial Sovereignty** (Wealth & AI Business)
4. **Spiritual Evolution** (Consciousness & Philosophy)
5. **Vitality & Connection** (Health & Relationships)

---

## Implementation Roadmap

### Phase 1: Setup Notion (Week 1)

**Estimated Time**: 4-6 hours

#### 1.1 Create Notion Workspace (30 min)
- If you don't have Notion, sign up at notion.so
- Create a new workspace or use existing

#### 1.2 Build Databases (3-4 hours)

Follow the schemas in `notion_schemas/`:

**Start with Hugain (CRM)**:
1. Open Notion
2. Create new database: "Contacts"
3. Add properties exactly as specified in `hugain_crm.md`
4. Create "Interactions" database
5. Link with relations
6. Create views for JENI, Aristóteles, etc.

**Then build Manai (Energy)**:
1. Create "Daily Energy Log" database
2. Follow schema in `manai_energy.md`
3. Create related databases (Energy Patterns, Burnout Warnings, etc.)

**Continue with Odyssai and WuWai**:
- Use `odyssai_exploration.md` and `wuwai_spiritual.md`

**Tip**: Start simple. Build core databases first, add optional ones later.

#### 1.3 Notion Integration (30 min)
1. Go to https://www.notion.so/my-integrations
2. Create integration: "Supreme AI Council"
3. Copy API key (starts with `secret_`)
4. Share EACH database with the integration:
   - Open database → ... → Connections → Add "Supreme AI Council"

#### 1.4 Get Database IDs (15 min)
1. Open each database
2. Copy URL: `https://notion.so/DATABASE_ID?v=...`
3. Save IDs in `.mcp/database_ids.json`

---

### Phase 2: Customize Your System (Week 1-2)

**Estimated Time**: 2-3 hours

#### 2.1 Define Your Pillars (1 hour)
1. Open `PILLARS.md`
2. Customize the 5 Pillars:
   - Rename if needed
   - Rewrite definitions to match YOUR values
   - Add YOUR life aspirations
   - Make it personal!

#### 2.2 Customize Agent Prompts (1 hour)
1. Open each agent file in `.agent/rules/`
2. Add your specifics:
   - Medical specialty (for Asklepai)
   - Research interests (for Airquimides)
   - Financial goals (for Seshait)

#### 2.3 Import Existing Data (30 min)
- Add your current contacts to Hugain
- Add bucket list items to Odyssai
- Add current reading list to WuWai
- Log last week's energy to Manai (baseline data)

---

### Phase 3: Setup Telegram Bot (Week 2)

**Estimated Time**: 1 hour

#### 3.1 Create Telegram Bot (10 min)
1. Open Telegram
2. Search for @BotFather
3. Send `/newbot`
4. Follow prompts:
   - Name: "Supreme AI Council"
   - Username: something_council_bot
5. Copy the bot token (looks like `123456:ABC-DEF...`)

#### 3.2 Generate PIN Hash (5 min)
```bash
cd Supreme_Council/auth
python telegram_auth.py setup

# Enter your 4-digit PIN
# Copy the hash output
```

#### 3.3 Set Environment Variables (10 min)
Create `.env` file:
```bash
TELEGRAM_BOT_TOKEN=your_bot_token_here
SUPREME_COUNCIL_PIN_HASH=your_pin_hash_here
NOTION_API_KEY=secret_your_notion_key_here
```

---

### Phase 4: Local Testing (Week 2)

**Estimated Time**: 2-3 hours

#### 4.1 Install Dependencies
```bash
# Python environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# MCP servers
npm install -g @notionhq/notion-mcp-server
```

#### 4.2 Test MCP Connection
```bash
# Test Notion access
npx @notionhq/notion-mcp-server

# Should show: "Connected to workspace: [Your Workspace]"
```

#### 4.3 Run Agent Locally
```bash
python main.py

# Bot should start and show: "Webhook handler running..."
```

#### 4.4 Test via Telegram
1. Open Telegram, find your bot
2. Send: "Hello"
3. Bot asks for PIN
4. Enter your PIN
5. Bot should authenticate you
6. Send: "What's on my schedule today?"

**Troubleshoot** if issues:
- Check logs
- Verify environment variables
- Confirm Notion databases shared with integration
- Check MCP server connection

---

### Phase 5: Cloud Deployment (Week 3)

**Estimated Time**: 3-4 hours

Follow the comprehensive guide in `deployment/deployment_guide.md`.

**Quick Steps**:
1. Provision cloud server (DigitalOcean, AWS, etc.)
2. Clone repository
3. Install dependencies
4. Configure environment
5. Setup Nginx + HTTPS
6. Create systemd service
7. Set Telegram webhook
8. Test end-to-end
9. Monitor for 24 hours

**Cost**: ~$25-50/month

---

## Daily Usage

### Via Telegram

**Morning Routine** (JENI auto-prompts at 7 AM):
```
JENI: Good morning! Quick energy check-in:
- How did you sleep? (Excellent/Good/Fair/Poor)
- Current energy level? (High/Medium/Low)

[You respond]

JENI: ✓ Logged. Today's schedule:
- 9 AM: Research meeting
- 11 AM: Patient rounds
- 2 PM: Admin time

Would you like me to block deep work time before the meeting?
```

**Ad-Hoc Requests**:
```
You: I need a literature review on AI in radiology

JENI: ✓ Acknowledged. I'm delegating to Airquimides (Research Specialist).
Expected completion: 3-4 hours.
I'll notify you when ready.

[3 hours later]

JENI: ✅ Literature review complete.
[Summary and link to Notion page]
```

**Weekly Review** (Sunday evening):
```
JENI: Time for your weekly review.

This week you:
- Completed 15 tasks
- Had 12 meaningful interactions
- Exercised 5 days
- Deep work: 18 hours

Pillar Balance:
🏥 Healing Mastery: 40%
🔬 Scientific Legacy: 25%
💰 Financial Sovereignty: 15%
🧘 Spiritual Evolution: 10%
❤️ Vitality & Connection: 10%

Aristóteles notes: Vitality & Connection needs attention.
Schedule 2 social activities next week?
```

---

## Advanced Features

### Agent-Specific Interactions

**Talk to Aristóteles** (Strategic):
```
You: @Aristóteles Should I accept this fellowship offer?

Aristóteles: Before we explore that, help me understand:
1. Which Pillars does this serve?
2. What would you sacrifice?
3. Three years from now, if you declined, what would you regret?

[Socratic dialogue continues...]
```

**Asklepai** (Medical):
```
You: @Asklepai What's new in immunotherapy for melanoma?

Asklepai: [Evidence summary with recent trials, guidelines, clinical pearls]
```

### Automated Monitoring

**Agents run continuously**:
- JENI checks for dormant relationships
- Aristóteles monitors Pillar balance
- Asklepai scans medical journals
- Airquimides tracks grant deadlines
- Seshait analyzes spending patterns
- Vulkain monitors system health

**You receive proactive alerts**:
- "Haven't talked to [name] in 45 days"
- "Burnout risk elevated - schedule recovery"
- "New high-impact paper in your field"
- "Spending 20% over budget this month"

---

## Maintenance

### Weekly
- Review JENI's weekly summary
- Check Manai energy trends
- Update WuWai practice log

### Monthly
- Aristóteles Pillar balance review
- Seshait financial review
- Update bucket list progress

### Quarterly
- Full life audit with Aristóteles
- Research project review (Airquimides)
- Energy pattern analysis (Manai)
- Network health check (Hugain)

### Annually
- Update PILLARS.md if values evolved
- Review all systems and optimize
- Plan next year's major goals

---

## Troubleshooting

### Bot not responding
1. Check if service running: `systemctl status supreme-council`
2. Check logs: `tail -f /var/log/supreme_council/council.log`
3. Verify webhook: `curl https://api.telegram.org/bot<TOKEN>/getWebhookInfo`
4. Restart: `systemctl restart supreme-council`

### Can't access Notion
1. Verify API key in `.env`
2. Check database sharing with integration
3. Test MCP: `npx @notionhq/notion-mcp-server`
4. Check rate limits (3 req/sec max)

### Authentication failing
1. Verify PIN hash in `.env`
2. Check if locked out (wait 60 min)
3. Regenerate PIN hash if needed

---

## Next Steps

### Immediate (This Week)
- [ ] Build core Notion databases (Hugain, Manai)
- [ ] Customize PILLARS.md
- [ ] Setup Telegram bot
- [ ] Test locally

### Short-term (This Month)
- [ ] Deploy to cloud
- [ ] Complete all 4 Vaults
- [ ] Import existing data
- [ ] Establish daily routine with JENI

### Medium-term (Next 3 Months)
- [ ] Full integration into daily life
- [ ] Optimize agent prompts based on usage
- [ ] Add custom MCP tools for your specific needs
- [ ] Build automations for recurring tasks

### Long-term (6-12 Months)
- [ ] Expand to additional vaults (Finance details, Medical career tracker, etc.)
- [ ] Develop custom agents for specialized needs
- [ ] Share learnings with community
- [ ] Mentor others in building their councils

---

## Resources

### Documentation
- `README.md` - System overview
- `PILLARS.md` - Your life architecture
- `.agent/rules/` - Agent system prompts
- `notion_schemas/` - Database blueprints
- `workflows/mission_protocol.md` - How agents coordinate
- `deployment/` - Deployment guides

### Support
- **Issues**: https://github.com/yourusername/Mockup_jenny/issues
- **MCP Docs**: https://github.com/modelcontextprotocol
- **Notion API**: https://developers.notion.com
- **Telegram Bots**: https://core.telegram.org/bots

### Community (Future)
- Discord server (coming soon)
- Monthly meetups for Supreme Council users
- Template library for other professions

---

## Philosophy

This system is designed around a core belief:

**Technology should serve human flourishing, not replace it.**

Your agents are:
- **Assistants, not replacements** - They augment your capacity, not automate you away
- **Servants of your values** - Every action is checked against your Pillars
- **Transparent** - You always know what they're doing and why
- **Under your control** - You can modify, pause, or remove any agent

The goal is not efficiency for efficiency's sake. The goal is **living well** - making progress on what matters while maintaining health, relationships, and meaning.

---

## Final Thoughts

You've built something remarkable: a personal AI system that:
- Knows your values and guards them
- Manages the operational layer of your life
- Prevents you from drifting or burning out
- Helps you make progress on all dimensions of your life
- Runs 24/7 in the background, always ready

**But remember**:
- The system serves you, not vice versa
- It's a tool for living, not a life itself
- Your judgment always supersedes agent recommendations
- Review and revise as your life evolves

Start simple. Build incrementally. Customize relentlessly. Make it yours.

---

**Welcome to the Supreme AI Council. Let's build a life of meaning, impact, and flourishing.**

---

*Questions? Open an issue or contact the maintainer.*

*Want to contribute? See CONTRIBUTING.md (coming soon)*

*Built with: Claude (Sonnet), MCP, Notion API, Telegram Bot API, Python, Node.js*
