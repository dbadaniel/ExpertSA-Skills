# Widget `star-rating`

Gerado do código-fonte do Elementor 4.4.0 (`star-rating.php`). O site pode ter outra versão: em caso de dúvida, confirme com `wsp_elementor_get_widget_schema`.


## Conteúdo › Star Rating

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `rating_scale` | select |  | `5`, `10` | "5" |  |
| `rating` | number |  |  | 5 |  |
| `star_style` | select |  | `star_fontawesome`, `star_unicode` | "star_fontawesome" |  |
| `unmarked_star_style` | choose |  | `solid`, `outline` | "solid" |  |
| `title` | text |  |  |  |  |
| `align` | choose | sim | `start`, `center`, `end`, `justify` |  |  |

## Estilo › Title

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `title_color` | color |  | global padrão `globals/colors?id=text` |  |  |
| `title_typography_*` | **grupo typography** (ver groups.md) | | liga com `title_typography_typography: "custom"`. Chaves: `title_typography_font_family`, `title_typography_font_size`, `title_typography_font_weight`, `title_typography_text_transform`, `title_typography_font_style`, `title_typography_text_decoration`, `title_typography_line_height`, `title_typography_letter_spacing`, `title_typography_word_spacing` | |  |
| `title_shadow_*` | **grupo text-shadow** (ver groups.md) | | liga com `title_shadow_text_shadow_type: "yes"`. Chaves: `title_shadow_text_shadow` | |  |
| `title_gap` | slider | sim | units: px,em,rem,custom |  |  |

## Estilo › Stars

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `icon_size` | slider | sim | units: px,em,rem,custom |  |  |
| `icon_space` | slider | sim | units: px,em,rem,custom |  |  |
| `stars_color` | color |  |  |  |  |
| `stars_unmarked_color` | color |  |  |  |  |
