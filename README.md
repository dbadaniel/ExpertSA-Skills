<p align="center">
  <img src="assets/Exsa-azul.png" alt="ExpertSA" width="420">
</p>

# ExpertSA Skills

Coleção de skills para agentes de IA no formato aberto `SKILL.md`, compatível com Google Antigravity, Claude Code e outros agentes que seguem o padrão Agent Skills.

## Skills

| Skill | Para que serve |
|---|---|
| [`elementor-wsp-mcp`](elementor-wsp-mcp/) | Cria e edita páginas Elementor no WordPress pelo [WSP WordPress MCP](https://github.com/bilalnaseer/wsp-wordpress-mcp), com referência de widgets extraída do código-fonte do Elementor. |

## Como instalar

Com um comando (precisa do Node.js 16.7+):
```bash
npx github:dbadaniel/ExpertSA-Skills elementor-wsp-mcp
```
Instala na pasta global de skills do Antigravity (`~/.gemini/config/skills/`). Sem o nome da skill, instala todas. Rodar de novo atualiza.

| Opção | Onde instala |
|---|---|
| *(nenhuma)* | `~/.gemini/config/skills/` — global, Antigravity 2.0 e IDE |
| `--project` | `./.agents/skills/` — só o projeto aberto |
| `--cli` | `~/.gemini/antigravity-cli/skills/` — Antigravity CLI |
| `--legacy` | `~/.gemini/antigravity/skills/` — versões antigas do IDE |
| `--list` | lista as skills disponíveis |

Também funciona com [`npx skills`](https://github.com/antfu/skills-cli) no modo por projeto: `npx skills add dbadaniel/ExpertSA-Skills --skill elementor-wsp-mcp -a antigravity`.

Instruções completas (incluindo configuração de MCP e instalação manual) ficam no README de cada skill.

## Licença
Cada skill tem sua própria licença dentro da pasta (ex.: `elementor-wsp-mcp/LICENSE`, GPL-3.0).

---

## ☕ Apoie o projeto

Este projeto é mantido ativamente para resolver gargalos operacionais reais. Se ele te poupou horas de desenvolvimento ou simplificou suas automações, considere apoiar:

**Chave Pix:** `expertsa.oficial@gmail.com`
