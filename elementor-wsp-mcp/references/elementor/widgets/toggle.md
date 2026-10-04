# Widget `toggle`

Gerado do código-fonte do Elementor 4.4.0 (`toggle.php`). O site pode ter outra versão: em caso de dúvida, confirme com `wsp_elementor_get_widget_schema`.


## Conteúdo › Toggle

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `tabs` | repeater |  |  | [{"tab_title": "Toggle #1", "tab_content": "Lorem ipsum dolo… |  |

**Itens do repeater `tabs`** (cada item precisa de `_id` único de 7 hex):

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `tab_title` | text |  |  | "Toggle Title" |  |
| `tab_content` | wysiwyg |  |  | "Toggle Content" |  |

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `selected_icon` | icons |  |  | {"value": "fas fa-caret-right", "library": "fa-solid"} |  |
| `selected_active_icon` | icons |  |  | {"value": "fas fa-caret-up", "library": "fa-solid"} | {"selected_icon[value]!": ""} |
| `title_html_tag` | select |  | `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `div` | "div" |  |
| `faq_schema` | switcher |  |  |  |  |

## Estilo › Toggle

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `border_width` | slider |  | units: px,%,em,rem,vw,custom |  |  |
| `border_color` | color |  |  |  |  |
| `space_between` | slider | sim | units: px,em,rem,custom |  |  |
| `box_shadow_*` | **grupo box-shadow** (ver groups.md) | | liga com `box_shadow_box_shadow_type: "yes"`. Chaves: `box_shadow_box_shadow`, `box_shadow_box_shadow_position` | |  |

## Estilo › Title

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `title_background` | color |  |  |  |  |
| `title_color` | color |  | global padrão `globals/colors?id=primary` |  |  |
| `tab_active_color` | color |  | global padrão `globals/colors?id=accent` |  |  |
| `title_typography_*` | **grupo typography** (ver groups.md) | | liga com `title_typography_typography: "custom"`. Chaves: `title_typography_font_family`, `title_typography_font_size`, `title_typography_font_weight`, `title_typography_text_transform`, `title_typography_font_style`, `title_typography_text_decoration`, `title_typography_line_height`, `title_typography_letter_spacing`, `title_typography_word_spacing` | |  |
| `title_shadow_*` | **grupo text-shadow** (ver groups.md) | | liga com `title_shadow_text_shadow_type: "yes"`. Chaves: `title_shadow_text_shadow` | |  |
| `title_padding` | dimensions | sim | units: px,%,em,rem,vw,custom |  |  |

## Estilo › Icon

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `icon_align` | choose |  | `left`, `right` | "left" |  |
| `icon_color` | color |  |  |  |  |
| `icon_active_color` | color |  |  |  |  |
| `icon_space` | slider | sim | units: px,em,rem,custom |  |  |

## Estilo › Content

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `content_background_color` | color |  |  |  |  |
| `content_color` | color |  | global padrão `globals/colors?id=text` |  |  |
| `content_typography_*` | **grupo typography** (ver groups.md) | | liga com `content_typography_typography: "custom"`. Chaves: `content_typography_font_family`, `content_typography_font_size`, `content_typography_font_weight`, `content_typography_text_transform`, `content_typography_font_style`, `content_typography_text_decoration`, `content_typography_line_height`, `content_typography_letter_spacing`, `content_typography_word_spacing` | |  |
| `content_shadow_*` | **grupo text-shadow** (ver groups.md) | | liga com `content_shadow_text_shadow_type: "yes"`. Chaves: `content_shadow_text_shadow` | |  |
| `content_padding` | dimensions | sim | units: px,%,em,rem,vw,custom |  |  |
