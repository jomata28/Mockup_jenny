# MCP Integration Guide - Model Context Protocol

**Version**: 1.0
**Last Updated**: 2026-01-19
**Purpose**: Configure and use Model Context Protocol for agent-database integration

---

## Overview

The Model Context Protocol (MCP) enables your Supreme AI Council agents to read and write to Notion databases, access files, browse the web, and interact with external APIs. This is the backbone of agent-database integration.

---

## What is MCP?

MCP is a protocol that allows AI agents to:
- **Query databases** (Notion, SQL, etc.)
- **Read/write files** (local filesystem)
- **Browse web** (for research)
- **Call APIs** (PubMed, financial data, etc.)
- **Execute tools** (custom integrations)

Think of MCP as the "hands" of your agents - it's how they manipulate the world outside their conversation context.

---

## MCP Architecture

```
┌─────────────────┐
│  Agent (JENI)   │
└────────┬────────┘
         │ Makes request
         ▼
┌─────────────────┐
│  MCP Protocol   │  ← Standard interface
└────────┬────────┘
         │
    ┌────┴─────────────────┬──────────────┐
    ▼                      ▼              ▼
┌─────────┐          ┌─────────┐    ┌─────────┐
│ Notion  │          │  File   │    │   Web   │
│  MCP    │          │ System  │    │ Browser │
│ Server  │          │   MCP   │    │   MCP   │
└────┬────┘          └─────────┘    └─────────┘
     │
     ▼
┌──────────────┐
│ Notion API   │
│  Databases   │
└──────────────┘
```

---

## MCP Server Configuration

### Location

MCP servers are configured in:
```
~/.config/claude-code/mcp_settings.json
```

Or for the Supreme AI Council agents specifically:
```
/home/user/Mockup_jenny/Supreme_Council/.mcp/config.json
```

### Configuration File Structure

```json
{
  "mcpServers": {
    "notion": {
      "command": "npx",
      "args": ["-y", "@notionhq/notion-mcp-server"],
      "env": {
        "NOTION_API_KEY": "${NOTION_API_KEY}"
      }
    },
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem"],
      "args": ["/home/user/Documents", "/home/user/Mockup_jenny"]
    },
    "web-browser": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-puppeteer"]
    }
  }
}
```

---

## Setting Up Notion MCP Server

### Step 1: Get Notion API Key

1. Go to https://www.notion.so/my-integrations
2. Click "New integration"
3. Name it: "Supreme AI Council"
4. Select your workspace
5. Copy the **Internal Integration Token** (starts with `secret_`)

### Step 2: Share Databases with Integration

For EACH database (Hugain, Manai, Odyssai, WuWai, etc.):
1. Open the database in Notion
2. Click "..." (three dots) → "Connections"
3. Search for "Supreme AI Council" integration
4. Click to connect

**Critical**: Do this for ALL databases your agents need to access.

### Step 3: Set Environment Variable

Add to your shell profile (`~/.bashrc` or `~/.zshrc`):
```bash
export NOTION_API_KEY="secret_your_actual_key_here"
```

Or use a `.env` file:
```bash
# Supreme_Council/.env
NOTION_API_KEY=secret_your_actual_key_here
```

**Security**: Never commit `.env` to git. Add to `.gitignore`.

### Step 4: Install Notion MCP Server

```bash
npm install -g @notionhq/notion-mcp-server
```

Or use `npx` (no install needed) as shown in config above.

### Step 5: Test Connection

```bash
# Test that Notion MCP server can start
npx @notionhq/notion-mcp-server

# Should see output like:
# Notion MCP Server started
# Connected to workspace: [Your Workspace Name]
```

---

## MCP Operations for Agents

### Query Notion Database

**Pattern**: Retrieve entries from a database

```python
# Pseudo-code (agents use this internally via MCP)
results = mcp.query_notion(
    database="Contacts",  # Database name or ID
    filter={
        "Status": "Active",
        "Connection_Strength": ["Inner Circle", "Close"]
    },
    sorts=[
        {"property": "Last_Contact", "direction": "ascending"}
    ],
    limit=10
)

# Returns array of database entries
for contact in results:
    print(contact.properties.Name)
    print(contact.properties.Last_Contact)
```

**Agent Usage Example** (JENI):
```
User: "Who do I need to reach out to this week?"

JENI queries Hugain:
- Filter: Next_Contact = this week
- Sort: By priority
- Returns: 5 contacts

JENI responds: "You have 5 people to connect with this week: [names]"
```

### Create Notion Page/Entry

**Pattern**: Add new entry to database

```python
mcp.create_notion_page(
    database="Daily_Energy_Log",
    properties={
        "Date": "2026-01-19",
        "Overall_Energy": "High",
        "Sleep_Quality": "Good",
        "Sleep_Hours": 7.5,
        "Morning_Energy": "High",
        "Meditation": 20,
        "Exercise": True
    }
)
```

**Agent Usage Example** (JENI):
```
User logs morning energy via Telegram

JENI creates entry in Manai:Daily_Energy_Log with data
JENI responds: "✓ Energy logged. Current streak: 15 days"
```

### Update Notion Page

**Pattern**: Modify existing entry

```python
mcp.update_notion_page(
    page_id="abc123...",  # ID of specific entry
    properties={
        "Status": "Completed",
        "Completed_Date": "2026-01-19"
    }
)
```

**Agent Usage Example** (JENI):
```
User: "Mark task 'Literature review' as done"

JENI finds task in Actions database
JENI updates Status → Completed
JENI responds: "✓ Marked complete. 3 tasks remaining today."
```

### Aggregate/Rollup Data

**Pattern**: Calculate statistics across entries

```python
# Get average energy for the week
avg_energy = mcp.aggregate_notion(
    database="Daily_Energy_Log",
    filter={"Date": "last_7_days"},
    aggregate="average",
    property="Overall_Energy"
)

# Count contacts by category
contact_counts = mcp.aggregate_notion(
    database="Contacts",
    group_by="Relationship_Type",
    aggregate="count"
)
```

**Agent Usage Example** (Aristóteles):
```
Weekly Pillar Balance calculation:
- Query all interactions this week
- Group by Pillar_Served
- Count hours per Pillar
- Flag if any Pillar got 0 attention
```

### Search Notion

**Pattern**: Full-text search across databases

```python
results = mcp.search_notion(
    query="AI radiology",
    filter={"property": "Type", "value": "Research"}
)
```

---

## Database ID Reference

Each Notion database has a unique ID. Store these for quick reference:

```json
{
  "databases": {
    "hugain": {
      "contacts": "DATABASE_ID_1",
      "interactions": "DATABASE_ID_2",
      "networking_goals": "DATABASE_ID_3"
    },
    "manai": {
      "daily_energy_log": "DATABASE_ID_4",
      "energy_patterns": "DATABASE_ID_5",
      "weekly_budget": "DATABASE_ID_6",
      "burnout_warnings": "DATABASE_ID_7",
      "recovery_activities": "DATABASE_ID_8"
    },
    "odyssai": {
      "adventures": "DATABASE_ID_9",
      "bucket_list": "DATABASE_ID_10",
      "travel_log": "DATABASE_ID_11"
    },
    "wuwai": {
      "practice_log": "DATABASE_ID_12",
      "wisdom_library": "DATABASE_ID_13",
      "reflections": "DATABASE_ID_14",
      "values": "DATABASE_ID_15",
      "purpose": "DATABASE_ID_16"
    }
  }
}
```

**How to get Database ID**:
1. Open database in Notion
2. Look at URL: `https://notion.so/[DATABASE_ID]?v=...`
3. Copy the ID (32 characters, letters/numbers)

Store in: `Supreme_Council/.mcp/database_ids.json`

---

## Additional MCP Servers

### File System Access

For reading local documents, research papers, etc.

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/home/user/Documents",
        "/home/user/Research",
        "/home/user/Mockup_jenny"
      ]
    }
  }
}
```

**Agent Usage** (Airquimides):
- Read research PDFs from local storage
- Access paper notes
- Reference saved articles

### Web Browser (Puppeteer)

For live web research and monitoring.

```json
{
  "mcpServers": {
    "puppeteer": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-puppeteer"]
    }
  }
}
```

**Agent Usage**:
- Airquimides: Check journal websites for new papers
- Seshait: Monitor financial data sources
- All: Fetch web content when needed

### PubMed API (Custom)

For medical literature search (Airquimides, Asklepai).

You'll need to create a custom MCP server:
```javascript
// pubmed-mcp-server.js
import { MCPServer } from '@modelcontextprotocol/sdk';

const server = new MCPServer({
  name: 'pubmed',
  version: '1.0.0'
});

server.tool('search_pubmed', async (params) => {
  const { query, max_results } = params;
  // Call PubMed E-utilities API
  const response = await fetch(
    `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=${query}&retmax=${max_results}&retmode=json`
  );
  return response.json();
});

server.start();
```

**Configuration**:
```json
{
  "mcpServers": {
    "pubmed": {
      "command": "node",
      "args": ["/path/to/pubmed-mcp-server.js"]
    }
  }
}
```

---

## Error Handling

### Common Errors

**1. "Notion integration not found"**
- Solution: Share database with integration in Notion settings

**2. "Invalid API key"**
- Solution: Check `NOTION_API_KEY` environment variable is set correctly

**3. "Property not found"**
- Solution: Verify property name matches exactly (case-sensitive)

**4. "Rate limit exceeded"**
- Solution: Implement rate limiting in agent code (max 3 requests/second to Notion)

**5. "MCP server not responding"**
- Solution: Check if server process is running, restart if needed

### Agent Error Handling Pattern

```python
try:
    results = mcp.query_notion(database="Contacts", filter={...})
except MCPConnectionError:
    # MCP server not reachable
    log_error("MCP connection failed")
    notify_vulkain("Notion MCP server down")
    fallback_to_cached_data()
except NotionAPIError as e:
    # Notion API returned error
    if e.code == "rate_limited":
        wait_and_retry()
    elif e.code == "unauthorized":
        notify_vulkain("Notion integration auth issue")
    else:
        log_error(f"Notion API error: {e}")
except Exception as e:
    # Unexpected error
    log_error(f"Unexpected MCP error: {e}")
    alert_user("Temporary database access issue")
```

---

## Rate Limits & Best Practices

### Notion API Limits

- **Rate Limit**: 3 requests per second
- **Best Practice**: Batch queries when possible
- **Caching**: Cache frequently accessed data locally

### Optimization Strategies

**1. Batch Reads**
```python
# Bad: Multiple separate queries
contact1 = mcp.get_notion_page(id1)
contact2 = mcp.get_notion_page(id2)
contact3 = mcp.get_notion_page(id3)

# Good: Single query with multiple results
contacts = mcp.query_notion(
    database="Contacts",
    filter={"ID": ["id1", "id2", "id3"]}
)
```

**2. Use Rollups Instead of Calculations**
```python
# Bad: Query all interactions, calculate in code
interactions = mcp.query_notion(database="Interactions", filter={"Contact": contact_id})
total_time = sum([i.duration for i in interactions])

# Good: Use Notion rollup property (pre-calculated)
contact = mcp.get_notion_page(contact_id)
total_time = contact.properties.Total_Time_Spent  # Rollup field
```

**3. Cache Non-Changing Data**
```python
# Cache Values, Purpose statements, Energy Patterns
# These change rarely - don't query every time
cache_values = load_from_cache("values")
if cache_is_stale(cache_values, max_age_hours=24):
    cache_values = mcp.query_notion(database="Values")
    save_to_cache("values", cache_values)
```

---

## Security Considerations

### API Key Storage

**Never**:
- ❌ Hard-code API keys in agent code
- ❌ Commit keys to git
- ❌ Share keys in messages/logs
- ❌ Store keys in plain text

**Always**:
- ✅ Use environment variables
- ✅ Use `.env` files (gitignored)
- ✅ Rotate keys quarterly
- ✅ Use minimum necessary permissions

### Data Privacy

**HIPAA Awareness**:
- Never store PHI (Protected Health Information) in Notion
- De-identify patient cases before logging
- Use pseudonyms, aggregate data
- Asklepai enforces this in clinical case discussions

**Financial Data**:
- Notion has encryption at rest and in transit
- Still, don't store:
  - Full credit card numbers
  - Social security numbers
  - Account passwords
- Store account nicknames, not account numbers

---

## Testing MCP Integration

### Test Checklist

Before deploying agents to production:

- [ ] Notion MCP server starts without errors
- [ ] Can query each database (Hugain, Manai, Odyssai, WuWai)
- [ ] Can create new entries in each database
- [ ] Can update existing entries
- [ ] Rollups calculate correctly
- [ ] Relations between databases work
- [ ] Rate limiting doesn't cause errors
- [ ] Error handling gracefully manages failures
- [ ] No API keys exposed in logs

### Test Script

```bash
#!/bin/bash
# test_mcp_integration.sh

echo "Testing Notion MCP Integration..."

# Test 1: Server starts
echo "1. Starting Notion MCP server..."
npx @notionhq/notion-mcp-server &
MCP_PID=$!
sleep 3
if ps -p $MCP_PID > /dev/null; then
   echo "✓ MCP server started (PID: $MCP_PID)"
else
   echo "✗ MCP server failed to start"
   exit 1
fi

# Test 2: Query database (requires agent to be running)
echo "2. Testing database query..."
# (Call agent to query Contacts database)

# Test 3: Create entry
echo "3. Testing create entry..."
# (Call agent to create test entry)

# Test 4: Update entry
echo "4. Testing update..."
# (Call agent to update test entry)

# Test 5: Delete test entry
echo "5. Cleaning up..."
# (Delete test entries)

echo "All tests passed ✓"
kill $MCP_PID
```

---

## Monitoring & Maintenance

### Logs to Monitor

**MCP Server Logs**:
```
~/.config/claude-code/mcp_logs/notion.log
```

Watch for:
- Connection errors
- Rate limit warnings
- API key expiration
- Slow queries (>2 seconds)

**Agent Logs** (Vulkain monitors these):
```
Supreme_Council/logs/jeni.log
Supreme_Council/logs/aristoteles.log
[etc. for each agent]
```

### Weekly MCP Health Check

Vulkain runs this automatically:

```python
# Weekly MCP health check
def mcp_health_check():
    checks = {
        "notion_connection": test_notion_connection(),
        "query_performance": measure_query_speed(),
        "error_rate": calculate_error_rate_last_week(),
        "api_quota": check_notion_api_quota()
    }

    if any(check == "unhealthy" for check in checks.values()):
        alert_user("MCP health issues detected")
        generate_diagnostic_report()
```

---

## Troubleshooting Guide

### Problem: Agents can't access Notion

**Diagnosis Steps**:
1. Check if NOTION_API_KEY is set: `echo $NOTION_API_KEY`
2. Verify integration has access to databases in Notion
3. Test MCP server manually: `npx @notionhq/notion-mcp-server`
4. Check agent logs for specific error messages

### Problem: Slow database queries

**Solutions**:
- Reduce query scope (use date filters)
- Increase use of cached data
- Use database views instead of filters
- Check if Notion is experiencing outages

### Problem: Rate limiting errors

**Solutions**:
- Implement exponential backoff
- Reduce query frequency
- Batch operations where possible
- Cache aggressively

---

## Advanced: Custom MCP Tools

You can build custom MCP tools for specialized needs.

**Example: Medical Journal Monitor**

```javascript
// medical-journal-mcp.js
import { MCPServer } from '@modelcontextprotocol/sdk';

const server = new MCPServer({ name: 'medical-journals' });

server.tool('check_new_papers', async (params) => {
  const { specialty, keywords, since_date } = params;

  // Query multiple journal APIs
  const nejm = await fetch_nejm(specialty, since_date);
  const lancet = await fetch_lancet(specialty, since_date);
  const jama = await fetch_jama(specialty, since_date);

  // Combine and filter by keywords
  const all_papers = [...nejm, ...lancet, ...jama];
  const relevant = filter_by_keywords(all_papers, keywords);

  return {
    count: relevant.length,
    papers: relevant.slice(0, 10),  // Top 10
    summary: generate_summary(relevant)
  };
});

server.start();
```

**Agent Usage** (Airquimides):
```
Weekly routine:
- Call medical-journals MCP tool
- Get new papers in user's specialty
- Add top papers to Notion Literature database
- Alert user if highly relevant paper found
```

---

## Resources

- **MCP Documentation**: https://github.com/modelcontextprotocol/specification
- **Notion API Reference**: https://developers.notion.com
- **Claude Agent SDK**: (Antigravity documentation)
- **MCP Server Examples**: https://github.com/modelcontextprotocol/servers

---

## Quick Reference

**Start MCP Server**:
```bash
npx @notionhq/notion-mcp-server
```

**Test Notion Connection**:
```bash
curl -H "Authorization: Bearer $NOTION_API_KEY" \
     -H "Notion-Version: 2022-06-28" \
     https://api.notion.com/v1/databases/DATABASE_ID/query
```

**Environment Variables**:
```bash
export NOTION_API_KEY="secret_..."
export MCP_LOG_LEVEL="info"
```

---

*MCP is the bridge between your agents' intelligence and your data. Protect it, monitor it, optimize it.*
