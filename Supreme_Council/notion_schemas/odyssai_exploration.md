# Odyssai - Exploration & Adventure Database Schema

**Vault Name**: Odyssai
**Purpose**: Document adventures, travel, experiences, and exploration
**Primary Agent**: JENI (with Aristóteles for meaning-making)
**Pillar Served**: Vitality & Connection, Spiritual Evolution

---

## Overview

Odyssai (inspired by Odyssey) captures the richness of your lived experiences beyond work. It's where adventures, travel, meaningful experiences, and personal discoveries are documented. This vault ensures you're living, not just achieving.

---

## Database: Adventures & Experiences

**Description**: Log of significant experiences and adventures

### Properties

| Property Name | Type | Description | Agent Usage |
|---------------|------|-------------|-------------|
| **Title** | Title | Name of adventure/experience | All agents reference |
| **Date** | Date | When it occurred (or started) | Chronological organization |
| **End Date** | Date | If multi-day (e.g., trip) | Duration calculation |
| **Type** | Select | Travel, Adventure, Event, Learning, Cultural, Social, Personal Milestone, Spontaneous | Categorize |
| **Location** | Text | Where it happened | Geographic tracking |
| **Location (Map)** | URL | Link to map/coordinates | Visual reference |
| **Country** | Select | For travel tracking | Country count |
| **With Whom** | Relation → Hugain:Contacts | People you were with | Connection tracking |
| **Duration** | Formula | Auto: End Date - Date | Time spent |
| **Pillar Served** | Multi-select | Which Pillar(s) this experience served | Aristóteles validates |
| **Intention** | Text | Why you did this / What you hoped to gain | Purpose awareness |
| **Experience Quality** | Select (1-10) | How meaningful/valuable was this | Subjective rating |
| **Energy Impact** | Select | Energizing, Neutral, Draining | Manai vault link |
| **Physical Challenge** | Select (1-10) | Physical difficulty/intensity | Track range |
| **Novel vs Familiar** | Select | Completely New, Somewhat New, Familiar | Novelty tracking |
| **Cost** | Number | Expense for experience | Seshait integration |
| **Cost Per Day** | Formula | Cost / Duration | Value assessment |
| **Worth It?** | Select | Absolutely, Yes, Neutral, No, Regret | Retrospective value |
| **Photos/Media** | Files & Media | Images, videos | Visual memory |
| **Story** | Text (long) | Narrative of what happened | Rich documentation |
| **Key Moments** | Text | Highlights and memorable parts | Quick reference |
| **People Met** | Text | New contacts made | Potential Hugain additions |
| **Lessons Learned** | Text | Insights and growth | Meaning-making |
| **Gratitude** | Text | What you're grateful for from this | Positive psychology |
| **Would Repeat?** | Checkbox | Do again? | Future planning |
| **Related Adventures** | Relation → Adventures | Similar or connected experiences | Build series |
| **Bucket List Item** | Relation → Bucket List | If this fulfilled a bucket list goal | Achievement tracking |
| **Status** | Select | Planned, Happening, Completed, Cancelled | Lifecycle |
| **Planning Notes** | Text | Pre-adventure planning | JENI helps organize |
| **Tags** | Multi-select | Nature, Adventure, Culture, Food, Art, Sports, Learning, etc. | Searchable |
| **Mood** | Select | Joyful, Peaceful, Excited, Reflective, Challenging, Mixed | Emotional tone |
| **Life Chapter** | Select | Medical School, Residency, Early Career, Mid-Career, etc. | Life stage context |
| **Created Date** | Created Time | When logged | Audit |

---

## Database: Bucket List & Life Goals

**Description**: Experiences you want to have before you die

### Properties

| Property Name | Type | Description | Agent Usage |
|---------------|------|-------------|-------------|
| **Experience** | Title | What you want to do | Clear goal |
| **Category** | Multi-select | Travel, Adventure, Learning, Achievement, Relationship, Creative | Type |
| **Pillar** | Select | Which Pillar this serves | Aristóteles ensures balance |
| **Priority** | Select | Must Do, High, Medium, Low, Someday | Urgency |
| **Difficulty** | Select | Easy, Moderate, Challenging, Extreme | Feasibility |
| **Estimated Cost** | Number | Financial requirement | Seshait planning |
| **Time Required** | Number | Days needed | Scheduling |
| **Best Time** | Text | Seasonal, age, life stage considerations | Timing |
| **Dependencies** | Text | What needs to happen first | Prerequisites |
| **Why This Matters** | Text | Personal significance | Motivation |
| **Progress** | Select | Not Started, Planning, In Progress, Completed, No Longer Relevant | Status |
| **Target Date** | Date | When you hope to do this | Goal setting |
| **Completed Date** | Date | When achieved | Celebration |
| **Related Adventure** | Relation → Adventures | Links to actual experience | Achievement connection |
| **Inspired By** | Text | Where this idea came from | Context |
| **Accountability** | Relation → Hugain:Contacts | Who knows about this goal | Social commitment |
| **Notes** | Text | Planning thoughts | JENI reference |

**Example Bucket List Items**:
- "Hike to Machu Picchu"
- "Publish a book"
- "Learn to speak Spanish fluently"
- "Scuba dive Great Barrier Reef"
- "Attend a meditation retreat for 7+ days"
- "See Northern Lights"
- "Mentor 10 medical students"

---

## Database: Travel Log

**Description**: Detailed tracking of places visited

### Properties

| Property Name | Type | Description | Agent Usage |
|---------------|------|-------------|-------------|
| **Location** | Title | City, region, or place | Primary identifier |
| **Country** | Select | Country visited | Country count |
| **Continent** | Select | Geographic grouping | Continental coverage |
| **Dates Visited** | Multi-date | All times you've been there | Revisit tracking |
| **Total Days** | Formula | Sum of all visits | Time spent |
| **Purpose** | Multi-select | Vacation, Conference, Work, Family, Adventure | Why you went |
| **Rating** | Select (1-10) | How much you loved it | Return potential |
| **Highlights** | Text | Best experiences there | Memory |
| **Would Return?** | Checkbox | Visit again? | Future travel planning |
| **Photos** | Files & Media | Visual documentation | Rich media |
| **Related Adventures** | Relation → Adventures | Experiences had there | Cross-reference |
| **Accommodation** | Text | Where you stayed | Recommendations |
| **Food Highlights** | Text | Memorable meals | Culinary memory |
| **People Met** | Text | Connections made | Hugain potential |
| **Local Insights** | Text | Cultural learnings | Education |
| **Travel Tips** | Text | Advice for future visitors (or yourself) | Practical knowledge |
| **Cost** | Number | Total spent | Seshait integration |

---

## Database: Learning & Growth Experiences

**Description**: Non-formal education, workshops, courses, retreats

### Properties

| Property Name | Type | Description | Agent Usage |
|---------------|------|-------------|-------------|
| **Experience** | Title | Name of course/workshop/retreat | Identifier |
| **Type** | Select | Course, Workshop, Retreat, Conference, Seminar, Self-Study | Category |
| **Topic** | Multi-select | Subject areas | Knowledge mapping |
| **Provider** | Text | Who offered it | Source tracking |
| **Date** | Date | When attended | Timeline |
| **Duration** | Number | Days or hours | Time investment |
| **Cost** | Number | Financial investment | Seshait ROI analysis |
| **Location** | Text | Where (in-person or online) | Context |
| **Pillar** | Multi-select | Which Pillar(s) this served | Aristóteles validates |
| **Key Learnings** | Text (long) | What you learned | Knowledge vault |
| **Skills Gained** | Multi-select | Practical skills acquired | Competency tracking |
| **Application** | Text | How you've applied this learning | Transfer to life |
| **Instructors** | Text | Who taught | Potential mentors for Hugain |
| **Peers Met** | Text | Fellow participants | Network building |
| **Books/Resources** | Text | Related materials | Further study |
| **Would Recommend?** | Checkbox | To others? | Value assessment |
| **Rating** | Select (1-10) | Quality of experience | Evaluation |
| **Certificate** | File | If received credential | Achievement |
| **Next Steps** | Text | How to go deeper | Continued growth |
| **Life Impact** | Text | How this changed you | Transformation tracking |

---

## Database: Personal Milestones

**Description**: Significant life events and achievements

### Properties

| Property Name | Type | Description | Agent Usage |
|---------------|------|-------------|-------------|
| **Milestone** | Title | What happened | Clear description |
| **Date** | Date | When it occurred | Chronological |
| **Type** | Select | Achievement, Life Event, Relationship, Health, Spiritual, Creative, Professional | Categorize |
| **Pillar** | Select | Which Pillar this belongs to | Context |
| **Significance** | Select (1-10) | How important is this | Weight |
| **Story** | Text (long) | Full narrative | Rich documentation |
| **Feelings** | Text | Emotional response | Psychological insight |
| **People Involved** | Relation → Hugain:Contacts | Who shared this | Connection |
| **Photo** | Files & Media | Visual memory | Commemoration |
| **Gratitude** | Text | What you're grateful for | Positive framing |
| **Lessons** | Text | What you learned | Growth |
| **Life Before vs After** | Text | How this changed things | Transformation marker |
| **Tags** | Multi-select | First-time, Achievement, Celebration, Challenge, Loss, Gain | Nuance |

**Example Milestones**:
- "Became a licensed physician"
- "First published research paper"
- "Completed first marathon"
- "Started AI freelance business"
- "Paid off student loans"
- "Moved to [city]"

---

## Relations & Rollups

### Adventures → Bucket List

- When adventure is completed, mark related bucket list item as "Completed"
- Rollup: Count of bucket list items achieved

### Adventures → Hugain (Contacts)

- Track who you've had adventures with
- Rollup in Hugain: Adventures count per contact
- Identify adventure buddies (high counts)

### Travel Log → Adventures

- Link specific adventures to places visited
- Rollup: Number of adventures per location

---

## Database Views for Agents

### JENI's Views

1. **Upcoming Adventures** - Status = Planned, sorted by Date
2. **This Year's Experiences** - Date = this year
3. **High-Value Experiences** - Experience Quality ≥8
4. **By Pillar** - Grouped by Pillar to see experiential balance

### Aristóteles' Views

1. **Pillar Distribution** - How many experiences per Pillar (balance check)
2. **Bucket List Progress** - Completed vs Not Started
3. **Transformational Experiences** - Significance ≥8
4. **Life Chapters** - Grouped by Life Chapter

### Seshait's Views

1. **Experience ROI** - Cost vs Experience Quality
2. **This Year's Travel Budget** - Sum of costs for travel
3. **Worth It Analysis** - Worth It = Absolutely or Yes

---

## Agent Integration Patterns

### JENI - Adventure Planning

**User**: "I want to plan a trip to Iceland"

**JENI**:
```
Great! Let me help you plan this adventure.

Creating Odyssai entry:
- Adding to Bucket List (if not already there)
- Creating Adventure (Status: Planned)
- What are your dates or preferred timeframe?
- Budget estimate?
- What experiences are must-haves? (Northern Lights, Blue Lagoon, Hiking, etc.)

I'll also:
- Check Manai for energy capacity during those dates
- Flag this with Seshait for budget allocation
- Link to Hugain if you want to invite anyone

Let's build your Iceland adventure!
```

### JENI - Post-Adventure Reflection

**After major experience**:
```
Welcome back from [adventure]!

Let's capture this while it's fresh:

1. How would you rate the experience? (1-10)
2. What were the highlights?
3. Any key moments or stories?
4. What did you learn?
5. Who did you meet?
6. Would you do it again?

[Prompts user through reflection]

Logging to Odyssai...
Adding photos when you're ready.
Updating Travel Log for [locations].

✓ Adventure documented for future memory!
```

### Aristóteles - Pillar Balance Check

**Quarterly**:
```python
# Check experiential balance across Pillars
experiences = mcp.query_notion(
    database="Adventures",
    filter={"Date": "last_90_days"}
)

pillar_distribution = group_by(experiences, "Pillar_Served")

# Alert if imbalance
if pillar_distribution["Vitality_Connection"] == 0:
    alert_aristoteles(
        "Zero adventure/experience for Vitality & Connection Pillar in Q1. "
        "Life is becoming too work-focused. Schedule restorative experiences."
    )
```

### Aristóteles - Bucket List Achievement Celebration

**When bucket list item completed**:
```
🎉 MILESTONE ACHIEVED!

You completed: [Bucket List Item]

This is significant because: [Why This Matters field]

Pillar honored: [Pillar]

Take a moment to:
- Celebrate this achievement
- Reflect on the journey
- Share with someone who matters
- Add next bucket list item in this category

What's calling you next?
```

### JENI - Annual Life Review

**End of year**:
```
ANNUAL ADVENTURE SUMMARY - 2026

📍 PLACES VISITED:
- Countries: [X] (new: [Y])
- Cities: [X]
- Continents: [list]

🎯 BUCKET LIST:
- Completed this year: [count] items
- Items: [list]
- Progress: [X]% of total bucket list

✨ TOP EXPERIENCES:
1. [Highest rated experience]
2. [Second highest]
3. [Third highest]

💡 KEY LEARNINGS:
[Aggregated lessons from all adventures]

🌱 LIFE CHAPTERS:
This year belonged to: [Life Chapter]

📊 PILLAR DISTRIBUTION:
How your adventures served your Pillars...

🎯 NEXT YEAR INTENTIONS:
Based on this year, what experiences are calling you for 2027?
```

---

## Gamification & Motivation

**Adventure Tracker Stats**:
- Countries visited: X / 195
- Continents: X / 7
- Bucket list completion: X%
- Adventures this year: X
- Days spent adventuring: X
- New experiences tried: X

**Streaks**:
- "Monthly adventure streak: 8 months"
- "You haven't had a Vitality & Connection experience in 45 days"

**Badges** (optional):
- World Traveler (25 countries)
- Adventurer (50 adventures logged)
- Bucket List Champion (10 items completed)
- Present Moment Master (high quality ratings, rich documentation)

---

## Sample Data

### Adventure Entry

```
Title: 7-Day Silent Meditation Retreat - Insight Meditation Society
Date: 2026-03-15
End Date: 2026-03-22
Type: Learning, Personal Milestone
Location: Barre, Massachusetts, USA
Country: USA
With Whom: [Solo]
Duration: 7 days
Pillar Served: Spiritual Evolution, Vitality & Connection
Intention: Deepen meditation practice, gain insight into mind patterns, reset from clinical burnout risk
Experience Quality: 10/10
Energy Impact: Draining initially, then deeply Energizing
Physical Challenge: 3/10 (sitting, walking)
Novel vs Familiar: Somewhat New (familiar with meditation, but never silent retreat)
Cost: $875
Cost Per Day: $125
Worth It?: Absolutely
Story: [Long narrative of the week, key insights, challenges, breakthroughs]
Key Moments:
- Day 3: Major breakthrough in understanding my reactivity patterns
- Day 5: First experience of genuine equanimity during difficult body sensations
- Day 6: Profound gratitude meditation that brought tears
Lessons Learned:
- My mind is far more active than I realized
- Silence reveals what noise covers
- Suffering comes from resistance, not from sensation itself
- I have more capacity for stillness than I thought
Gratitude: Time away from demands, skilled teachers, supportive community, this privilege
Would Repeat?: ✓ Yes - plan to do annually
Status: Completed
Tags: Meditation, Spiritual, Solitude, Silence, Retreat, Insight
Mood: Reflective, Peaceful, Transformative
Life Chapter: Early Career
```

### Bucket List Entry

```
Experience: Complete an Ironman Triathlon
Category: Adventure, Achievement
Pillar: Vitality & Connection
Priority: High
Difficulty: Extreme
Estimated Cost: $2,500 (entry, gear, training, travel)
Time Required: 6 months training + 1 week for event
Best Time: When not in peak research/clinical demands
Dependencies: Build base fitness, injury-free, time for training
Why This Matters: Ultimate test of mental and physical endurance. Proof I can do hard things. Honor my body's capability.
Progress: Planning
Target Date: 2027-09-01
Notes: Start training Jan 2027. Need coach. Consider Ironman Lake Placid or Arizona.
```

---

## Setup Checklist

Before agents use Odyssai:
- [ ] Adventures & Experiences database created
- [ ] Bucket List & Life Goals database created
- [ ] Travel Log database created
- [ ] Learning & Growth Experiences database created
- [ ] Personal Milestones database created
- [ ] Relations configured between databases
- [ ] Rollups for stats tracking
- [ ] Views created for each agent
- [ ] JENI prompts configured for post-adventure reflection
- [ ] Aristóteles quarterly experiential balance check scheduled
- [ ] Import existing bucket list items
- [ ] Import past major adventures/travel

---

*Odyssai: Don't just work. Live. Adventure. Explore. Remember.*

*"The purpose of life is to live it, to taste experience to the utmost, to reach out eagerly and without fear for newer and richer experience." - Eleanor Roosevelt*
