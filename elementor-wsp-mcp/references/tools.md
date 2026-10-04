# Referência das ferramentas (WSP MCP v2.9.x)

Nomes MCP usam underscore (`wsp_elementor_get_page`). No wp-admin, cada uma tem um interruptor em **MCP → Settings** com o nome em barra (`wsp/elementor-get-page`). As de Elementor só existem se o plugin Elementor estiver ativo. `*` = obrigatório.

## Páginas e mídia

| Ferramenta | Parâmetros | Retorno / observações |
|---|---|---|
| `wsp_create_page` | `title`*, `content`* (pode ser `""`), `status`, `parent`, `slug`, `elementor` (bool) | `{ id, url, elementor }`. Com `elementor: true` grava `_elementor_edit_mode=builder` e uma árvore vazia. Requer `publish_pages`. |
| `wsp_get_pages` | filtros de listagem | Lista páginas (Elementor ou não). |
| `wsp_update_page` | `id`*, `title`, `content`, `status`… | Use para publicar (`status: "publish"`) — só com pedido explícito. |
| `wsp_upload_media_from_url` | `url`* , título/alt opcionais | Retorna o attachment `id` e `url`. Use em `image: {url, id}`. |
| `wsp_upload_media` | `data` (base64) **ou** `url`, `mime_type` | Só jpg/png/gif/webp. |
| `wsp_list_media` / `wsp_get_media` | busca / `id` | Para reaproveitar imagens já existentes. |
| `wsp_get_site_info` | — | URL do site, versão etc. |

## Elementor — leitura

| Ferramenta | Parâmetros | Retorno / observações |
|---|---|---|
| `wsp_elementor_list_pages` | `post_type` (padrão `page`), `status` (padrão `publish`!), `per_page` (20) | `{ pages:[{id,title,url,status,type}], total }`. **Rascunhos não aparecem por padrão** — passe `status: "any"` ou `"draft"`. |
| `wsp_elementor_get_page` | `post_id`* | `{ structure: [{ id, type, widget_type?, preview?, children? }] }`. Árvore **simplificada**: sem settings. `preview` = primeiras ~8 palavras de `title`/`text`/`editor`/`url`. |
| `wsp_elementor_get_element` | `post_id`*, `element_id`* | `{ id, type, widget_type, settings }` com **todos** os settings crus. |
| `wsp_elementor_find_element` | `post_id`*, `widget_type`, `search` | `{ results:[{id,type,widget_type}] }`. `search` é busca textual no JSON dos settings (ex.: um trecho do título, um hex de cor). |
| `wsp_elementor_list_templates` | `type` (`page`, `section`, `header`, `footer`…), `per_page` | Templates da biblioteca. Não há ferramenta para inserir um template numa página. |
| `wsp_elementor_get_widget_schema` | `widget_type`* | Controles do widget agrupados (conteúdo, estilo, avançado) com chaves, tipos e defaults. **Fonte da verdade** para nomes de settings. |
| `wsp_elementor_get_active_kit` | — | `{ colors:[{title,color}], fonts:[…], layout:{container_width,…}, raw_settings }`. Os `_id` das cores globais (para `__globals__`) estão em `raw_settings.system_colors[]._id` e `raw_settings.custom_colors[]._id`. |
| `wsp_elementor_get_breakpoints` | — | Limites desktop/tablet/mobile. Sufixos: `_tablet`, `_mobile`. |
| `wsp_elementor_get_page_settings` | `post_id`* | Template, fundo, etc. da página. |

## Elementor — escrita

| Ferramenta | Parâmetros | Comportamento real |
|---|---|---|
| `wsp_elementor_add_container` | `post_id`*, `type` (`container` padrão \| `section` \| `column`), `parent_id`, `settings`, `position` | Sem `parent_id` → nível raiz (fim da página, ou índice `position`). Retorna `{ element_id }`. Cria sempre com `isInner:false`. |
| `wsp_elementor_add_widget` | `post_id`*, `widget_type`*, `container_id`, `settings`, `position` | Sem `container_id` → vai para o **primeiro** container/column da página (evite). Recusa `section` como alvo e os tipos bloqueados. Retorna `{ element_id }`. |
| `wsp_elementor_update_element` | `post_id`*, `element_id`*, `settings`* | **Merge raso**: objetos aninhados enviados substituem o objeto inteiro. |
| `wsp_elementor_remove_element` | `post_id`*, `element_id`* | Remove o elemento e todos os filhos. Irreversível. |
| `wsp_elementor_duplicate_element` | `post_id`*, `element_id`*, `parent_id`, `position` | Clona com IDs novos (recursivo). Sem `parent_id`: insere logo após o original. |
| `wsp_elementor_move_element` | `post_id`*, `element_id`*, `new_parent_id` (vazio = raiz), `position` | |
| `wsp_elementor_copy_styles` | `post_id`*, `source_id`*, `destination_id`*, `merge` | ⚠️ Copia **todos** os settings da origem, inclusive o texto (`title`, `editor`, `text`…). Depois de copiar, **reaplique o conteúdo** do destino com `update_element`. `merge:false` (padrão) apaga o que o destino tinha. |
| `wsp_elementor_convert_css` | `css`* (objeto `{ "padding": "20px 40px" }`) | Só converte, não grava. Gera chaves de **widget** (`_padding`, `_margin`, `_border_radius`) e `color → title_color`. Suporta: padding, margin, border-radius, border-width, border-style, border-color, background-color, color, font-size, font-weight, text-align, width, height, gap, opacity, display. |
| `wsp_elementor_update_page_settings` | `post_id`*, `page_template` (`elementor_canvas` \| `elementor_header_footer` \| `default`), `hide_title`, `content_width` `{unit,size}`, `background_color`, `settings` | |
| `wsp_elementor_update_active_kit` | `system_colors` `[{_id,title,color}]`, `container_width`, `space_between_widgets` | Afeta o site inteiro. Requer `manage_options`. |
| `wsp_elementor_regenerate_css` | — | Limpa o cache de CSS do Elementor. Requer `manage_options`. |

## Ultimate Addons for Elementor (só se o UAE estiver ativo)

Existem ~45 ferramentas `wsp_uae_*`. As úteis aqui:
- `wsp_uae_builder_build { post_id, json_tree }` — `json_tree` é uma **string** JSON com a árvore completa do `_elementor_data`. **Sobrescreve a página inteira.** Útil para montar uma página nova de uma vez (cada elemento precisa de `id` 8-hex, `elType`, `settings`, `elements`; widgets também `widgetType`).
- `wsp_uae_builder_list_widget_types` — lista todos os widgets registrados (inclui widgets Pro/terceiros).
- `wsp_uae_builder_undo` — tenta restaurar a última revisão, mas as escritas via MCP não criam revisões; não conte com ele.

## Erros comuns

| Mensagem | Causa / ação |
|---|---|
| `This post was not built with Elementor.` | Página criada sem `elementor:true`. Crie outra com `elementor:true` (não há ferramenta para converter). |
| `Container not found.` / `Parent element not found.` | ID errado ou elemento removido. Releia com `get_page`. |
| `Target is a section (legacy layout)…` | Mire numa `column` dentro da section. |
| `No container or column found…` | Página vazia: crie um container antes. |
| `Widget type "html" is not allowed…` | Tipo bloqueado. Use heading/text-editor/etc. |
| Ferramenta não existe | Interruptor desligado em MCP → Settings ou Elementor inativo. |
| `Session not found or expired` | Reconecte; atualize o plugin para ≥ 2.6.8. |
