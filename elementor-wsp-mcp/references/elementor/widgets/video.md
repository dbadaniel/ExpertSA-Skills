# Widget `video`

Gerado do código-fonte do Elementor 4.4.0 (`video.php`). O site pode ter outra versão: em caso de dúvida, confirme com `wsp_elementor_get_widget_schema`.


## Conteúdo › Video

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `video_type` | select |  | `youtube`, `vimeo`, `dailymotion`, `videopress`, `hosted` | "youtube" |  |
| `youtube_url` | text |  |  | "https://www.youtube.com/watch?v=XHOmBV4js_E" | {"video_type": "youtube"} |
| `vimeo_url` | text |  |  | "https://vimeo.com/235215203" | {"video_type": "vimeo"} |
| `dailymotion_url` | text |  |  | "https://www.dailymotion.com/video/x6tqhqb" | {"video_type": "dailymotion"} |
| `insert_url` | switcher |  |  |  | {"video_type": ["hosted", "videopress"]} |
| `hosted_url` | media |  |  |  | {"video_type": ["hosted", "videopress"], "insert_url": ""} |
| `external_url` | url |  |  |  | {"video_type": "hosted", "insert_url": "yes"} |
| `videopress_url` | text |  |  | "https://videopress.com/v/ZCAOzTNk" | {"video_type": "videopress", "insert_url": "yes"} |
| `start` | number |  |  |  |  |
| `end` | number |  |  |  | {"video_type": ["youtube", "hosted"]} |
| `autoplay` | switcher |  |  |  |  |
| `play_on_mobile` | switcher |  |  |  | {"autoplay": "yes"} |
| `mute` | switcher |  |  |  |  |
| `loop` | switcher |  |  |  | {"video_type!": "dailymotion"} |
| `controls` | switcher |  |  | "yes" | {"video_type!": "vimeo"} |
| `showinfo` | switcher |  |  | "yes" | {"video_type": ["dailymotion"]} |
| `cc_load_policy` | switcher |  |  |  | {"video_type": ["youtube"], "controls": "yes"} |
| `logo` | switcher |  |  | "yes" | {"video_type": ["dailymotion"]} |
| `yt_privacy` | switcher |  |  |  | {"video_type": ["youtube", "vimeo"]} |
| `lazy_load` | switcher |  |  |  |  |
| `rel` | select |  | ``, `yes` |  | {"video_type": "youtube"} |
| `vimeo_title` | switcher |  |  | "yes" | {"video_type": "vimeo"} |
| `vimeo_portrait` | switcher |  |  | "yes" | {"video_type": "vimeo"} |
| `vimeo_byline` | switcher |  |  | "yes" | {"video_type": "vimeo"} |
| `color` | color |  |  |  | {"video_type": ["vimeo", "dailymotion"]} |
| `download_button` | switcher |  |  |  | {"video_type": "hosted"} |
| `preload` | select |  | `metadata`, `auto`, `none` | "metadata" | {"video_type": "hosted", "autoplay": ""} |
| `poster` | media |  |  |  | {"video_type": "hosted"} |

## Conteúdo › Image Overlay

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `show_image_overlay` | switcher |  |  |  |  |
| `image_overlay_*` | **grupo image-size** (ver groups.md) | | Chaves: `image_overlay_size`, `image_overlay_custom_dimension` | | {"show_image_overlay": "yes"} |
| `show_play_icon` | switcher |  |  | "yes" | {"show_image_overlay": "yes", "image_overlay[url]!": ""} |
| `play_icon` | icons |  |  |  | {"show_image_overlay": "yes", "show_play_icon!": ""} |
| `lightbox` | switcher |  |  |  | {"show_image_overlay": "yes", "image_overlay[url]!": ""} |

## Estilo › Video

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `aspect_ratio` | select |  | `169`, `219`, `43`, `32`, `11`, `916` | "169" |  |
| `css_filters_*` | **grupo css-filter** (ver groups.md) | | liga com `css_filters_css_filter: "custom"`. Chaves: `css_filters_blur`, `css_filters_brightness`, `css_filters_contrast`, `css_filters_saturate`, `css_filters_hue` | |  |

## Estilo › Image Overlay

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `play_icon_color` | color |  |  |  | {"show_image_overlay": "yes", "show_play_icon": "yes"} |
| `play_icon_size` | slider | sim | units: px,em,rem,custom |  | {"show_image_overlay": "yes", "show_play_icon": "yes"} |
| `play_icon_text_shadow_*` | **grupo text-shadow** (ver groups.md) | | liga com `play_icon_text_shadow_text_shadow_type: "yes"`. Chaves: `play_icon_text_shadow_text_shadow` | | {"show_image_overlay": "yes", "show_play_icon": "yes", "play_icon[libr… |

## Estilo › Lightbox

| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |
|---|---|---|---|---|---|
| `lightbox_color` | color |  |  |  |  |
| `lightbox_ui_color` | color |  |  |  |  |
| `lightbox_ui_color_hover` | color |  |  |  |  |
| `lightbox_content_animation` | animation | sim |  |  |  |
| `lightbox_video_width` | slider |  | units: px,%,em,rem,vw,custom | {"unit": "%"} | {"lightbox_video_width!": "", "lightbox_content_position!": ""} |
| `lightbox_content_position` | select |  | ``, `top` |  | {"lightbox_video_width!": "", "lightbox_content_position!": ""} |
