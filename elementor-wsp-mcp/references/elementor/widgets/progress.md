# Widget `progress`

Gerado do código-fonte do Elementor 4.4.0 (`progress.php`). O site pode ter outra versão: em caso de dúvida, confirme com `wsp_elementor_get_widget_schema`.


## Conteúdo › Progress Bar

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `title` | text |  |  | "My Skill" |  |
| `title_tag` | select |  | `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `div`, `span`, `p` | "span" | {"title!": ""} |
| `title_display` | switcher |  |  | "yes" | {"title!": ""} |
| `progress_type` | select |  | ``, `info`, `success`, `warning`, `danger` |  | {"progress_type!": ""} |
| `percent` | slider |  |  | {"size": 50, "unit": "%"} |  |
| `display_percentage` | switcher |  | ligado=`show` | "show" | {"percent!": ""} |
| `inner_text` | text |  |  | "Web Designer" |  |

## Estilo › Progress Bar

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `title_color` | color |  | global padrão `globals/colors?id=primary` |  | {"title!": ""} |
| `typography_*` | **grupo typography** (ver groups.md) | | liga com `typography_typography: "custom"`. Chaves: `typography_font_family`, `typography_font_size`, `typography_font_weight`, `typography_text_transform`, `typography_font_style`, `typography_text_decoration`, `typography_line_height`, `typography_letter_spacing`, `typography_word_spacing` | | {"title!": ""} |
| `title_shadow_*` | **grupo text-shadow** (ver groups.md) | | liga com `title_shadow_text_shadow_type: "yes"`. Chaves: `title_shadow_text_shadow` | | {"title!": ""} |
| `bar_color` | color |  | global padrão `globals/colors?id=primary` |  |  |
| `bar_bg_color` | color |  |  |  |  |
| `bar_height` | slider |  | units: px,em,rem,custom |  |  |
| `bar_border_radius` | slider |  | units: px,%,em,rem,custom |  |  |
| `bar_inline_color` | color |  |  |  | {"inner_text!": ""} |
| `bar_inner_typography_*` | **grupo typography** (ver groups.md) | | liga com `bar_inner_typography_typography: "custom"`. Chaves: `bar_inner_typography_font_family`, `bar_inner_typography_font_size`, `bar_inner_typography_font_weight`, `bar_inner_typography_text_transform`, `bar_inner_typography_font_style`, `bar_inner_typography_text_decoration`, `bar_inner_typography_letter_spacing`, `bar_inner_typography_word_spacing` | | {"inner_text!": ""} |
| `bar_inner_shadow_*` | **grupo text-shadow** (ver groups.md) | | liga com `bar_inner_shadow_text_shadow_type: "yes"`. Chaves: `bar_inner_shadow_text_shadow` | | {"inner_text!": ""} |
