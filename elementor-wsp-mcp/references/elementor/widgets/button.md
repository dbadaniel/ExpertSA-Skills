# Widget `button`

Gerado do código-fonte do Elementor 4.4.0 (`button.php`). O site pode ter outra versão: em caso de dúvida, confirme com `wsp_elementor_get_widget_schema`.


## Conteúdo › Button

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `button_type` | select |  | ``, `info`, `success`, `warning`, `danger` |  |  |
| `text` | text |  |  | "Click here" |  |
| `link` | url |  |  | {"url": "#"} |  |
| `size` | select |  | `xs`, `sm`, `md`, `lg`, `xl` | "sm" | {"size[value]!": "sm"} |
| `selected_icon` | icons |  |  |  |  |
| `icon_align` | choose |  | `row`, `row-reverse` | "row" | {"text!": "", "selected_icon[value]!": ""} |
| `icon_indent` | slider |  | units: px,em,rem,custom |  | {"text!": "", "selected_icon[value]!": ""} |
| `button_css_id` | text |  |  |  |  |

## Estilo › Button

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `align` | choose | sim | `left`, `center`, `right`, `justify` |  |  |
| `content_align` | choose | sim | `start`, `center`, `end`, `space-between` |  | {"align": "justify"} |
| `typography_*` | **grupo typography** (ver groups.md) | | liga com `typography_typography: "custom"`. Chaves: `typography_font_family`, `typography_font_size`, `typography_font_weight`, `typography_text_transform`, `typography_font_style`, `typography_text_decoration`, `typography_line_height`, `typography_letter_spacing`, `typography_word_spacing` | |  |
| `text_shadow_*` | **grupo text-shadow** (ver groups.md) | | liga com `text_shadow_text_shadow_type: "yes"`. Chaves: `text_shadow_text_shadow` | |  |
| `button_text_color` (Normal) | color |  |  |  |  |
| `background_*` | **grupo background** (ver groups.md) | | liga com `background_background` ("classic"/"gradient"). Chaves: `background_gradient_notice`, `background_color`, `background_color_stop`, `background_color_b`, `background_color_b_stop`, `background_gradient_type`, `background_gradient_angle`, `background_gradient_position`, `background_position`, `background_xpos`, `background_ypos`, `background_attachment`, `background_attachment_alert`, `background_repeat` | |  |  (Normal)
| `button_box_shadow_*` | **grupo box-shadow** (ver groups.md) | | liga com `button_box_shadow_box_shadow_type: "yes"`. Chaves: `button_box_shadow_box_shadow`, `button_box_shadow_box_shadow_position` | |  |  (Normal)
| `hover_color` (Hover) | color |  |  |  |  |
| `button_background_hover_*` | **grupo background** (ver groups.md) | | liga com `button_background_hover_background` ("classic"/"gradient"). Chaves: `button_background_hover_gradient_notice`, `button_background_hover_color`, `button_background_hover_color_stop`, `button_background_hover_color_b`, `button_background_hover_color_b_stop`, `button_background_hover_gradient_type`, `button_background_hover_gradient_angle`, `button_background_hover_gradient_position`, `button_background_hover_position`, `button_background_hover_xpos`, `button_background_hover_ypos`, `button_background_hover_attachment`, `button_background_hover_attachment_alert`, `button_background_hover_repeat` | |  |  (Hover)
| `button_hover_border_color` (Hover) | color |  |  |  |  |
| `button_hover_box_shadow_*` | **grupo box-shadow** (ver groups.md) | | liga com `button_hover_box_shadow_box_shadow_type: "yes"`. Chaves: `button_hover_box_shadow_box_shadow`, `button_hover_box_shadow_box_shadow_position` | |  |  (Hover)
| `button_hover_transition_duration` (Hover) | slider |  | units: s,ms,custom | {"unit": "s"} |  |
| `hover_animation` (Hover) | hover_animation |  |  |  |  |
| `border_*` | **grupo border** (ver groups.md) | | liga com `border_border` ("solid"/"dashed"/…). Chaves: `border_width`, `border_color` | |  |
| `border_radius` | dimensions | sim | units: px,%,em,rem,custom |  |  |
| `text_padding` | dimensions | sim | units: px,%,em,rem,vw,custom |  |  |
