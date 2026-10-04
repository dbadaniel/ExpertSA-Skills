---
name: elementor-wsp-mcp
description: Builds and edits Elementor pages, header/footer templates and WordPress navigation menus on a WordPress site through the WSP WordPress MCP server (tools named wsp_elementor_*, wsp_*menu*, wsp_create_page). Use when the user asks to create, design, edit, fix, restyle or inspect an Elementor page, section, landing page, hero, header, footer, menu, container or widget on WordPress, or mentions "Elementor", "WSP MCP", "menu", "cabeçalho" or "página no WordPress". Do not use for theme/plugin PHP development, Gutenberg-only pages, or WooCommerce product data.
---

# Elementor via WSP WordPress MCP

Esta skill ensina o agente a construir e editar páginas Elementor **remotamente**, pelo servidor MCP do plugin *WSP MCP – AI Agents Connector* (`/wp-json/wsp-mcp/v1/mcp`). Não há acesso a arquivos do WordPress: tudo acontece através das ferramentas `wsp_*`.

Leia os arquivos de referência quando precisar dos detalhes:
- `references/tools.md` — todas as ferramentas do MCP, parâmetros e retornos reais.
- `references/elementor/` — **conhecimento do Elementor extraído do código-fonte oficial (4.4.0)**: um arquivo por widget (`widgets/<tipo>.md`) com cada chave, tipo, opções válidas, padrão e condição; `container.md`; `advanced-common.md` (aba Avançado); `groups.md` (typography, background, border…); `README.md` (modelo de dados, formatos de valor, responsivo, globais).
- `references/settings-cheatsheet.md` — resumo rápido dos settings mais usados.
- `references/recipes.md` — receitas prontas de seções (hero, features, CTA, depoimentos, FAQ, rodapé).
- `references/menus.md` — menus do WordPress, widget de menu do Elementor e cabeçalho: onde está cada coisa e como corrigir.

**Regra de ouro:** antes de enviar settings de um widget, abra `references/elementor/widgets/<tipo>.md` e use só chaves e valores que aparecem lá. Não invente nomes de chave nem valores de `select`/`choose`. Se o widget não estiver na pasta (Pro ou de terceiros), use `wsp_elementor_get_widget_schema`.

## Use esta skill quando
- Pedirem para criar uma página/landing page no Elementor.
- Pedirem para editar texto, cor, espaçamento, imagem ou layout de uma página Elementor existente.
- Pedirem para corrigir ou mudar um menu, cabeçalho ou rodapé.
- Pedirem para inspecionar a estrutura de uma página, o kit global (cores/fontes) ou os breakpoints.

## Não use quando
- A tarefa for escrever PHP de tema/plugin, editar arquivos do servidor ou mexer em banco.
- A página não for do Elementor (Gutenberg puro) — use `wsp_update_page` com HTML de blocos.

---

## Primeiro: é um ajuste ou uma página nova?

**Ajuste/correção** (trocar texto, cor, link, item de menu, consertar algo quebrado): use o **caminho curto** abaixo. Não leia o kit, os breakpoints nem faça plano de página.
**Página nova ou redesenho de seção**: siga os Passos 0 a 5 mais abaixo.

### Caminho curto (meta: resolver em 3 a 6 chamadas)
1. **Identifique onde a coisa mora** com a tabela abaixo, *antes* de qualquer chamada. A maior causa de voltas é procurar no lugar errado (ex.: procurar o menu dentro da página).
2. Vá direto ao alvo com **uma** chamada de localização (`find_element` com `search`, `get_menu_items`, `list_templates`…).
3. Leia só o elemento-alvo (`get_element`), não a página inteira.
4. Faça **uma** escrita com todas as mudanças juntas.
5. Confirme com uma leitura do mesmo elemento e diga ao usuário o que mudou.
Se depois de 2 tentativas de localização o alvo não aparecer, **pare e pergunte** ao usuário (em qual página está, um texto que aparece perto, print). Não varra o site.

### Onde cada coisa mora

| O usuário fala de… | Onde está de verdade | Ferramentas |
|---|---|---|
| Itens do menu (nome, link, ordem, adicionar/remover, submenu) | **Menu do WordPress** (Aparência → Menus), não no Elementor | `wsp_get_menus` (já mostra em qual local cada menu está) → `wsp_get_menu_items` → `wsp_update_menu_item` / `wsp_add_menu_item` / `wsp_delete_menu_item` |
| Menu errado aparecendo, menu sumiu | Qual menu está ligado ao local, ou qual menu o widget usa | `wsp_get_menu_locations`, `wsp_assign_menu_location`; ou setting `menu` do widget `nav-menu` |
| Aparência do menu (cor, fonte, hover, alinhamento, hambúrguer no mobile) | Widget de menu dentro do **template de cabeçalho** do Elementor | `wsp_elementor_list_templates {type:"header"}` → `find_element {widget_type:"nav-menu"}` no ID do template → `get_element` → `update_element` |
| Logo, botão ou fundo do cabeçalho/rodapé | **Template** `header`/`footer` (Theme Builder), não a página | `wsp_elementor_list_templates` → ferramentas `wsp_elementor_*` com o ID do template como `post_id` |
| Conteúdo de uma página | A própria página | `wsp_elementor_list_pages {status:"any"}` → `find_element {search:"trecho do texto"}` |
| Algo igual em todas as páginas | Template (header/footer/section global) ou kit | `list_templates`; cores/fontes globais: `get_active_kit` |

Templates do Elementor são posts como qualquer página: **todas as ferramentas `wsp_elementor_*` funcionam neles** passando o ID do template como `post_id`.
Sem template de cabeçalho (sem Elementor Pro, cabeçalho vem do tema): só os **itens** do menu são editáveis pelo MCP; o visual fica no Personalizar do tema. Diga isso ao usuário em vez de procurar mais. Detalhes: `references/menus.md`.

### Regras de eficiência (sempre)
- **Não releia o que já leu.** Guarde IDs e settings na conversa.
- `wsp_elementor_get_page` só quando precisar da árvore; para achar um elemento use `find_element` com `search` (trecho de texto, URL, hex) ou `widget_type`.
- Não chame `wsp_elementor_get_widget_schema` para widgets que têm arquivo em `references/elementor/widgets/`. Para widgets Pro (ex.: `nav-menu`), chame **uma vez** e guarde.
- Agrupe as mudanças do mesmo elemento numa única `update_element`.
- Não chame `regenerate_css` em ajustes de texto/link; só depois de mudanças de estilo, e uma vez no final.
- Explique ao usuário em uma linha o que vai fazer antes de começar, e em uma linha o resultado no final.

## Passo 0 — Verificar as ferramentas (sempre)

Confira quais ferramentas `wsp_*` estão disponíveis na sessão. O plugin só expõe as que o admin ligou em **WP Admin → MCP → Settings** (todas as de Elementor vêm DESLIGADAS por padrão).

Mínimo para construir páginas:
`wsp_create_page`, `wsp_elementor_list_pages`, `wsp_elementor_get_page`, `wsp_elementor_get_element`, `wsp_elementor_add_container`, `wsp_elementor_add_widget`, `wsp_elementor_update_element`, `wsp_elementor_remove_element`, `wsp_elementor_get_widget_schema`, `wsp_elementor_update_page_settings`.

Recomendadas: `wsp_elementor_get_active_kit`, `wsp_elementor_get_breakpoints`, `wsp_elementor_find_element`, `wsp_elementor_list_templates`, `wsp_elementor_duplicate_element`, `wsp_elementor_move_element`, `wsp_elementor_copy_styles`, `wsp_elementor_regenerate_css`, `wsp_upload_media_from_url`, `wsp_list_media`, `wsp_get_site_info`.

Para menus: `wsp_get_menus`, `wsp_get_menu_items`, `wsp_get_menu_locations`, `wsp_add_menu_item`, `wsp_update_menu_item`, `wsp_delete_menu_item`, `wsp_assign_menu_location` (grupo "Menus" no MCP → Settings; requer plugin ≥ 2.9.0).

Se faltar alguma necessária, **pare** e diga ao usuário exatamente quais interruptores ligar em MCP → Settings (grupos "Elementor", "Pages", "Media" ou "Menus"). Não tente contornar.

## Passo 1 — Descobrir o contexto do site (só para página nova)

1. `wsp_elementor_get_active_kit` → anote as cores globais (ids `primary`, `secondary`, `text`, `accent` e as custom) e fontes. **Use as cores/fontes do kit** em vez de inventar hex, a menos que o usuário peça outra paleta.
2. `wsp_elementor_get_breakpoints` → saiba quais sufixos responsivos existem (`_tablet`, `_mobile`, às vezes `_laptop`, `_widescreen`…).
3. Para editar algo existente: `wsp_elementor_list_pages` → `wsp_elementor_get_page`.

## Passo 2 — Planejar antes de escrever

Antes de qualquer chamada de escrita, escreva um plano curto da página: lista de seções, e para cada seção a árvore `container → containers internos → widgets` com o conteúdo de texto. Para páginas inteiras, mostre o plano ao usuário e espere o OK. Para ajustes pequenos, siga direto.

## Passo 3 — Criar a página (página nova)

```json
wsp_create_page { "title": "Minha Landing", "content": "", "status": "draft", "elementor": true }
```
- **Sempre `status: "draft"`** a menos que o usuário peça para publicar.
- `elementor: true` é obrigatório; sem isso as ferramentas `wsp_elementor_*` recusam a página ("This post was not built with Elementor").
- Guarde o `id` retornado (é o `post_id` de tudo daqui pra frente).

Depois defina o template:
```json
wsp_elementor_update_page_settings { "post_id": 123, "page_template": "elementor_header_footer", "hide_title": true }
```
`elementor_canvas` = sem header/rodapé do tema (landing pages). `elementor_header_footer` = largura total com header/rodapé. `default` = template do tema.

## Passo 4 — Construir de cima para baixo

Regras de construção:
1. **Use Containers (flexbox)**, não Sections/Columns, a menos que a página já use o layout legado.
2. Crie o container raiz da seção: `wsp_elementor_add_container { post_id, settings }` (sem `parent_id` = vai para o fim da página; `position` para inserir num índice).
3. Containers internos: `wsp_elementor_add_container { post_id, parent_id: "<id do pai>", settings }`.
4. Widgets: `wsp_elementor_add_widget { post_id, widget_type, container_id, settings }`.
5. **Sempre passe `container_id` / `parent_id` explícito.** Sem ele, o widget cai no *primeiro* container da página — quase nunca é o que você quer.
6. **Mande os settings completos já na criação** (texto + estilo) para economizar chamadas.
7. Guarde cada `element_id` retornado num mapa mental `nome-lógico → id` (ex.: `hero.root = a1b2c3d4`).
8. Chaves e valores: consulte `references/elementor/widgets/<tipo>.md` (ou `container.md`). Se o site rodar uma versão muito diferente do Elementor, ou o widget não estiver lá, chame `wsp_elementor_get_widget_schema { widget_type }`. O schema do próprio site vence qualquer referência.
9. **Container-filho como coluna**: sempre `content_width: "full"` + `width`. Com `boxed` (o padrão), `width` é ignorado.
10. **Use só widgets clássicos.** Os elementos "Atomic" do Elementor 4 (`e-heading`, `e-button`, `div-block`, `flexbox`…) usam outro formato de dados e o WSP MCP não os suporta.
11. Imagens: suba com `wsp_upload_media_from_url` (ou `wsp_upload_media` com base64) e use `{ "url": "...", "id": <attachment_id> }` no setting `image`.

## Passo 5 — Verificar

1. Após cada seção, `wsp_elementor_get_page { post_id }` e confira que a árvore bate com o plano (tipos, ordem, aninhamento, previews de texto).
2. No fim, `wsp_elementor_regenerate_css` (se disponível).
3. Entregue ao usuário: link de preview (`url` do create_page) e link do editor: `<site>/wp-admin/post.php?post=<ID>&action=elementor`. Recomende abrir no editor e clicar **Atualizar** uma vez — isso faz o Elementor normalizar o JSON e regenerar o CSS da página.

## Editar uma página existente

1. Localize: `wsp_elementor_find_element { post_id, widget_type?, search? }` ou leia a árvore com `wsp_elementor_get_page`.
2. Leia os settings atuais: `wsp_elementor_get_element { post_id, element_id }`. **Guarde esse JSON na conversa** — é o único "backup" que você terá.
3. Atualize só o que mudou: `wsp_elementor_update_element { post_id, element_id, settings: {...} }`.
   - O merge é **raso** (`array_merge`): chaves de topo não enviadas são preservadas, mas um objeto aninhado enviado (ex.: `padding`, `typography_font_size`, `link`, repeaters como `icon_list`) **substitui o objeto inteiro**. Envie o objeto completo.
4. Reorganizar: `wsp_elementor_move_element`, `wsp_elementor_duplicate_element` (gera IDs novos), `wsp_elementor_copy_styles` (`merge: true` para não apagar o resto).

## Segurança e limites (leia)

- **Não existe desfazer confiável.** As escritas gravam direto no `_elementor_data`, sem criar revisão. Em página publicada: antes de `remove`, `move` ou mudanças grandes, confirme com o usuário e guarde o `get_element` de tudo que vai mudar. Para redesenhos grandes, prefira construir numa página nova em rascunho.
- **Nunca publique** (`wsp_update_page status: "publish"`) sem pedido explícito.
- **Bloqueado pelo plugin** (vai falhar ou ser descartado silenciosamente):
  - widgets `html`, `shortcode`, `code`, `code-highlight`;
  - chaves `custom_css`, `_attributes`, `custom_attributes`, `__dynamic__`;
  - `<script>`, `<style>` e atributos `on*` em qualquer texto (passa por `wp_kses_post`).
  Não tente contornar. Se o design exigir CSS customizado, faça com os controles nativos; se for impossível, diga ao usuário o CSS exato para ele colar em *Elementor → Site Settings → Custom CSS*.
- `wsp_uae_builder_build` (só existe se o Ultimate Addons estiver ativo) **sobrescreve a página inteira** com o JSON enviado. Use só em página nova/vazia e com confirmação.
- `wsp_elementor_update_active_kit` altera o site todo — só com pedido explícito.

## Armadilhas conhecidas

- Containers usam `padding` / `margin`; widgets usam `_padding` / `_margin` (aba Avançado). `wsp_elementor_convert_css` sempre gera `_padding`/`_margin` e mapeia `color` para `title_color` (só serve para heading). Para containers, **renomeie as chaves** ou escreva os settings à mão.
- Valores dimensionais são objetos: `{ "unit": "px", "size": 48 }`; caixas são `{ "top": "20", "right": "20", "bottom": "20", "left": "20", "unit": "px", "isLinked": true }` (números como string); `flex_gap` é `{ "column": "20", "row": "20", "isLinked": true, "unit": "px" }`.
- Alinhamento **não é padronizado** no Elementor 4: `heading`/`text-editor`/`image` usam `start`/`center`/`end`; `button`/`social-icons`/`divider` usam `left`/`center`/`right`; `icon-box.position` usa `block-start`/`inline-start`. Copie do arquivo do widget.
- Ao usar estilo customizado de tipografia, inclua `"typography_typography": "custom"`, senão o Elementor ignora `typography_font_size` etc.
- Fundo exige o "switch": `"background_background": "classic"` junto de `background_color`.
- `wsp_elementor_copy_styles` copia **todos** os settings, inclusive o texto. Depois de copiar, reaplique o conteúdo do destino (`title`, `editor`, `text`…) com `update_element`.
- `wsp_elementor_list_pages` só lista publicadas por padrão; para ver rascunhos passe `status: "any"`.
- Widget dentro de `section` legada falha: mire na `column` dentro dela.
- Containers internos são criados com `isInner: false` pela ferramenta. Funciona no front; se o editor exibir algo estranho, abrir e salvar a página no editor normaliza.
- Itens de repeater (`icon_list`, `tabs`, `social_icon_list`, `carousel`…) precisam de `_id` único de 7 caracteres hex em cada item.
- Erro `Session not found or expired`: reinicialize a conexão MCP (atualize o plugin para ≥ 2.6.8).
- Toda escrita fica registrada em **MCP → Audit Log** no wp-admin — útil para o usuário revisar o que foi feito.
