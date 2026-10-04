# Widget `image-gallery`

Gerado do código-fonte do Elementor 4.4.0 (`image-gallery.php`). O site pode ter outra versão: em caso de dúvida, confirme com `wsp_elementor_get_widget_schema`.


## Conteúdo › Basic Gallery

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `wp_gallery` | gallery |  |  |  |  |
| `thumbnail_*` | **grupo image-size** (ver groups.md) | | Chaves: `thumbnail_size`, `thumbnail_custom_dimension` | |  |
| `gallery_columns` | select |  | `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10` | 4 |  |
| `gallery_display_caption` | select |  | `none`, `` |  |  |
| `gallery_link` | select |  | `file`, `attachment`, `none` | "file" |  |
| `open_lightbox` | select |  | `default`, `yes`, `no` | "default" | {"gallery_link": "file"} |
| `gallery_rand` | select |  | ``, `rand` |  |  |

## Estilo › Images

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `image_spacing` | select |  | ``, `custom` |  |  |
| `image_spacing_custom` | slider |  | units: px,em,rem,custom | {"size": 15} | {"image_spacing": "custom"} |
| `image_border_*` | **grupo border** (ver groups.md) | | liga com `image_border_border` ("solid"/"dashed"/…). Chaves: `image_border_width`, `image_border_color` | |  |
| `image_border_radius` | dimensions | sim | units: px,%,em,rem,custom |  |  |

## Estilo › Caption

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `align` | choose | sim | `start`, `center`, `end`, `justify` | "center" | {"gallery_display_caption": ""} |
| `text_color` | color |  |  |  | {"gallery_display_caption": ""} |
| `typography_*` | **grupo typography** (ver groups.md) | | liga com `typography_typography: "custom"`. Chaves: `typography_font_family`, `typography_font_size`, `typography_font_weight`, `typography_text_transform`, `typography_font_style`, `typography_text_decoration`, `typography_line_height`, `typography_letter_spacing`, `typography_word_spacing` | | {"gallery_display_caption": ""} |
| `caption_shadow_*` | **grupo text-shadow** (ver groups.md) | | liga com `caption_shadow_text_shadow_type: "yes"`. Chaves: `caption_shadow_text_shadow` | | {"gallery_display_caption": ""} |
| `caption_space` | slider | sim | units: px,%,em,rem,custom |  | {"gallery_display_caption": ""} |
