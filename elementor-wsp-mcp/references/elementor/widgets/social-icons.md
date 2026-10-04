# Widget `social-icons`

Gerado do código-fonte do Elementor 4.4.0 (`social-icons.php`). O site pode ter outra versão: em caso de dúvida, confirme com `wsp_elementor_get_widget_schema`.


## Conteúdo › Social Icons

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `social_icon_list` | repeater |  |  | [{"social_icon": {"value": "fab fa-facebook", "library": "fa… |  |

**Itens do repeater `social_icon_list`** (cada item precisa de `_id` único de 7 hex):

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `social_icon` | icons |  |  | {"value": "fab fa-wordpress", "library": "fa-brands"} |  |
| `link` | url |  |  | {"is_external": "true"} |  |
| `item_icon_color` | select |  | `default`, `custom` | "default" |  |
| `item_icon_primary_color` | color |  |  |  | {"item_icon_color": "custom"} |
| `item_icon_secondary_color` | color |  |  |  | {"item_icon_color": "custom"} |

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `shape` | select |  | `square`, `rounded`, `circle` | "rounded" |  |
| `columns` | select | sim |  | "0" |  |
| `align` | choose | sim | `left`, `center`, `right` | "center" |  |

## Estilo › Icon

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `icon_color` | select |  | `default`, `custom` | "default" |  |
| `icon_primary_color` | color |  |  |  | {"icon_color": "custom"} |
| `icon_secondary_color` | color |  |  |  | {"icon_color": "custom"} |
| `icon_size` | slider | sim | units: px,rem,vw,custom |  |  |
| `icon_padding` | slider | sim | units: px,em,rem,custom | {"unit": "em"} |  |
| `icon_spacing` | slider | sim | units: px,em,rem,custom | {"size": 5} |  |
| `row_gap` | slider | sim | units: px,em,rem,custom | {"size": 0} |  |
| `image_border_*` | **grupo border** (ver groups.md) | | liga com `image_border_border` ("solid"/"dashed"/…). Chaves: `image_border_width`, `image_border_color` | |  |
| `border_radius` | dimensions | sim | units: px,%,em,rem,custom |  |  |

## Estilo › Icon Hover

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `hover_primary_color` | color |  |  |  | {"icon_color": "custom"} |
| `hover_secondary_color` | color |  |  |  | {"icon_color": "custom"} |
| `hover_border_color` | color |  |  |  | {"image_border_border!": ""} |
| `hover_animation` | hover_animation |  |  |  |  |
