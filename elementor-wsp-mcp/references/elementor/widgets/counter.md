# Widget `counter`

Gerado do código-fonte do Elementor 4.4.0 (`counter.php`). O site pode ter outra versão: em caso de dúvida, confirme com `wsp_elementor_get_widget_schema`.


## Conteúdo › Counter

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `starting_number` | number |  |  | 0 |  |
| `ending_number` | number |  |  | 100 |  |
| `prefix` | text |  |  |  |  |
| `suffix` | text |  |  |  |  |
| `duration` | number |  |  | 2000 |  |
| `thousand_separator` | switcher |  |  | "yes" |  |
| `thousand_separator_char` | select |  | ``, `.`, ` `, `_`, `'` |  | {"thousand_separator": "yes"} |
| `title` | text |  |  | "Cool Number" |  |
| `title_tag` | select |  | `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `div`, `span`, `p` | "div" | {"title!": ""} |

## Estilo › Counter

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `title_position` | choose | sim | `before`, `after`, `start`, `end` |  | {"title!": ""} |
| `title_horizontal_alignment` | choose | sim | `start`, `center`, `end` |  | {"title!": ""} |
| `title_vertical_alignment` | choose | sim | `start`, `center`, `end` |  | {"title!": "", "title_position": ["start", "end"]} |
| `title_gap` | slider | sim | units: px,em,rem,custom |  | {"title!": "", "title_position": ["", "before", "after"]} |
| `number_position` | choose | sim | `start`, `center`, `end`, `stretch` |  |  |
| `number_alignment` | choose | sim | `start`, `center`, `end` |  | {"number_position": "stretch"} |
| `number_gap` | slider | sim | units: px,em,rem,custom |  |  |

## Estilo › Number

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `number_color` | color |  | global padrão `globals/colors?id=primary` |  |  |
| `typography_number_*` | **grupo typography** (ver groups.md) | | liga com `typography_number_typography: "custom"`. Chaves: `typography_number_font_family`, `typography_number_font_size`, `typography_number_font_weight`, `typography_number_text_transform`, `typography_number_font_style`, `typography_number_text_decoration`, `typography_number_line_height`, `typography_number_letter_spacing`, `typography_number_word_spacing` | |  |
| `number_stroke_*` | **grupo text-stroke** (ver groups.md) | | liga com `number_stroke_text_stroke_type: "yes"`. Chaves: `number_stroke_text_stroke`, `number_stroke_stroke_color` | |  |
| `number_shadow_*` | **grupo text-shadow** (ver groups.md) | | liga com `number_shadow_text_shadow_type: "yes"`. Chaves: `number_shadow_text_shadow` | |  |

## Estilo › Title

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `title_color` | color |  | global padrão `globals/colors?id=secondary` |  | {"title!": ""} |
| `typography_title_*` | **grupo typography** (ver groups.md) | | liga com `typography_title_typography: "custom"`. Chaves: `typography_title_font_family`, `typography_title_font_size`, `typography_title_font_weight`, `typography_title_text_transform`, `typography_title_font_style`, `typography_title_text_decoration`, `typography_title_line_height`, `typography_title_letter_spacing`, `typography_title_word_spacing` | | {"title!": ""} |
| `title_stroke_*` | **grupo text-stroke** (ver groups.md) | | liga com `title_stroke_text_stroke_type: "yes"`. Chaves: `title_stroke_text_stroke`, `title_stroke_stroke_color` | | {"title!": ""} |
| `title_shadow_*` | **grupo text-shadow** (ver groups.md) | | liga com `title_shadow_text_shadow_type: "yes"`. Chaves: `title_shadow_text_shadow` | | {"title!": ""} |
