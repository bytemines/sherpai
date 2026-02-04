# ASCII Diagram Reference Guide

*Curated collection of high-value ASCII patterns for system presentation*

---

## Quick Creation Guidelines

> **Read these rules FIRST before creating any ASCII diagram**

### 1. Alignment Rules (Critical)

**Always verify before finalizing:**
```
✓ CORRECT (uniform width, aligned edges):
┌──────────┐    ┌──────────┐    ┌──────────┐
│  Box A   │───▶│  Box B   │───▶│  Box C   │
└──────────┘    └──────────┘    └──────────┘

✗ WRONG (uneven widths, misaligned):
┌──────────┐    ┌───────┐    ┌─────────────┐
│  Box A   │───▶│ Box B │───▶│   Box C      │
└──────────┘    └───────┘    └─────────────┘
```

### 2. Quick Validation Checklist

Before presenting any diagram, verify:

```
□ All boxes in a row have SAME width
□ Vertical lines (│) form straight columns
□ Arrows have consistent length (───▶ not ─▶)
□ Labels are padded to fill box width
□ Gaps between boxes are uniform (4 spaces recommended)
```

**Quick visual test:** Squint at the diagram — misalignment becomes obvious.

### 3. Essential Characters

**Box Drawing:**
```
Corners:    ┌  ┐  └  ┘
Edges:      │  ─
T-joins:    ├  ┤  ┬  ┴
Cross:      ┼
```

**Arrows & Flow:**
```
Single direction:    ───▶   ◀───   ▲   ▼
Bi-directional:      ◀───▶  ◀──▶
```

**Decision & Status:**
```
Decision points:     ◆  ◇
Start/end states:    ○  ●
Process blocks:      □  ■
```

### 4. Choose the Right Pattern

| Use Case | Pattern |
|----------|---------|
| Component relationships | Simple Component Flow |
| Service boundaries | Cross-Boundary Architecture |
| Logic flow | Decision Flow |
| API calls | Sequence Pattern |
| Status tracking | State Machine |
| File organization | Hierarchical Structure |
| Feature comparison | Configuration Matrix |
| Project phases | Timeline |
| Async communication | Message Queue Pattern |
| Data processing | Data Pipeline Flow |
| Infrastructure | Cloud Architecture Pattern |

### 5. Adaptation Rules

- **Replace labels** with your specific components/services
- **Maintain alignment** — consistent spacing and borders
- **Scale complexity** — add more boxes/steps as needed
- **Keep flow direction** — left-to-right or top-to-bottom

### 6. Presentation Tips

- **Start simple** — begin with basic pattern, add complexity gradually
- **Label clearly** — use meaningful names, not generic terms
- **Group visually** — use whitespace and borders to show relationships
- **Test readability** — can non-technical stakeholders follow the flow?

---

## Brainstorming Pipeline (Skill-Specific)

**3-Phase Overview:**
```
┌─────────────┐      ┌─────────────────────┐      ┌─────────────┐
│  UNDERSTAND │ ───▶ │  EXPLORE & COMPARE  │ ───▶ │   DESIGN    │
│  (clarify)  │      │  (options + scores) │      │  (build it) │
└─────────────┘      └─────────────────────┘      └─────────────┘
```

**Detailed View:**
```
┌──────────────────────────────────────┐
│  PHASE 1: UNDERSTAND                 │
│  • Check project state               │
│  • Ask questions (dependent/batch)   │
│  • Confirm: purpose, constraints     │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│  PHASE 2: EXPLORE & COMPARE          │
│  For EACH approach:                  │
│  • Mini diagram + What/Win/Risk      │
│  Then ONE comparison table:          │
│  • Scores (ROI, Simple, etc.)        │
│  • Strengths/Weaknesses/Fails when   │
│  • Add hybrid if it beats top score  │
│  • Recommend → User approves         │
│  • Clarify chosen (if needed)        │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│  PHASE 3: DESIGN                     │
│  • Full architecture diagram         │
│  • Components, Data Flow, Errors     │
│  • Validate each section with user   │
│  • Summary card with trade-offs      │
└──────────────────────────────────────┘
```

**Approach Card Template:**
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

---

## Essential Diagram Patterns

### System Architecture

**Simple Component Flow** — *Foundation pattern*
```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Frontend  │───▶│   Backend   │───▶│  Database   │
│   (React)   │    │  (Node.js)  │    │ (PostgreSQL)│
└─────────────┘    └─────────────┘    └─────────────┘
```

**Cross-Boundary Service Architecture** — *Advanced pattern*
```
┌─────────────────────────┐     ┌───────────────────────────────────────────────────────┐
│         Browser         │     │                          ARC                          │
│                         │     │                                                       │
│  ┌───────────────────┐  │     │  ┌────────────┐    ┌───────┐    ┌──────────────┐    │
│  │    Web Payment    │◀─┼─────┼─▶│ PaymentApp │◀──▶│  TWA  │◀──▶│ Play Billing │    │
│  └───────────────────┘  │     │  └────────────┘    └───────┘    └──────────────┘    │
│                         │     │                                                       │
└─────────────────────────┘     └───────────────────────────────────────────────────────┘
```

---

### Process Flow

**Decision Flow with Error Handling** — *Essential logic pattern*
```
       Start
         │
         ▼
    ┌──────────┐
    │Validation│
    └────┬─────┘
         │
         ▼
       Valid?
      ┌──┴──┐
      │     │
     Yes    No
      │     │
      ▼     ▼
   Process Error
      │     │
      ▼     │
   Success◀─┘
```

---

### Sequence & Interaction

**API Communication Pattern** — *Essential for distributed systems*
```
    Client             Server            Database
      │                  │                  │
      │─── Request ─────▶│                  │
      │                  │─── Query ───────▶│
      │                  │◀── Result ───────│
      │◀── Response ─────│                  │
      │                  │                  │
```

---

### State Management

**State Machine Flow** — *Essential for status tracking*
```
[Idle] ──event──▶ [Processing] ──complete──▶ [Done]
   ▲                    │                      │
   └───── error ────────┘                      │
   ◀───── reset ───────────────────────────────┘
```

---

### Hierarchical Structure

**File/Project Structure** — *Essential for documentation*
```
project/
├── src/
│   ├── components/
│   │   ├── Button.jsx
│   │   └── Form.jsx
│   └── utils/
│       └── helpers.js
├── docs/
└── tests/
```

---

### Comparison & Configuration

**Feature/Configuration Matrix** — *Essential for stakeholder presentations*
```
┌────────────┬───────────┬───────────┬────────────┐
│ Feature    │ Basic     │ Pro       │ Enterprise │
├────────────┼───────────┼───────────┼────────────┤
│ Users      │ 10        │ 100       │ Unlimited  │
├────────────┼───────────┼───────────┼────────────┤
│ Storage    │ 1GB       │ 100GB     │ 1TB        │
├────────────┼───────────┼───────────┼────────────┤
│ Support    │ Email     │ Chat      │ Phone      │
└────────────┴───────────┴───────────┴────────────┘
```

---

### Timeline & Planning

**Project Timeline** — *Essential for planning presentations*
```
    Q1 2024        Q2 2024        Q3 2024        Q4 2024
       │              │              │              │
       ├── Phase 1 ───┤              │              │
       │              ├── Phase 2 ───┤              │
       │              │              ├── Phase 3 ───┤
       │              │              │              ├── Launch
```

---

### Data Flow & Events

**Message Queue Pattern** — *Essential for async communication*
```
   Producer          Queue           Consumer
      │                │                │
      │── publish ────▶│                │
      │                ├─[msg1]         │
      │                ├─[msg2]────────▶│── process
      │                ├─[msg3]         │
      │── publish ────▶│                │
      │                │                │
```

**Data Pipeline Flow** — *Essential for ETL/data processing*
```
Source Data ───▶ Transform ───▶ Validate ───▶ Store ───▶ Analytics
      │              │              │            │            │
 ┌──────────┐   ┌──────────┐   ┌──────────┐ ┌──────────┐ ┌──────────┐
 │ Raw CSV  │   │  Clean   │   │ Business │ │ Database │ │Dashboard │
 │  Files   │   │ & Format │   │  Rules   │ │          │ │ Reports  │
 └──────────┘   └──────────┘   └──────────┘ └──────────┘ └──────────┘
```

---

### Infrastructure & Deployment

**Cloud Architecture Pattern** — *Essential for modern deployments*
```
Internet ───▶ Load Balancer ───▶ App Servers ───▶ Database
                    │                  │              │
               ┌─────────┐       ┌───────────┐   ┌──────────┐
               │ AWS ALB │       │    ECS    │   │   RDS    │
               │         │       │┌─────────┐│   │          │
               └─────────┘       ││ App x3  ││   │  Master  │
                                 │└─────────┘│   │ + Replica│
                                 └───────────┘   └──────────┘
```

---

## Summary

**Why These Patterns**: Selected based on presentation value, adaptability across domains, and stakeholder clarity. These curated patterns cover 95% of system presentation needs.

**For brainstorming**: Diagrams don't need to be pixel-perfect. Use the quick checklist, focus on clarity over precision.

*Use these patterns to communicate system design effectively.*
