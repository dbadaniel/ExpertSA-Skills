# Widget `image`

Gerado do código-fonte do Elementor 4.4.0 (`image.php`). O site pode ter outra versão: em caso de dúvida, confirme com `wsp_elementor_get_widget_schema`.


## Conteúdo › Image

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `image_*` | **grupo image-size** (ver groups.md) | | Chaves: `image_size`, `image_custom_dimension` | | {"image[url]!": ""} |
| `caption_source` | select |  | `none`, `attachment`, `custom` | "none" | {"image[url]!": ""} |
| `caption` | text |  |  |  | {"image[url]!": "", "caption_source": "custom"} |
| `link_to` | select |  | `none`, `file`, `custom` | "none" | {"image[url]!": ""} |
| `link` | url |  |  |  | {"image[url]!": "", "link_to": "custom"} |
| `open_lightbox` | select |  | `default`, `yes`, `no` | "default" | {"image[url]!": "", "link_to": "file"} |

## Estilo › Image

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `align` | choose | sim | `start`, `center`, `end` |  |  |
| `width` | slider | sim | units: px,%,em,rem,vw,custom | {"unit": "%"} |  |
| `space` | slider | sim | units: px,%,em,rem,vw,custom | {"unit": "%"} |  |
| `height` | slider | sim | units: px,%,em,rem,vh,custom |  |  |
| `object-fit` | select | sim | ``, `fill`, `cover`, `contain`, `scale-down` |  | {"height[size]!": ""} |
| `object-position` | select | sim | `center center`, `center left`, `center right`, `top center`, `top left`, `top right`, `bottom center`, `bottom left`, `bottom right` | "center center" | {"height[size]!": "", "object-fit": ["cover", "contain", "scale-down"]… |
| `opacity` (Normal) | slider |  |  |  |  |
| `css_filters_*` | **grupo css-filter** (ver groups.md) | | liga com `css_filters_css_filter: "custom"`. Chaves: `css_filters_blur`, `css_filters_brightness`, `css_filters_contrast`, `css_filters_saturate`, `css_filters_hue` | |  |  (Normal)
| `opacity_hover` (Hover) | slider |  |  |  |  |
| `css_filters_hover_*` | **grupo css-filter** (ver groups.md) | | liga com `css_filters_hover_css_filter: "custom"`. Chaves: `css_filters_hover_blur`, `css_filters_hover_brightness`, `css_filters_hover_contrast`, `css_filters_hover_saturate`, `css_filters_hover_hue` | |  |  (Hover)
| `background_hover_transition` (Hover) | slider |  |  |  |  |
| `hover_animation` (Hover) | hover_animation |  |  |  |  |
| `image_border_*` | **grupo border** (ver groups.md) | | liga com `image_border_border` ("solid"/"dashed"/…). Chaves: `image_border_width`, `image_border_color` | |  |
| `image_border_radius` | dimensions | sim | units: px,%,em,rem,custom |  |  |
| `image_box_shadow_*` | **grupo box-shadow** (ver groups.md) | | liga com `image_box_shadow_box_shadow_type: "yes"`. Chaves: `image_box_shadow_box_shadow` | |  |

## Estilo › Caption

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `caption_align` | choose | sim | `start`, `center`, `end`, `justify` |  |  |
| `text_color` | color |  | global padrão `globals/colors?id=text` |  |  |
| `caption_background_color` | color |  |  |  |  |
| `caption_typography_*` | **grupo typography** (ver groups.md) | | liga com `caption_typography_typography: "custom"`. Chaves: `caption_typography_font_family`, `caption_typography_font_size`, `caption_typography_font_weight`, `caption_typography_text_transform`, `caption_typography_font_style`, `caption_typography_text_decoration`, `caption_typography_line_height`, `caption_typography_letter_spacing`, `caption_typography_word_spacing` | |  |
| `caption_text_shadow_*` | **grupo text-shadow** (ver groups.md) | | liga com `caption_text_shadow_text_shadow_type: "yes"`. Chaves: `caption_text_shadow_text_shadow` | |  |
| `caption_space` | slider | sim | units: px,em,rem,custom |  |  |
