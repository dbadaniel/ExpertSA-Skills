# Widget `image-carousel`

Gerado do código-fonte do Elementor 4.4.0 (`image-carousel.php`). O site pode ter outra versão: em caso de dúvida, confirme com `wsp_elementor_get_widget_schema`.


## Conteúdo › Image Carousel

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `carousel_name` | text |  |  | "Image Carousel" |  |
| `carousel` | gallery |  |  |  |  |
| `thumbnail_*` | **grupo image-size** (ver groups.md) | | Chaves: `thumbnail_size`, `thumbnail_custom_dimension` | |  |
| `slides_to_show` | select | sim | ``, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10` |  |  |
| `slides_to_scroll` | select | sim | ``, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10` |  | {"slides_to_show!": "1"} |
| `image_stretch` | select |  | `no`, `yes` | "no" |  |
| `navigation` | select |  | `both`, `arrows`, `dots`, `none` | "both" |  |
| `navigation_previous_icon` | icons |  |  |  |  |
| `navigation_next_icon` | icons |  |  |  |  |
| `link_to` | select |  | `none`, `file`, `custom` | "none" |  |
| `link` | url |  |  |  | {"link_to": "custom"} |
| `open_lightbox` | select |  | `default`, `yes`, `no` | "default" | {"link_to": "file"} |
| `caption_type` | select |  | ``, `title`, `caption`, `description` |  |  |

## Conteúdo › Additional Options

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `lazyload` | switcher |  |  |  |  |
| `autoplay` | switcher |  | ligado=`yes` | "yes" |  |
| `pause_on_hover` | switcher |  | ligado=`yes` | "yes" | {"autoplay": "yes"} |
| `pause_on_interaction` | switcher |  | ligado=`yes` | "yes" | {"autoplay": "yes"} |
| `autoplay_speed` | number |  |  | 5000 | {"autoplay": "yes"} |
| `infinite` | switcher |  | ligado=`yes` | "yes" |  |
| `effect` | select |  | `slide`, `fade` | "slide" | {"slides_to_show": "1"} |
| `speed` | number |  |  | 500 |  |
| `direction` | select |  | `ltr`, `rtl` | "ltr" |  |

## Estilo › Navigation

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `arrows_position` | select |  | `inside`, `outside` | "inside" | {"navigation": ["arrows", "both"]} |
| `arrows_size` | slider | sim | units: px,em,rem,custom |  | {"navigation": ["arrows", "both"]} |
| `arrows_color` | color |  |  |  | {"navigation": ["arrows", "both"]} |
| `dots_position` | select |  | `outside`, `inside` | "outside" | {"navigation": ["dots", "both"]} |
| `dots_gap` | slider | sim | units: px,em,rem,custom |  | {"navigation": ["dots", "both"]} |
| `dots_size` | slider | sim | units: px,em,rem,custom |  | {"navigation": ["dots", "both"]} |
| `dots_inactive_color` | color |  |  |  | {"navigation": ["dots", "both"]} |
| `dots_color` | color |  |  |  | {"navigation": ["dots", "both"]} |

## Estilo › Image

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `gallery_vertical_align` | choose | sim | `flex-start`, `center`, `flex-end` |  | {"slides_to_show!": "1"} |
| `image_spacing` | select |  | ``, `custom` |  | {"slides_to_show!": "1"} |
| `image_spacing_custom` | slider | sim | units: px | {"size": 20} | {"image_spacing": "custom", "slides_to_show!": "1"} |
| `image_border_*` | **grupo border** (ver groups.md) | | liga com `image_border_border` ("solid"/"dashed"/…). Chaves: `image_border_width`, `image_border_color` | |  |
| `image_border_radius` | dimensions | sim | units: px,%,em,rem,custom |  |  |

## Estilo › Caption

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `caption_align` | choose | sim | `start`, `center`, `end`, `justify` | "center" |  |
| `caption_text_color` | color |  |  |  |  |
| `caption_typography_*` | **grupo typography** (ver groups.md) | | liga com `caption_typography_typography: "custom"`. Chaves: `caption_typography_font_family`, `caption_typography_font_size`, `caption_typography_font_weight`, `caption_typography_text_transform`, `caption_typography_font_style`, `caption_typography_text_decoration`, `caption_typography_line_height`, `caption_typography_letter_spacing`, `caption_typography_word_spacing` | |  |
| `caption_shadow_*` | **grupo text-shadow** (ver groups.md) | | liga com `caption_shadow_text_shadow_type: "yes"`. Chaves: `caption_shadow_text_shadow` | |  |
| `caption_space` | slider | sim | units: px,%,em,rem,custom |  |  |
