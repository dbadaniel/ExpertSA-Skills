# Widget `heading`

Gerado do código-fonte do Elementor 4.4.0 (`heading.php`). O site pode ter outra versão: em caso de dúvida, confirme com `wsp_elementor_get_widget_schema`.


## Conteúdo › Heading

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `title` | textarea |  |  | "Add Your Heading Text Here" |  |
| `link` | url |  |  | {"url": ""} |  |
| `size` | select |  | `default`, `small`, `medium`, `large`, `xl`, `xxl` | "default" | {"size!": "default"} |
| `header_size` | select |  | `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `div`, `span`, `p` | "h2" |  |

## Estilo › Heading

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `align` | choose | sim | `start`, `center`, `end`, `justify` |  |  |
| `typography_*` | **grupo typography** (ver groups.md) | | liga com `typography_typography: "custom"`. Chaves: `typography_font_family`, `typography_font_size`, `typography_font_weight`, `typography_text_transform`, `typography_font_style`, `typography_text_decoration`, `typography_line_height`, `typography_letter_spacing`, `typography_word_spacing` | |  |
| `text_stroke_*` | **grupo text-stroke** (ver groups.md) | | liga com `text_stroke_text_stroke_type: "yes"`. Chaves: `text_stroke_text_stroke`, `text_stroke_stroke_color` | |  |
| `text_shadow_*` | **grupo text-shadow** (ver groups.md) | | liga com `text_shadow_text_shadow_type: "yes"`. Chaves: `text_shadow_text_shadow` | |  |
| `blend_mode` | select |  | ``, `multiply`, `screen`, `overlay`, `darken`, `lighten`, `color-dodge`, `saturation`, `color`, `difference`, `exclusion`, `hue`, `luminosity` |  |  |
| `title_color` (Normal) | color |  | global padrão `globals/colors?id=primary` |  |  |
| `title_hover_color` (Hover) | color |  |  |  |  |
| `title_hover_color_transition_duration` (Hover) | slider |  | units: s,ms,custom | {"unit": "s"} |  |
