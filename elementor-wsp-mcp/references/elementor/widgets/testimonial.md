# Widget `testimonial`

Gerado do código-fonte do Elementor 4.4.0 (`testimonial.php`). O site pode ter outra versão: em caso de dúvida, confirme com `wsp_elementor_get_widget_schema`.


## Conteúdo › Testimonial

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `testimonial_content` | textarea |  |  | "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut… |  |
| `testimonial_image_*` | **grupo image-size** (ver groups.md) | | Chaves: `testimonial_image_size`, `testimonial_image_custom_dimension` | |  |
| `testimonial_name` | text |  |  | "John Doe" |  |
| `testimonial_job` | text |  |  | "Designer" |  |
| `link` | url |  |  |  |  |
| `testimonial_image_position` | choose |  | `aside`, `top` | "aside" | {"testimonial_image[url]!": ""} |
| `testimonial_alignment` | choose | sim | `start`, `center`, `end` | "center" |  |

## Estilo › Content

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `content_content_color` | color |  | global padrão `globals/colors?id=text` |  |  |
| `content_typography_*` | **grupo typography** (ver groups.md) | | liga com `content_typography_typography: "custom"`. Chaves: `content_typography_font_family`, `content_typography_font_size`, `content_typography_font_weight`, `content_typography_text_transform`, `content_typography_font_style`, `content_typography_text_decoration`, `content_typography_line_height`, `content_typography_letter_spacing`, `content_typography_word_spacing` | |  |
| `content_shadow_*` | **grupo text-shadow** (ver groups.md) | | liga com `content_shadow_text_shadow_type: "yes"`. Chaves: `content_shadow_text_shadow` | |  |

## Estilo › Image

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `image_size` | slider | sim | units: px,%,em,rem,vw,custom |  |  |
| `image_border_*` | **grupo border** (ver groups.md) | | liga com `image_border_border` ("solid"/"dashed"/…). Chaves: `image_border_width`, `image_border_color` | |  |
| `image_border_radius` | dimensions | sim | units: px,%,em,rem,custom |  |  |

## Estilo › Name

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `name_text_color` | color |  | global padrão `globals/colors?id=primary` |  |  |
| `name_typography_*` | **grupo typography** (ver groups.md) | | liga com `name_typography_typography: "custom"`. Chaves: `name_typography_font_family`, `name_typography_font_size`, `name_typography_font_weight`, `name_typography_text_transform`, `name_typography_font_style`, `name_typography_text_decoration`, `name_typography_line_height`, `name_typography_letter_spacing`, `name_typography_word_spacing` | |  |
| `name_shadow_*` | **grupo text-shadow** (ver groups.md) | | liga com `name_shadow_text_shadow_type: "yes"`. Chaves: `name_shadow_text_shadow` | |  |

## Estilo › Title

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `job_text_color` | color |  | global padrão `globals/colors?id=secondary` |  |  |
| `job_typography_*` | **grupo typography** (ver groups.md) | | liga com `job_typography_typography: "custom"`. Chaves: `job_typography_font_family`, `job_typography_font_size`, `job_typography_font_weight`, `job_typography_text_transform`, `job_typography_font_style`, `job_typography_text_decoration`, `job_typography_line_height`, `job_typography_letter_spacing`, `job_typography_word_spacing` | |  |
| `job_shadow_*` | **grupo text-shadow** (ver groups.md) | | liga com `job_shadow_text_shadow_type: "yes"`. Chaves: `job_shadow_text_shadow` | |  |
