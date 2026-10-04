# Widget `alert`

Gerado do código-fonte do Elementor 4.4.0 (`alert.php`). O site pode ter outra versão: em caso de dúvida, confirme com `wsp_elementor_get_widget_schema`.


## Conteúdo › Alert

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `alert_type` | select |  | `info`, `success`, `warning`, `danger` | "info" |  |

## Estilo › Title

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `alert_title_*` | **grupo typography** (ver groups.md) | | liga com `alert_title_typography: "custom"`. Chaves: `alert_title_font_family`, `alert_title_font_size`, `alert_title_font_weight`, `alert_title_text_transform`, `alert_title_font_style`, `alert_title_text_decoration`, `alert_title_line_height`, `alert_title_letter_spacing`, `alert_title_word_spacing` | |  |

## Estilo › Description

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `alert_description_*` | **grupo typography** (ver groups.md) | | liga com `alert_description_typography: "custom"`. Chaves: `alert_description_font_family`, `alert_description_font_size`, `alert_description_font_weight`, `alert_description_text_transform`, `alert_description_font_style`, `alert_description_text_decoration`, `alert_description_line_height`, `alert_description_letter_spacing`, `alert_description_word_spacing` | |  |

## Conteúdo › Alert

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `show_dismiss` | switcher |  | ligado=`show` | "show" |  |
| `dismiss_icon` | icons |  |  |  | {"show_dismiss": "show"} |

## Estilo › Alert

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `background` | color |  |  |  |  |
| `border_color` | color |  |  |  |  |
| `border_left-width` | slider |  | units: px,%,em,rem,custom |  |  |

## Estilo › Title

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `title_color` | color |  |  |  |  |
| `title_shadow_*` | **grupo text-shadow** (ver groups.md) | | liga com `title_shadow_text_shadow_type: "yes"`. Chaves: `title_shadow_text_shadow` | |  |

## Estilo › Description

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `description_color` | color |  |  |  |  |
| `description_shadow_*` | **grupo text-shadow** (ver groups.md) | | liga com `description_shadow_text_shadow_type: "yes"`. Chaves: `description_shadow_text_shadow` | |  |

## Estilo › Dismiss Icon

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `dismiss_icon_size` | slider | sim | units: px,em,rem,custom |  |  |
| `dismiss_icon_vertical_position` | slider | sim | units: px,%,em,rem,vh,custom |  |  |
| `dismiss_icon_horizontal_position` | slider | sim | units: px,%,em,rem,vw,custom |  |  |
| `dismiss_icon_normal_color` (Normal) | color |  |  |  |  |
| `dismiss_icon_hover_color` (Hover) | color |  |  |  |  |
| `dismiss_icon_hover_transition_duration` (Hover) | slider |  |  |  |  |
