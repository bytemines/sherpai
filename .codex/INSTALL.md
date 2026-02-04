# Installing SherpAI for Codex

## Installation

1. **Clone repository**:
   ```bash
   mkdir -p ~/.codex/sherpai
   git clone https://github.com/bytemines/sherpai.git ~/.codex/sherpai
   ```

2. **Update ~/.codex/AGENTS.md** to include:
   ```markdown
   ## SherpAI Brainstorming

   When starting creative work (features, components, architecture) or when the user mentions "brainstorming", load and follow:
   `~/.codex/sherpai/skills/brainstorming-mastermind/SKILL.md`
   ```

## Usage

The skill activates when you:
- Say "brainstorming" or "let's brainstorm"
- Start creative work (features, components, design)

Or explicitly: "Use the brainstorming-mastermind skill"
