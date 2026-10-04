# Widget `divider`

Gerado do código-fonte do Elementor 4.4.0 (`divider.php`). O site pode ter outra versão: em caso de dúvida, confirme com `wsp_elementor_get_widget_schema`.


## Conteúdo › Divider

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `style` | select |  |  | "solid" |  |
| `width` | slider | sim | units: px,%,em,rem,vw,custom | {"size": 100, "unit": "%"} |  |
| `align` | choose | sim | `left`, `center`, `right` |  |  |
| `look` | choose |  | `line`, `line_text`, `line_icon` | "line" |  |
| `text` | text |  |  | "Divider" | {"look": "line_text"} |
| `html_tag` | select |  | `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `div`, `span`, `p` | "span" | {"look": "line_text"} |
| `icon` | icons |  |  | {"value": "fas fa-star", "library": "fa-solid"} | {"look": "line_icon"} |

## Estilo › Divider

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `color` | color |  | global padrão `globals/colors?id=secondary` | "#000" |  |
| `weight` | slider |  | units: px,em,rem,custom | {"size": 1} | {"style": ["solid", "double", "dotted", "dashed", "curly", "curved", "… |
| `pattern_height` | slider |  |  | {"size": 20} | {"style!": ["", "solid", "double", "dotted", "dashed"]} |
| `pattern_size` | slider |  | units: px,%,em,rem,custom | {"size": 20} | {"style!": ["multiple", "dots_tribal", "trees_2_tribal", "rounds_triba… |
| `gap` | slider | sim |  | {"size": 15} |  |

## Estilo › Text

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `text_color` | color |  | global padrão `globals/colors?id=secondary` |  |  |
| `typography_*` | **grupo typography** (ver groups.md) | | liga com `typography_typography: "custom"`. Chaves: `typography_font_family`, `typography_font_size`, `typography_font_weight`, `typography_text_transform`, `typography_font_style`, `typography_text_decoration`, `typography_line_height`, `typography_letter_spacing`, `typography_word_spacing` | |  |
| `text_stroke_*` | **grupo text-stroke** (ver groups.md) | | liga com `text_stroke_text_stroke_type: "yes"`. Chaves: `text_stroke_text_stroke`, `text_stroke_stroke_color` | |  |
| `text_align` | choose |  | `left`, `center`, `right` | "center" |  |
| `text_spacing` | slider | sim | units: px,%,em,rem,vw,custom |  |  |

## Estilo › Icon

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `icon_view` | select |  | `default`, `stacked`, `framed` | "default" |  |
| `icon_size` | slider | sim | units: px,em,rem,custom |  |  |
| `icon_padding` | slider |  | units: px,em,rem,custom |  | {"icon_view!": "default"} |
| `primary_color` | color |  | global padrão `globals/colors?id=secondary` |  |  |
| `secondary_color` | color |  |  |  | {"icon_view!": "default"} |
| `icon_align` | choose |  | `left`, `center`, `right` | "center" |  |
| `icon_spacing` | slider | sim | units: px,em,rem,custom |  |  |
| `rotate` | slider | sim | units: deg,grad,rad,turn,custom | {"unit": "deg"} |  |
| `icon_border_width` | slider |  | units: px,%,em,rem,vw,custom |  | {"icon_view": "framed"} |
| `border_radius` | slider |  | units: px,%,em,rem,custom |  | {"icon_view!": "default"} |
