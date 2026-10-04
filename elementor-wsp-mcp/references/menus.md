# Menus e cabeçalho

Um "problema no menu" pode estar em três lugares diferentes. Descubra qual **antes** de chamar ferramentas.

| Sintoma | Camada | Onde corrigir |
|---|---|---|
| Item com nome/link errado, falta item, ordem errada, submenu | **Itens** (menu do WordPress) | Ferramentas `wsp_*menu*` |
| Aparece o menu errado / menu vazio / sumiu | **Ligação** (qual menu está no local do tema, ou qual menu o widget usa) | `wsp_assign_menu_location` ou setting `menu` do widget |
| Cor, fonte, espaçamento, hover, alinhamento, hambúrguer/dropdown no mobile | **Visual** (widget de menu no template de cabeçalho do Elementor) | `wsp_elementor_*` no ID do template |

## 1. Itens do menu (WordPress)

Primeira chamada, quase sempre: **`wsp_get_menus`**. Ela devolve todos os menus com `id`, `name`, `slug`, `item_count` e `locations` (locais do tema onde estão ligados). Com isso você já sabe qual menu é o do cabeçalho.

```text
wsp_get_menus → { menus: [ { id: 12, name: "Principal", slug: "principal", item_count: 6, locations: ["primary"] } ] }
wsp_get_menu_items { menu: 12 } → { items: [ { id, title, url, parent, order, type, object, object_id, target, classes } ] }
```

- Renomear / trocar link / mover: `wsp_update_menu_item { item_id, title?, url?, parent?, order? }`. Só os campos enviados mudam.
- Submenu: `parent` = `id` do item pai (0 = nível de cima). `order` = posição (1, 2, 3…).
- Adicionar: `wsp_add_menu_item { menu, type, title?, url?, object_id?, parent?, order? }`.
  - `type: "custom"` precisa de `title` + `url` (links externos, âncoras `#contato`, WhatsApp).
  - `type: "page"` / `"post"` / `"category"` precisa de `object_id` (ID da página/post/categoria). O tipo tem que bater com o objeto, senão dá erro.
- Remover: `wsp_delete_menu_item { item_id }` — apaga definitivo, sem lixeira. Confirme com o usuário.
- Itens de página (`type: "post_type"`) usam o título da página se `title` estiver vazio, e o link segue a página automaticamente. Para trocar o destino de um item de página, apague e crie outro (o `update` não muda `object_id`).
- **Não dá pelo MCP:** abrir em nova aba (`target`), classes CSS, descrição do item, ícones de menu. Diga ao usuário que é em Aparência → Menus → Opções de tela.

## 2. Ligação: qual menu aparece

- Menu do tema (cabeçalho do tema, não do Elementor): `wsp_get_menu_locations` → `wsp_assign_menu_location { location: "primary", menu: 12 }`.
- Widget de menu do Elementor Pro (`nav-menu`): o setting `menu` guarda o **slug** do menu (ex.: `"principal"`). Confirme com `wsp_elementor_get_widget_schema { widget_type: "nav-menu" }` (uma vez) e corrija com `update_element { settings: { menu: "<slug>" } }`.
- Widget "Menu do WordPress" (Elementor grátis, `widgetType: "wp-widget-nav_menu"`): o menu fica em `settings.wp.nav_menu` (ID). Como `wp` é um objeto, envie-o completo.

## 3. Visual do menu (template de cabeçalho)

O cabeçalho feito no Elementor é um **template** do Theme Builder (Elementor Pro), não parte da página.

```text
1) wsp_elementor_list_templates { type: "header" }  → [{ id: 345, title: "Cabeçalho", type: "header" }]
2) wsp_elementor_find_element { post_id: 345, widget_type: "nav-menu" }  → [{ id: "8f2a1c3d", ... }]
3) wsp_elementor_get_element { post_id: 345, element_id: "8f2a1c3d" }    → settings atuais
4) wsp_elementor_get_widget_schema { widget_type: "nav-menu" }           → só se a chave necessária não estiver nos settings atuais
5) wsp_elementor_update_element { post_id: 345, element_id: "8f2a1c3d", settings: { ...só o que muda... } }
6) wsp_elementor_regenerate_css (se mudou estilo)
```

- Se `list_templates {type:"header"}` vier vazio: tente `list_templates` sem `type` (alguns sites salvam como `section`) e procure pelo título. Se ainda não houver, o cabeçalho é do **tema**: o visual não é editável pelo MCP (fica em Aparência → Personalizar). Diga isso ao usuário e ofereça corrigir os itens.
- Às vezes o menu está dentro da própria página (landing pages com template Canvas). Nesse caso use `find_element { post_id: <página>, widget_type: "nav-menu" }`.
- Ao mudar o cabeçalho, a mudança vale para o site inteiro (todas as páginas que usam esse template). Avise o usuário.
- Se o usuário disser só "o menu está quebrado", faça **uma** pergunta curta para saber a camada (ex.: "É o texto/link de algum item, ou a aparência, como cor, alinhamento ou o menu no celular?") em vez de investigar as três.

## Erros comuns
| Mensagem | Causa |
|---|---|
| `Menu not found.` | `menu` aceita ID, slug ou nome; confira com `wsp_get_menus`. |
| `Menu item not found.` | `item_id` é o `id` do item (de `get_menu_items`), não o ID da página. |
| `object_id: page not found.` | `type` não bate com o objeto (ex.: `type: "page"` com ID de post). |
| `Unknown theme location` | Use um `location` listado em `wsp_get_menu_locations`. |
| Ferramenta de menu não existe | Ligue o grupo "Menus" em MCP → Settings (plugin ≥ 2.9.0). |
