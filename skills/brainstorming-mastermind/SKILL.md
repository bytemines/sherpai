---
name: brainstorming-mastermind
description: "Use for brainstorming sessions and before any creative work - creating features, building components, adding functionality, or modifying behavior. Explores user intent, requirements and design before implementation with systematic evaluation."
---

# Brainstorming for Technical & Product Development

## Overview

Turn ideas into fully formed designs through collaborative dialogue with systematic thinking. Generate diverse solutions, **critique approaches using multiple lenses**, and score options with clear trade-offs.

**Core principle**: Critique the real problem directly — use analogies as one tool among several to reveal blind spots.

---

## The Brainstorming Pipeline

### Phase 1: Understand the Idea

- Check current project state first (files, docs, recent commits)
- Ask questions to refine the idea:
  - **Dependent questions** (answer affects next) → One at a time
  - **Independent questions** (don't block each other) → Batch them
- Focus on: purpose, constraints, success criteria, stakeholders

---

### Phase 2: Generate & Explore (3-5 Approaches)

#### For EACH approach:

**Step 1: Describe the Approach**
- What it is and why it could work (2-3 sentences)

**Step 2: Find an Analogy** *(optional but powerful)*
- "This is like [familiar system] because..."
- Connects to something the user understands

**Step 3: Critique the Approach**

Critique the **real solution** using three lenses:

| Lens | Question |
|------|----------|
| **Direct Analysis** | "What are the real trade-offs here?" |
| **Analogy Lens** | "What do similar systems teach us?" |
| **Domain Knowledge** | "What do I know about this space?" |

**Critique questions with all three lenses:**

| Question | Direct Analysis | Analogy Lens | Domain Knowledge |
|----------|-----------------|--------------|------------------|
| **Strengths** | What does this approach do well for OUR problem? | What works in similar systems? | What patterns succeed in this domain? |
| **Weaknesses** | Where does this fall short for OUR needs? | What gaps do similar systems reveal? | What commonly fails here? |
| **Assumptions** | What must be true for this to work? | What assumptions exist in analogous systems? | What do experts assume in this space? |
| **Failure Modes** | How could this break in OUR context? | How have similar systems failed? | What are known failure patterns? |
| **Unique Aspects** | What's different about THIS problem? | Where does the analogy break? | What makes our situation special? |

**Key insight**: The analogy is a **lens, not the target**. Always bring critique back to the real problem.

#### Gather information by type:

| Info Type | Question | Action |
|-----------|----------|--------|
| **Procedural** | "How to do it?" | Think through actual execution steps |
| **Conceptual** | "What is it?" | Map connections & big picture |
| **Evidence** | "What proves it?" | Store concrete examples for later |

---

### Phase 3: Score, Hybrid & Select

#### Score each approach (1-10) on relevant dimensions:

**Always include:**
- **ROI/Value**: Benefit vs investment (time, complexity, resources)
- **YAGNI/Simplicity**: How much unnecessary complexity does this add?

**Include when relevant:**
- **SOLID Principles**: For code architecture decisions
- **Security**: When risk exposure matters (lower priority otherwise)

**Pick 3-4 additional from:**
- **Technical Feasibility**: Can we build this with current skills/tools?
- **User Experience**: How well does this solve the user's real problem?
- **Maintainability**: How easy to debug, extend, and modify?
- **Performance**: Speed, scalability, resource usage
- **Time to Market**: How quickly can we deliver value?
- **Integration**: How well does this fit with existing systems?
- **Team Capability**: Do we have the skills to execute?

#### Present scores:

```markdown
| Approach | ROI | Simplicity | [Dim 3] | [Dim 4] | [Dim 5] | **Total** |
|----------|-----|------------|---------|---------|---------|-----------|
| A: Name  | 7   | 8          | 6       | 7       | 8       | **7.2**   |
| B: Name  | 9   | 6          | 8       | 9       | 8       | **8.0**   |
| C: Name  | 5   | 9          | 5       | 6       | 7       | **6.4**   |
```

#### Consider Hybrid Approach:

After scoring, look for opportunities to combine the best parts.

**Rules:**
- Only propose hybrid if it **beats the top score**
- If no hybrid beats the winner → skip this step
- Score the hybrid using the same dimensions

#### Adjustment Loop:
- If adjustments needed → refine and re-score
- Repeat until confident in recommendation

#### Recommend:
> "I suggest [Approach X] because [reason backed by scores and critique insights]"

---

### Phase 4: Present Final Design

#### 1. Architecture Overview
- ASCII diagram showing the solution structure
- **Reference**: Use [diagram-reference.md](diagram-reference.md) for diagram patterns and construction

#### 2. Present Design in Sections
- Break into 200-300 word sections
- Cover: architecture, components, data flow, error handling, testing
- **Validate each section** with user before continuing
- Be ready to adjust

#### 3. Final Summary

```markdown
## Recommendation: [Chosen Approach]

**Score: X.X/10**

**Why this wins**: [Explain using insights from critique — both direct analysis and analogy]

**Trade-offs accepted**: [What we're consciously giving up]

**Reconsider if**: [Specific conditions that would change this decision]
```

---

### After the Design

**Documentation:**
- Write to `docs/plans/YYYY-MM-DD-<topic>-design.md`
- Include: problem context, approaches considered, scores, reasoning
- Commit to git

**Implementation (if continuing):**
- Ask: "Ready to create implementation plan?"
- Break into phases and milestones

---

## Examples

### Example 1: Caching System Critique

**Approach**: Add Redis caching layer for API responses

**Analogy**: "This is like a restaurant's prep station — pre-preparing common items instead of cooking from scratch each time."

**Critique using all three lenses:**

| Question | Direct Analysis | Analogy Lens | Domain Knowledge |
|----------|-----------------|--------------|------------------|
| **Strengths** | Reduces DB load, faster responses for repeated queries | Prep stations handle rush hour well | Redis is battle-tested, sub-ms latency |
| **Weaknesses** | Adds infrastructure complexity, cache invalidation is hard | Prep food gets stale | Cache stampede on cold start is a known issue |
| **Assumptions** | Access patterns are predictable, stale data is acceptable briefly | Assumes we know "commonly ordered" items | Assumes Redis cluster won't be a bottleneck |
| **Failure Modes** | Cache corruption, memory exhaustion, thundering herd | If prep station fails, kitchen slows but works | Redis failover can cause brief outages |
| **Unique Aspects** | Our data has complex relationships (unlike simple prep items) | Food spoils physically; our data might become logically invalid | We need event-driven invalidation, not just TTL |

**Insight from critique**: The analogy reveals we need graceful degradation (kitchen still works without prep), but breaks down for invalidation — we need explicit event-driven cache busting, not just time-based expiry.

---

### Example 2: Hybrid Decision

**Initial Scores:**
| Approach | ROI | Simplicity | Performance | **Total** |
|----------|-----|------------|-------------|-----------|
| A: React SPA | 8 | 6 | 9 | **7.7** |
| B: Server-rendered | 7 | 9 | 6 | **7.3** |
| C: Static site | 6 | 8 | 8 | **7.3** |

**Hybrid consideration**: "What if we combine A's interactivity with B's initial load? → Next.js"

**Hybrid Score:**
| Approach | ROI | Simplicity | Performance | **Total** |
|----------|-----|------------|-------------|-----------|
| **Hybrid: Next.js** | 9 | 7 | 9 | **8.3** |

**Result**: Hybrid beats top (8.3 > 7.7) → **Propose hybrid**

---

## Key Principles

### Exploration
- **Questions**: Dependent → one at a time | Independent → batch
- **Critique the approach, not just the analogy** — analogy is a lens
- **Three lenses**: Direct analysis + Analogy + Domain knowledge
- **Think through execution** — work through actual steps
- **Challenge assumptions** — question what seems "obvious"

### Evaluation
- **Always ROI and YAGNI** — these matter for every decision
- **SOLID when relevant** — for architecture decisions
- **Security when required** — lower priority unless context demands
- **Hybrid only if it wins** — don't propose if it doesn't beat top score
- **Ground in evidence** — concrete examples, not generic reasoning

### Quality
- **Validate incrementally** — check each section with user
- **Adjust and re-score** — update scores when things change
- **Document reasoning** — future you needs to understand "why"
- **YAGNI ruthlessly** — remove unnecessary complexity

---

*Transform ideas into well-reasoned designs by critiquing approaches directly, using analogies as one lens among several, and scoring trade-offs systematically.*
