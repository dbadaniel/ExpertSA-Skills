# ExpertSA Skills

Coleção de skills para agentes de IA no formato aberto `SKILL.md`, compatível com Google Antigravity, Claude Code e outros agentes que seguem o padrão Agent Skills.

## Skills

| Skill | Para que serve |
|---|---|
| [`elementor-wsp-mcp`](elementor-wsp-mcp/) | Cria e edita páginas Elementor no WordPress pelo [WSP WordPress MCP](https://github.com/bilalnaseer/wsp-wordpress-mcp), com referência de widgets extraída do código-fonte do Elementor. |

## Como instalar uma skill no Antigravity

Cada pasta deste repositório é uma skill independente. Copie a pasta da skill desejada para:

- **Global (todos os projetos):** `~/.gemini/antigravity/skills/<nome-da-skill>/`
- **Só um projeto:** `<seu-projeto>/.agents/skills/<nome-da-skill>/`

Exemplo (Mac/Linux):
```bash
git clone https://github.com/dbadaniel/ExpertSA-Skills.git ~/ExpertSA-Skills
mkdir -p ~/.gemini/antigravity/skills
cp -r ~/ExpertSA-Skills/elementor-wsp-mcp ~/.gemini/antigravity/skills/
```

Instruções completas (incluindo Windows e configuração de MCP) ficam no README de cada skill.

## Licença
Cada skill tem sua própria licença dentro da pasta (ex.: `elementor-wsp-mcp/LICENSE`, GPL-3.0).
