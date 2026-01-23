# Supreme AI Council - Gemini Antigravity Setup

🚀 **GEMINI-POWERED ANTIGRAVITY** - Your multi-agent system running on Google Gemini

This guide will help you set up and run your Supreme AI Council using Google's Gemini API instead of Claude.

---

## Why Gemini 2.0?

✅ **FREE TIER**: 15 requests/minute, 1500 requests/day (generous!)
✅ **LATEST MODEL**: Gemini 2.0 Flash Experimental (cutting edge!)
✅ **MULTIMODAL**: Native image, video, audio support
✅ **LONG CONTEXT**: 1M+ token context window
✅ **BLAZING FAST**: Optimized for speed with flash architecture
✅ **COST-EFFECTIVE**: Very competitive pricing
✅ **IMPROVED QUALITY**: Better reasoning and understanding than 1.5

---

## Quick Start (5 Minutes)

### 1. Get Gemini API Key

1. Go to **https://aistudio.google.com/app/apikey**
2. Click **"Create API Key"** or **"Get API key"**
3. Select **"Create API key in new project"** (or use existing project)
4. Copy your API key (starts with `AIza...`)

**It's that easy!** No credit card required for free tier.

---

### 2. Install Dependencies

```bash
cd Supreme_Council

# Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install all dependencies
pip install -r requirements.txt
```

---

### 3. Configure Environment

```bash
# Copy template
cp .env.example .env

# Edit configuration
nano .env  # or use your preferred editor
```

**Add these values:**

```bash
# ============================================
# GOOGLE GEMINI API (REQUIRED)
# ============================================
GEMINI_API_KEY=AIzaSy...your_key_here

# ============================================
# TELEGRAM BOT TOKENS (You already have 2)
# ============================================
JENI_BOT_TOKEN=8304075167:AAFIm8GA8Ocx-uEZi2SUmQArDG1zys5SHu4
ARISTOTELES_BOT_TOKEN=8511536107:AAEiRI271IxJCxE98JTC3ZqVH7vRs_zNG4M

# Get these from BotFather (optional for now)
ASKLEPAI_BOT_TOKEN=your_token_here
AIRQUIMIDES_BOT_TOKEN=your_token_here
SESHAIT_BOT_TOKEN=your_token_here
VULKAIN_BOT_TOKEN=your_token_here

# ============================================
# SECURITY
# ============================================
# Generate PIN hash:
MASTER_PIN_HASH=<generate_below>
```

**Generate PIN hash:**
```bash
python3 -c "import hashlib; print(hashlib.sha256('YOUR_PIN'.encode()).hexdigest())"
```

Example:
```bash
python3 -c "import hashlib; print(hashlib.sha256('123456'.encode()).hexdigest())"
# Output: 8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92
```

---

### 4. Launch Your Bots!

```bash
python3 main.py
```

**Expected output:**

```
🚀 Initializing Antigravity Runtime...
Antigravity Runtime initialized with Gemini
✅ Loaded agent: JENI
✅ Loaded agent: Aristoteles
✅ Loaded agent: Asklepai
✅ Loaded agent: Airquimides
✅ Loaded agent: Seshait
✅ Loaded agent: Vulkain
📊 Loaded 6 agents
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
✨ SUPREME AI COUNCIL IS ONLINE
============================================================
```

---

### 5. Test on Telegram

1. Open Telegram
2. Search for your bot (e.g., `@YourJENIBot`)
3. Send `/start`
4. Authenticate: `/auth YOUR_PIN`
5. Start chatting!

Example:
```
You: /start
JENI: 🌟 Welcome to JENI 🌟

You: /auth 123456
JENI: ✅ Authentication successful!

You: What's the capital of France?
JENI: The capital of France is Paris. It's one of the most...
```

---

## Gemini Models Explained

Your agents use **`gemini-2.0-flash-exp`** by default. Here are your options:

### Available Models

| Model | Best For | Speed | Quality | Context |
|-------|----------|-------|---------|---------|
| `gemini-2.0-flash-exp` | 🚀 **LATEST!** Best all-around | Very Fast | ⭐⭐⭐⭐⭐ | 1M tokens |
| `gemini-1.5-pro` | Complex reasoning tasks | Medium | ⭐⭐⭐⭐⭐ | 2M tokens |
| `gemini-1.5-flash` | Quick responses, high throughput | Fast | ⭐⭐⭐⭐ | 1M tokens |

**Current setup**: All agents use `gemini-2.0-flash-exp` (latest experimental model!)

### Change Model Per Agent

Edit `agents/*.agent.json`:

```json
{
  "name": "JENI",
  "model": "gemini-1.5-flash",  // ← Change this
  "temperature": 0.7,
  ...
}
```

**Restart bots** to apply changes.

---

## Architecture Overview

```
┌──────────────────────────────────────────┐
│     Telegram Bots (JENI, Aristoteles)   │
└──────────────────┬───────────────────────┘
                   │
┌──────────────────▼───────────────────────┐
│      Antigravity Runtime Manager         │
│  - Loads agent configs from agents/      │
│  - Reads system prompts from .agent/     │
│  - Routes messages to correct agent      │
│  - Manages conversation history          │
└──────────────────┬───────────────────────┘
                   │
┌──────────────────▼───────────────────────┐
│         Google Gemini API                │
│  - gemini-2.0-flash-exp model                  │
│  - System instructions (your prompts)    │
│  - Chat sessions per user                │
└──────────────────┬───────────────────────┘
                   │
┌──────────────────▼───────────────────────┐
│     Optional: MCP → Notion Databases     │
└──────────────────────────────────────────┘
```

### How It Works

1. **User messages bot** on Telegram → JENI receives "What should I focus on today?"
2. **Bot authenticates user** → Checks PIN hash
3. **Bot calls Antigravity** → `runtime.route_message("JENI", user_id, message)`
4. **Runtime loads agent** → Reads `agents/jeni.agent.json` + `.agent/rules/JENI.md`
5. **Creates Gemini chat** → New chat session with system instructions
6. **Sends to Gemini** → User message + conversation history
7. **Returns response** → Gemini generates response → Bot → User

**Stateful**: Each agent remembers conversation history per user!

---

## Configuration Files

### Agent Configurations (`agents/`)

Each `.agent.json` file defines:

```json
{
  "name": "JENI",
  "description": "Primary Personal AI Assistant",
  "model": "gemini-2.0-flash-exp",                    // Gemini model
  "system_prompt_file": "../.agent/rules/JENI.md",  // System instructions
  "temperature": 0.7,                           // Creativity (0.0 - 1.0)
  "max_tokens": 4096,                          // Max response length
  "tools": [...],                              // MCP tools (Notion, etc.)
  "capabilities": [...],                       // Agent capabilities
  "routing": {                                 // Agent delegation rules
    "can_delegate_to": ["aristoteles", ...]
  }
}
```

### System Prompts (`.agent/rules/`)

These **huge markdown files** define each agent's personality:

- `JENI.md` - Primary assistant instructions
- `Aristoteles.md` - Strategic mentor instructions
- `Asklepai.md` - Medical specialist instructions
- etc.

**These are loaded automatically** by Antigravity and sent as `system_instruction` to Gemini.

---

## Customization

### Change Agent Personality

1. Edit the system prompt:
   ```bash
   nano .agent/rules/JENI.md
   ```

2. Restart bots:
   ```bash
   python3 main.py
   ```

Changes apply immediately!

### Change Agent Behavior

Edit `agents/jeni.agent.json`:

```json
{
  "temperature": 0.9,     // More creative
  "max_tokens": 8192,     // Longer responses
  "model": "gemini-1.5-flash"  // Faster responses
}
```

### Add New Agent

1. **Create system prompt**: `.agent/rules/NewAgent.md`
2. **Create config**: `agents/newagent.agent.json`
3. **Get bot token**: BotFather → `/newbot`
4. **Add to .env**: `NEWAGENT_BOT_TOKEN=...`
5. **Create bot class**: `src/bots/newagent_bot.py`
6. **Import in main.py**
7. **Restart**

That's it!

---

## Notion Integration (Optional)

Your agents can access Notion databases through MCP:

### Setup Notion

1. Create Notion integration: https://www.notion.so/my-integrations
2. Copy integration token (starts with `secret_`)
3. Share databases with integration
4. Get database IDs from URLs
5. Add to `.env`:
   ```bash
   NOTION_API_KEY=secret_...
   NOTION_DATABASE_HUGAIN=abc123...
   NOTION_DATABASE_MANAI=def456...
   NOTION_DATABASE_ODYSSAI=ghi789...
   NOTION_DATABASE_WUWAI=jkl012...
   ```

### Use in Conversation

```
You: Add a new contact to my CRM
JENI: I've added [Name] to your Hugain CRM database!
      [Shows Notion page link]
```

*(Not yet fully implemented - MCP integration coming soon)*

---

## Troubleshooting

### "GEMINI_API_KEY not found"

**Problem**: Missing or invalid API key

**Solution**:
```bash
# Check .env file
cat .env | grep GEMINI_API_KEY

# Verify it's loaded
python3 -c "from dotenv import load_dotenv; import os; load_dotenv(); print(os.getenv('GEMINI_API_KEY'))"
```

Should show your API key (starts with `AIza...`)

### "Agent 'XXX' not found in Antigravity runtime"

**Problem**: Agent config file missing or broken

**Solution**:
```bash
# Check agents directory
ls agents/

# Verify JSON syntax
python3 -c "import json; print(json.load(open('agents/jeni.agent.json')))"
```

### "Authentication failed!"

**Problem**: Wrong PIN or incorrect hash

**Solution**:
```bash
# Regenerate hash
python3 -c "import hashlib; print(hashlib.sha256('YOUR_PIN'.encode()).hexdigest())"

# Update in .env
MASTER_PIN_HASH=<paste_new_hash>

# Restart bots
python3 main.py
```

### Bot not responding

**Checklist**:
1. ✅ Is `main.py` still running?
2. ✅ Did you authenticate? `/auth YOUR_PIN`
3. ✅ Is GEMINI_API_KEY valid?
4. ✅ Check terminal for error messages

### Gemini Rate Limits

**Free tier limits**:
- 15 requests/minute
- 1500 requests/day
- 1M tokens/minute

**If you hit limits**:
- Wait a minute
- Reduce bot usage
- Upgrade to paid tier (very cheap)

---

## Gemini vs Claude Comparison

| Feature | Gemini 1.5 Pro | Claude Sonnet 4 |
|---------|----------------|-----------------|
| **Free tier** | ✅ Generous (1500/day) | ❌ None |
| **Cost** | $$ Cheap | $$$ Expensive |
| **Context** | 2M tokens | 200K tokens |
| **Speed** | Fast | Very fast |
| **Quality** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Multimodal** | ✅ Yes | ⚠️ Limited |
| **Long text** | ✅ Excellent | ✅ Excellent |

**Bottom line**: Gemini is **perfect** for this project. Free, fast, and capable!

---

## Advanced Features

### Conversation History

Each agent remembers your conversation:

```
You: What's my name?
JENI: You haven't told me yet! What would you like me to call you?

You: Call me John
JENI: Got it, John! Nice to meet you.

You: What's my name?
JENI: Your name is John!
```

**Per-user, per-agent** - different users have separate histories.

### Agent Delegation

JENI can delegate to specialists (coming soon):

```
You (to JENI): I have a medical question about...
JENI: Let me consult Asklepai for this medical question...
      [Routes to Asklepai agent internally]
      [Returns Asklepai's response]
```

### Clear History

```python
# In code (add as /reset command if desired)
runtime = get_runtime()
agent = runtime.get_agent("jeni")
agent.clear_history(user_id)
```

---

## Cost Estimates

### Gemini Pricing (if you exceed free tier)

**Input**: $0.000125 per 1K characters (~$0.50 per 4M chars)
**Output**: $0.000375 per 1K characters (~$1.50 per 4M chars)

**Example daily usage**:
- 100 conversations/day
- Average 500 chars input + 1500 chars output per conversation
- **Cost**: ~$0.08/day = **$2.40/month**

**Extremely affordable!**

---

## What You Built 🎉

✅ **Multi-agent Telegram bot system**
✅ **6 specialized AI agents** (JENI, Aristóteles, Asklepai, etc.)
✅ **Antigravity runtime** (agent orchestration)
✅ **Gemini API integration** (free tier available!)
✅ **Stateful conversations** (remembers context)
✅ **PIN authentication** (secure access)
✅ **Scalable architecture** (easy to extend)
✅ **Notion integration ready** (optional MCP)

---

## Next Steps

### ✅ Phase 1: Basic System (YOU ARE HERE)
- 2 bots running (JENI + Aristóteles)
- Gemini API working
- Authentication working
- Conversations working

### 🚀 Phase 2: Full Council (Get remaining tokens)
- Get 4 more bot tokens from BotFather
- Add to `.env`
- Restart → 6 agents online!

### 🔧 Phase 3: Notion Integration
- Set up Notion API
- Connect databases
- Enable CRM, task tracking, etc.

### 🌐 Phase 4: Production Deployment
- Deploy to cloud server (Railway, Render)
- 24/7 operation
- Monitoring & logging
- Follow `deployment/deployment_guide.md`

---

## Support

**Documentation**:
- `GEMINI_SETUP.md` ← You are here
- `ANTIGRAVITY_SETUP.md` - Detailed architecture guide
- `GETTING_STARTED.md` - Original comprehensive guide
- `.agent/rules/*.md` - Agent system prompts

**Get Help**:
- Check terminal logs for errors
- Review agent configs in `agents/`
- Test Gemini API separately: https://aistudio.google.com

---

## Why This Is Awesome

🎯 **Agent-based architecture** - Each agent is a specialist
🧠 **Powered by Gemini** - Google's best AI, free tier
📱 **Telegram interface** - Chat from anywhere
🔐 **Secure** - PIN authentication
💾 **Stateful** - Remembers conversations
🎨 **Customizable** - Edit JSON configs, not code
🚀 **Scalable** - Add agents easily
🆓 **FREE** - Gemini free tier is generous

---

## Quick Reference

### Launch Bots
```bash
python3 main.py
```

### Test Gemini API
```bash
python3 -c "import google.generativeai as genai; import os; from dotenv import load_dotenv; load_dotenv(); genai.configure(api_key=os.getenv('GEMINI_API_KEY')); model = genai.GenerativeModel('gemini-2.0-flash-exp'); response = model.generate_content('Hello'); print(response.text)"
```

### Check Loaded Agents
```bash
python3 -c "from src.agents.antigravity_runtime import get_runtime; r = get_runtime(); print(f'Agents: {r.list_agents()}')"
```

### Generate PIN Hash
```bash
python3 -c "import hashlib; print(hashlib.sha256('YOUR_PIN'.encode()).hexdigest())"
```

---

**Welcome to your Gemini-powered Supreme AI Council!** 🏛️✨

Your personal multi-agent intelligence network is ready to help you achieve excellence across all Five Pillars of your life.

*"The only way to do great work is to love what you do." - Steve Jobs*
