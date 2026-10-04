# Column (layout legado) — `elType: "column"`

Gerado do código-fonte do Elementor 4.4.0 (`column.php`). O site pode ter outra versão: em caso de dúvida, confirme com `wsp_elementor_get_widget_schema`.


## Layout › Layout

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `_inline_size` | number | sim |  |  |  |
| `content_position` | select | sim | ``, `top`, `center`, `bottom`, `space-between`, `space-around`, `space-evenly` |  |  |
| `align` | select | sim | ``, `flex-start`, `center`, `flex-end`, `space-between`, `space-around`, `space-evenly` |  |  |
| `space_between_widgets` | number | sim |  |  |  |
| `html_tag` | select |  | ``, `div`, `header`, `footer`, `main`, `article`, `section`, `aside`, `nav` |  |  |

## Estilo › Background

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `background_*` | **grupo background** (ver groups.md) | | liga com `background_background` ("classic"/"gradient"). Chaves: `background_gradient_notice`, `background_color`, `background_color_stop`, `background_color_b`, `background_color_b_stop`, `background_gradient_type`, `background_gradient_angle`, `background_gradient_position`, `background_image`, `background_position`, `background_xpos`, `background_ypos`, `background_attachment`, `background_attachment_alert` | |  |  (Normal)
| `background_hover_*` | **grupo background** (ver groups.md) | | liga com `background_hover_background` ("classic"/"gradient"). Chaves: `background_hover_gradient_notice`, `background_hover_color`, `background_hover_color_stop`, `background_hover_color_b`, `background_hover_color_b_stop`, `background_hover_gradient_type`, `background_hover_gradient_angle`, `background_hover_gradient_position`, `background_hover_image`, `background_hover_position`, `background_hover_xpos`, `background_hover_ypos`, `background_hover_attachment`, `background_hover_attachment_alert` | |  |  (Hover)
| `background_hover_transition` (Hover) | slider |  |  | {"size": 0.3} |  |

## Estilo › Background Overlay

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `background_overlay_*` | **grupo background** (ver groups.md) | | liga com `background_overlay_background` ("classic"/"gradient"). Chaves: `background_overlay_gradient_notice`, `background_overlay_color`, `background_overlay_color_stop`, `background_overlay_color_b`, `background_overlay_color_b_stop`, `background_overlay_gradient_type`, `background_overlay_gradient_angle`, `background_overlay_gradient_position`, `background_overlay_image`, `background_overlay_position`, `background_overlay_xpos`, `background_overlay_ypos`, `background_overlay_attachment`, `background_overlay_attachment_alert` | |  |  (Normal)
| `background_overlay_opacity` (Normal) | slider | sim |  | {"size": 0.5} | {"background_overlay_background": ["classic", "gradient"]} |
| `css_filters_*` | **grupo css-filter** (ver groups.md) | | liga com `css_filters_css_filter: "custom"`. Chaves: `css_filters_blur`, `css_filters_brightness`, `css_filters_contrast`, `css_filters_saturate`, `css_filters_hue` | |  |  (Normal)
| `overlay_blend_mode` (Normal) | select |  | ``, `multiply`, `screen`, `overlay`, `darken`, `lighten`, `color-dodge`, `saturation`, `color`, `difference`, `exclusion`, `hue`, `luminosity` |  |  |
| `background_overlay_hover_*` | **grupo background** (ver groups.md) | | liga com `background_overlay_hover_background` ("classic"/"gradient"). Chaves: `background_overlay_hover_gradient_notice`, `background_overlay_hover_color`, `background_overlay_hover_color_stop`, `background_overlay_hover_color_b`, `background_overlay_hover_color_b_stop`, `background_overlay_hover_gradient_type`, `background_overlay_hover_gradient_angle`, `background_overlay_hover_gradient_position`, `background_overlay_hover_image`, `background_overlay_hover_position`, `background_overlay_hover_xpos`, `background_overlay_hover_ypos`, `background_overlay_hover_attachment`, `background_overlay_hover_attachment_alert` | |  |  (Hover)
| `background_overlay_hover_opacity` (Hover) | slider | sim |  | {"size": 0.5} | {"background_overlay_hover_background": ["classic", "gradient"]} |
| `css_filters_hover_*` | **grupo css-filter** (ver groups.md) | | liga com `css_filters_hover_css_filter: "custom"`. Chaves: `css_filters_hover_blur`, `css_filters_hover_brightness`, `css_filters_hover_contrast`, `css_filters_hover_saturate`, `css_filters_hover_hue` | |  |  (Hover)
| `background_overlay_hover_transition` (Hover) | slider |  |  | {"size": 0.3} |  |

## Estilo › Border

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `border_*` | **grupo border** (ver groups.md) | | liga com `border_border` ("solid"/"dashed"/…). Chaves: `border_width`, `border_color` | |  |  (Normal)
| `border_radius` (Normal) | dimensions | sim | units: px,%,em,rem,custom |  |  |
| `box_shadow_*` | **grupo box-shadow** (ver groups.md) | | liga com `box_shadow_box_shadow_type: "yes"`. Chaves: `box_shadow_box_shadow`, `box_shadow_box_shadow_position` | |  |  (Normal)
| `border_hover_*` | **grupo border** (ver groups.md) | | liga com `border_hover_border` ("solid"/"dashed"/…). Chaves: `border_hover_width`, `border_hover_color` | |  |  (Hover)
| `border_radius_hover` (Hover) | dimensions | sim | units: px,%,em,rem,custom |  |  |
| `box_shadow_hover_*` | **grupo box-shadow** (ver groups.md) | | liga com `box_shadow_hover_box_shadow_type: "yes"`. Chaves: `box_shadow_hover_box_shadow`, `box_shadow_hover_box_shadow_position` | |  |  (Hover)
| `border_hover_transition` (Hover) | slider |  |  | {"size": 0.3} |  |

## Estilo › Typography

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `heading_color` | color |  |  |  |  |
| `color_text` | color |  |  |  |  |
| `color_link` | color |  |  |  |  |
| `color_link_hover` | color |  |  |  |  |
| `text_align` | choose | sim | `start`, `center`, `end`, `justify` |  |  |

## Avançado › Advanced

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `margin` | dimensions | sim | units: px,%,em,rem,vw,custom |  |  |
| `padding` | dimensions | sim | units: px,%,em,rem,vw,custom |  |  |
| `z_index` | number | sim |  |  |  |
| `_element_id` | text |  |  |  |  |
| `css_classes` | text |  |  |  |  |

## Avançado › Motion Effects

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `animation` | animation | sim |  |  |  |
| `animation_duration` | select |  | `slow`, ``, `fast` |  | {"animation!": ""} |
| `animation_delay` | number |  |  |  | {"animation!": ""} |

## Avançado › Responsive
