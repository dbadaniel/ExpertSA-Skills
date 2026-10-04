# Conhecimento do Elementor (extraído do código-fonte 4.4.0)

Os arquivos desta pasta foram **gerados automaticamente** a partir do repositório oficial `elementor/elementor` (versão 4.4.0): cada `add_control` real de cada widget, com chave, tipo, opções válidas, padrão e condição. São a referência principal para nomes de settings. O cheatsheet curto fica em `../settings-cheatsheet.md`.

## Como usar
1. Antes de criar/editar um widget, abra `widgets/<widget_type>.md` (ex.: `widgets/button.md`).
2. Para containers, abra `container.md`. Para margens/padding/posicionamento de qualquer widget, `advanced-common.md`.
3. Linhas "grupo X" expandem para várias chaves: veja `groups.md` (e o interruptor de cada grupo).
4. Se o site rodar outra versão do Elementor e algo não funcionar, confirme com `wsp_elementor_get_widget_schema`.

## Índice
| Arquivo | Conteúdo |
|---|---|
| `container.md` | Container flexbox/grid (`elType: "container"`) |
| `advanced-common.md` | Aba Avançado de todos os widgets (`_margin`, `_padding`, `_element_id`, `_flex_*`, posição, z-index, animação) |
| `groups.md` | Grupos: typography, background, border, box-shadow, text-shadow, text-stroke, css-filter, flex-container, flex-item, grid-container, image-size |
| `widgets/*.md` | accordion, alert, audio, button, counter, divider, google_maps, heading, icon, icon-box, icon-list, image, image-box, image-carousel, image-gallery, menu-anchor, progress, rating, read-more, social-icons, spacer, star-rating, tabs, testimonial, text-editor, toggle, video |
| `legacy-section.md`, `legacy-column.md` | Layout antigo (só para editar páginas que já usam) |

Widgets que **não** estão aqui: `html`, `shortcode` (bloqueados pelo WSP MCP), `sidebar` e widgets do WordPress, e widgets do Elementor Pro (form, posts, nav-menu, slides, price-table…). Para Pro, use `wsp_elementor_get_widget_schema`.

## Modelo de dados (`_elementor_data`)

Uma página é um array JSON de elementos. Cada elemento:

```json
{
  "id": "a1b2c3d4",              // 8 hex, único na página
  "elType": "container",         // container | widget | section | column
  "isInner": false,              // true para containers aninhados (a ferramenta sempre grava false)
  "settings": { ... },           // só as chaves que diferem do padrão
  "elements": [ ... ],           // filhos
  "widgetType": "heading"        // só quando elType = widget
}
```

As ferramentas do WSP MCP montam essa estrutura para você; você só envia `settings`.

## Formatos de valor (das classes de controle do Elementor)

| Tipo de controle | Formato |
|---|---|
| `text`, `textarea`, `wysiwyg`, `select`, `choose`, `color` | string |
| `switcher` | `"yes"` (ou o `return_value` indicado) / `""` |
| `number` | número |
| `slider` | `{ "unit": "px", "size": 24 }` |
| `dimensions` | `{ "top": "10", "right": "10", "bottom": "10", "left": "10", "unit": "px", "isLinked": true }` (strings) |
| `gaps` (ex.: `flex_gap`) | `{ "column": "20", "row": "20", "isLinked": true, "unit": "px" }` |
| `url` | `{ "url": "https://…", "is_external": "on" ou "", "nofollow": "on" ou "" }` |
| `media` | `{ "url": "https://…/img.jpg", "id": 123 }` |
| `icons` | `{ "value": "fas fa-star", "library": "fa-solid" }` (`fa-regular`, `fa-brands`) |
| `repeater` | array de objetos; cada item com `"_id": "<7 hex>"` |
| `gallery` | `[ { "id": 1, "url": "…" }, … ]` |
| `font` | nome da família (`"Inter"`) |

## Responsivo
Controle marcado "sim" na coluna *Resp.* aceita sufixos: `_tablet`, `_mobile` (e `_laptop`, `_tablet_extra`, `_mobile_extra`, `_widescreen` se ativados no site; veja `wsp_elementor_get_breakpoints`). Sem sufixo = desktop. Mobile herda do tablet, que herda do desktop.

## Cores e tipografia globais
Controles com "global padrão" já herdam do kit quando você não envia nada. Para ligar explicitamente:
```json
"__globals__": { "title_color": "globals/colors?id=primary", "typography_typography": "globals/typography?id=primary" }
```
IDs de sistema: cores `primary`, `secondary`, `text`, `accent`; tipografia `primary`, `secondary`, `text`, `accent`. Se `__globals__` tiver valor para uma chave, o global vence e o valor local é ignorado. Para usar um hex fixo num elemento que já está ligado a um global, envie também `"__globals__": { "<chave>": "" }` (lembrando que `__globals__` é substituído inteiro no `update_element`: reenvie as outras ligações).

## Opções de `choose`/`select` variam por widget (atenção)
Não presuma `left`/`right`: no Elementor 4 cada widget tem seu próprio conjunto. **Sempre copie o valor da coluna "Opções" do arquivo do widget.** Exemplos verificados no 4.4.0:
- `start`/`center`/`end`(/`justify`): `heading.align`, `text-editor.align`, `image.align`, `icon-box.text_align`, `image-box.text_align`, `testimonial.testimonial_alignment`, `star-rating.align`, `icon-list.icon_align`.
- `left`/`center`/`right`(/`justify`): `button.align`, `social-icons.align`, `divider.align`.
- `button.icon_align`: `row` (ícone antes) / `row-reverse` (ícone depois).
- `icon-box.position`: `block-start` (topo), `inline-start`, `inline-end`, `block-end`. Já `image-box.position`: `top`, `left`, `right`.
- Container: `width` só vale com `content_width: "full"`; com `"boxed"` use `boxed_width`.
- `flex_gap` é do tipo `gaps` (`column`/`row`), não slider.

## Elementor 4 "Atomic" (e-heading, e-button, div-block, flexbox…)
O Elementor 4 tem uma nova geração de elementos ("Atomic") com outro formato de dados (props tipadas `$$type` e estilos em classes). Ela vem **desligada por padrão** (experimento beta `e_atomic_elements`). O WSP MCP grava no formato clássico. **Use só os widgets clássicos desta pasta**; não crie `e-*`, `div-block` nem `flexbox` pelo WSP MCP.
