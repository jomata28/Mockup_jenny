# WuWai - Spiritual & Philosophical Database Schema

**Vault Name**: WuWai
**Purpose**: Spiritual growth, philosophical inquiry, wisdom cultivation, meaning-making
**Primary Agent**: Aristóteles (with JENI for practice tracking)
**Pillar Served**: Spiritual Evolution

---

## Overview

WuWai (inspired by Wu Wei - effortless action / being in flow) is your inner landscape database. It tracks contemplative practices, philosophical insights, values evolution, and the search for meaning. This is where your spiritual and intellectual growth is documented.

---

## Database: Contemplative Practice Log

**Description**: Daily tracking of meditation, prayer, journaling, and spiritual practices

### Properties

| Property Name | Type | Description | Agent Usage |
|---------------|------|-------------|-------------|
| **Date** | Date (Title) | Practice date | Chronological tracking |
| **Meditation** | Number | Minutes of meditation | Consistency tracking |
| **Meditation Type** | Multi-select | Vipassana, Loving-Kindness, Breath, Body Scan, Mantra, Zen, Other | Method tracking |
| **Meditation Quality** | Select (1-10) | Depth of practice | Subjective assessment |
| **Journaling** | Number | Minutes spent journaling | Writing practice |
| **Journaling Focus** | Multi-select | Gratitude, Reflection, Morning Pages, Stream of Consciousness, Philosophical Inquiry, Dream Analysis | Type of journaling |
| **Prayer/Contemplation** | Number | Minutes in prayer or contemplation | Spiritual practice |
| **Reading Wisdom Texts** | Number | Minutes reading sacred/philosophical texts | Study time |
| **Texts Read** | Text | Which books/texts today | Knowledge tracking |
| **Yoga/Embodied Practice** | Number | Minutes of yoga or embodied spirituality | Integration |
| **Nature Contemplation** | Number | Minutes in nature for spiritual connection | Earth connection |
| **Total Practice Time** | Formula | Sum of all practice minutes | Daily total |
| **Practice Streak** | Formula | Days in a row with practice | Motivation |
| **Insights** | Text (long) | What arose during practice | Wisdom capture |
| **Challenges** | Text | Difficulties encountered (monkey mind, resistance, etc.) | Honesty |
| **Gratitude** | Text | Three things you're grateful for | Positive psychology |
| **Intention for Tomorrow** | Text | What you'll focus on next session | Forward momentum |
| **Mood Before** | Select | Emotional state before practice | Baseline |
| **Mood After** | Select | Emotional state after practice | Impact measurement |
| **Integration** | Text | How you'll bring practice into daily life | Application |
| **Energy Impact** | Select | Energizing, Calming, Neutral, Draining | Manai link |
| **Related Reading** | Relation → Wisdom Library | Books/articles that informed practice | Knowledge |

---

## Database: Wisdom Library

**Description**: Books, articles, teachings, quotes that shape your philosophy

### Properties

| Property Name | Type | Description | Agent Usage |
|---------------|------|-------------|-------------|
| **Title** | Title | Name of book/article/teaching | Identifier |
| **Author/Teacher** | Text | Who created this | Attribution |
| **Type** | Select | Book, Article, Essay, Lecture, Podcast, Video, Quote Collection | Format |
| **Tradition** | Multi-select | Buddhism, Stoicism, Christianity, Taoism, Secular Philosophy, Psychology, Mysticism, Integral, Other | Lineage |
| **Topics** | Multi-select | Suffering, Compassion, Meaning, Death, Consciousness, Ethics, Virtue, Freedom, Truth, Love | Themes |
| **Status** | Select | Want to Read, Reading, Completed, Reference, Abandoned | Reading lifecycle |
| **Priority** | Select | High, Medium, Low | Reading queue |
| **Pages** | Number | Length | Time estimate |
| **Date Started** | Date | When you began | Progress |
| **Date Completed** | Date | When finished | Completion |
| **Rating** | Select (1-10) | Personal value | Quality |
| **Impact** | Select | Life-Changing, Significant, Moderate, Minimal | Transformation level |
| **Key Insights** | Text (long) | Main takeaways | Synthesis |
| **Favorite Quotes** | Text (long) | Passages that resonated | Reference |
| **How It Changed Me** | Text | Specific shifts in thinking/being | Growth tracking |
| **Application** | Text | How you're applying these teachings | Praxis |
| **Would Recommend** | Checkbox | To others on similar path | Quality signal |
| **Related Texts** | Relation → Wisdom Library | Similar or complementary works | Knowledge graph |
| **Notes & Highlights** | Files & Media | PDF notes, highlights export | Deep reference |
| **Practice Influence** | Relation → Contemplative Practice Log | Days when this informed practice | Connection |

---

## Database: Philosophical Reflections

**Description**: Your own philosophical writings, questions, and explorations

### Properties

| Property Name | Type | Description | Agent Usage |
|---------------|------|-------------|-------------|
| **Title** | Title | Theme or question being explored | Identifier |
| **Date** | Date | When written | Chronology |
| **Type** | Select | Question, Insight, Essay, Dialogue (with text), Stream of Consciousness, Response to Life Event | Format |
| **Philosophical Domain** | Multi-select | Ethics, Metaphysics, Epistemology, Aesthetics, Meaning, Consciousness, Death, Suffering, Joy | Area |
| **Life Context** | Text | What prompted this reflection | Grounding |
| **Question** | Text | Central question being explored | Focus |
| **Reflection** | Text (long) | Your thinking, exploration, insights | Main content |
| **Influences** | Relation → Wisdom Library | Thinkers/texts that shaped this | Sources |
| **Related Pillar** | Select | Which Pillar this reflection connects to | Integration |
| **Life Stage** | Select | Youth, Medical School, Early Career, Mid-Career, Elder, etc. | Developmental context |
| **Resolution** | Text | If question resolved, what's your current view | Evolution |
| **Open Questions** | Text | What remains unresolved | Continued inquiry |
| **Revisit Date** | Date | When to revisit this question | Future engagement |
| **Tags** | Multi-select | Death, Love, Calling, Medicine, Compassion, Purpose, etc. | Searchable |

**Example Reflection Titles**:
- "Why does suffering exist, and what is my relationship to it as a physician?"
- "What is the good life for someone in my position?"
- "How do I reconcile ambition with contentment?"
- "What is my responsibility to future generations?"
- "How do I hold hope and realism simultaneously?"

---

## Database: Values & Principles

**Description**: Your evolving ethical framework and core principles

### Properties

| Property Name | Type | Description | Agent Usage |
|---------------|------|-------------|-------------|
| **Value/Principle** | Title | Core value or guiding principle | Identifier |
| **Definition** | Text | What this means to you | Clarity |
| **Why It Matters** | Text | Origin and importance | Grounding |
| **How I Live It** | Text | Practical application | Integrity check |
| **Related Pillar** | Multi-select | Which Pillar(s) this supports | Integration |
| **Source** | Text | Where this value came from (upbringing, experience, philosophy, etc.) | Understanding |
| **In Tension With** | Relation → Values & Principles | Conflicting values | Complexity |
| **Examples** | Text | Specific instances of living this value | Concrete evidence |
| **Violations** | Text | Times you've betrayed this value | Shadow work |
| **Evolution** | Text | How this value has changed over time | Growth |
| **Current Status** | Select | Core Value, Aspirational, Evolving, Former Value | Lifecycle |
| **Strength** | Select (1-10) | How well you live this | Self-assessment |
| **Date Added** | Date | When recognized as a value | Timeline |
| **Last Reviewed** | Date | Most recent reflection | Maintenance |

**Example Values**:
- Compassion: "Recognizing suffering in others and self, responding with kindness"
- Integrity: "Alignment between values, words, and actions"
- Courage: "Acting on what's right despite fear"
- Wisdom: "Seeing clearly and responding skillfully"
- Service: "Using my gifts to reduce suffering in the world"

---

## Database: Meaning & Purpose

**Description**: Your evolving understanding of your life's purpose and meaning

### Properties

| Property Name | Type | Description | Agent Usage |
|---------------|------|-------------|-------------|
| **Date** | Date (Title) | When this was written | Evolution tracking |
| **Life Stage** | Select | Medical School, Residency, Early Career, Mid-Career, Later Life | Context |
| **Purpose Statement** | Text (long) | Your current sense of purpose/calling | Core |
| **What Gives Life Meaning** | Text | Sources of meaning | Understanding |
| **Legacy Intention** | Text | What you want to leave behind | Long-term vision |
| **Calling/Vocation** | Text | How you understand your work as calling | Professional meaning |
| **Core Question** | Text | The question your life is answering | Focus |
| **Related Pillars** | Multi-select | How this connects to Pillars | Integration |
| **Influences** | Relation → Wisdom Library | Thinkers who shaped this understanding | Sources |
| **Doubts** | Text | Uncertainties about purpose | Honesty |
| **Affirmations** | Text | What you know to be true | Confidence |
| **How to Know I'm On Path** | Text | Markers of alignment | Navigation |
| **How to Know I've Drifted** | Text | Warning signs | Course correction |
| **Next Review** | Date | When to revisit | Regular check |

---

## Database: Spiritual Teachers & Mentors

**Description**: People (living or dead) who guide your spiritual path

### Properties

| Property Name | Type | Description | Agent Usage |
|---------------|------|-------------|-------------|
| **Name** | Title | Teacher's name | Identifier |
| **Tradition** | Multi-select | Buddhist, Stoic, Christian, Secular, etc. | Lineage |
| **Living/Historical** | Select | Alive, Deceased | Contemporary access |
| **Access** | Select | Personal Contact, Books, Recordings, Historical Study | How you learn from them |
| **Key Teachings** | Text (long) | Core messages | Synthesis |
| **Books/Works** | Relation → Wisdom Library | Their writings you've engaged | Connection |
| **Impact on You** | Text | How they've shaped you | Influence |
| **Favorite Quote** | Text | Most meaningful teaching | Essence |
| **Application** | Text | How you practice their teachings | Praxis |
| **Contact** | Relation → Hugain:Contacts | If accessible person | Real relationship |

**Example Teachers**:
- Thich Nhat Hanh (Mindfulness, Engaged Buddhism)
- Marcus Aurelius (Stoicism)
- Pema Chödrön (Tibetan Buddhism, Working with difficulty)
- Viktor Frankl (Meaning, Logotherapy)
- Thomas Merton (Contemplative Christianity)

---

## Database: Death Contemplation & Memento Mori

**Description**: Reflections on mortality, death awareness practice

### Properties

| Property Name | Type | Description | Agent Usage |
|---------------|------|-------------|-------------|
| **Date** | Date (Title) | When contemplated | Tracking |
| **Prompt** | Text | What led to this reflection (death in family, patient death, meditation, etc.) | Context |
| **Reflection** | Text (long) | Your thoughts on death, mortality, impermanence | Main content |
| **Age Now** | Number | Your current age | Life stage |
| **Estimated Years Left** | Number | If you live to 85, how many years remain | Urgency |
| **What This Makes Real** | Text | How death awareness shifts priorities | Impact |
| **Regrets to Avoid** | Text | What you'd regret not doing | Motivation |
| **Gratitude** | Text | What you're grateful for given impermanence | Appreciation |
| **Changes to Make** | Text | How this changes your living | Action |
| **Fear vs Acceptance** | Text | Your relationship with death now | Evolution |
| **Integration** | Text | How to carry this awareness forward | Sustainability |

---

## Relations & Rollups

### Contemplative Practice → Wisdom Library

- Track which texts informed your practice
- Rollup: Most referenced texts in practice

### Philosophical Reflections → Values & Principles

- Link reflections that led to value clarifications
- Track values evolution through reflections

### Purpose Statements → All Other Databases

- Ensure contemplative practices serve purpose
- Align values with purpose
- Check if philosophical reflections deepen purpose

---

## Database Views for Agents

### Aristóteles' Views

1. **Current Purpose Statement** - Most recent entry in Meaning & Purpose
2. **Core Values** - Status = Core Value, sorted by Strength
3. **Life-Changing Wisdom** - Impact = Life-Changing
4. **Unresolved Questions** - Philosophical Reflections with Open Questions
5. **Values in Tension** - Values that conflict (for integration work)

### JENI's Views

1. **Daily Practice Log** - This week's entries
2. **Practice Streak** - Current streak count
3. **Reading Queue** - Wisdom Library Status = Want to Read, sorted by Priority
4. **Currently Reading** - Status = Reading

---

## Agent Integration Patterns

### JENI - Daily Practice Prompt

**Morning**:
```
Good morning. Would you like to set a contemplative intention for today?

Options:
- 20-min morning meditation
- Journaling prompt: [Rotation of prompts]
- Reading: Continue [Current Book]
- Gratitude practice
- Or just note intention

Today's practice:
```

**Evening**:
```
Evening practice check-in:

Did you practice today?
- Meditation: [X] min
- Journaling: [X] min
- Reading: [X] min
- Other: [X]

Quick reflection:
- One insight from today's practice?
- One thing you're grateful for?

Logging to WuWai...
Current practice streak: [X] days
```

### Aristóteles - Purpose Alignment Check

**Quarterly**:
```
QUARTERLY PURPOSE REFLECTION

Your last purpose statement (from [date]):
"[Purpose statement]"

Questions for this quarter:
1. Does this still ring true?
2. How have you lived this?
3. Where have you drifted?
4. What wants to evolve?

Based on your Pillars and activities this quarter, you seem to be:
[Analysis of alignment]

Would you like to update your purpose statement, or does it still serve?
```

### Aristóteles - Values Integrity Audit

**Monthly**:
```
VALUES INTEGRITY CHECK

Your core values:
1. [Value 1] - Strength: [X/10]
2. [Value 2] - Strength: [X/10]
3. [Value 3] - Strength: [X/10]

This month, you demonstrated:
✓ [Value]: [Example of living this]
⚠ [Value]: [Example of violation or struggle]

Reflection question:
Where is there gap between your espoused values and your lived values?

This awareness is the beginning of integrity.
```

### Aristóteles - Meaning Crisis Intervention

**If meaning crisis detected**:
```
I notice you may be experiencing a meaning crisis:
- Recent reflections express existential doubt
- Contemplative practice has dropped off
- Emotional state trending toward cynicism/detachment

This is not a failure. This is part of the path.

Suggestions:
1. Return to Purpose database - read your own words from meaningful periods
2. Death contemplation - reconnect with mortality for urgency and clarity
3. Read texts that previously moved you
4. Consider reaching out to spiritual mentor
5. Schedule deep nature time or retreat

What resonates?
```

---

## Sample Data

### Contemplative Practice Log Entry

```
Date: 2026-01-19
Meditation: 30
Meditation Type: Vipassana, Loving-Kindness
Meditation Quality: 7/10
Journaling: 20
Journaling Focus: Morning Pages, Philosophical Inquiry
Prayer/Contemplation: 0
Reading Wisdom Texts: 15
Texts Read: "The Miracle of Mindfulness" - Thich Nhat Hanh, Ch. 3
Yoga/Embodied Practice: 0
Nature Contemplation: 10
Total Practice Time: 75 minutes
Insights: "Noticed strong aversion to bodily pain during sit - same aversion pattern shows up in my impatience with difficult patients. The connection is clear."
Challenges: "Mind very scattered first 10 minutes. Judged myself. Then remembered judging is just another thought. That softened it."
Gratitude:
1. Another day alive and healthy
2. Access to these teachings
3. Time and space to practice
Intention for Tomorrow: "Return to breath earlier when mind wanders. 20-min minimum."
Mood Before: Stressed
Mood After: Calm
Integration: "Today in clinic, when patient was frustrating me, I paused, took 3 breaths, remembered they're suffering too. Compassion arose."
Energy Impact: Calming
```

### Philosophical Reflection

```
Title: On Being Both Healer and Human
Date: 2026-01-19
Type: Question, Essay
Philosophical Domain: Ethics, Meaning, Suffering
Life Context: Difficult patient death this week. I couldn't save them. Feeling the weight of this.
Question: "How do I hold my responsibility as a healer alongside my human limitations? Where is the line between professional duty and self-compassion?"
Reflection:
I've been taught to be competent, thorough, diligent. To do everything possible. But everything possible wasn't enough this time. They died anyway.

Part of me wants to believe I could have done more. Another part knows I did everything reasonable. The Stoics would say to focus only on what's in my control - my effort, my care, my skill. The outcome was never mine to control.

But that feels cold. It matters that they died.

Maybe the paradox is: I have to care deeply AND hold lightly. Total commitment to healing, total acceptance that I'm not God. The Bodhisattva vow - save all beings, knowing you can't save all beings.

This is the work. Not just the medicine, but this.
Influences: [Link to Marcus Aurelius, Pema Chödrön, Buddhist texts]
Open Questions: "How do I grieve each death without burning out from accumulated grief?"
Revisit Date: 2026-04-19 (check in 3 months)
Tags: Medicine, Death, Compassion, Suffering, Calling
```

### Value Entry

```
Value/Principle: Compassion
Definition: Recognizing suffering in others and in myself, and responding with kindness rather than judgment or aversion
Why It Matters: The core of why I became a physician. Suffering is universal. Compassion is the only sane response.
How I Live It:
- With patients: See the person, not just the disease
- With colleagues: Remember everyone is struggling with something
- With myself: Self-compassion when I fail or struggle
Related Pillar: Healing Mastery, Spiritual Evolution
Source: Buddhist teachings, my grandmother's example, patient interactions that broke my heart open
In Tension With: Efficiency (compassion takes time), Boundaries (can't save everyone)
Examples:
- Spent extra 20 min with anxious patient even when behind schedule
- Forgave myself for diagnostic error instead of spiraling into shame
Violations:
- Snapped at nurse last week when stressed - wasn't kind
- Judged myself harshly for being tired
Evolution: Used to think compassion was weakness. Now see it as strength and wisdom.
Current Status: Core Value
Strength: 7/10 (strong with patients, weaker with myself)
Date Added: 2023-06-15
Last Reviewed: 2026-01-15
```

---

## Gamification & Insights

**Practice Stats**:
- Current meditation streak: X days
- Total practice hours this year: X
- Books completed: X
- Life-changing insights captured: X
- Purpose statement evolution: X versions

**Aristóteles Insights**:
- "Your practice deepens during difficult periods - suffering catalyzes growth"
- "You've read widely but applied narrowly - integration opportunity"
- "Your contemplative practices all serve Spiritual Evolution Pillar - 0% serving other Pillars. How might mindfulness enhance your medical work?"

---

## Setup Checklist

Before agents use WuWai:
- [ ] Contemplative Practice Log database created
- [ ] Wisdom Library database created
- [ ] Philosophical Reflections database created
- [ ] Values & Principles database created
- [ ] Meaning & Purpose database created
- [ ] Spiritual Teachers & Mentors database created
- [ ] Death Contemplation database created
- [ ] Relations configured between databases
- [ ] Views created for agents
- [ ] JENI morning/evening practice prompts configured
- [ ] Aristóteles quarterly purpose review scheduled
- [ ] Import existing values and principles
- [ ] Import current reading list
- [ ] Write initial purpose statement

---

*WuWai: The examined life. The cultivated soul. The search for what's true and beautiful and worth living for.*

*"The unexamined life is not worth living." - Socrates*

*"We are not human beings having a spiritual experience. We are spiritual beings having a human experience." - Pierre Teilhard de Chardin*
