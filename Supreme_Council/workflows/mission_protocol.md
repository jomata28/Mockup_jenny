# Mission Protocol - Task Delegation & Execution Framework

**Version**: 1.0
**Last Updated**: 2026-01-19
**Owner**: Supreme AI Council

---

## Overview

The Mission Protocol defines how tasks flow through the Supreme AI Council, from user input through JENI to specialist agents and back to the user. This ensures consistent, high-quality execution while maintaining strategic alignment.

---

## Protocol Principles

1. **Single Point of Entry**: All user requests enter through JENI (via Telegram)
2. **Intelligent Routing**: JENI delegates to the specialist best equipped to handle the task
3. **Strategic Alignment**: All tasks verified against Pillars by Aristóteles when appropriate
4. **Transparent Communication**: User always knows who's working on what
5. **Closed Loop**: Every task gets a definitive resolution reported to user

---

## Mission Lifecycle

```
┌─────────────┐
│ 1. INITIATE │  User sends request via Telegram
└─────┬───────┘
      │
┌─────▼────────┐
│ 2. RECEIVE   │  JENI receives and authenticates
└─────┬────────┘
      │
┌─────▼─────────┐
│ 3. ANALYZE    │  JENI determines task type and specialist
└─────┬─────────┘
      │
┌─────▼─────────┐
│ 4. ROUTE      │  JENI delegates to specialist(s)
└─────┬─────────┘
      │
┌─────▼─────────┐
│ 5. EXECUTE    │  Specialist performs task
└─────┬─────────┘
      │
┌─────▼──────────┐
│ 6. SYNTHESIZE  │  JENI compiles results into executive summary
└─────┬──────────┘
      │
┌─────▼──────────┐
│ 7. DELIVER     │  User receives results
└─────┬──────────┘
      │
┌─────▼──────────┐
│ 8. ARCHIVE     │  Task logged to Notion for future reference
└────────────────┘
```

---

## Example Mission: Research Literature Review

### Full Protocol Walkthrough

**User Request** (via Telegram):
```
User: I need a literature review on AI applications in radiology for lung cancer screening
```

---

### 1. INITIATE
User submits request via Telegram. Message arrives at JENI's webhook.

---

### 2. RECEIVE & AUTHENTICATE

**JENI**:
```
Please enter your 4-digit PIN to continue.
```

**User**:
```
[PIN entered]
```

**JENI**:
```
✓ Authenticated.

Request received: Literature review on AI in radiology for lung cancer screening

I'm analyzing this now...
```

---

### 3. ANALYZE

**JENI's Internal Analysis**:
```
Request Type: Research / Literature Review
Domain: Medical (radiology) + Scientific (literature analysis)
Complexity: High (requires systematic search and synthesis)
Estimated Time: 2-4 hours
Pillar Relevance: Scientific Legacy, Healing Mastery

Specialist Selection:
- Primary: Airquimides (Research) - leads literature review
- Secondary: Asklepai (Medical) - validates clinical relevance

Strategic Check: Not needed (clearly aligned with user's Pillars)
```

---

### 4. ROUTE

**JENI to User**:
```
✓ Acknowledged. I'm delegating this to Airquimides (Research Specialist).

Expected completion: 3-4 hours
I'll notify you when the review is ready.
```

**JENI to Airquimides** (Internal):
```
MISSION BRIEFING - ID: MIS-20260119-001

REQUESTING USER: [User name]
SOURCE: Telegram direct request

MISSION TYPE: Literature Review

TOPIC: AI applications in radiology for lung cancer screening

CONTEXT:
- User is MD and AI freelancer
- User specializes in [medical specialty]
- This relates to both clinical practice (Healing Mastery) and potential research (Scientific Legacy)

SCOPE:
- Comprehensive but focused (not exhaustive systematic review)
- Emphasis on clinical application and current evidence
- Include both diagnostic AI and screening protocols
- Timeline: Last 5 years primarily, seminal older papers if critical

DELIVERABLES REQUIRED:
1. Executive Summary (3-4 paragraphs)
2. Key findings organized by theme
3. Annotated bibliography of top 10-15 papers
4. Identification of knowledge gaps or research opportunities
5. Clinical application recommendations
6. Full literature database in Notion

DEADLINE: Within 4 hours (flexible)

COORDINATION:
- I will route your completed review to Asklepai for clinical validation
- You may consult Asklepai if clinical questions arise during review

Please confirm receipt and estimated completion time.
```

**Airquimides**:
```
Mission MIS-20260119-001 received and accepted.

Estimated completion: 3 hours

Beginning literature search now.
I'll provide progress update at 1.5 hour mark.

- Airquimides
```

---

### 5. EXECUTE

**Airquimides' Execution**:

**T+0:00** - Begin systematic literature search
- Databases: PubMed, Scopus, Web of Science
- Keywords: "artificial intelligence" OR "machine learning" OR "deep learning" AND "radiology" AND "lung cancer" AND "screening"
- Filters: English, last 5 years, human studies
- Initial results: 347 papers

**T+0:30** - Screen abstracts for relevance
- Inclusion criteria: AI models for lung cancer screening in radiology
- Exclusion: Treatment AI, non-imaging AI, opinion pieces without data
- Relevant papers: 42

**T+1:00** - Full-text review of top papers
- Categorize by: Diagnostic performance, Implementation studies, Reviews, Novel methods

**T+1:30** - Progress Update to JENI
```
Airquimides → JENI:

Progress update on MIS-20260119-001 (50% complete):

- 42 relevant papers identified from initial search of 347
- Top 15 papers selected for detailed analysis
- Emerging themes: CNN-based screening, low-dose CT optimization, integration with radiology workflow
- Notable gap: Implementation barriers in clinical settings

On track for 3-hour completion.
```

**JENI → User**:
```
Update: Airquimides is 50% complete with your literature review.
Progress is on track. Expect results in ~1.5 hours.
```

**T+2:30** - Synthesis and writing
- Draft executive summary
- Create thematic organization
- Write annotations for top papers
- Identify research opportunities

**T+2:45** - Create Notion database entry
- Add all 42 papers to Literature Library
- Tag with topic, relevance, key findings
- Link to Research Ideas database

**T+3:00** - Final review and quality check

**Airquimides → JENI**:
```
Mission MIS-20260119-001 COMPLETED

Deliverable ready for user review.

Summary: Comprehensive review of 42 papers on AI in lung cancer screening.
Notable findings: High sensitivity/specificity in controlled studies, but implementation gap in clinical practice.

Should I route to Asklepai for clinical integration review, or deliver directly?
```

**JENI**:
```
Route to Asklepai for clinical validation, then I'll synthesize for user.
```

---

**JENI to Asklepai**:
```
MISSION: Clinical Validation Review
SUBJECT: Airquimides' literature review on AI lung cancer screening

Airquimides has completed a comprehensive literature review.
Please review findings for:
1. Clinical applicability in current practice
2. Integration opportunities for user's clinical work
3. Any red flags or misinterpretations

Review attached: [Link to Airquimides' report]

Time needed: ~30 minutes

Confirm receipt.
```

**Asklepai**:
```
Confirmed. Reviewing now.
```

**T+3:20** - Asklepai review complete

**Asklepai → JENI**:
```
Clinical review complete.

ASSESSMENT:
✓ Literature review is comprehensive and accurate
✓ Performance metrics correctly interpreted
✓ Clinical context appropriate

ADDITIONS:
- Added note on FDA-approved lung cancer AI tools (3 current approvals)
- Highlighted ACR guidelines on AI integration
- Flagged most clinically relevant papers for user's practice setting

CLINICAL INTEGRATION OPPORTUNITIES:
User could:
1. Pilot AI screening tool in their radiology workflow
2. Collaborate on implementation research (gap identified)
3. Serve as medical advisor for lung cancer AI companies

Ready for user delivery.
```

---

### 6. SYNTHESIZE

**JENI compiles**:
- Airquimides' comprehensive review
- Asklepai's clinical validation and additions
- Action items and opportunities
- Links to Notion databases

---

### 7. DELIVER

**JENI to User** (via Telegram):
```
✅ Literature Review Complete

Your research on AI in lung cancer screening is ready.

**Executive Summary:**
Airquimides reviewed 42 high-quality papers on AI applications in lung cancer screening. The evidence shows strong diagnostic performance in controlled settings (sensitivity 85-95%, specificity 80-90%), but a significant implementation gap exists in real-world clinical practice. Most AI tools use convolutional neural networks on low-dose CT scans.

**Key Findings:**
• 3 FDA-approved AI tools currently available
• Performance comparable to expert radiologists in studies
• Integration challenges: workflow disruption, radiologist training, liability concerns
• Underexplored area: Cost-effectiveness and patient outcomes

**Clinical Relevance (from Asklepai):**
You could integrate these tools in your practice. ACR has published guidelines for AI adoption in radiology departments. Strong opportunity for implementation research.

**Business Opportunity (from Seshait perspective):**
Medical AI consulting opportunity - hospitals need expert guidance on implementing these tools.

**Full Report:** [Link to Notion page with complete review]

**Top 5 Must-Read Papers:** [Link to curated list]

**Next Steps - What would you like to do?**
1. Deep dive into specific subtopic?
2. Explore implementation research opportunity?
3. Connect with AI companies in this space?
4. Archive and move to next task?

Let me know how else I can help with this.
```

---

### 8. ARCHIVE

**JENI's Internal Actions**:
1. Log mission to Completed Missions database
2. Tag with Pillars served (Scientific Legacy, Healing Mastery)
3. Record time spent (3.5 hours total)
4. Note specialists involved (Airquimides primary, Asklepai validation)
5. Create retrievable reference for future similar requests

**Notion Database Entry**:
```
Mission: AI Lung Cancer Screening Literature Review
Date: 2026-01-19
Specialists: Airquimides (lead), Asklepai (validation)
Time: 3.5 hours
Outcome: Comprehensive review delivered
Pillars: Scientific Legacy, Healing Mastery
Follow-up: Potential implementation research project
Status: Completed
User Satisfaction: [To be collected]
```

---

## Task Routing Matrix

**How JENI Decides Which Specialist**:

| Request Type | Primary Specialist | Secondary | Strategic Check |
|--------------|-------------------|-----------|-----------------|
| Medical question | Asklepai | - | No |
| Research literature review | Airquimides | Asklepai (if medical) | No |
| Grant opportunity | Airquimides | Seshait (financials) | No |
| AI business decision | Seshait | Asklepai (if medical AI) | Yes (if major) |
| Financial planning | Seshait | - | Yes (if life-changing) |
| Career decision | Aristóteles | Domain specialist | Yes (always) |
| Major life decision | Aristóteles | - | Yes (always) |
| Schedule management | JENI (handles directly) | - | No |
| System issue | Vulkain | - | No |
| Goal setting | Aristóteles | Domain specialist | Yes (always) |
| CRM/networking | JENI via Hugain | - | No |
| Energy/time management | JENI via Manai | Aristóteles (if burnout) | If concerning |

---

## Multi-Specialist Missions

**When Multiple Specialists Needed**:

### Example: "Should I accept this fellowship?"

**JENI Routes To**:
1. **Aristóteles** (Primary) - Strategic & Pillar alignment
2. **Asklepai** - Medical career trajectory analysis
3. **Seshait** - Financial implications
4. **Airquimides** - Academic reputation and research opportunities

**Execution**:
- Specialists work in parallel
- Each provides domain analysis
- JENI synthesizes into decision framework
- Aristóteles provides final strategic recommendation
- User makes ultimate decision

---

## Emergency Protocol

**When User Needs Immediate Response**:

**User**:
```
URGENT: [request]
```

**JENI**:
- Skip normal queue
- Provide immediate response if within capability
- If requires specialist: Flag as URGENT priority
- Target response: <30 minutes
- Keep user updated every 10 minutes

**Urgent Escalation Criteria**:
- Medical emergency (route to Asklepai + recommend seeking immediate care)
- System failure (route to Vulkain)
- Security incident (route to Vulkain)
- Time-sensitive deadline (same-day grant submission, etc.)

---

## Quality Control

**After Task Completion**:

1. **User Feedback Collection** (optional):
   ```
   How would you rate this result?
   ⭐⭐⭐⭐⭐ Excellent
   ⭐⭐⭐⭐ Good
   ⭐⭐⭐ Acceptable
   ⭐⭐ Needs improvement
   ⭐ Unsatisfactory

   [Optional: Brief feedback]
   ```

2. **Logged for Improvement**:
   - Patterns in low ratings analyzed
   - Specialist performance tracking
   - Process bottlenecks identified
   - Continuous improvement

---

## Common Mission Types

### 1. Information Retrieval
- User asks question
- JENI queries appropriate Vault or specialist
- Result delivered in <5 minutes
- Logged to Notion

### 2. Analysis Task
- User provides data/situation
- Specialist analyzes
- Structured report delivered
- Recommendations provided

### 3. Creative/Generative Task
- User needs content created (proposal, manuscript section, etc.)
- Specialist drafts
- User reviews and requests revisions
- Iterative until satisfied

### 4. Decision Support
- User facing decision
- Multiple specialists provide input
- Aristóteles synthesizes for strategic lens
- User decides; system logs decision and rationale

### 5. Ongoing Monitoring
- User wants continuous tracking (new papers, stock prices, etc.)
- Specialist sets up automated monitoring
- Periodic reports generated
- Alerts for significant events

---

## Mission Protocol Best Practices

**For JENI**:
- Always acknowledge receipt within 30 seconds
- Set clear expectations on timeline
- Provide progress updates for tasks >1 hour
- Synthesize multi-specialist input into coherent narrative
- Close the loop (confirm user satisfied)

**For Specialists**:
- Confirm mission receipt and estimated completion
- Provide progress updates if task >2 hours
- Ask clarifying questions early (don't assume)
- Deliver results in structured format
- Flag any concerns or blockers immediately

**For User**:
- Provide context when possible (helps specialists prioritize)
- Specify urgency if time-sensitive
- Give feedback on results (helps system improve)

---

## Version History

- **v1.0** (2026-01-19): Initial Mission Protocol established

---

*This protocol ensures every mission is executed with precision, strategic alignment, and user satisfaction.*
