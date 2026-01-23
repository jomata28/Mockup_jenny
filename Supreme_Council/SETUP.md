# Supreme AI Council - Setup Guide

Get your multi-agent Telegram bot system running in minutes! 🚀

## Quick Start Checklist

- [ ] Python 3.11+ installed
- [ ] 2+ Telegram bot tokens from BotFather
- [ ] Anthropic API key
- [ ] Notion API key (optional for full features)
- [ ] Environment variables configured
- [ ] Dependencies installed
- [ ] Bots running!

---

## 1. Prerequisites

### System Requirements
- **Python**: 3.11 or higher
- **OS**: Linux, macOS, or Windows (WSL recommended)
- **Internet**: Stable connection for API calls

### Required API Keys

| Service | Required? | How to Get |
|---------|-----------|------------|
| Telegram Bot Tokens | ✅ Yes | BotFather on Telegram |
| Anthropic API | ✅ Yes | https://console.anthropic.com |
| Notion API | ⚠️ Optional* | https://www.notion.so/my-integrations |

*Notion is optional - bots will work without it but can't access your databases

---

## 2. Get Your Telegram Bot Tokens

You already have 2 tokens:

✅ **JENI**: `8304075167:AAFIm8GA8Ocx-uEZi2SUmQArDG1zys5SHu4`
✅ **Aristóteles**: `8511536107:AAEiRI271IxJCxE98JTC3ZqVH7vRs_zNG4M`

### Get the Remaining 4 Tokens

1. Open Telegram and search for **@BotFather**
2. Send `/newbot` for each agent:
   - **Asklepai** (medical bot)
   - **Airquimides** (research bot)
   - **Seshait** (financial bot)
   - **Vulkain** (system bot)
3. Choose a name and username for each
4. Copy each token BotFather gives you

**Example:**
```
You: /newbot
BotFather: Alright, a new bot. How are we going to call it?
You: Asklepai Medical Assistant
BotFather: Good. Now let's choose a username for your bot...
You: AsklepaiMedBot
BotFather: Done! Here's your token: 7123456789:AAHdqTcvCH1vGWJxfSeofSAs0K5PALDsaw
```

---

## 3. Installation

### Clone & Navigate
```bash
cd /home/user/Mockup_jenny/Supreme_Council
```

### Install Python Dependencies
```bash
pip install -r requirements.txt
```

Or with virtual environment (recommended):
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

## 4. Environment Configuration

### Create Your .env File

```bash
cp .env.example .env
nano .env  # or use your preferred editor
```

### Fill in Your Secrets

Edit `.env` and replace placeholder values:

```bash
# ============================================
# TELEGRAM BOT TOKENS
# ============================================
JENI_BOT_TOKEN=8304075167:AAFIm8GA8Ocx-uEZi2SUmQArDG1zys5SHu4
ARISTOTELES_BOT_TOKEN=8511536107:AAEiRI271IxJCxE98JTC3ZqVH7vRs_zNG4M
ASKLEPAI_BOT_TOKEN=<paste_your_asklepai_token>
AIRQUIMIDES_BOT_TOKEN=<paste_your_airquimides_token>
SESHAIT_BOT_TOKEN=<paste_your_seshait_token>
VULKAIN_BOT_TOKEN=<paste_your_vulkain_token>

# ============================================
# ANTHROPIC API
# ============================================
ANTHROPIC_API_KEY=sk-ant-api03-<your_key_here>

# ============================================
# NOTION API (Optional)
# ============================================
NOTION_API_KEY=secret_<your_integration_key>
NOTION_DATABASE_HUGAIN=<database_id>
NOTION_DATABASE_MANAI=<database_id>
NOTION_DATABASE_ODYSSAI=<database_id>
NOTION_DATABASE_WUWAI=<database_id>

# ============================================
# SECURITY
# ============================================
MASTER_PIN_HASH=<generate_this_next>
```

### Generate Your PIN Hash

Choose a secure PIN (numbers only, 4-6 digits recommended), then hash it:

```bash
python3 -c "import hashlib; print(hashlib.sha256('YOUR_PIN_HERE'.encode()).hexdigest())"
```

Example:
```bash
python3 -c "import hashlib; print(hashlib.sha256('123456'.encode()).hexdigest())"
# Output: 8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92
```

Copy the output and paste it as `MASTER_PIN_HASH` in your `.env` file.

⚠️ **Important**: Never commit your `.env` file to git! It's already in `.gitignore`.

---

## 5. Launch Your Bots!

### Start All Bots

```bash
python3 main.py
```

You should see output like:

```
============================================================
🚀 SUPREME AI COUNCIL - INITIALIZATION
============================================================
✅ JENI bot registered successfully
✅ Aristóteles bot registered successfully
⚠️  Asklepai bot token not configured (skipping)
⚠️  Airquimides bot token not configured (skipping)
⚠️  Seshait bot token not configured (skipping)
⚠️  Vulkain bot token not configured (skipping)
============================================================
📊 Active Bots: 2/6
============================================================
🔧 Initializing bot applications...
🔄 Starting in POLLING mode...
============================================================
✨ SUPREME AI COUNCIL IS ONLINE
============================================================
```

### Test Your Bots on Telegram

1. Open Telegram
2. Search for your bot (e.g., `@YourJENIBot`)
3. Send `/start`
4. Authenticate: `/auth YOUR_PIN`
5. Start chatting!

---

## 6. Notion Integration (Optional)

### Create Notion Integration

1. Go to https://www.notion.so/my-integrations
2. Click **"+ New integration"**
3. Name it "Supreme AI Council"
4. Select your workspace
5. Copy the **Internal Integration Token** (starts with `secret_`)

### Share Databases with Integration

For each of your 4 databases (Hugain, Manai, Odyssai, WuWai):

1. Open the database in Notion
2. Click **"..."** (top right)
3. Select **"Add connections"**
4. Choose **"Supreme AI Council"** integration
5. Copy the database ID from URL:
   - URL: `https://notion.so/Your-Database-abc123def456...`
   - ID: `abc123def456...` (the part after last `/`)

### Update .env with Database IDs

```bash
NOTION_API_KEY=secret_YourIntegrationToken
NOTION_DATABASE_HUGAIN=abc123...
NOTION_DATABASE_MANAI=def456...
NOTION_DATABASE_ODYSSAI=ghi789...
NOTION_DATABASE_WUWAI=jkl012...
```

Restart your bots after updating `.env`.

---

## 7. Usage Examples

### Talk to JENI (Primary Assistant)

```
You: /start
JENI: 🌟 Welcome to JENI 🌟
      I'm your primary Personal AI Assistant!

You: /auth 123456
JENI: ✅ Authentication successful! Session established.

You: What should I focus on today?
JENI: Based on your Five Pillars, let me help you prioritize...
```

### Consult Aristóteles (Strategic Mentor)

```
You: I'm struggling to balance my clinical work with research time.
     Should I focus more on publishing or patient care?

Aristóteles: This touches on the tension between two of your pillars:
             Healing Mastery and Scientific Legacy. Let me ask you
             some questions to help you find clarity...
```

---

## 8. Troubleshooting

### "No bots configured!" Error

**Problem**: No bot tokens in `.env` or all tokens are placeholders
**Solution**: Double-check your `.env` file has actual tokens (not `your_token_here`)

### "Authentication failed!" Error

**Problem**: PIN hash doesn't match
**Solution**:
1. Regenerate hash: `python3 -c "import hashlib; print(hashlib.sha256('YOUR_PIN'.encode()).hexdigest())"`
2. Update `MASTER_PIN_HASH` in `.env`
3. Restart bots

### "Notion MCP not available" Warning

**Problem**: Notion integration not configured
**Solution**: Either:
- Add Notion credentials to `.env` (see Section 6)
- Ignore this warning - bots work without Notion

### Bot Not Responding

**Checklist:**
1. ✅ Is `main.py` still running? (check terminal)
2. ✅ Is bot token correct? (test by messaging bot)
3. ✅ Did you authenticate? (send `/auth YOUR_PIN`)
4. ✅ Check logs for errors in terminal

### API Rate Limits

**Anthropic**:
- Free tier: 50 requests/day
- Paid tier: Much higher limits
- **Solution**: Upgrade to paid tier for heavy usage

**Notion**:
- Rate limit: 3 requests/second
- **Solution**: Built-in rate limiting in `notion_client.py`

---

## 9. Production Deployment

### For 24/7 Operation

**Options:**

1. **Cloud Server** (Recommended)
   - Use Railway, Render, or DigitalOcean
   - Follow your existing `deployment/deployment_guide.md`
   - Use systemd or PM2 to keep bots running

2. **Local Machine** (Development)
   - Use `screen` or `tmux` to keep running in background
   - Not recommended for 24/7 operation

### Example: Background with Screen

```bash
screen -S supreme_council
python3 main.py
# Press Ctrl+A, then D to detach

# Reattach later:
screen -r supreme_council
```

---

## 10. Next Steps

### Now That It's Running

✅ **You have working bots!** Here's what to do next:

1. **Add Remaining Bot Tokens**
   - Get tokens for Asklepai, Airquimides, Seshait, Vulkain
   - Add to `.env`
   - Restart to activate all 6 agents

2. **Set Up Notion Integration**
   - Connect your databases
   - Test with JENI: "Add a contact to my CRM"

3. **Customize Agent Behaviors**
   - Edit `.agent/rules/*.md` files
   - Restart bots to load new prompts

4. **Deploy to Production**
   - Follow `deployment/deployment_guide.md`
   - Set up monitoring
   - Configure backups

5. **Build Advanced Features**
   - Inter-agent communication
   - Scheduled tasks (daily briefings)
   - Custom workflows

---

## 11. Architecture Overview

```
┌─────────────────────┐
│   Telegram Users    │
│  (You on mobile)    │
└──────────┬──────────┘
           │
┌──────────▼──────────────────────────────────┐
│         main.py (Bot Manager)               │
│  Runs all 6 bots concurrently              │
└──────────┬──────────────────────────────────┘
           │
    ┌──────┴──────┬──────────┬─────────┬─────────┐
    │             │          │         │         │
┌───▼───┐  ┌─────▼────┐  ┌──▼──┐  ┌──▼──┐  ┌──▼──┐
│ JENI  │  │Aristóteles│  │Ask- │  │Air- │  │Etc. │
│ Bot   │  │   Bot     │  │lepai│  │qui- │  │     │
└───┬───┘  └─────┬────┘  └──┬──┘  └──┬──┘  └─────┘
    │            │           │        │
    └────────────┴───────────┴────────┘
                 │
        ┌────────▼────────┐
        │  Claude API     │
        │  (Anthropic)    │
        └────────┬────────┘
                 │
        ┌────────▼────────┐
        │  Notion Vaults  │
        │  (via MCP)      │
        └─────────────────┘
```

**How It Works:**

1. User messages bot on Telegram
2. Bot authenticates user (PIN)
3. Bot loads agent's system prompt from `.agent/rules/`
4. Bot calls Claude API with prompt + user message
5. Claude generates response as that agent
6. Bot optionally logs to Notion (CRM, tasks, etc.)
7. Response sent back to user on Telegram

---

## Support

**Issues?**
- Check logs in terminal
- Review this guide
- Check your existing docs: `GETTING_STARTED.md`, `deployment/`

**Want to Extend?**
- Add custom commands in `src/bots/base_bot.py`
- Add Notion methods in `src/mcp/notion_client.py`
- Customize agent prompts in `.agent/rules/`

---

## Security Notes

🔒 **Important Security Practices:**

1. **Never commit `.env`** - Contains secrets!
2. **Use strong PINs** - 6+ digits, not sequential
3. **Rotate tokens regularly** - Every 3-6 months
4. **Monitor logs** - Watch for suspicious activity
5. **Restrict bot access** - Only share with trusted users
6. **Use HTTPS** - When deploying with webhooks
7. **Backup databases** - Export Notion data regularly

---

## What You Just Built 🎉

You now have:
- ✅ Multi-agent Telegram bot system
- ✅ 2-6 specialized AI agents (expandable)
- ✅ PIN-based authentication
- ✅ Claude-powered conversations
- ✅ Notion database integration (optional)
- ✅ Scalable architecture for future growth

**Welcome to the Supreme AI Council!** 🏛️

Your personal AI intelligence network is now online and ready to help you
achieve excellence across all Five Pillars of your life.

*"The only true wisdom is in knowing you know nothing." - Socrates*
