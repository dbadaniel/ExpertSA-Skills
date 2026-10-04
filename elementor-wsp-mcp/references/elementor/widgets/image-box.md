# Widget `image-box`

Gerado do código-fonte do Elementor 4.4.0 (`image-box.php`). O site pode ter outra versão: em caso de dúvida, confirme com `wsp_elementor_get_widget_schema`.


## Conteúdo › Image Box

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `image` | media |  |  | {"url": ""} |  |
| `thumbnail_*` | **grupo image-size** (ver groups.md) | | Chaves: `thumbnail_size`, `thumbnail_custom_dimension` | | {"image[url]!": ""} |
| `title_text` | text |  |  | "This is the heading" |  |
| `description_text` | textarea |  |  | "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut… |  |
| `link` | url |  |  |  |  |
| `title_size` | select |  | `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `div`, `span`, `p` | "h3" |  |

## Estilo › Box

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `position` | choose | sim | `left`, `top`, `right` | "top" | {"image[url]!": ""} |
| `content_vertical_alignment` | choose | sim | `top`, `middle`, `bottom` | "top" | {"position!": "top"} |
| `text_align` | choose | sim | `start`, `center`, `end`, `justify` |  |  |
| `image_space` | slider | sim | units: px,%,em,rem,vw,custom | {"size": 15} | {"image[url]!": ""} |
| `title_bottom_space` | slider | sim | units: px,em,rem,custom |  |  |

## Estilo › Image

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `image_size` | slider | sim | units: px,%,em,rem,vw,custom | {"size": 30, "unit": "%"} |  |
| `image_height` | slider | sim | units: px,%,em,rem,vh,custom |  |  |
| `image_object_fit` | select | sim | ``, `fill`, `cover`, `contain`, `scale-down` |  | {"image_height[size]!": ""} |
| `image_object_position` | select | sim | `center center`, `center left`, `center right`, `top center`, `top left`, `top right`, `bottom center`, `bottom left`, `bottom right` | "center center" | {"image_height[size]!": "", "image_object_fit": ["cover", "contain", "… |
| `image_border_*` | **grupo border** (ver groups.md) | | liga com `image_border_border` ("solid"/"dashed"/…). Chaves: `image_border_width`, `image_border_color` | |  |
| `image_border_radius` | slider | sim | units: px,%,em,rem,custom |  |  |
| `image_box_shadow_*` | **grupo box-shadow** (ver groups.md) | | liga com `image_box_shadow_box_shadow_type: "yes"`. Chaves: `image_box_shadow_box_shadow`, `image_box_shadow_box_shadow_position` | |  |
| `css_filters_*` | **grupo css-filter** (ver groups.md) | | liga com `css_filters_css_filter: "custom"`. Chaves: `css_filters_blur`, `css_filters_brightness`, `css_filters_contrast`, `css_filters_saturate`, `css_filters_hue` | |  |  (Normal)
| `image_opacity` (Normal) | slider |  |  |  |  |
| `css_filters_hover_*` | **grupo css-filter** (ver groups.md) | | liga com `css_filters_hover_css_filter: "custom"`. Chaves: `css_filters_hover_blur`, `css_filters_hover_brightness`, `css_filters_hover_contrast`, `css_filters_hover_saturate`, `css_filters_hover_hue` | |  |  (Hover)
| `image_opacity_hover` (Hover) | slider |  |  |  |  |
| `background_hover_transition` (Hover) | slider |  |  | {"size": 0.3} |  |
| `hover_animation` (Hover) | hover_animation |  |  |  |  |

## Estilo › Content

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `title_typography_*` | **grupo typography** (ver groups.md) | | liga com `title_typography_typography: "custom"`. Chaves: `title_typography_font_family`, `title_typography_font_size`, `title_typography_font_weight`, `title_typography_text_transform`, `title_typography_font_style`, `title_typography_text_decoration`, `title_typography_line_height`, `title_typography_letter_spacing`, `title_typography_word_spacing` | |  |
| `title_stroke_*` | **grupo text-stroke** (ver groups.md) | | liga com `title_stroke_text_stroke_type: "yes"`. Chaves: `title_stroke_text_stroke`, `title_stroke_stroke_color` | |  |
| `title_shadow_*` | **grupo text-shadow** (ver groups.md) | | liga com `title_shadow_text_shadow_type: "yes"`. Chaves: `title_shadow_text_shadow` | |  |
| `title_color` (Normal) | color |  | global padrão `globals/colors?id=primary` |  |  |
| `hover_title_color` (Hover) | color |  | global padrão `globals/colors?id=primary` |  |  |
| `hover_title_color_transition_duration` (Hover) | slider |  | units: s,ms,custom | {"unit": "s"} |  |
| `description_typography_*` | **grupo typography** (ver groups.md) | | liga com `description_typography_typography: "custom"`. Chaves: `description_typography_font_family`, `description_typography_font_size`, `description_typography_font_weight`, `description_typography_text_transform`, `description_typography_font_style`, `description_typography_text_decoration`, `description_typography_line_height`, `description_typography_letter_spacing`, `description_typography_word_spacing` | |  |
| `description_shadow_*` | **grupo text-shadow** (ver groups.md) | | liga com `description_shadow_text_shadow_type: "yes"`. Chaves: `description_shadow_text_shadow` | |  |
| `description_color` | color |  | global padrão `globals/colors?id=text` |  |  |
