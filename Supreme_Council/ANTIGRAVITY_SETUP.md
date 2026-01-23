# Supreme AI Council - Antigravity Setup Guide

🚀 **ANTIGRAVITY VERSION** - Powered by the Antigravity Agent Runtime

This guide will help you set up and run your multi-agent Telegram bot system using the Antigravity architecture.

---

## What is Antigravity?

**Antigravity** is an agent runtime architecture that:
- **Separates agent configuration from implementation**
- Each agent is defined in JSON with its own system prompt
- Agents are managed by a central runtime orchestrator
- Supports agent-to-agent communication and delegation
- Integrates with MCP (Model Context Protocol) for Notion access

### Architecture Overview

```
┌──────────────────────────────────────────────────┐
│         Telegram Bots (Interface Layer)          │
│   (JENI, Aristóteles, Asklepai, etc.)           │
└─────────────────┬────────────────────────────────┘
                  │
┌─────────────────▼────────────────────────────────┐
│         Antigravity Runtime Manager              │
│  - Loads agent configurations                    │
│  - Routes messages to agents                     │
│  - Manages conversation history                  │
│  - Handles agent delegation                      │
└─────────────────┬────────────────────────────────┘
                  │
         ┌────────┴────────┐
         │                 │
┌────────▼──────┐  ┌──────▼───────┐
│  Claude API   │  │  MCP Servers │
│  (Anthropic)  │  │   (Notion)   │
└───────────────┘  └──────────────┘
```

---

## Quick Start

### 1. Prerequisites

✅ **Python 3.11+**
✅ **Telegram bot tokens** (from BotFather)
✅ **Anthropic API key**
✅ **Notion API key** (optional)

---

### 2. Installation

```bash
cd Supreme_Council

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

### 3. Agent Configuration

Your agents are already configured in the `agents/` directory:

```
agents/
├── jeni.agent.json          # Primary assistant
├── aristoteles.agent.json   # Strategic mentor
├── asklepai.agent.json      # Medical specialist
├── airquimides.agent.json   # Research specialist
├── seshait.agent.json       # Financial strategist
└── vulkain.agent.json       # System operations
```

#### Agent Configuration Structure

Each `.agent.json` file defines:

```json
{
  "name": "JENI",
  "description": "Primary Personal AI Assistant",
  "model": "claude-sonnet-4-20250514",
  "system_prompt_file": "../.agent/rules/JENI.md",
  "temperature": 0.7,
  "max_tokens": 4096,
  "tools": [
    {
      "type": "mcp",
      "server": "notion",
      "description": "Access to Notion databases"
    }
  ],
  "capabilities": [
    "task_coordination",
    "agent_delegation",
    "notion_integration"
  ],
  "routing": {
    "can_delegate_to": ["aristoteles", "asklepai", ...]
  }
}
```

**Key Components:**
- `system_prompt_file`: Points to your `.agent/rules/*.md` prompts
- `tools`: MCP servers this agent can use
- `routing`: Which agents this agent can delegate to

---

### 4. Environment Configuration

Create your `.env` file:

```bash
cp .env.example .env
nano .env
```

**Required variables:**

```bash
# Telegram Bot Tokens
JENI_BOT_TOKEN=8304075167:AAFIm8GA8Ocx-uEZi2SUmQArDG1zys5SHu4
ARISTOTELES_BOT_TOKEN=8511536107:AAEiRI271IxJCxE98JTC3ZqVH7vRs_zNG4M
ASKLEPAI_BOT_TOKEN=<get_from_botfather>
AIRQUIMIDES_BOT_TOKEN=<get_from_botfather>
SESHAIT_BOT_TOKEN=<get_from_botfather>
VULKAIN_BOT_TOKEN=<get_from_botfather>

# Anthropic API (REQUIRED)
ANTHROPIC_API_KEY=sk-ant-api03-your-key-here

# Notion API (Optional)
NOTION_API_KEY=secret_your_integration_key
NOTION_DATABASE_HUGAIN=<database_id>
NOTION_DATABASE_MANAI=<database_id>
NOTION_DATABASE_ODYSSAI=<database_id>
NOTION_DATABASE_WUWAI=<database_id>

# Security
MASTER_PIN_HASH=<generate_with_command_below>
```

**Generate PIN hash:**

```bash
python3 -c "import hashlib; print(hashlib.sha256('YOUR_PIN'.encode()).hexdigest())"
```

---

### 5. Launch Antigravity System

```bash
python3 main.py
```

**Expected Output:**

```
============================================================
🚀 Initializing Antigravity Runtime...
✅ Loaded agent: JENI
✅ Loaded agent: Aristoteles
✅ Loaded agent: Asklepai
✅ Loaded agent: Airquimides
✅ Loaded agent: Seshait
✅ Loaded agent: Vulkain
✅ Antigravity Runtime loaded with 6 agents
============================================================
🚀 SUPREME AI COUNCIL - INITIALIZATION
============================================================
✅ JENI bot registered successfully
✅ Aristóteles bot registered successfully
⚠️  Asklepai bot token not configured (skipping)
...
============================================================
📊 Active Bots: 2/6
============================================================
🔄 Starting in POLLING mode...
✨ SUPREME AI COUNCIL IS ONLINE
============================================================
```

---

## How Antigravity Works

### Message Flow

1. **User sends message** on Telegram to bot (e.g., JENI)
2. **Bot authenticates user** (PIN verification)
3. **Bot calls Antigravity Runtime** with message
4. **Runtime routes to correct agent** (e.g., "JENI")
5. **Agent loads its system prompt** from `.agent/rules/JENI.md`
6. **Agent calls Claude API** with prompt + message + history
7. **Response returned** through runtime → bot → user

### Agent Delegation Example

```python
User → JENI: "I need help with a difficult medical case"

JENI (thinks): "This requires medical expertise, I should delegate"
      ↓
JENI → Antigravity Runtime → Asklepai
      ↓
Asklepai: Provides detailed medical analysis
      ↓
JENI → User: Forwards Asklepai's response
```

---

## Customizing Agents

### Modify Agent Behavior

Edit the system prompts in `.agent/rules/`:

```bash
nano .agent/rules/JENI.md
```

**After editing:**
1. Restart `main.py`
2. Antigravity reloads all agent configurations
3. Changes take effect immediately

### Modify Agent Configuration

Edit the JSON config in `agents/`:

```bash
nano agents/jeni.agent.json
```

**You can change:**
- `temperature`: Creativity level (0.0 - 1.0)
- `max_tokens`: Response length
- `routing.can_delegate_to`: Which agents can be delegated to
- `capabilities`: List of agent capabilities

---

## Advanced Features

### Agent-to-Agent Communication

JENI can delegate to specialists:

```python
# In JENI's system prompt (.agent/rules/JENI.md)
"When you receive medical questions, delegate to Asklepai"
"For research queries, delegate to Airquimides"
"For strategic decisions, consult Aristóteles"
```

Delegation is handled through the Antigravity runtime's routing system.

### Conversation History

Each agent maintains conversation history per user:

- **Stateful**: Agent remembers context within conversation
- **Per-user**: Different users have separate histories
- **Configurable**: Last 10 messages kept by default

### MCP Integration (Notion)

Agents can access Notion through MCP:

```python
# Agent can:
- Query Notion databases
- Create new pages
- Update existing entries
- Track tasks, goals, contacts
```

**Configured in agent JSON:**
```json
"tools": [
  {
    "type": "mcp",
    "server": "notion",
    "description": "Access to Notion databases"
  }
]
```

---

## Troubleshooting

### "Agent 'XXX' not found in Antigravity runtime"

**Problem**: Agent configuration file missing or has errors

**Solution**:
```bash
# Check agents directory
ls agents/

# Verify JSON syntax
python3 -c "import json; print(json.load(open('agents/jeni.agent.json')))"
```

### "Failed to load system prompt"

**Problem**: System prompt file path is wrong

**Solution**:
```bash
# Check path in agent config
cat agents/jeni.agent.json | grep system_prompt_file

# Verify file exists
ls .agent/rules/JENI.md
```

### "ANTHROPIC_API_KEY not found"

**Problem**: Missing or invalid API key

**Solution**:
```bash
# Check .env file
cat .env | grep ANTHROPIC_API_KEY

# Verify it's loaded
python3 -c "from dotenv import load_dotenv; import os; load_dotenv(); print(os.getenv('ANTHROPIC_API_KEY'))"
```

---

## Architecture Deep Dive

### Antigravity Runtime Components

**1. AgentConfig** (`src/agents/antigravity_runtime.py`)
- Loads agent configuration from JSON
- Parses system prompts
- Validates settings

**2. AntigravityAgent**
- Wraps Claude API with agent-specific config
- Manages conversation history per user
- Handles temperature, max_tokens, etc.

**3. AntigravityRuntime**
- Central orchestrator (singleton)
- Loads all agents at startup
- Routes messages to correct agent
- Manages agent lifecycle

### File Structure

```
Supreme_Council/
├── agents/                     # Antigravity agent configs
│   ├── jeni.agent.json
│   ├── aristoteles.agent.json
│   └── ...
├── .agent/rules/              # System prompts (unchanged)
│   ├── JENI.md
│   ├── Aristoteles.md
│   └── ...
├── src/
│   ├── agents/
│   │   ├── antigravity_runtime.py  # Core runtime
│   │   └── __init__.py
│   ├── bots/
│   │   ├── base_bot.py        # Uses Antigravity
│   │   ├── jeni_bot.py
│   │   └── ...
│   └── mcp/
│       └── notion_client.py   # MCP integration
├── main.py                    # Initializes Antigravity
└── .env                       # Configuration
```

---

## Performance & Scaling

### Response Times

- **First message**: ~2-3 seconds (includes agent initialization)
- **Follow-up messages**: ~1-2 seconds (agent already loaded)
- **With Notion queries**: +0.5-1 second

### Concurrent Users

Antigravity handles multiple users concurrently:
- Each user has separate conversation history
- Agents are shared across users (singleton)
- Thread-safe conversation management

### Cost Optimization

**Tips to reduce API costs:**

1. **Use appropriate models**:
   - Simple tasks: `claude-haiku-4-20250514` (faster, cheaper)
   - Complex tasks: `claude-sonnet-4-20250514` (current default)

2. **Adjust max_tokens** in agent configs:
   ```json
   "max_tokens": 2048  // Instead of 4096 for shorter responses
   ```

3. **Limit conversation history**:
   - Currently keeps last 10 messages
   - Reduce for cost savings

---

## Next Steps

### ✅ You Now Have:

- 6 Antigravity-powered agents
- Telegram bot interface
- PIN authentication
- Notion integration (optional)
- Scalable architecture

### 🚀 To Expand:

1. **Add more agents**:
   - Create new `.agent.json` in `agents/`
   - Create system prompt in `.agent/rules/`
   - Get bot token from BotFather
   - Restart system

2. **Enable inter-agent communication**:
   - Implement delegation in system prompts
   - Use `routing.can_delegate_to` in configs

3. **Add MCP servers**:
   - Calendar integration
   - Email access
   - Custom databases

4. **Deploy to production**:
   - Follow `deployment/deployment_guide.md`
   - Use cloud server (Railway, Render, AWS)
   - Set up monitoring

---

## Support & Resources

**Documentation**:
- `SETUP.md` - Basic setup (non-Antigravity)
- `GETTING_STARTED.md` - Comprehensive guide
- `deployment/deployment_guide.md` - Production deployment

**Agent Prompts**:
- `.agent/rules/*.md` - Full system prompts

**Configuration**:
- `agents/*.agent.json` - Agent configs
- `.env.example` - Environment template

---

## Philosophy

Antigravity embodies the principle of **separation of concerns**:

- **Configuration** (JSON) is separate from **implementation** (code)
- **System prompts** define agent behavior, not hardcoded logic
- **Runtime** manages lifecycle, bots just interface
- **Scalable** - add new agents without touching core code

This makes your Supreme AI Council:
- ✅ Easy to modify (edit JSON, not code)
- ✅ Easy to extend (add new agents quickly)
- ✅ Easy to test (agents are isolated)
- ✅ Production-ready (robust runtime management)

---

**Welcome to the Antigravity-powered Supreme AI Council!** 🏛️⚡

Your personal multi-agent intelligence network, running on cutting-edge agent architecture.

*"We are what we repeatedly do. Excellence, then, is not an act, but a habit." - Aristotle*
