# Hugain - Personal & Professional CRM Database Schema

**Vault Name**: Hugain
**Purpose**: Track and nurture personal and professional relationships
**Primary Agent**: JENI (with input from all agents)
**Pillar Served**: Vitality & Connection

---

## Database: Contacts

**Description**: Master database of all people in your network

### Properties

| Property Name | Type | Description | Agent Usage |
|---------------|------|-------------|-------------|
| **Name** | Title | Full name of contact | All agents for reference |
| **Relationship Type** | Multi-select | Personal, Professional, Medical, Research, AI Business, Mentor, Mentee, Family | JENI categorizes; Agents filter |
| **Connection Strength** | Select | Inner Circle, Close, Regular, Acquaintance, Dormant | JENI tracks; Aristóteles monitors for Pillar health |
| **Organization** | Text | Employer, institution, or affiliation | Asklepai (medical network), Airquimides (research network) |
| **Role/Title** | Text | Their position or role | All agents |
| **Email** | Email | Primary email address | JENI for outreach |
| **Phone** | Phone | Phone number | JENI for communication |
| **LinkedIn** | URL | LinkedIn profile | Seshait (business networking) |
| **Tags** | Multi-select | Skill areas, shared interests, conference met, etc. | All agents filter by relevant tags |
| **Pillar Relevance** | Multi-select | Which of your 5 Pillars this person supports | Aristóteles ensures Pillar balance in network |
| **Last Contact** | Date | Last meaningful interaction | JENI alerts if dormant too long |
| **Next Contact** | Date | Planned next touchpoint | JENI schedules and reminds |
| **Contact Frequency** | Select | Weekly, Monthly, Quarterly, Annually, As-Needed | JENI enforces relationship rhythm |
| **Value Exchange** | Select | Mutual Mentorship, Learning, Collaboration, Social, Referrals | Understand relationship dynamic |
| **Location** | Text | City, state/country | For in-person meetups |
| **Birthday** | Date | For relationship maintenance | JENI sends reminders |
| **How We Met** | Text | Origin story of relationship | Context for all agents |
| **Conversation History** | Relation → Interactions | Links to interaction log | JENI maintains; all review |
| **Projects Together** | Relation → Projects | Shared work | Airquimides (research), Seshait (business) |
| **Notes** | Text (long) | Free-form notes, context, important details | All agents read for context |
| **Referral Potential** | Select | High, Medium, Low, N/A | Seshait for business development |
| **Give Value To Them** | Text | How you can help them | Relationship reciprocity tracking |
| **Get Value From Them** | Text | How they help you | Relationship reciprocity tracking |
| **Status** | Select | Active, On Hold, Dormant, Archived | JENI manages contact lifecycle |
| **Created Date** | Created Time | When added to CRM | All agents |
| **Last Updated** | Last Edited Time | Most recent modification | All agents |

---

## Database: Interactions

**Description**: Log of all meaningful interactions with contacts

### Properties

| Property Name | Type | Description | Agent Usage |
|---------------|------|-------------|-------------|
| **Title** | Title | Brief description (e.g., "Coffee with John - Discussed AI collaboration") | JENI creates; all review |
| **Contact** | Relation → Contacts | Who you interacted with | Links to master contact |
| **Date** | Date | When interaction occurred | JENI for tracking |
| **Interaction Type** | Select | Meeting (In-Person), Meeting (Virtual), Phone Call, Email, Text/Message, Conference, Social Event | JENI categorizes |
| **Duration** | Number | Minutes spent | Manai integration (energy/time) |
| **Pillar Served** | Multi-select | Which Pillar(s) this interaction supported | Aristóteles for balance |
| **Quality** | Select | High Value, Good, Neutral, Low Value | Relationship ROI tracking |
| **Key Topics** | Multi-select | What was discussed | Searchable by agents |
| **Action Items** | Text | Follow-ups needed | JENI converts to tasks |
| **Insights Gained** | Text (long) | What you learned or realized | All agents reference |
| **Value Given** | Text | How you helped them | Track giving |
| **Value Received** | Text | How they helped you | Track receiving |
| **Next Steps** | Text | What happens next | JENI tracks |
| **Energy Impact** | Select | Energizing, Neutral, Draining | Manai vault link for energy management |
| **Created By** | Created By | Auto-filled | Audit trail |
| **Created Date** | Created Time | When logged | All agents |

---

## Database: Networking Goals

**Description**: Intentional relationship-building objectives

### Properties

| Property Name | Type | Description | Agent Usage |
|---------------|------|-------------|-------------|
| **Goal** | Title | What you want to achieve (e.g., "Connect with 5 AI researchers in oncology") | Aristóteles validates; JENI executes |
| **Pillar** | Select | Which Pillar this serves | Aristóteles ensures alignment |
| **Target Date** | Date | When you want to achieve this | JENI tracks deadlines |
| **Status** | Select | Active, On Track, Behind, Completed, Paused | JENI monitors |
| **Progress** | Number | % complete (0-100) | Visual progress tracking |
| **Target Contacts** | Relation → Contacts | Specific people to connect with | JENI prioritizes |
| **Strategies** | Text | How you'll achieve this | JENI and relevant specialist collaborate |
| **Why This Matters** | Text | Purpose and motivation | Aristóteles references |
| **Success Criteria** | Text | How you'll know you've succeeded | All agents |
| **Completed Date** | Date | When achieved | Historical tracking |

---

## Relations & Rollups

### Contact → Interactions Rollup

**In Contacts Database**:
- **Total Interactions** (Rollup): Count of related interactions
- **Last Interaction Date** (Rollup): Max date from interactions
- **Average Interaction Quality** (Rollup): Average of quality scores
- **Total Time Spent** (Rollup): Sum of interaction durations

These rollups help JENI identify:
- Relationships that need attention (low interaction count)
- VIP contacts (high interaction frequency & quality)
- Energy drains (consistently draining interactions)

---

## Database Views for Agents

### JENI's Views

1. **Need Attention** - Contacts where Last Contact > Contact Frequency threshold
2. **This Week's Contacts** - Next Contact = this week
3. **VIPs** - Connection Strength = Inner Circle or Close
4. **By Pillar** - Grouped by Pillar Relevance

### Aristóteles' Views

1. **Pillar Balance** - Contacts grouped by Pillar, showing distribution
2. **Value Alignment** - Filter for contacts aligned with values
3. **Network Health** - Dashboard view of connection strength distribution

### Asklepai's Views

1. **Medical Network** - Relationship Type contains "Medical"
2. **Mentors in Medicine** - Role/Title contains clinical/academic terms + Mentor tag
3. **Collaboration Opportunities** - Medical contacts with projects

### Airquimides' Views

1. **Research Network** - Relationship Type contains "Research"
2. **Potential Collaborators** - Research contacts with high value exchange
3. **Academic Mentors** - Research + Mentor tags

### Seshait's Views

1. **Business Network** - Relationship Type contains "AI Business"
2. **High Referral Potential** - Referral Potential = High
3. **Client Pipeline** - Business contacts by status

---

## Agent Integration Patterns

### JENI - Relationship Maintenance

**Daily Check**:
```python
# Check for contacts needing attention
contacts_due = mcp.query_notion(
    database="Contacts",
    filter={
        "Status": "Active",
        "Next_Contact": "today"
    }
)

# Alert user
for contact in contacts_due:
    send_reminder(f"Reach out to {contact.name} today")
```

**Weekly Dormant Alert**:
```python
# Find relationships going dormant
dormant_risks = mcp.query_notion(
    database="Contacts",
    filter={
        "Connection_Strength": ["Inner Circle", "Close"],
        "Last_Contact": "<30_days_ago"
    }
)

if dormant_risks:
    alert_user("Important relationships need attention")
```

### Aristóteles - Pillar Balance Check

**Monthly Pillar Distribution**:
```python
# Analyze network by Pillar
pillar_distribution = mcp.aggregate_notion(
    database="Interactions",
    filter={"Date": "last_30_days"},
    group_by="Pillar_Served"
)

# Check if Vitality & Connection Pillar healthy
if connection_pillar_health < threshold:
    flag_to_aristoteles("Vitality & Connection Pillar neglected")
```

### Seshait - Business Network ROI

**Quarterly Business Network Value**:
```python
# Identify high-value business contacts
business_contacts = mcp.query_notion(
    database="Contacts",
    filter={
        "Relationship_Type": "AI Business",
        "Referral_Potential": "High"
    }
)

# Cross-reference with AI projects revenue
# Suggest outreach strategy
```

---

## Sample Data (for setup)

### Example Contact Entry

```
Name: Dr. Sarah Chen
Relationship Type: Professional, Medical, Research
Connection Strength: Close
Organization: Stanford Medical Center
Role/Title: Professor of Radiology, AI Research Lead
Tags: AI, Radiology, Mentor, Conference-RSNA2025
Pillar Relevance: Healing Mastery, Scientific Legacy, Vitality & Connection
Last Contact: 2026-01-10
Next Contact: 2026-02-10
Contact Frequency: Monthly
Value Exchange: Mutual Mentorship
Location: Palo Alto, CA
How We Met: RSNA conference 2024, connected over AI in radiology panel
Notes: Expert in lung cancer screening AI. Has NIH R01 grant. Open to collaboration on implementation research. Loves hiking.
Referral Potential: High (knows many AI health tech companies)
Give Value To Them: Share clinical insights, patient perspective on AI
Get Value From Them: Research mentorship, grant writing advice, academic network access
Status: Active
```

### Example Interaction Entry

```
Title: Video call with Dr. Chen - Discussed lung cancer AI collaboration
Contact: Dr. Sarah Chen
Date: 2026-01-10
Interaction Type: Meeting (Virtual)
Duration: 60
Pillar Served: Scientific Legacy, Vitality & Connection
Quality: High Value
Key Topics: AI Radiology, Research Collaboration, Grant Opportunities
Action Items:
- Draft research proposal outline by Jan 20
- Intro to her postdoc (contact: Michael Torres)
- Review her latest paper before Feb meeting
Insights Gained: Implementation research is underfunded but high-impact. She has connections at NIH program officers.
Value Given: Shared clinical perspective on AI integration barriers
Value Received: Research mentorship, potential collaboration, network intro
Next Steps: Send proposal outline, schedule Feb follow-up
Energy Impact: Energizing
```

---

## Gamification & Insights (Optional)

**Relationship Insights JENI Can Surface**:
- "You've maintained 85% of your Inner Circle relationships this month 🎯"
- "Your medical network has grown by 12 contacts this quarter"
- "Reminder: You haven't talked to [Name] in 45 days (last was monthly cadence)"
- "High-value interactions up 20% this month - energizing conversations!"

**Aristóteles Strategic Insights**:
- "Your network is heavily weighted toward Scientific Legacy Pillar (68% of interactions). Consider balancing with Vitality & Connection activities."
- "You have 3 mentors but 0 mentees. Consider pillar alignment - teaching supports legacy."

---

## Setup Checklist

Before agents use Hugain:
- [ ] Contacts database created with all properties
- [ ] Interactions database created with all properties
- [ ] Networking Goals database created
- [ ] Relations configured (Contact ↔ Interactions)
- [ ] Rollups configured in Contacts database
- [ ] Views created for each agent
- [ ] Sample contacts imported (at least 5-10 to test)
- [ ] JENI can read/write to all three databases via MCP
- [ ] Reminder system configured

---

*Hugain: Your relationship intelligence system. Because connection is a Pillar of your life.*
