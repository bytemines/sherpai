---
name: codebase-analysis
description: "Use when analyzing a codebase for health, large files, organization issues, refactoring opportunities, or onboarding to a new project. Also use when code feels messy, hard to navigate, or when you suspect structural problems."
---

# Codebase Analysis

Scan, score, and analyze a codebase across three lenses in parallel. Python script does fast deterministic scanning; three agents do deep reasoning concurrently. Produces a persistent report.

**Core principle:** Numbers first, judgment second. Script finds what's big/complex, agents read the actual code to decide what matters.

---

## Agents

This skill orchestrates three agents that run **in parallel** (they are independent):

| Agent | File | Job |
|-------|------|-----|
| **file-size-analyzer** | `agents/file-size-analyzer.md` | Read large files, assess KEEP/SPLIT/CONSIDER |
| **scope-organizer** | `agents/scope-organizer.md` | Map directory structure, check cohesion & coupling |
| **pattern-detector** | `agents/pattern-detector.md` | Grep for naming, errors, anti-patterns, good patterns |

---

## When to Use

- Onboarding to a new/unfamiliar codebase
- "This repo feels messy" — need concrete data
- Pre-refactoring assessment
- Periodic health checks
- After rapid growth phases

**Do NOT use for:**
- Single file reviews (just read the file)
- Known bugs (use systematic-debugging)
- Style-only issues (use a linter)

---

## Step 1: Run the Scanner

Run `analyzer.py` from this skill's directory. It scans the filesystem, counts lines/keywords/imports, scores files, and groups by scope.

```bash
# ASCII overview for the user
python skills/codebase-analysis/analyzer.py --root . --ascii

# JSON data for agents
python skills/codebase-analysis/analyzer.py --root . > /tmp/codebase-scan.json
```

**Flags:** `--threshold N` (min lines, default 200), `--scope path/` (focus areas)

Present the ASCII report to the user. Read the JSON output — this is the data you'll feed to agents.

---

## Step 2: Spawn 3 Agents in Parallel

From the JSON scan results, prepare the data slices and launch all three agents simultaneously using the Agent tool. **All three in a single message — do NOT wait between them.**

### Agent 1: file-size-analyzer
**Input:** Top 10 largest files (or all files in `urgent`/`refactor` categories) with their paths, line counts, scores, and language.
**Prompt template:**
```
Analyze these files from a codebase scan. For each, read the file and assess KEEP/SPLIT/CONSIDER.

Project: {project_name} ({project_type})
Files:
{for each file: path, lines, score, language, category}

Follow your agent instructions for process and output format.
```

### Agent 2: scope-organizer
**Input:** The `scopes` section from the JSON with file counts, total lines, and file lists per scope.
**Prompt template:**
```
Analyze the organization of this codebase. Check each scope for cohesion, coupling, and structural issues.

Project: {project_name} ({project_type}, {structure})
Scopes:
{for each scope: name, file_count, total_lines, avg_lines, max_lines, file list}

Follow your agent instructions for process and output format.
```

### Agent 3: pattern-detector
**Input:** Full file list from the JSON (paths and languages).
**Prompt template:**
```
Detect patterns, conventions, and anti-patterns across this codebase.

Project: {project_name} ({project_type})
Root: {root_path}
Files ({count} above threshold):
{for each file: path, language}

Follow your agent instructions for process and output format.
```

---

## Step 3: Synthesize Report

Once all three agents return, merge their findings into a single report file at `.sherpai/codebase-analysis-report.md`:

```markdown
# Codebase Health Report: {project_name}
> Generated: {date} | Threshold: {N} lines | Files scanned: {N}

## Health: [HEALTHY / NEEDS ATTENTION / URGENT]

## Priority Actions
1. [URGENT] ... (source: file-size-analyzer/scope-organizer/pattern-detector)
2. [HIGH] ...
3. [MEDIUM] ...

## File Size Analysis
(file-size-analyzer results — condensed)

## Organization
(scope-organizer results — condensed)

## Patterns & Conventions
(pattern-detector results — condensed)

## Good Patterns to Preserve
(from pattern-detector — what's working well)

## Metrics Snapshot
(key numbers from analyzer.py for future comparison)
```

**Priority ordering:** urgency x impact x ease-of-fix.

After writing the report, tell the user the path and show the Priority Actions section.

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Spawning agents sequentially | All 3 in ONE message — they're independent |
| Not running the script first | Script is faster than manual scanning — always run it |
| Agents missing context | Include project type, structure, and root path in every prompt |
| Report is just concatenation | Synthesize — deduplicate, cross-reference, prioritize |
| Vague priorities | Every priority action needs: file path, what to do, which agent found it |
