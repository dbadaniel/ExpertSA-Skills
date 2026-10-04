# Container (flexbox/grid) — `elType: "container"`

Gerado do código-fonte do Elementor 4.4.0 (`container.php`). O site pode ter outra versão: em caso de dúvida, confirme com `wsp_elementor_get_widget_schema`.


## Layout › Container

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `container_type` | select |  | `flex`, `grid` | "flex" |  |
| `content_width` | select |  | `boxed`, `full` | "boxed" |  |
| `width` | slider | sim | units: px,%,em,rem,vw,custom | {"unit": "%"} | {"content_width": "full"} |
| `boxed_width` | slider | sim | units: px,%,em,rem,vw,custom | {"unit": "px"} | {"content_width": "boxed"} |
| `min_height` | slider | sim | units: px,em,rem,vh,custom |  |  |
| `flex_*` | **grupo flex-container** (ver groups.md) | | Chaves: `flex_items`, `flex_direction`, `flex_justify_content`, `flex_align_items`, `flex_gap`, `flex_wrap`, `flex_align_content` | | {"container_type": ["flex"]} |
| `grid_*` | **grupo grid-container** (ver groups.md) | | Chaves: `grid_items_grid`, `grid_outline`, `grid_columns_grid`, `grid_rows_grid`, `grid_gaps`, `grid_auto_flow`, `grid_justify_items`, `grid_align_items`, `grid_justify_content`, `grid_align_content` | | {"container_type": ["grid"]} |

## Layout › Additional Options

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `overflow` | select |  | ``, `hidden`, `auto` |  |  |
| `html_tag` | select |  | ``, `div`, `header`, `footer`, `main`, `article`, `section`, `aside`, `nav`, `a` |  |  |
| `link` | url |  |  |  | {"html_tag": "a"} |

## Estilo › Background

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `background_*` | **grupo background** (ver groups.md) | | liga com `background_background` ("classic"/"gradient"). Chaves: `background_gradient_notice`, `background_color`, `background_color_stop`, `background_color_b`, `background_color_b_stop`, `background_gradient_type`, `background_gradient_angle`, `background_gradient_position`, `background_image`, `background_position`, `background_xpos`, `background_ypos`, `background_attachment`, `background_attachment_alert` | |  |  (Normal)
| `background_hover_*` | **grupo background** (ver groups.md) | | liga com `background_hover_background` ("classic"/"gradient"). Chaves: `background_hover_gradient_notice`, `background_hover_color`, `background_hover_color_stop`, `background_hover_color_b`, `background_hover_color_b_stop`, `background_hover_gradient_type`, `background_hover_gradient_angle`, `background_hover_gradient_position`, `background_hover_image`, `background_hover_position`, `background_hover_xpos`, `background_hover_ypos`, `background_hover_attachment`, `background_hover_attachment_alert` | |  |  (Hover)
| `background_hover_transition` (Hover) | slider |  |  | {"size": 0.3} | {"background_hover_background": ["classic", "gradient"]} |

## Estilo › Background Overlay

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `background_overlay_*` | **grupo background** (ver groups.md) | | liga com `background_overlay_background` ("classic"/"gradient"). Chaves: `background_overlay_gradient_notice`, `background_overlay_color`, `background_overlay_color_stop`, `background_overlay_color_b`, `background_overlay_color_b_stop`, `background_overlay_gradient_type`, `background_overlay_gradient_angle`, `background_overlay_gradient_position`, `background_overlay_image`, `background_overlay_position`, `background_overlay_xpos`, `background_overlay_ypos`, `background_overlay_attachment`, `background_overlay_attachment_alert` | |  |  (Normal)
| `background_overlay_opacity` (Normal) | slider | sim |  | {"size": 0.5} | {"background_overlay_background": ["classic", "gradient"]} |
| `css_filters_*` | **grupo css-filter** (ver groups.md) | | liga com `css_filters_css_filter: "custom"`. Chaves: `css_filters_blur`, `css_filters_brightness`, `css_filters_contrast`, `css_filters_saturate`, `css_filters_hue` | |  |  (Normal)
| `overlay_blend_mode` (Normal) | select |  | ``, `multiply`, `screen`, `overlay`, `darken`, `lighten`, `color-dodge`, `saturation`, `color`, `luminosity` |  |  |
| `background_overlay_hover_*` | **grupo background** (ver groups.md) | | liga com `background_overlay_hover_background` ("classic"/"gradient"). Chaves: `background_overlay_hover_gradient_notice`, `background_overlay_hover_color`, `background_overlay_hover_color_stop`, `background_overlay_hover_color_b`, `background_overlay_hover_color_b_stop`, `background_overlay_hover_gradient_type`, `background_overlay_hover_gradient_angle`, `background_overlay_hover_gradient_position`, `background_overlay_hover_image`, `background_overlay_hover_position`, `background_overlay_hover_xpos`, `background_overlay_hover_ypos`, `background_overlay_hover_attachment`, `background_overlay_hover_attachment_alert` | |  |  (Hover)
| `background_overlay_hover_opacity` (Hover) | slider | sim |  | {"size": 0.5} | {"background_overlay_hover_background": ["classic", "gradient"]} |
| `background_overlay_hover_transition` (Hover) | slider |  |  |  | {"background_overlay_hover_background": ["classic", "gradient"]} |
| `css_filters_hover_*` | **grupo css-filter** (ver groups.md) | | liga com `css_filters_hover_css_filter: "custom"`. Chaves: `css_filters_hover_blur`, `css_filters_hover_brightness`, `css_filters_hover_contrast`, `css_filters_hover_saturate`, `css_filters_hover_hue` | |  |  (Hover)

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

## Estilo › Shape Divider

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `shape_divider_top` (Top) | visual_choice |  |  |  |  |
| `shape_divider_top_color` (Top) | color |  |  |  | {"shape_divider_top!": ""} |
| `shape_divider_top_width` (Top) | slider | sim | units: %,vw,custom | {"unit": "%"} | {"shape_divider_top": []} |
| `shape_divider_top_height` (Top) | slider | sim | units: px,em,rem,custom |  | {"shape_divider_top!": ""} |
| `shape_divider_top_flip` (Top) | switcher |  |  |  | {"shape_divider_top": []} |
| `shape_divider_top_negative` (Top) | switcher |  |  |  | {"shape_divider_top": []} |
| `shape_divider_top_above_content` (Top) | switcher |  |  |  | {"shape_divider_top!": ""} |
| `shape_divider_bottom` (Bottom) | visual_choice |  |  |  |  |
| `shape_divider_bottom_color` (Bottom) | color |  |  |  | {"shape_divider_bottom!": ""} |
| `shape_divider_bottom_width` (Bottom) | slider | sim | units: %,vw,custom | {"unit": "%"} | {"shape_divider_bottom": []} |
| `shape_divider_bottom_height` (Bottom) | slider | sim | units: px,em,rem,custom |  | {"shape_divider_bottom!": ""} |
| `shape_divider_bottom_flip` (Bottom) | switcher |  |  |  | {"shape_divider_bottom": []} |
| `shape_divider_bottom_negative` (Bottom) | switcher |  |  |  | {"shape_divider_bottom": []} |
| `shape_divider_bottom_above_content` (Bottom) | switcher |  |  |  | {"shape_divider_bottom!": ""} |

## Avançado › Layout

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `margin` | dimensions | sim | units: px,%,em,rem,vw,custom |  |  |
| `padding` | dimensions | sim | units: px,%,em,rem,vw,custom |  |  |
| `grid_column` | select | sim | ``, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `custom` |  |  |
| `grid_column_custom` | text | sim |  |  | {"grid_column": "custom"} |
| `grid_row` | select | sim | ``, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `custom` |  |  |
| `grid_row_custom` | text | sim |  |  | {"grid_row": "custom"} |
| `_flex_*` | **grupo flex-item** (ver groups.md) | | Chaves: `_flex_basis_type`, `_flex_basis`, `_flex_align_self`, `_flex_order`, `_flex_order_custom`, `_flex_size`, `_flex_grow`, `_flex_shrink` | |  |
| `position` | select |  | ``, `absolute`, `fixed` |  |  |
| `_offset_orientation_h` | choose |  | `start`, `end` | "start" | {"position!": ""} |
| `_offset_x` | slider | sim | units: px,%,em,rem,vw,vh,custom | {"size": 0} | {"_offset_orientation_h!": "end", "position!": ""} |
| `_offset_x_end` | slider | sim | units: px,%,em,rem,vw,vh,custom | {"size": 0} | {"_offset_orientation_h": "end", "position!": ""} |
| `_offset_orientation_v` | choose |  | `start`, `end` | "start" | {"position!": ""} |
| `_offset_y` | slider | sim | units: px,%,em,rem,vh,vw,custom | {"size": 0} | {"_offset_orientation_v!": "end", "position!": ""} |
| `_offset_y_end` | slider | sim | units: px,%,em,rem,vh,vw,custom | {"size": 0} | {"_offset_orientation_v": "end", "position!": ""} |
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
