<p align="center">
  <img src="../assets/Exsa-azul.png" alt="ExpertSA" width="420">
</p>

# Skill: Elementor via WSP MCP (Google Antigravity)

Ensina o agente do Antigravity a criar e editar páginas Elementor no seu WordPress usando o plugin gratuito **WSP MCP** (github.com/bilalnaseer/wsp-wordpress-mcp).

## 1. No WordPress

1. Instale e ative o plugin **WSP MCP – AI Agents Connector** (WordPress 6.9+, PHP 7.4+). Elementor precisa estar ativo.
2. Vá em **MCP → Settings** e ligue:
   - Grupo **Pages**: Create Page, Get Pages (e Update Page, se quiser que o agente publique).
   - Grupo **Media**: Upload Media From URL, Upload Media, List Media.
   - Grupo **Menus**: todas (para o agente corrigir itens e locais de menu; plugin 2.9.0 ou mais novo).
   - Grupo **Elementor**: todas (ou pelo menos List Pages, Get Page, Get Element, Find Element, Add Container, Add Widget, Update Element, Remove Element, Get Widget Schema, Get Active Kit, Get Breakpoints, Update Page Settings, Duplicate, Move, Regenerate CSS).
3. Vá em **MCP → Connection**, aba **Antigravity**, e copie o snippet (já vem com URL e chave).

> Dica de segurança: comece num site de **staging**. As escritas não criam revisão, então não há "desfazer". Todo o histórico fica em **MCP → Audit Log**.

## 2. No Antigravity — conectar o MCP

Abra o menu `…` do painel do agente → **MCP Servers** → **Manage MCP Servers** → **View raw config** e cole dentro de `mcpServers`:

```json
{
  "mcpServers": {
    "wordpress": {
      "serverUrl": "https://SEU-SITE.com/wp-json/wsp-mcp/v1/mcp",
      "headers": { "Authorization": "Bearer SUA_CHAVE" }
    }
  }
}
```
(o campo é `serverUrl`, não `url`). Salve e atualize a lista de servidores; as ferramentas `wsp_*` devem aparecer.

## 3. No Antigravity — instalar a skill

Esta skill fica na pasta `elementor-wsp-mcp/` do repositório [ExpertSA-Skills](https://github.com/dbadaniel/ExpertSA-Skills). Clone o repositório e copie a pasta para a pasta de skills do Antigravity.

**Mac / Linux (global, todos os projetos):**
```bash
git clone https://github.com/dbadaniel/ExpertSA-Skills.git ~/ExpertSA-Skills
mkdir -p ~/.gemini/antigravity/skills
cp -r ~/ExpertSA-Skills/elementor-wsp-mcp ~/.gemini/antigravity/skills/
```

**Windows (PowerShell):**
```powershell
git clone https://github.com/dbadaniel/ExpertSA-Skills.git "$env:USERPROFILE\ExpertSA-Skills"
New-Item -ItemType Directory -Force "$env:USERPROFILE\.gemini\antigravity\skills"
Copy-Item -Recurse "$env:USERPROFILE\ExpertSA-Skills\elementor-wsp-mcp" "$env:USERPROFILE\.gemini\antigravity\skills\"
```

**Só para um projeto:** copie a pasta para `<seu-projeto>/.agents/skills/`.

O resultado precisa ser `.../skills/elementor-wsp-mcp/SKILL.md` (sem pasta duplicada). Reinicie o Antigravity depois.

**Atualizar:** `git -C ~/ExpertSA-Skills pull` e copie a pasta de novo. (No Mac/Linux, em vez de copiar você pode criar um link uma vez: `ln -s ~/ExpertSA-Skills/elementor-wsp-mcp ~/.gemini/antigravity/skills/elementor-wsp-mcp`; aí basta o `git pull`.)

Sem git? Baixe o ZIP pelo botão **Code → Download ZIP** do repositório, descompacte e copie só a pasta `elementor-wsp-mcp`.

## 4. Usar

Exemplos de pedido:
- "Crie uma landing page em rascunho no Elementor para uma clínica de fisioterapia: hero, 3 benefícios, depoimentos, FAQ e CTA para WhatsApp."
- "Na página Home, troque o título do hero e deixe os botões verdes."
- "Mostre a estrutura da página Sobre e diga o que está quebrado no mobile."

O agente vai: checar as ferramentas, ler o kit de cores/fontes, propor a estrutura, criar em rascunho, montar seção por seção, conferir e te entregar o link do preview e do editor.

## Conhecimento do Elementor
A pasta `references/elementor/` contém a referência de todos os widgets gratuitos, do container e dos grupos de estilo, **extraída do código-fonte oficial do Elementor 4.4.0**. Quando atualizar o Elementor, regenere com `scripts/extract-elementor/run.sh` (instruções no README de lá).

## Limites (vêm do plugin, não da skill)
- Não insere widget HTML/shortcode/código nem CSS customizado (bloqueio de segurança do plugin).
- Não insere templates salvos da biblioteca numa página.
- Não converte página Gutenberg existente em Elementor.

## Créditos e licença
- MCP: [WSP WordPress MCP](https://github.com/bilalnaseer/wsp-wordpress-mcp) (WebSensePro, GPL-2.0).
- Referência de controles gerada a partir do [Elementor](https://github.com/elementor/elementor) (GPL-3.0).
- Esta skill é distribuída sob a GPL-3.0 (veja `LICENSE`). Projeto independente, sem vínculo com Elementor, WebSensePro ou Google.

---

## ☕ Apoie o projeto

Este projeto é mantido ativamente para resolver gargalos operacionais reais. Se ele te poupou horas de desenvolvimento ou simplificou suas automações, considere apoiar:

**Chave Pix:** `expertsa.oficial@gmail.com`
