# Widget `tabs`

Gerado do código-fonte do Elementor 4.4.0 (`tabs.php`). O site pode ter outra versão: em caso de dúvida, confirme com `wsp_elementor_get_widget_schema`.


## Conteúdo › Tabs

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `tabs` | repeater |  |  | [{"tab_title": "Tab #1", "tab_content": "Lorem ipsum dolor s… |  |

**Itens do repeater `tabs`** (cada item precisa de `_id` único de 7 hex):

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `tab_title` | text |  |  | "Tab Title" |  |
| `tab_content` | wysiwyg |  |  | "Tab Content" |  |

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `type` | choose |  | `vertical`, `horizontal` | "horizontal" |  |
| `tabs_align_horizontal` | choose |  | ``, `center`, `end`, `stretch` |  | {"type": "horizontal"} |
| `tabs_align_vertical` | choose |  | ``, `center`, `end`, `stretch` |  | {"type": "vertical"} |

## Estilo › Tabs

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `navigation_width` | slider |  | units: px,%,em,rem,custom | {"unit": "%"} | {"type": "vertical"} |
| `border_width` | slider |  | units: px,%,em,rem,vw,custom | {"size": 1} |  |
| `border_color` | color |  |  |  |  |
| `background_color` | color |  |  |  |  |
| `tab_color` | color |  | global padrão `globals/colors?id=primary` |  |  |
| `tab_active_color` | color |  | global padrão `globals/colors?id=accent` |  |  |
| `tab_typography_*` | **grupo typography** (ver groups.md) | | liga com `tab_typography_typography: "custom"`. Chaves: `tab_typography_font_family`, `tab_typography_font_size`, `tab_typography_font_weight`, `tab_typography_text_transform`, `tab_typography_font_style`, `tab_typography_text_decoration`, `tab_typography_line_height`, `tab_typography_letter_spacing`, `tab_typography_word_spacing` | |  |
| `text_stroke_*` | **grupo text-stroke** (ver groups.md) | | liga com `text_stroke_text_stroke_type: "yes"`. Chaves: `text_stroke_text_stroke`, `text_stroke_stroke_color` | |  |
| `title_shadow_*` | **grupo text-shadow** (ver groups.md) | | liga com `title_shadow_text_shadow_type: "yes"`. Chaves: `title_shadow_text_shadow` | |  |
| `title_align` | choose |  | `start`, `center`, `end` |  | {"tabs_align": "stretch"} |
| `content_color` | color |  | global padrão `globals/colors?id=text` |  |  |
| `content_typography_*` | **grupo typography** (ver groups.md) | | liga com `content_typography_typography: "custom"`. Chaves: `content_typography_font_family`, `content_typography_font_size`, `content_typography_font_weight`, `content_typography_text_transform`, `content_typography_font_style`, `content_typography_text_decoration`, `content_typography_line_height`, `content_typography_letter_spacing`, `content_typography_word_spacing` | |  |
| `content_shadow_*` | **grupo text-shadow** (ver groups.md) | | liga com `content_shadow_text_shadow_type: "yes"`. Chaves: `content_shadow_text_shadow` | |  |
