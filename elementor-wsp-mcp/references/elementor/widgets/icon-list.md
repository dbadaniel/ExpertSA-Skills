# Widget `icon-list`

Gerado do código-fonte do Elementor 4.4.0 (`icon-list.php`). O site pode ter outra versão: em caso de dúvida, confirme com `wsp_elementor_get_widget_schema`.


## Conteúdo › Icon List

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `view` | choose |  | `traditional`, `inline` | "traditional" |  |
| `icon_list` | repeater |  |  | [{"text": "List Item #1", "selected_icon": {"value": "fas fa… |  |

**Itens do repeater `icon_list`** (cada item precisa de `_id` único de 7 hex):

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `text` | text |  |  | "List Item" |  |
| `selected_icon` | icons |  |  | {"value": "fas fa-check", "library": "fa-solid"} |  |
| `link` | url |  |  |  |  |

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `link_click` | select |  | `full_width`, `inline` | "full_width" |  |

## Estilo › List

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `space_between` | slider | sim | units: px,em,rem,custom |  |  |
| `icon_align` | choose | sim | `start`, `center`, `end` |  |  |
| `divider` | switcher |  |  |  |  |
| `divider_style` | select |  | `solid`, `double`, `dotted`, `dashed` | "solid" | {"divider": "yes"} |
| `divider_weight` | slider |  | units: px,em,rem,custom | {"size": 1} | {"divider": "yes"} |
| `divider_width` | slider |  | units: px,%,em,rem,vw,custom | {"unit": "%"} | {"divider": "yes", "view!": "inline"} |
| `divider_height` | slider |  | units: px,%,em,rem,vh,custom | {"unit": "%"} | {"divider": "yes", "view": "inline"} |
| `divider_color` | color |  | global padrão `globals/colors?id=text` | "#ddd" | {"divider": "yes"} |

## Estilo › Icon

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `icon_color` (Normal) | color |  | global padrão `globals/colors?id=primary` |  |  |
| `icon_color_hover` (Hover) | color |  |  |  |  |
| `icon_color_hover_transition` (Hover) | slider |  | units: s,ms,custom | {"unit": "s", "size": 0.3} |  |
| `icon_size` | slider | sim | units: px,%,em,rem,vw,custom | {"size": 14} |  |
| `text_indent` | slider |  | units: px,%,em,rem,vw,custom |  |  |
| `icon_self_align` | choose | sim | `left`, `center`, `right` |  |  |
| `icon_self_vertical_align` | choose | sim | `flex-start`, `center`, `flex-end` |  |  |
| `icon_vertical_offset` | slider | sim | units: px,em,rem,custom | {"size": 0} |  |

## Estilo › Text

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `icon_typography_*` | **grupo typography** (ver groups.md) | | liga com `icon_typography_typography: "custom"`. Chaves: `icon_typography_font_family`, `icon_typography_font_size`, `icon_typography_font_weight`, `icon_typography_text_transform`, `icon_typography_font_style`, `icon_typography_text_decoration`, `icon_typography_line_height`, `icon_typography_letter_spacing`, `icon_typography_word_spacing` | |  |
| `text_shadow_*` | **grupo text-shadow** (ver groups.md) | | liga com `text_shadow_text_shadow_type: "yes"`. Chaves: `text_shadow_text_shadow` | |  |
| `text_color` (Normal) | color |  | global padrão `globals/colors?id=secondary` |  |  |
| `text_color_hover` (Hover) | color |  |  |  |  |
| `text_color_hover_transition` (Hover) | slider |  | units: s,ms,custom | {"unit": "s", "size": 0.3} |  |
