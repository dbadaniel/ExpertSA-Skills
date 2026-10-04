# Cheatsheet rápido (verificado contra o Elementor 4.4.0)

Resumo dos settings mais usados. A referência completa e gerada do código-fonte está em `elementor/` (um arquivo por widget, mais `container.md`, `advanced-common.md`, `groups.md`). Formatos de valor, responsivo e globais: `elementor/README.md`.

## Regras que mais causam erro silencioso
1. Grupo precisa do interruptor: `typography_typography: "custom"`, `background_background: "classic"`, `border_border: "solid"`, `box_shadow_box_shadow_type: "yes"`.
2. Container-filho usado como coluna: `content_width: "full"` + `width`. Com `boxed`, `width` é ignorado.
3. Containers usam `padding`/`margin`; widgets usam `_padding`/`_margin`.
4. Opções de alinhamento variam por widget (`start`/`end` em uns, `left`/`right` em outros). Copie do arquivo do widget.
5. Objetos aninhados e repeaters são substituídos inteiros no `update_element`.

## Container
```json
{
  "content_width": "boxed",                       // "boxed" | "full"
  "boxed_width": { "unit": "px", "size": 1140 },  // só com boxed
  "width": { "unit": "%", "size": 50 },           // só com full
  "min_height": { "unit": "vh", "size": 80 },
  "flex_direction": "row",                        // row | column | row-reverse | column-reverse  (resp.)
  "flex_direction_mobile": "column",
  "flex_justify_content": "space-between",        // flex-start | center | flex-end | space-between | space-around | space-evenly
  "flex_align_items": "center",                   // flex-start | center | flex-end | stretch
  "flex_gap": { "column": "24", "row": "24", "isLinked": true, "unit": "px" },
  "flex_wrap": "wrap",                            // nowrap | wrap
  "padding": { "top": "80", "right": "24", "bottom": "80", "left": "24", "unit": "px", "isLinked": false },
  "background_background": "classic",
  "background_color": "#0f172a",
  "border_radius": { "top": "12", "right": "12", "bottom": "12", "left": "12", "unit": "px", "isLinked": true },
  "html_tag": "section"                           // div | header | footer | main | article | section | aside | nav | a
}
```
Grid: `container_type: "grid"` + `grid_columns_grid {unit:"fr", size:3}`, `grid_rows_grid`, `grid_gaps` (ver `elementor/container.md` e `groups.md`).
Gradiente: `background_background:"gradient"`, `background_color`, `background_color_b`, `background_gradient_angle {unit:"deg",size:135}`.
Imagem de fundo: `background_image {url,id}`, `background_position:"center center"`, `background_size:"cover"`, `background_repeat:"no-repeat"`; overlay: `background_overlay_background:"classic"`, `background_overlay_color`, `background_overlay_opacity {size:0.6}`.
Sombra: `box_shadow_box_shadow_type:"yes"`, `box_shadow_box_shadow {horizontal:0,vertical:10,blur:30,spread:0,color:"rgba(0,0,0,.12)"}`.
Filho de container flex (aba Avançado): `_flex_size: "grow"` / `"none"` / `"custom"`, `_flex_align_self`, `_flex_order`.

## Aba Avançado de widgets
`_margin`, `_padding` (dimensões), `_element_width` (`""`, `"inherit"`, `"auto"`, `"initial"`) + `_element_custom_width`, `_element_id` (âncora), `_css_classes`, `_z_index`, `_background_background` + `_background_color`, `_border_border`… Lista completa: `elementor/advanced-common.md`.

## Widgets

| Widget | Conteúdo | Estilo principal |
|---|---|---|
| `heading` | `title`, `header_size` (`h1`…`h6`,`div`,`span`,`p`), `link` | `align` (`start`/`center`/`end`/`justify`), `title_color`, `typography_*` |
| `text-editor` | `editor` (HTML simples) | `align` (`start`/`center`/`end`/`justify`), `text_color`, `link_color`, `typography_*`, `paragraph_spacing` |
| `button` | `text`, `link`, `size` (`xs`/`sm`/`md`/`lg`/`xl`), `selected_icon`, `icon_align` (`row`/`row-reverse`), `icon_indent` | `align` (`left`/`center`/`right`/`justify`), `button_text_color`, `background_background`+`background_color`, `hover_color`, `button_background_hover_background`+`button_background_hover_color`, `border_border`, `border_radius`, `text_padding`, `typography_*` |
| `image` | `image {url,id}`, `image_size` (`full`/`large`/`medium`/`thumbnail`), `link_to` (`none`/`file`/`custom`), `link`, `caption_source` | `align` (`start`/`center`/`end`), `width`, `height`, `object-fit`, `image_border_radius`, `image_box_shadow_*` |
| `icon` | `selected_icon`, `view` (`default`/`stacked`/`framed`), `link` | `align`, `primary_color`, `size` |
| `icon-box` | `selected_icon`, `title_text`, `description_text`, `link`, `title_size` | `position` (`block-start`/`inline-start`/`inline-end`/`block-end`), `text_align` (`start`/`center`/`end`/`justify`), `primary_color`, `title_color`, `description_color`, `title_typography_*`, `description_typography_*` |
| `image-box` | `image`, `title_text`, `description_text`, `link` | `position` (`top`/`left`/`right`), `text_align`, `title_color`, `description_color` |
| `icon-list` | `view` (`traditional`/`inline`), `icon_list[]` {`_id`,`text`,`selected_icon`,`link`} | `space_between`, `icon_color`, `text_color`, `icon_align` |
| `spacer` | `space {unit:"px",size:40}` | — |
| `divider` | `style`, `width`, `look`, `text` | `align` (`left`/`center`/`right`), `color`, `weight`, `gap` |
| `testimonial` | `testimonial_content`, `testimonial_image`, `testimonial_name`, `testimonial_job`, `testimonial_image_position` | `testimonial_alignment` (`start`/`center`/`end`), `content_content_color`, `name_text_color`, `job_text_color` |
| `accordion` / `toggle` | `tabs[]` {`_id`,`tab_title`,`tab_content`}, `faq_schema` | `title_color`, `tab_active_color`, `content_color`, `border_color`, `icon_align` (`left`/`right`) |
| `tabs` | `tabs[]` {`_id`,`tab_title`,`tab_content`}, `type` (`horizontal`/`vertical`) | `tab_color`, `tab_active_color`, `content_color` |
| `counter` | `starting_number`, `ending_number`, `prefix`, `suffix`, `title`, `duration` | `number_color`, `title_color`, `typography_number_*`, `typography_title_*` |
| `progress` | `title`, `percent {unit:"%",size:80}`, `inner_text`, `display_percentage` | `bar_color`, `bar_bg_color`, `bar_height` |
| `social-icons` | `social_icon_list[]` {`_id`,`social_icon`,`link`}, `shape` (`square`/`rounded`/`circle`) | `align` (`left`/`center`/`right`), `icon_color` (`default`/`custom`) + `icon_primary_color`, `icon_size`, `icon_spacing` |
| `video` | `video_type` (`youtube`/`vimeo`/`dailymotion`/`hosted`…), `youtube_url`, `autoplay`/`mute`/`loop` (`"yes"`), `image_overlay` | `aspect_ratio` (`169`, `43`, `11`…) |
| `google_maps` | `address`, `zoom {size:14}` | `height {unit:"px",size:400}` |
| `image-carousel` | `carousel[]` {`id`,`url`}, `slides_to_show` (`"3"`), `navigation` (`both`/`arrows`/`dots`/`none`), `autoplay` | `image_spacing`, `arrows_color`, `dots_color` |
| `star-rating` | `rating_scale`, `rating`, `star_style`, `title` | `align`, `stars_color`, `icon_size` |
| `alert` | `alert_type` (`info`/`success`/`warning`/`danger`), `alert_title`, `alert_description` | `title_color`, `description_color` |

Widgets Pro (form, posts, nav-menu, slides, price-table, call-to-action, countdown, flip-box…): não estão no repositório gratuito. Use `wsp_elementor_get_widget_schema`.

## Bloqueados pelo WSP MCP
Tipos `html`, `shortcode`, `code`, `code-highlight`; chaves `custom_css`, `_attributes`, `custom_attributes`, `__dynamic__` (são removidas em qualquer nível, inclusive dentro de `link`); `<script>`, `<style>`, `<iframe>` e `on*=` nos textos.
