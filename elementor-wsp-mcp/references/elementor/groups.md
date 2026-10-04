# Grupos de controles (prefixo + campo)

Um grupo é um conjunto de chaves com prefixo comum. Se um widget tem o grupo `typography` com nome `title_typography`, as chaves ficam `title_typography_font_size`, `title_typography_font_weight` etc. O **interruptor** do grupo precisa ser enviado junto, senão o Elementor ignora os outros campos.

| Grupo | Interruptor (chave = `<nome>_<campo>`) |
|---|---|
| typography | `<nome>_typography: "custom"` |
| background | `<nome>_background: "classic"` ou `"gradient"` (ou `"video"`/`"slideshow"` em containers) |
| border | `<nome>_border: "solid"` (`dashed`, `dotted`, `double`, `groove`, `none`) |
| box-shadow | `<nome>_box_shadow_type: "yes"` |
| text-shadow | `<nome>_text_shadow_type: "yes"` |
| text-stroke | `<nome>_text_stroke_type: "yes"` |
| css-filter | `<nome>_css_filter: "custom"` |
| flex-container / grid-container / image-size / flex-item | sem interruptor |


## background

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `<nome>_background` | choose |  |  |  |  |
| `<nome>_color` | color |  |  |  | {"background": ["classic", "gradient", "video"]} |
| `<nome>_color_stop` | slider | sim | units: %,custom | {"unit": "%", "size": 0} | {"background": ["gradient"]} |
| `<nome>_color_b` | color |  |  | "#f2295b" | {"background": ["gradient"]} |
| `<nome>_color_b_stop` | slider | sim | units: %,custom | {"unit": "%", "size": 100} | {"background": ["gradient"]} |
| `<nome>_gradient_type` | select |  | `linear`, `radial` | "linear" | {"background": ["gradient"]} |
| `<nome>_gradient_angle` | slider | sim | units: deg,grad,rad,turn,custom | {"unit": "deg", "size": 180} | {"background": ["gradient"], "gradient_type": "linear"} |
| `<nome>_gradient_position` | select | sim | `center center`, `center left`, `center right`, `top center`, `top left`, `top right`, `bottom center`, `bottom left`, `bottom right` | "center center" | {"background": ["gradient"], "gradient_type": "radial"} |
| `<nome>_image` | media | sim |  |  | {"background": ["classic"]} |
| `<nome>_position` | select | sim | ``, `center center`, `center left`, `center right`, `top center`, `top left`, `top right`, `bottom center`, `bottom left`, `bottom right`, `initial` |  | {"background": ["classic"], "image[url]!": ""} |
| `<nome>_xpos` | slider | sim | units: px,%,em,rem,vw,custom | {"size": 0} | {"background": ["classic"], "position": ["initial"], "image[url]!": ""… |
| `<nome>_ypos` | slider | sim | units: px,%,em,rem,vh,custom | {"size": 0} | {"background": ["classic"], "position": ["initial"], "image[url]!": ""… |
| `<nome>_attachment` | select |  | ``, `scroll`, `fixed` |  | {"background": ["classic"], "image[url]!": ""} |
| `<nome>_repeat` | select | sim | ``, `no-repeat`, `repeat`, `repeat-x`, `repeat-y` |  | {"background": ["classic"], "image[url]!": ""} |
| `<nome>_size` | select | sim | ``, `auto`, `cover`, `contain`, `initial` |  | {"background": ["classic"], "image[url]!": ""} |
| `<nome>_bg_width` | slider | sim | units: px,%,em,rem,vw,custom | {"size": 100, "unit": "%"} | {"background": ["classic"], "size": ["initial"], "image[url]!": ""} |

## border

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `<nome>_border` | select |  | ``, `none`, `solid`, `double`, `dotted`, `dashed`, `groove` |  |  |
| `<nome>_width` | dimensions | sim | units: px,em,rem,vw,custom |  | {"border!": ["", "none"]} |
| `<nome>_color` | color |  |  |  | {"border!": ["", "none"]} |

## box-shadow

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `<nome>_box_shadow` | box_shadow |  |  |  |  |
| `<nome>_box_shadow_position` | select |  | ` `, `inset` | " " |  |

## css-filter

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `<nome>_blur` | slider |  |  | {"size": 0} |  |
| `<nome>_brightness` | slider |  |  | {"size": 100} |  |
| `<nome>_contrast` | slider |  |  | {"size": 100} |  |
| `<nome>_saturate` | slider |  |  | {"size": 100} |  |
| `<nome>_hue` | slider |  |  | {"size": 0} |  |

## flex-container

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `<nome>_direction` | choose | sim | `row`, `column`, `row-reverse`, `column-reverse` |  |  |
| `<nome>_justify_content` | choose | sim | `flex-start`, `center`, `flex-end`, `space-between`, `space-around`, `space-evenly` |  |  |
| `<nome>_align_items` | choose | sim | `flex-start`, `center`, `flex-end`, `stretch` |  |  |
| `<nome>_gap` | gaps | sim | units: px,%,em,rem,vw,custom | {"unit": "px"} |  |
| `<nome>_wrap` | choose | sim | `nowrap`, `wrap` |  |  |
| `<nome>_align_content` | choose | sim | `flex-start`, `center`, `flex-end`, `space-between`, `space-around`, `space-evenly` |  | {"wrap": "wrap"} |

## flex-item

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `<nome>_basis_type` | select | sim | ``, `custom` |  |  |
| `<nome>_basis` | slider | sim | units: px,%,em,rem,vw,custom | {"unit": "%"} | {"basis_type": "custom"} |
| `<nome>_align_self` | choose | sim | `flex-start`, `center`, `flex-end`, `stretch` |  |  |
| `<nome>_order` | choose | sim | `start`, `end`, `custom` |  |  |
| `<nome>_order_custom` | number | sim |  |  | {"order": "custom"} |
| `<nome>_size` | choose | sim | `none`, `grow`, `shrink`, `custom` |  |  |
| `<nome>_grow` | number | sim |  | 1 | {"size": "custom"} |
| `<nome>_shrink` | number | sim |  | 1 | {"size": "custom"} |

## grid-container

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `<nome>_outline` | switcher |  |  | "yes" |  |
| `<nome>_columns_grid` | slider | sim | units: fr,custom | {"unit": "fr", "size": 3} |  |
| `<nome>_rows_grid` | slider | sim | units: fr,custom | {"unit": "fr", "size": 2} |  |
| `<nome>_gaps` | gaps | sim | units: px,%,em,rem,vw,custom | {"unit": "px"} |  |
| `<nome>_auto_flow` | select | sim | `row`, `column` | "row" |  |
| `<nome>_justify_items` | choose | sim | `start`, `center`, `end`, `stretch` |  |  |
| `<nome>_align_items` | choose | sim | `start`, `center`, `end`, `stretch` |  |  |
| `<nome>_justify_content` | choose | sim | `start`, `center`, `end`, `space-between`, `space-around`, `space-evenly` |  | {"columns_grid[unit]": "custom"} |
| `<nome>_align_content` | choose | sim | `start`, `center`, `end`, `space-between`, `space-around`, `space-evenly` |  | {"rows_grid[unit]": "custom"} |

## image-size

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `<nome>_size` | select |  |  |  |  |
| `<nome>_custom_dimension` | image_dimensions |  |  |  | {"size": "custom"} |

## text-shadow

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `<nome>_text_shadow` | text_shadow |  |  |  |  |

## text-stroke

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `<nome>_text_stroke` | slider | sim | units: px,em,rem,custom |  |  |
| `<nome>_stroke_color` | color |  |  | "#000" |  |

## typography

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `<nome>_font_family` | font |  |  |  |  |
| `<nome>_font_size` | slider | sim | units: px,em,rem,vw,custom |  |  |
| `<nome>_font_weight` | select |  | `100`, `200`, `300`, `400`, `500`, `600`, `700`, `800`, `900`, ``, `normal`, `bold` |  |  |
| `<nome>_text_transform` | select |  | ``, `uppercase`, `lowercase`, `capitalize`, `none` |  |  |
| `<nome>_font_style` | select |  | ``, `normal`, `italic`, `oblique` |  |  |
| `<nome>_text_decoration` | select |  | ``, `underline`, `overline`, `line-through`, `none` |  |  |
| `<nome>_line_height` | slider | sim | units: px,em,rem,lh,rlh,custom |  |  |
| `<nome>_letter_spacing` | slider | sim | units: px,em,rem,custom |  |  |
| `<nome>_word_spacing` | slider | sim | units: px,em,rem,custom |  |  |
