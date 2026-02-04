# Diagram Reference Guide

*Reference collection for ASCII and Mermaid diagrams - load only when creating architecture visualizations*

---

## ASCII Alignment Rules (Critical)

```
✓ CORRECT (uniform width, aligned edges):
┌──────────┐    ┌──────────┐    ┌──────────┐
│  Box A   │───▶│  Box B   │───▶│  Box C   │
└──────────┘    └──────────┘    └──────────┘

✗ WRONG (uneven widths, misaligned):
┌──────────┐    ┌───────┐    ┌─────────────┐
│  Box A   │───▶│ Box B │───▶│   Box C     │
└──────────┘    └───────┘    └─────────────┘
```

**Checklist before presenting:**
- [ ] All boxes in a row have **identical width**
- [ ] Vertical lines (`│`) align in columns
- [ ] Arrows (`───▶`) have consistent length
- [ ] Gaps between boxes are uniform (4 spaces)

---

## Essential Characters

**Box Drawing:**
```
Corners:    ┌  ┐  └  ┘
Edges:      │  ─
T-joins:    ├  ┤  ┬  ┴
Cross:      ┼
```

**Arrows:**
```
Single:     ───▶   ◀───   ▲   ▼
Bi-dir:     ◀───▶
```

---

## Pattern Reference

### Simple Component Flow
```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Frontend  │───▶│   Backend   │───▶│  Database   │
└─────────────┘    └─────────────┘    └─────────────┘
```

### Decision Flow
```
       Start
         │
         ▼
    ┌──────────┐
    │Validation│
    └────┬─────┘
         │
       Valid?
      ┌──┴──┐
     Yes    No
      │     │
      ▼     ▼
   Process Error
```

### API Sequence
```
    Client             Server            Database
      │                  │                  │
      │─── Request ─────▶│                  │
      │                  │─── Query ───────▶│
      │                  │◀── Result ───────│
      │◀── Response ─────│                  │
```

### State Machine
```
[Idle] ──event──▶ [Processing] ──complete──▶ [Done]
   ▲                    │                      │
   └───── error ────────┘                      │
   ◀───── reset ───────────────────────────────┘
```

### File Structure
```
project/
├── src/
│   ├── components/
│   └── utils/
├── docs/
└── tests/
```

---

## Brainstorming Pipeline Visual (3 Phases)

```
┌─────────────┐      ┌─────────────────────┐      ┌─────────────┐
│  UNDERSTAND │ ───▶ │  EXPLORE & COMPARE  │ ───▶ │   DESIGN    │
│  (clarify)  │      │  (options + scores) │      │  (build it) │
└─────────────┘      └─────────────────────┘      └─────────────┘
```

### Detailed View

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
│  • Scores (ROI, Simple, UX, etc.)    │
│  • Strengths/Weaknesses/Fails when   │
│  • Add hybrid if it beats top score  │
│  • Recommend winner                  │
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

---

## Mermaid Diagrams

### Main Workflow (3 Phases)

```mermaid
flowchart LR
    subgraph P1["1: UNDERSTAND"]
        P1A["Check state"] --> P1B["Ask questions"] --> P1C["Confirm goals"]
    end
    subgraph P2["2: EXPLORE & COMPARE"]
        P2A["Show approaches<br/>with diagrams"] --> P2B["Score table"]
        P2B --> P2C{"Hybrid?"}
        P2C -->|beats top| P2D["Add to table"]
        P2C -->|no| P2E["Skip"]
        P2D --> P2F["Recommend"]
        P2E --> P2F
    end
    subgraph P3["3: DESIGN"]
        P3A["Architecture"] --> P3B["Sections"] --> P3C{"OK?"}
        P3C -->|adjust| P3B
        P3C -->|yes| P3D["Summary card"]
    end
    P1 ==> P2 ==> P3
```

### Quick Reference

```mermaid
flowchart LR
    A["UNDERSTAND"] ==> B["EXPLORE & COMPARE<br/>diagrams + scores + hybrid"] ==> C["DESIGN<br/>architecture + sections"]
    B -.->|hybrid?| B
    C -.->|iterate| C
```

### Approach Card Pattern

```mermaid
flowchart TB
    subgraph card["APPROACH: Name"]
        direction TB
        diagram["📊 Mini Diagram"]
        what["What: description"]
        win["Win: why it might work"]
        risk["Risk: main concern"]
    end
```

---

*Use these patterns to communicate system design effectively.*
