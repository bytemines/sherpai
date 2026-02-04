# Installing SherpAI for OpenCode

## Installation

1. **Clone repository**:
   ```bash
   mkdir -p ~/.config/opencode/sherpai
   git clone https://github.com/bytemines/sherpai.git ~/.config/opencode/sherpai
   ```

2. **Create skills symlink**:
   ```bash
   mkdir -p ~/.config/opencode/skills
   ln -sf ~/.config/opencode/sherpai/skills/brainstorming-mastermind \
     ~/.config/opencode/skills/brainstorming-mastermind
   ```

3. **Restart OpenCode**

## Usage

The skill activates when you:
- Say "brainstorming" or "let's brainstorm"
- Start creative work (features, components, design)

Or explicitly: `use use_skill tool with skill_name: "brainstorming-mastermind"`

## Updating

```bash
cd ~/.config/opencode/sherpai && git pull
```
