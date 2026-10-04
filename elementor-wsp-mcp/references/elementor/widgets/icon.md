# Widget `icon`

Gerado do código-fonte do Elementor 4.4.0 (`icon.php`). O site pode ter outra versão: em caso de dúvida, confirme com `wsp_elementor_get_widget_schema`.


## Conteúdo › Icon

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `selected_icon` | icons |  |  | {"value": "fas fa-star", "library": "fa-solid"} |  |
| `view` | select |  | `default`, `stacked`, `framed` | "default" |  |
| `shape` | select |  | `square`, `rounded`, `circle` | "circle" | {"view!": "default"} |
| `link` | url |  |  |  |  |

## Estilo › Icon

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `align` | choose | sim | `start`, `center`, `end` | "center" |  |
| `primary_color` (Normal) | color |  | global padrão `globals/colors?id=primary` |  |  |
| `secondary_color` (Normal) | color |  |  |  | {"view!": "default"} |
| `hover_primary_color` (Hover) | color |  |  |  |  |
| `hover_secondary_color` (Hover) | color |  |  |  | {"view!": "default"} |
| `hover_animation` (Hover) | hover_animation |  |  |  |  |
| `size` | slider | sim | units: px,%,em,rem,vw,custom |  |  |
| `fit_to_size` | switcher |  |  |  | {"selected_icon[library]": "svg"} |
| `icon_padding` | slider |  | units: px,%,em,rem,custom |  | {"view!": "default"} |
| `rotate` | slider | sim | units: deg,grad,rad,turn,custom | {"unit": "deg"} |  |
| `border_width` | dimensions |  | units: px,%,em,rem,vw,custom |  | {"view": "framed"} |
| `border_radius` | dimensions | sim | units: px,%,em,rem,custom |  | {"view!": "default"} |
