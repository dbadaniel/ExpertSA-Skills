# Aba Avançado comum a TODOS os widgets

Gerado do código-fonte do Elementor 4.4.0 (`common-base.php`). O site pode ter outra versão: em caso de dúvida, confirme com `wsp_elementor_get_widget_schema`.


## Avançado › Layout

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `_margin` | dimensions | sim | units: px,%,em,rem,vw,custom |  |  |
| `_padding` | dimensions | sim | units: px,%,em,rem,vw,custom |  |  |
| `_element_width` | select | sim | ``, `inherit`, `auto`, `initial` |  |  |
| `_element_custom_width` | slider | sim | units: px,%,em,rem,vw,custom | {"unit": "%"} | {"_element_width": "initial"} |
| `_grid_column` | select | sim | ``, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `custom` |  |  |
| `_grid_column_custom` | text | sim |  |  | {"_grid_column": "custom"} |
| `_grid_row` | select | sim | ``, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `custom` |  |  |
| `_grid_row_custom` | text | sim |  |  | {"_grid_row": "custom"} |
| `_element_vertical_align` | choose | sim | `flex-start`, `center`, `flex-end` |  | {"_element_width!": "", "_position": ""} |
| `_position` | select |  | ``, `absolute`, `fixed` |  |  |
| `_offset_orientation_h` | choose |  | `start`, `end` | "start" | {"_position!": ""} |
| `_offset_x` | slider | sim | units: px,%,em,rem,vw,vh,custom | {"size": 0} | {"_offset_orientation_h!": "end", "_position!": ""} |
| `_offset_x_end` | slider | sim | units: px,%,em,rem,vw,vh,custom | {"size": 0} | {"_offset_orientation_h": "end", "_position!": ""} |
| `_offset_orientation_v` | choose |  | `start`, `end` | "start" | {"_position!": ""} |
| `_offset_y` | slider | sim | units: px,%,em,rem,vh,vw,custom | {"size": 0} | {"_offset_orientation_v!": "end", "_position!": ""} |
| `_offset_y_end` | slider | sim | units: px,%,em,rem,vh,vw,custom | {"size": 0} | {"_offset_orientation_v": "end", "_position!": ""} |
| `_z_index` | number | sim |  |  |  |
| `_element_id` | text |  |  |  |  |
| `_css_classes` | text |  |  |  |  |

## Avançado › Motion Effects

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `_animation` | animation | sim |  |  |  |
| `animation_duration` | select |  | `slow`, ``, `fast` |  | {"_animation!": ""} |
| `_animation_delay` | number |  |  |  | {"_animation!": ""} |

## Avançado › Background

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `_background_*` | **grupo background** (ver groups.md) | | liga com `_background_background` ("classic"/"gradient"). Chaves: `_background_gradient_notice`, `_background_color`, `_background_color_stop`, `_background_color_b`, `_background_color_b_stop`, `_background_gradient_type`, `_background_gradient_angle`, `_background_gradient_position`, `_background_image`, `_background_position`, `_background_xpos`, `_background_ypos`, `_background_attachment`, `_background_attachment_alert` | |  |  (Normal)
| `_background_hover_*` | **grupo background** (ver groups.md) | | liga com `_background_hover_background` ("classic"/"gradient"). Chaves: `_background_hover_gradient_notice`, `_background_hover_color`, `_background_hover_color_stop`, `_background_hover_color_b`, `_background_hover_color_b_stop`, `_background_hover_gradient_type`, `_background_hover_gradient_angle`, `_background_hover_gradient_position`, `_background_hover_image`, `_background_hover_position`, `_background_hover_xpos`, `_background_hover_ypos`, `_background_hover_attachment`, `_background_hover_attachment_alert` | |  |  (Hover)
| `_background_hover_transition` (Hover) | slider |  |  |  |  |

## Avançado › Border

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `_border_*` | **grupo border** (ver groups.md) | | liga com `_border_border` ("solid"/"dashed"/…). Chaves: `_border_width`, `_border_color` | |  |  (Normal)
| `_border_radius` (Normal) | dimensions | sim | units: px,%,em,rem,custom |  |  |
| `_box_shadow_*` | **grupo box-shadow** (ver groups.md) | | liga com `_box_shadow_box_shadow_type: "yes"`. Chaves: `_box_shadow_box_shadow`, `_box_shadow_box_shadow_position` | |  |  (Normal)
| `_border_hover_*` | **grupo border** (ver groups.md) | | liga com `_border_hover_border` ("solid"/"dashed"/…). Chaves: `_border_hover_width`, `_border_hover_color` | |  |  (Hover)
| `_border_radius_hover` (Hover) | dimensions | sim | units: px,%,em,rem,custom |  |  |
| `_box_shadow_hover_*` | **grupo box-shadow** (ver groups.md) | | liga com `_box_shadow_hover_box_shadow_type: "yes"`. Chaves: `_box_shadow_hover_box_shadow`, `_box_shadow_hover_box_shadow_position` | |  |  (Hover)
| `_border_hover_transition` (Hover) | slider |  |  |  |  |

## Avançado › Mask

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `_mask_switch` | switcher |  |  |  |  |
| `_mask_shape` | visual_choice |  | `circle`, `oval-vertical`, `oval-horizontal`, `pill-vertical`, `pill-horizontal`, `triangle`, `diamond`, `pentagon`, `hexagon-vertical`, `hexagon-horizontal`, `heptagon`, `octagon`, `parallelogram-right`, `parallelogram-left` … | "circle" | {"_mask_switch!": ""} |
| `_mask_image` | media | sim |  |  | {"_mask_switch!": "", "_mask_shape": "custom"} |
| `_mask_size` | select | sim | `contain`, `cover`, `custom` | "contain" | {"_mask_switch!": ""} |
| `_mask_size_scale` | slider | sim | units: px,%,em,rem,vw,custom | {"unit": "%", "size": 100} | {"_mask_switch!": "", "_mask_size": "custom"} |
| `_mask_position` | select | sim | `center center`, `center left`, `center right`, `top center`, `top left`, `top right`, `bottom center`, `bottom left`, `bottom right`, `custom` | "center center" | {"_mask_switch!": ""} |
| `_mask_position_x` | slider | sim | units: px,%,em,rem,vw,custom | {"unit": "%", "size": 0} | {"_mask_switch!": "", "_mask_position": "custom"} |
| `_mask_position_y` | slider | sim | units: px,%,em,rem,vw,custom | {"unit": "%", "size": 0} | {"_mask_switch!": "", "_mask_position": "custom"} |
| `_mask_repeat` | select | sim | `no-repeat`, `repeat`, `repeat-x`, `repeat-Y`, `round`, `space` | "no-repeat" | {"_mask_switch!": "", "_mask_size!": "cover"} |

## Avançado › Responsive
