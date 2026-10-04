# Widget `text-editor`

Gerado do código-fonte do Elementor 4.4.0 (`text-editor.php`). O site pode ter outra versão: em caso de dúvida, confirme com `wsp_elementor_get_widget_schema`.


## Conteúdo › Text Editor

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `editor` | wysiwyg |  |  | "<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.… |  |
| `drop_cap` | switcher |  |  |  |  |
| `text_columns` | select | sim | ``, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10` |  |  |
| `column_gap` | slider | sim | units: px,%,em,rem,vw,custom |  |  |

## Estilo › Text Editor

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `align` | choose | sim | `start`, `center`, `end`, `justify` |  |  |
| `typography_*` | **grupo typography** (ver groups.md) | | liga com `typography_typography: "custom"`. Chaves: `typography_font_family`, `typography_font_size`, `typography_font_weight`, `typography_text_transform`, `typography_font_style`, `typography_text_decoration`, `typography_line_height`, `typography_letter_spacing`, `typography_word_spacing` | |  |
| `text_shadow_*` | **grupo text-shadow** (ver groups.md) | | liga com `text_shadow_text_shadow_type: "yes"`. Chaves: `text_shadow_text_shadow` | |  |
| `paragraph_spacing` | slider | sim | units: px,em,rem,vh,custom |  |  |
| `text_color` (Normal) | color |  | global padrão `globals/colors?id=text` |  |  |
| `link_color` (Normal) | color |  |  |  |  |
| `link_hover_color` (Hover) | color |  |  |  |  |
| `link_hover_color_transition_duration` (Hover) | slider |  | units: s,ms,custom | {"unit": "s"} |  |

## Estilo › Drop Cap

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `drop_cap_view` | select |  | `default`, `stacked`, `framed` | "default" |  |
| `drop_cap_primary_color` | color |  | global padrão `globals/colors?id=primary` |  |  |
| `drop_cap_secondary_color` | color |  |  |  | {"drop_cap_view!": "default"} |
| `drop_cap_shadow_*` | **grupo text-shadow** (ver groups.md) | | liga com `drop_cap_shadow_text_shadow_type: "yes"`. Chaves: `drop_cap_shadow_text_shadow` | |  |
| `drop_cap_size` | slider |  | units: px,em,rem,custom | {"size": 5} | {"drop_cap_view!": "default"} |
| `drop_cap_space` | slider |  | units: px,em,rem,custom | {"size": 10} |  |
| `drop_cap_border_radius` | slider |  | units: px,%,em,rem,custom | {"unit": "%"} | {"drop_cap_view!": "default"} |
| `drop_cap_border_width` | dimensions |  | units: px,%,em,rem,vw,custom |  | {"drop_cap_view": "framed"} |
| `drop_cap_typography_*` | **grupo typography** (ver groups.md) | | liga com `drop_cap_typography_typography: "custom"`. Chaves: `drop_cap_typography_font_family`, `drop_cap_typography_font_size`, `drop_cap_typography_font_weight`, `drop_cap_typography_text_transform`, `drop_cap_typography_font_style`, `drop_cap_typography_text_decoration`, `drop_cap_typography_line_height`, `drop_cap_typography_word_spacing` | |  |
