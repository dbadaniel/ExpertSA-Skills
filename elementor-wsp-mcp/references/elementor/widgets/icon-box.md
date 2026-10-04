# Widget `icon-box`

Gerado do código-fonte do Elementor 4.4.0 (`icon-box.php`). O site pode ter outra versão: em caso de dúvida, confirme com `wsp_elementor_get_widget_schema`.


## Conteúdo › Icon Box

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `selected_icon` | icons |  |  | {"value": "fas fa-star", "library": "fa-solid"} |  |
| `view` | select |  | `default`, `stacked`, `framed` | "default" | {"selected_icon[value]!": ""} |
| `shape` | select |  | `square`, `rounded`, `circle` | "circle" | {"view!": "default", "selected_icon[value]!": ""} |
| `title_text` | text |  |  | "This is the heading" |  |
| `description_text` | textarea |  |  | "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut… |  |
| `link` | url |  |  |  |  |
| `title_size` | select |  | `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `div`, `span`, `p` | "h3" |  |

## Estilo › Box

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `position` | choose | sim | `inline-start`, `inline-end`, `block-start`, `block-end` | "block-start" | {"selected_icon[value]!": ""} |
| `content_vertical_alignment` | choose | sim | `top`, `middle`, `bottom` | "top" | {"selected_icon[value]!": "", "position": ["left", "right", "inline-st… |
| `text_align` | choose | sim | `start`, `center`, `end`, `justify` |  |  |
| `icon_space` | slider | sim | units: px,%,em,rem,vw,custom | {"size": 15} | {"selected_icon[value]!": ""} |
| `title_bottom_space` | slider | sim | units: px,em,rem,custom |  |  |

## Estilo › Icon

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `primary_color` (Normal) | color |  | global padrão `globals/colors?id=primary` |  |  |
| `secondary_color` (Normal) | color |  |  |  | {"view!": "default"} |
| `hover_primary_color` (Hover) | color |  |  |  |  |
| `hover_secondary_color` (Hover) | color |  |  |  | {"view!": "default"} |
| `hover_icon_colors_transition_duration` (Hover) | slider |  | units: s,ms,custom | {"unit": "s"} |  |
| `hover_animation` (Hover) | hover_animation |  |  |  |  |
| `icon_size` | slider | sim | units: px,%,em,rem,vw,custom |  |  |
| `icon_padding` | slider | sim | units: px,%,em,rem,vw,custom |  | {"view!": "default"} |
| `rotate` | slider | sim | units: deg,grad,rad,turn,custom | {"unit": "deg"} |  |
| `border_width` | dimensions | sim | units: px,%,em,rem,vw,custom |  | {"view": "framed"} |
| `border_radius` | dimensions | sim | units: px,%,em,rem,custom |  | {"view!": "default"} |

## Estilo › Content

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `title_typography_*` | **grupo typography** (ver groups.md) | | liga com `title_typography_typography: "custom"`. Chaves: `title_typography_font_family`, `title_typography_font_size`, `title_typography_font_weight`, `title_typography_text_transform`, `title_typography_font_style`, `title_typography_text_decoration`, `title_typography_line_height`, `title_typography_letter_spacing`, `title_typography_word_spacing` | |  |
| `text_stroke_*` | **grupo text-stroke** (ver groups.md) | | liga com `text_stroke_text_stroke_type: "yes"`. Chaves: `text_stroke_text_stroke`, `text_stroke_stroke_color` | |  |
| `title_shadow_*` | **grupo text-shadow** (ver groups.md) | | liga com `title_shadow_text_shadow_type: "yes"`. Chaves: `title_shadow_text_shadow` | |  |
| `title_color` (Normal) | color |  | global padrão `globals/colors?id=primary` |  |  |
| `hover_title_color` (Hover) | color |  | global padrão `globals/colors?id=primary` |  |  |
| `hover_title_color_transition_duration` (Hover) | slider |  | units: s,ms,custom | {"unit": "s"} |  |
| `description_typography_*` | **grupo typography** (ver groups.md) | | liga com `description_typography_typography: "custom"`. Chaves: `description_typography_font_family`, `description_typography_font_size`, `description_typography_font_weight`, `description_typography_text_transform`, `description_typography_font_style`, `description_typography_text_decoration`, `description_typography_line_height`, `description_typography_letter_spacing`, `description_typography_word_spacing` | |  |
| `description_shadow_*` | **grupo text-shadow** (ver groups.md) | | liga com `description_shadow_text_shadow_type: "yes"`. Chaves: `description_shadow_text_shadow` | |  |
| `description_color` | color |  | global padrão `globals/colors?id=text` |  |  |
