# SherpAI

AI-powered brainstorming skill that turns rough ideas into well-reasoned designs through systematic exploration.

## How it works

When you start building something, SherpAI doesn't let you jump into code. It steps back, asks what you're really trying to do, explores multiple approaches with systematic critique, and presents a validated design.

```mermaid
flowchart LR
    subgraph P1["1. UNDERSTAND"]
        A1[Check context] --> A2[Ask questions] --> A3[Confirm goals]
    end

    subgraph P2["2. EXPLORE & COMPARE"]
        B1[Show 3-4 approaches<br/>with diagrams] --> B2[Score table]
        B2 --> B3{Hybrid?}
        B3 -->|beats top| B4[Add hybrid]
        B3 -->|no| B5[Skip]
        B4 --> B6[Recommend]
        B5 --> B6
        B6 --> B7{Approved?}
        B7 -->|no| B1
        B7 -->|yes| B8[Clarify chosen]
    end

    subgraph P3["3. DESIGN"]
        C1[Architecture] --> C2[Validate sections] --> C3[Summary card]
    end

    P1 --> P2 --> P3
```

**The Three-Lens Critique:**
- **Direct Analysis** - What are the real trade-offs?
- **Analogy Lens** - What do similar systems teach us?
- **Domain Knowledge** - What do experts know about this space?

## Installation

### Claude Code (Recommended)

```bash
# Add marketplace and install
/plugin marketplace add bytemines/sherpai
/plugin install sherpai@sherpai-marketplace
```

### Claude Code (Alternative)

```bash
# Direct clone to plugins directory
git clone https://github.com/bytemines/sherpai.git ~/.claude/plugins/sherpai
```

### Codex

```
Fetch and follow instructions from https://raw.githubusercontent.com/bytemines/sherpai/main/.codex/INSTALL.md
```

### OpenCode

```
Fetch and follow instructions from https://raw.githubusercontent.com/bytemines/sherpai/main/.opencode/INSTALL.md
```

## Usage

The skill triggers automatically when you:
- Say "brainstorming" or "let's brainstorm"
- Start creative work (features, components, architecture)
- Ask to design or plan something

Or invoke directly: `/sherpai:brainstorming-mastermind`

## License

MIT
