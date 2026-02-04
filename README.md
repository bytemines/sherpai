# SherpAI

AI-powered brainstorming skill that turns rough ideas into well-reasoned designs through systematic exploration.

## How it works

When you start building something, SherpAI doesn't let you jump into code. It steps back, asks what you're really trying to do, explores multiple approaches with systematic critique, and presents a validated design.

```mermaid
flowchart LR
    subgraph P1["1. UNDERSTAND"]
        A1[Check context] --> A2[Ask questions] --> A3[Clarify goals]
    end

    subgraph P2["2. EXPLORE"]
        B1[Generate 3-5 approaches] --> B2[Critique with 3 lenses]
    end

    subgraph P3["3. SCORE"]
        C1[Rate each approach] --> C2{Hybrid wins?}
        C2 -->|Yes| C3[Propose hybrid]
        C2 -->|No| C4[Keep best]
    end

    subgraph P4["4. PRESENT"]
        D1[Architecture diagram] --> D2[Validate sections] --> D3[Final summary]
    end

    P1 --> P2 --> P3 --> P4
```

**The Three-Lens Critique:**
- **Direct Analysis** - What are the real trade-offs?
- **Analogy Lens** - What do similar systems teach us?
- **Domain Knowledge** - What do experts know about this space?

## Installation

### Claude Code

```bash
# Clone to plugins directory
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
