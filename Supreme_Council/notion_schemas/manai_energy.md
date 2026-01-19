# Manai - Energy Portfolio Database Schema

**Vault Name**: Manai
**Purpose**: Track mental/physical bandwidth, energy levels, and optimize performance
**Primary Agent**: JENI (with Aristóteles for pattern analysis)
**Pillar Served**: Vitality & Connection

---

## Overview

Manai is your energy management system. It tracks your physical and mental capacity, identifies energy patterns, prevents burnout, and optimizes your schedule for peak performance. The name "Manai" comes from "mana" (spiritual energy/life force).

---

## Database: Daily Energy Log

**Description**: Daily tracking of energy, health metrics, and capacity

### Properties

| Property Name | Type | Description | Agent Usage |
|---------------|------|-------------|-------------|
| **Date** | Date (Title) | The day being tracked | All agents reference |
| **Overall Energy** | Select | Very High, High, Medium, Low, Very Low | JENI daily prompt; Aristóteles monitors trends |
| **Sleep Quality** | Select | Excellent, Good, Fair, Poor | Major energy predictor |
| **Sleep Hours** | Number | Actual hours slept | Correlate with energy |
| **Morning Energy** | Select | High, Medium, Low | Optimize AM schedule |
| **Afternoon Energy** | Select | High, Medium, Low | Identify afternoon slumps |
| **Evening Energy** | Select | High, Medium, Low | Pattern recognition |
| **Mental Clarity** | Select (1-10) | Focus and cognitive sharpness | JENI schedules deep work when high |
| **Physical Energy** | Select (1-10) | Body vitality and strength | Schedule physical activities |
| **Emotional State** | Select | Great, Good, Neutral, Stressed, Burned Out | Aristóteles burnout monitoring |
| **Stress Level** | Select (1-10) | Perceived stress | Intervention trigger |
| **Exercise** | Checkbox | Did you exercise today? | Energy correlation |
| **Exercise Type** | Multi-select | Cardio, Strength, Yoga, Walking, Sports, None | Track what energizes |
| **Exercise Duration** | Number | Minutes | Quantify |
| **Meditation/Mindfulness** | Number | Minutes of practice | WuWai vault link |
| **Meals Quality** | Select | Excellent, Good, Fair, Poor | Nutrition impact on energy |
| **Caffeine Intake** | Select | None, Low (1 cup), Medium (2-3), High (4+) | Track stimulant use |
| **Alcohol** | Select | None, Light (1), Moderate (2-3), Heavy (4+) | Impact on recovery |
| **Deep Work Blocks** | Number | # of focused work sessions completed | Productivity tracking |
| **Deep Work Hours** | Number | Total hours in deep work | Capacity measurement |
| **Meetings Count** | Number | # of meetings | Energy drain |
| **Meeting Hours** | Number | Total time in meetings | Opportunity cost |
| **Social Interactions** | Select | High, Medium, Low, None | Introvert/extrovert energy |
| **Social Quality** | Select | Energizing, Neutral, Draining | Who you spent time with matters |
| **Screen Time** | Number | Hours (estimate) | Digital wellness |
| **Outdoor Time** | Number | Minutes outside | Restoration factor |
| **Recovery Activities** | Multi-select | Reading, Nature, Music, Hobbies, Family Time, Solitude | What restores you |
| **Energy Drains Today** | Text | What depleted energy | Pattern identification |
| **Energy Sources Today** | Text | What boosted energy | Amplify these |
| **Sickness/Pain** | Select | None, Minor, Moderate, Severe | Health tracking |
| **Symptoms** | Text | If unwell, what symptoms | Asklepai integration |
| **Medications Taken** | Text | Track adherence and effects | Health log |
| **Energy Forecast Tomorrow** | Select | High, Medium, Low | Evening prediction |
| **Pillar Time Distribution** | Text (auto-calculated) | Time spent per Pillar today | Aristóteles balance check |
| **Notes** | Text (long) | Free-form daily reflections | All agents |
| **Created Time** | Created Time | Auto | Audit |

---

## Database: Energy Patterns

**Description**: Identified patterns in your energy and capacity

### Properties

| Property Name | Type | Description | Agent Usage |
|---------------|------|-------------|-------------|
| **Pattern Name** | Title | e.g., "Monday AM = Peak Deep Work" | JENI uses for scheduling |
| **Pattern Type** | Select | Time of Day, Day of Week, Activity-Based, People-Based, Environmental | Categorize |
| **Description** | Text | Full explanation of pattern | All agents understand |
| **Energy Impact** | Select | High Boost, Moderate Boost, Neutral, Moderate Drain, High Drain | Quantify effect |
| **Confidence Level** | Select | Strong Evidence, Moderate, Hypothesis | Based on data points |
| **Data Points** | Number | How many instances observed | Statistical confidence |
| **Recommendation** | Text | What to do with this insight | JENI executes |
| **Status** | Select | Active Pattern, Hypothesis, Disproven, Historical | Lifecycle |
| **Discovered Date** | Date | When pattern identified | Track |
| **Related Energy Logs** | Relation → Daily Energy Log | Link to evidence | View data |

**Example Patterns**:
- "Tuesday mornings after Monday off = highest mental clarity"
- "Back-to-back meetings for 4+ hours = severe afternoon energy crash"
- "Exercise before 9 AM = 30% higher overall daily energy"
- "Interactions with [certain people] consistently draining"
- "Deep work blocks >90 min = diminishing returns"

---

## Database: Energy Budget & Capacity

**Description**: Weekly/monthly energy allocation and limits

### Properties

| Property Name | Type | Description | Agent Usage |
|---------------|------|-------------|-------------|
| **Week Of** | Date (Title) | Week starting date | JENI plans week |
| **Estimated Energy** | Select | Very High, High, Medium, Low, Very Low | Weekly forecast |
| **Deep Work Capacity** | Number | Max hours of deep work this week | JENI schedules within limits |
| **Meeting Budget** | Number | Max meeting hours tolerable | JENI enforces |
| **Social Energy Budget** | Number | Social interaction capacity | Introvert management |
| **Available Hours** | Number | Total discretionary hours (non-sleep/work) | Time scarcity awareness |
| **Committed Hours** | Number | Already scheduled | Remaining capacity |
| **Buffer Hours** | Number | Unscheduled recovery time | Prevent overcommitment |
| **Recovery Needed** | Select | None, Light, Moderate, Significant | Last week's toll |
| **Major Events** | Text | Conferences, deadlines, travel affecting energy | Context |
| **Energy-First Priorities** | Text | What MUST get focus this week | JENI protects these |
| **Energy Strategy** | Text | How you'll manage energy this week | Proactive planning |
| **Actual Energy (Week End)** | Select | Actual energy level at week's end | Compare to forecast |
| **Lessons Learned** | Text | What you learned about your energy | Continuous improvement |
| **Pillar Focus** | Multi-select | Which Pillars get energy this week | Aristóteles validates |

---

## Database: Burnout Warning System

**Description**: Track burnout risk factors and early intervention

### Properties

| Property Name | Type | Description | Agent Usage |
|---------------|------|-------------|-------------|
| **Week Of** | Date (Title) | Week being assessed | JENI monitors weekly |
| **Burnout Risk Score** | Select (1-10) | Composite risk level | 7+ triggers intervention |
| **Physical Exhaustion** | Select (1-10) | Body fatigue | Component score |
| **Emotional Exhaustion** | Select (1-10) | Feeling drained | Component score |
| **Cynicism/Detachment** | Select (1-10) | Loss of meaning | Component score |
| **Reduced Efficacy** | Select (1-10) | Feeling ineffective | Component score |
| **Sleep Disruption** | Checkbox | Persistent poor sleep? | Red flag |
| **Anhedonia** | Checkbox | Loss of pleasure in previously enjoyable activities? | Red flag |
| **Irritability** | Checkbox | Increased frustration? | Red flag |
| **Work Hours** | Number | Total hours worked this week | Overwork indicator |
| **Recovery Time** | Number | Hours spent in recovery activities | Undersupply indicator |
| **Pillars Neglected** | Multi-select | Which Pillars got zero attention | Aristóteles alert |
| **Warning Signs** | Text | Specific symptoms observed | Qualitative data |
| **Intervention Taken** | Text | What was done to address risk | Action log |
| **Status** | Select | Green (Safe), Yellow (Watch), Orange (Intervene), Red (Crisis) | Traffic light system |
| **Follow-Up Date** | Date | When to reassess | JENI schedules check-in |

**Intervention Triggers**:
- Burnout Risk Score ≥7 → Aristóteles escalation
- Status = Orange → JENI schedules mandatory recovery day
- Status = Red → Aristóteles + Asklepai crisis protocol
- 3 consecutive weeks Yellow → Aristóteles strategic review

---

## Database: Recovery Activities

**Description**: Catalog of activities that restore your energy

### Properties

| Property Name | Type | Description | Agent Usage |
|---------------|------|-------------|-------------|
| **Activity Name** | Title | e.g., "Morning walk in nature" | JENI suggests when low energy |
| **Category** | Select | Physical, Mental, Social, Spiritual, Creative, Rest | Type of restoration |
| **Energy Restoration** | Select (1-10) | How much this restores | Ranking |
| **Time Required** | Number | Minutes needed | JENI schedules appropriate duration |
| **Effort Required** | Select | None (passive), Low, Medium, High | When exhausted, suggest low-effort |
| **Context Needed** | Text | What's required (location, people, equipment) | Feasibility check |
| **Best Time** | Multi-select | Morning, Afternoon, Evening, Night, Weekend | Timing optimization |
| **Frequency** | Select | Daily, Few/Week, Weekly, Few/Month, Monthly, Rare | Ideal cadence |
| **Last Done** | Date | Most recent instance | JENI reminds if overdue |
| **Pillar Served** | Multi-select | Which Pillars this supports | Aristóteles integration |
| **Triggers** | Text | When to deploy this activity | Conditional use |
| **Barriers** | Text | What prevents doing this | Problem-solve |
| **Notes** | Text | Additional context | All agents |

**Example Entries**:
- "20-min meditation: Mental restoration=9, Morning, Daily, Spiritual Evolution Pillar"
- "Hiking: Physical restoration=10, Time=120min, Effort=Medium, Weekend, Vitality Pillar"
- "Reading fiction: Mental restoration=7, Evening, Low effort, Spiritual Evolution Pillar"
- "Call with [friend]: Social restoration=8, Time=30min, Evening, Vitality & Connection Pillar"

---

## Relations & Rollups

### Daily Energy Log → Energy Patterns

**Pattern Detection Algorithm** (Aristóteles + JENI):
1. Analyze 30+ days of Daily Energy Logs
2. Identify correlations (e.g., exercise → higher energy)
3. Create Energy Pattern entries
4. JENI uses patterns for scheduling optimization

### Weekly Energy Budget → Daily Energy Log Rollup

**In Weekly Budget**:
- **Avg Daily Energy** (Rollup): Average Overall Energy from that week's logs
- **Total Deep Work Hours** (Rollup): Sum from daily logs
- **Total Meeting Hours** (Rollup): Sum from daily logs
- **Recovery Hours** (Rollup): Sum of recovery activities

Compare budgeted vs actual to improve forecasting.

---

## Database Views for Agents

### JENI's Views

1. **Today's Energy** - Just today's log entry (for morning/evening updates)
2. **This Week** - Last 7 days for trend spotting
3. **High Energy Days** - Overall Energy = Very High or High (learn from these)
4. **Low Energy Days** - Overall Energy = Low or Very Low (understand causes)
5. **Recovery Needed** - Burnout Warning status ≠ Green

### Aristóteles' Views

1. **Burnout Dashboard** - All burnout warnings with risk scores
2. **Pillar Balance Over Time** - Energy distribution across Pillars
3. **Pattern Library** - All identified energy patterns
4. **Monthly Trends** - Aggregated data by month

### Asklepai's Views

1. **Health Concerns** - Logs with Sickness/Pain ≠ None
2. **Sleep Issues** - Sleep Quality = Poor for multiple days
3. **Exercise Adherence** - Daily exercise checkbox tracking

---

## Agent Integration Patterns

### JENI - Morning Energy Check-In

**Every Morning (07:00)**:
```python
# Prompt user for today's energy forecast
message = "Good morning! Quick energy check-in:"
questions = [
    "How did you sleep? (Excellent/Good/Fair/Poor)",
    "Current energy level? (High/Medium/Low)",
    "Any constraints today? (illness, poor sleep, etc.)"
]

# Log to Daily Energy Log
mcp.create_notion_page(
    database="Daily_Energy_Log",
    properties={
        "Date": today,
        "Morning_Energy": user_response,
        "Sleep_Quality": user_sleep_response
        # ... other properties
    }
)

# Adjust today's schedule if low energy
if energy == "Low":
    reschedule_intensive_tasks()
    suggest_recovery_activities()
```

### JENI - Evening Energy Reflection

**Every Evening (21:00)**:
```python
# Review day's energy
prompt_reflection = [
    "Overall energy today? (Very High → Very Low)",
    "What drained your energy?",
    "What boosted your energy?",
    "Forecast for tomorrow? (High/Med/Low)"
]

# Update daily log with actuals
# Calculate energy budget for tomorrow based on forecast
```

### Aristóteles - Weekly Burnout Check

**Every Sunday Evening**:
```python
# Aggregate week's data
week_data = mcp.query_notion(
    database="Daily_Energy_Log",
    filter={"Date": "last_7_days"}
)

# Calculate burnout risk factors
physical_exhaustion = avg(week_data, "Physical_Energy")
emotional_state = mood_analysis(week_data, "Emotional_State")
work_hours = sum(week_data, "Deep_Work_Hours") + sum(week_data, "Meeting_Hours")

# Compute risk score
burnout_risk = calculate_burnout_risk(
    physical_exhaustion,
    emotional_state,
    work_hours,
    recovery_time
)

# Create Burnout Warning entry
if burnout_risk >= 5:
    alert_aristoteles("Burnout risk elevated")
    recommend_intervention()
```

### JENI - Energy-Based Scheduling

**Daily**:
```python
# Retrieve energy patterns
patterns = mcp.query_notion(
    database="Energy_Patterns",
    filter={"Status": "Active Pattern"}
)

# Schedule tasks according to energy
# High-energy morning → Deep work (research, writing)
# Medium-energy afternoon → Meetings, emails
# Low-energy evening → Recovery, light tasks

# Example:
if today.weekday == "Monday" and time == "9:00 AM":
    # Pattern: Monday AM = Peak Deep Work
    schedule_deep_work_block(duration=90)
```

---

## Sample Data

### Daily Energy Log Entry

```
Date: 2026-01-19
Overall Energy: High
Sleep Quality: Good
Sleep Hours: 7.5
Morning Energy: High
Afternoon Energy: Medium
Evening Energy: Low
Mental Clarity: 8/10
Physical Energy: 7/10
Emotional State: Great
Stress Level: 3/10
Exercise: ✓
Exercise Type: Cardio, Strength
Exercise Duration: 45
Meditation/Mindfulness: 20
Meals Quality: Excellent
Caffeine Intake: Medium (2-3)
Alcohol: None
Deep Work Blocks: 2
Deep Work Hours: 3.5
Meetings Count: 2
Meeting Hours: 1.5
Social Interactions: Medium
Social Quality: Energizing
Screen Time: 8
Outdoor Time: 30
Recovery Activities: Reading, Music
Energy Drains Today: Afternoon administrative tasks, back-to-back meetings
Energy Sources Today: Morning workout, focused research time, good sleep
Sickness/Pain: None
Energy Forecast Tomorrow: High
Notes: Great productive day. Exercise + early start set positive tone. Need to reduce afternoon admin tasks - very draining.
```

### Energy Pattern Entry

```
Pattern Name: Post-Exercise Morning Boost
Pattern Type: Activity-Based
Description: When I exercise before 9 AM, my energy level throughout the day is 30-40% higher, mental clarity peaks, and I complete 50% more deep work.
Energy Impact: High Boost
Confidence Level: Strong Evidence
Data Points: 23 instances over 6 weeks
Recommendation: Prioritize AM exercise 5x/week. Schedule most important deep work 9-11 AM post-exercise.
Status: Active Pattern
Discovered Date: 2026-01-05
```

---

## Gamification & Insights

**Weekly Energy Report** (Auto-generated by JENI):
```
WEEKLY ENERGY REPORT
Week of Jan 13-19, 2026

⚡ ENERGY SUMMARY:
Average Energy: High (↑ from last week)
Best Day: Wednesday (Very High)
Challenging Day: Friday (Low - reason: poor sleep)

💪 VITALITY WINS:
✓ Exercised 6/7 days (goal: 5)
✓ Meditation streak: 12 days
✓ Deep work: 18 hours (above capacity estimate)

⚠️ WATCH AREAS:
⚠ Screen time average: 9.2 hours (target: <8)
⚠ Sleep: 2 nights under 7 hours

📊 PILLAR TIME:
Healing Mastery: 40%
Scientific Legacy: 25%
Financial Sovereignty: 15%
Spiritual Evolution: 10%
Vitality & Connection: 10%

🎯 BURNOUT RISK: Green (Score: 3/10)

🚀 NEXT WEEK OPTIMIZATION:
Based on your energy patterns:
- Schedule deep work Mon/Tue/Wed AM (highest energy)
- Limit meetings to 2 hours/day max
- Add 30min outdoor time daily
- Protect Friday for recovery (pattern: low energy end of week)
```

---

## Advanced Features

### Predictive Energy Forecasting

Using 90+ days of data, Aristóteles + JENI can:
- Predict tomorrow's energy with 70%+ accuracy
- Identify upcoming high-risk burnout weeks
- Recommend optimal work patterns
- Suggest preventive recovery

### Energy ROI Analysis

Seshait integration:
- Calculate financial ROI of energy optimization
- "Investing 45min/day in exercise yields 2 extra deep work hours = $X value"
- Justify recovery time economically

---

## Setup Checklist

Before agents use Manai:
- [ ] Daily Energy Log database created with all properties
- [ ] Energy Patterns database created
- [ ] Energy Budget & Capacity database created
- [ ] Burnout Warning System database created
- [ ] Recovery Activities database created
- [ ] Relations configured between databases
- [ ] Rollups configured for weekly summaries
- [ ] Views created for each agent
- [ ] JENI morning/evening prompts scheduled
- [ ] Aristóteles weekly burnout check scheduled
- [ ] First week of manual logging (to establish baseline)

---

*Manai: Your energy is finite. Manage it like the precious resource it is.*
