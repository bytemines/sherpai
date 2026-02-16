---
name: brainstorming-mastermind
description: "Use when starting creative work, designing features, planning architecture, or facing decisions with multiple valid approaches. Also use when requirements are unclear or you're tempted to jump straight to implementation."
---

# Brainstorming for Technical & Product Development

Visual-first, low-friction brainstorming. Show approaches with diagrams, compare side-by-side, decide fast.

**Core principle**: Critique the real problem directly — use analogies as one lens among several to reveal blind spots.

---

## When to Use

**Symptoms that trigger this skill:**
- "Let's build X" or "I need to implement Y"
- Multiple valid approaches exist (or might exist)
- Requirements feel unclear or incomplete
- You're tempted to start coding immediately
- Design decisions that affect architecture
- Team disagreement on approach

**Do NOT use for:**
- Bug fixes with obvious solutions
- Trivial changes (typos, config tweaks)
- Tasks where the approach is explicitly specified

---

## Red Flags — STOP If You Think These

| Thought | Reality |
|---------|---------|
| "This is simple, I'll just build it" | Simple-seeming tasks often have hidden complexity. Run Phase 1. |
| "I already know the best approach" | Your assumption may be wrong. Show 3 options anyway. |
| "User wants it fast, skip the process" | Fast ≠ skip. Compress phases, don't eliminate them. |
| "Diagrams aren't needed here" | Visual-first is core. Always show diagrams. |
| "The answer is obvious" | If obvious, the score table will prove it. Don't assume. |
| "I'll brainstorm in my head" | Externalize it. User can't see your thinking. |
| "One option is clearly best" | Show the comparison. Let the scores speak. |
| "The user gave enough context, no questions needed" | Users leave out constraints they assume are obvious. Ask anyway. |
| "I can infer the requirements" | Inferred requirements are assumptions. Validate them in Phase 1. |

**If you catch yourself thinking any of these: STOP. Follow the pipeline.**

---

## The Pipeline

```
┌─────────────┐      ┌─────────────────────┐      ┌─────────────┐
│  PHASE 1    │ ───▶ │  PHASE 2            │ ───▶ │  PHASE 3    │
│  UNDERSTAND │      │  EXPLORE & COMPARE  │      │  DESIGN     │
│  (clarify)  │      │  (options + scores)  │      │  (build it) │
└─────────────┘      └─────────────────────┘      └─────────────┘
     ▲                                                   │
     └───── Return here if assumptions surface ──────────┘
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

<GATE exit="phase-1">
STOP. Before showing ANY approaches, diagrams, or options, verify ALL of these:
- You asked at least ONE clarifying question and the user answered it
- You know the PURPOSE of what is being built
- You know the CONSTRAINTS (time, tech, scope)
- You know WHO this is for

If ANY of these are missing, stay in Phase 1. Ask another question.
Do NOT show approaches, score tables, or diagrams until this gate is satisfied.
</GATE>

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

<GATE exit="phase-2">
STOP. Before designing anything, verify ALL of these:
- You showed at least 3 approaches with diagrams
- You presented a score table comparing all approaches
- You gave a recommendation with reasoning
- The user explicitly approved an approach

If the user has NOT approved, wait. Do NOT proceed to Phase 3.
If you skipped diagrams or the score table, go back and show them.
</GATE>

### Before Design — Clarify the Chosen Approach:

Once user approves an approach, check for **approach-specific questions** not yet answered:
- Implementation details unique to this option
- Integration points that only matter for this approach
- Constraints that become relevant now

> "Before I design [X], a few quick questions specific to this approach: ..."

**If no questions remain → proceed directly to Phase 3.** Don't invent questions or add friction.

---

## Phase 3: Design

**Goal**: Present the approved approach with enough detail to build.

<GATE exit="phase-3">
STOP. Before writing ANY code, scaffolding, or invoking implementation tools, verify:
- You completed Phase 1 (questions asked and answered)
- You completed Phase 2 (approaches compared, user approved one)
- You are about to present the design, NOT implement it

This gate applies regardless of project size or perceived simplicity.
</GATE>

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

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Skipping Phase 1 clarification | Always ask questions first. Even "obvious" requirements have hidden assumptions. |
| Text-only approach descriptions | Every approach needs a mini diagram. No exceptions. |
| Separate analysis per approach | Use ONE comparison table. Side-by-side reveals trade-offs. |
| Forcing hybrid when it doesn't fit | Only propose hybrid if it actually beats top score. Sometimes simple wins. |
| Proceeding without user approval | Phase 2 ends with "Recommend X" and waiting. User must approve before Phase 3. |
| Over-engineering the design | YAGNI applies. Design what's needed, not what might be needed. |
| Ignoring team constraints | "Best" technically ≠ best for this team. Include capability in scoring. |
| Long paragraphs instead of diagrams | If you're writing >3 sentences, you probably need a diagram instead. |
| Showing approaches without asking questions | Phase 1 exists for a reason. You cannot skip it, even if the task seems clear. |

---

*Turn ideas into decisions with diagrams, scores, and clear trade-offs.*
