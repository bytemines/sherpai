---
name: brainstorming-mastermind
description: "Use for brainstorming sessions and before any creative work - creating features, building components, adding functionality, or modifying behavior. Explores user intent, requirements and design before implementation."
---

# Brainstorming for Technical & Product Development

Visual-first, low-friction brainstorming. Show approaches with diagrams, compare side-by-side, decide fast.

**Core principle**: Critique the real problem directly — use analogies as one lens among several to reveal blind spots.

---

## The Pipeline

```
┌─────────────┐      ┌─────────────────────┐      ┌─────────────┐
│  UNDERSTAND │ ───▶ │  EXPLORE & COMPARE  │ ───▶ │   DESIGN    │
│  (clarify)  │      │  (options + scores) │      │  (build it) │
└─────────────┘      └─────────────────────┘      └─────────────┘
```

---

## Phase 1: Understand

**Goal**: Get clarity fast.

1. Check project state (files, docs, recent commits)
2. Ask questions:
   - **Dependent** (answer affects next) → one at a time
   - **Independent** (don't block each other) → batch them
3. Confirm: purpose, constraints, who it's for

*Do not proceed to Phase 2 until you have complete clarity on goals, constraints, and requirements.*

---

## Phase 2: Explore & Compare

**Goal**: Show 3-4 options visually, score them, user picks one.

### For EACH Approach (keep it tight):

```
┌─────────────────────────────────────────────────────────┐
│  APPROACH NAME                                          │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  [Simple diagram - show the core structure]             │
│                                                         │
├─────────────────────────────────────────────────────────┤
│  What: 1-2 sentences describing the approach            │
│  Why it might win: 1 sentence                           │
│  Risk: 1 sentence                                       │
└─────────────────────────────────────────────────────────┘
```

*See [diagram-reference.md](diagram-reference.md) for diagram patterns*

### Then ONE Score Table:

| Approach | ROI | Simple | [Dim 3] | [Dim 4] | Risk | Score |
|----------|-----|--------|---------|---------|------|-------|
| A: Name  | 8   | 7      | 8       | 7       | Med  | 7.7   |
| B: Name  | 6   | 9      | 5       | 8       | Low  | 6.7   |
| C: Name  | 7   | 5      | 9       | 6       | High | 7.0   |

**Scoring dimensions:**
- **Always**: ROI/Value, YAGNI/Simplicity
- **When relevant**: SOLID Principles, Security
- **Pick 2-4 more**: Choose dimensions that matter most for THIS problem.

### Then ONE Comparative Analysis:

Critique all approaches together using three lenses:
- **Direct Analysis** — What are the real trade-offs?
- **Analogy Lens** — What do similar systems teach us?
- **Domain Knowledge** — What patterns succeed/fail here?

| Dimension | A: Name | B: Name | C: Name |
|-----------|---------|---------|---------|
| **Strengths** | ... | ... | ... |
| **Weaknesses** | ... | ... | ... |
| **Assumptions** | ... | ... | ... |
| **Fails when** | ... | ... | ... |

### Hybrid Check:
- Can we combine the best parts?
- If yes → **add hybrid to both tables** and score it
- Only recommend hybrid if it **beats top score**
- If no good hybrid → skip

### Recommend:
> "**Suggest [X]** because [1-2 sentences backed by scores]"

*User approves or requests adjustments. Loop until approved.*

---

## Phase 3: Design

**Goal**: Present the approved approach with enough detail to build.

### 1. Complete Architecture Diagram

Expand from the simple diagram into full component detail.

*See [diagram-reference.md](diagram-reference.md) for patterns*

### 2. Key Sections (validate each with user):

- **Components**: What are the parts?
- **Data Flow**: How does information move?
- **Integrations**: What external systems?
- **Error Handling**: What can go wrong?

*200-300 words per section. Check with user before continuing.*

### 3. Summary Card:

```
┌─────────────────────────────────────────────────────────┐
│  RECOMMENDATION: [Approach Name]          Score: X.X/10 │
├─────────────────────────────────────────────────────────┤
│  Why: [1-2 sentences]                                   │
│  Trade-offs: [What we're giving up]                     │
│  Reconsider if: [Conditions that change this]           │
└─────────────────────────────────────────────────────────┘
```

---

## After Design

- **Document**: Write to `docs/plans/YYYY-MM-DD-<topic>-design.md`
- **Build**: Ask "Ready to build?" → break into phases and milestones

---

## Example: Caching Decision

### Approaches:

**A: Redis Cache**
```
Client ──▶ Cache ──▶ DB
              └─miss─▶
```
What: Add Redis layer for API responses
Win: Sub-ms reads, proven tech
Risk: Cache invalidation complexity

**B: In-Memory**
```
Client ──▶ [App Memory] ──▶ DB
```
What: Store in application memory
Win: No infrastructure, simple
Risk: Lost on restart, no sharing

**C: CDN Edge**
```
Client ──▶ CDN ──▶ Origin
```
What: Cache at CDN level
Win: Global, zero app changes
Risk: Stale content, less control

### Score Table:

| Approach | ROI | Simple | Perf | Risk | Score |
|----------|-----|--------|------|------|-------|
| A: Redis | 8 | 6 | 9 | Med | 7.7 |
| B: Memory | 6 | 9 | 6 | Low | 7.0 |
| C: CDN | 7 | 8 | 8 | Med | 7.7 |
| **Hybrid: Redis + CDN** | 9 | 5 | 10 | Med | **8.0** |

### Comparative Analysis:

| Dimension | Redis | Memory | CDN | Hybrid |
|-----------|-------|--------|-----|--------|
| Strengths | Fast, scalable | No infra | Global reach | Best of both |
| Weaknesses | Ops overhead | Not shared | Stale content | Complex setup |
| Assumptions | Redis available | Single instance ok | Static content | Team can manage both |
| Fails when | Redis down | App restarts | Need fresh data | Either layer fails |

**Recommend**: Hybrid (Redis + CDN) — CDN for static/public, Redis for dynamic/auth. Best performance, acceptable complexity.

---

## Principles

- **Visual first** — diagrams before paragraphs
- **Compare, don't repeat** — one table across approaches, not per-approach
- **Three lenses** — critique using direct analysis, analogies, and domain knowledge
- **Score to decide** — numbers force clarity
- **Hybrid only if better** — don't add complexity for its own sake
- **User decides** — LLM recommends, user approves
- **Validate incrementally** — check each section with user
- **YAGNI** — remove unnecessary complexity

---

*Turn ideas into decisions with diagrams, scores, and clear trade-offs.*
