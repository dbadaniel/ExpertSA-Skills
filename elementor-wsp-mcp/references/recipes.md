# Receitas de seções

Cada receita é uma sequência de chamadas. `<ID>` = `post_id`; `$nome` = `element_id` retornado por uma chamada anterior. Troque hex fixos por `__globals__` quando o kit tiver as cores certas.

---

## 1. Hero (título + subtítulo + 2 botões + imagem à direita)

```text
1) wsp_elementor_add_container
   { post_id:<ID>, settings:{
       content_width:"boxed", html_tag:"section",
       flex_direction:"row", flex_direction_mobile:"column",
       flex_align_items:"center",
       flex_gap:{column:"48",row:"32",isLinked:false,unit:"px"},
       min_height:{unit:"vh",size:85},
       padding:{top:"96",right:"24",bottom:"96",left:"24",unit:"px",isLinked:false},
       padding_mobile:{top:"56",right:"20",bottom:"56",left:"20",unit:"px",isLinked:false},
       background_background:"classic", background_color:"#0f172a" } }
   → $hero

2) wsp_elementor_add_container  { post_id:<ID>, parent_id:$hero, settings:{
       content_width:"full", width:{unit:"%",size:55}, width_mobile:{unit:"%",size:100},
       flex_direction:"column", flex_gap:{column:"20",row:"20",isLinked:true,unit:"px"} } }
   → $heroText

3) wsp_elementor_add_container  { post_id:<ID>, parent_id:$hero, settings:{
       content_width:"full", width:{unit:"%",size:45}, width_mobile:{unit:"%",size:100} } }
   → $heroMedia

4) wsp_elementor_add_widget heading → container_id:$heroText
   { title:"Título forte com a promessa principal", header_size:"h1", title_color:"#ffffff",
     typography_typography:"custom",
     typography_font_size:{unit:"px",size:56}, typography_font_size_mobile:{unit:"px",size:36},
     typography_font_weight:"800", typography_line_height:{unit:"em",size:1.1} }

5) wsp_elementor_add_widget text-editor → container_id:$heroText
   { editor:"<p>Subtítulo que explica para quem é e qual o resultado.</p>", text_color:"#cbd5e1",
     typography_typography:"custom", typography_font_size:{unit:"px",size:20} }

6) wsp_elementor_add_container  { post_id:<ID>, parent_id:$heroText, settings:{
       content_width:"full", flex_direction:"row", flex_wrap:"wrap", flex_gap:{column:"12",row:"12",isLinked:true,unit:"px"} } }
   → $heroCtas

7) wsp_elementor_add_widget button → container_id:$heroCtas
   { text:"Quero começar", link:{url:"#contato"}, size:"lg",
     background_background:"classic", background_color:"#22c55e", button_text_color:"#0f172a",
     border_radius:{top:"8",right:"8",bottom:"8",left:"8",unit:"px",isLinked:true} }

8) wsp_elementor_add_widget button → container_id:$heroCtas
   { text:"Ver como funciona", link:{url:"#como-funciona"}, size:"lg",
     background_background:"classic", background_color:"rgba(255,255,255,0)",
     button_text_color:"#ffffff", border_border:"solid",
     border_width:{top:"1",right:"1",bottom:"1",left:"1",unit:"px",isLinked:true}, border_color:"#ffffff" }

9) (imagem) wsp_upload_media_from_url { url:"..." } → {id, url}
   wsp_elementor_add_widget image → container_id:$heroMedia
   { image:{url:"...", id:<attachment_id>}, image_size:"large",
     image_border_radius:{top:"16",right:"16",bottom:"16",left:"16",unit:"px",isLinked:true} }
```

## 2. Grade de benefícios (3 colunas de icon-box)

```text
1) add_container raiz { content_width:"boxed", html_tag:"section", flex_direction:"column",
     flex_align_items:"center", padding:{top:"80",right:"24",bottom:"80",left:"24",unit:"px",isLinked:false} } → $feat
2) add_widget heading → $feat { title:"Por que escolher a gente", header_size:"h2", align:"center" }
3) add_container → parent $feat { content_width:"full", flex_direction:"row", flex_direction_mobile:"column", flex_wrap:"wrap",
     flex_gap:{column:"24",row:"24",isLinked:true,unit:"px"} } → $grid
4) Para cada benefício (3x):
   add_container → parent $grid { content_width:"full", width:{unit:"%",size:31}, width_mobile:{unit:"%",size:100},
     padding:{top:"32",right:"24",bottom:"32",left:"24",unit:"px",isLinked:false},
     background_background:"classic", background_color:"#f8fafc",
     border_radius:{top:"12",right:"12",bottom:"12",left:"12",unit:"px",isLinked:true} } → $card
   add_widget icon-box → $card { selected_icon:{value:"fas fa-bolt",library:"fa-solid"},
     title_text:"Rápido", description_text:"Explicação curta do benefício.", position:"block-start", text_align:"start", primary_color:"#22c55e" }
```
Atalho: monte o primeiro card completo e use `wsp_elementor_duplicate_element` 2x; depois `update_element` só em `title_text`/`description_text`/`selected_icon` de cada clone (pegue os IDs com `get_page`).

## 3. Faixa de CTA

```text
add_container raiz { content_width:"boxed", flex_direction:"row", flex_direction_mobile:"column",
  flex_justify_content:"space-between", flex_align_items:"center",
  padding:{top:"56",right:"40",bottom:"56",left:"40",unit:"px",isLinked:false},
  background_background:"gradient", background_color:"#4f46e5", background_color_b:"#7c3aed",
  background_gradient_angle:{unit:"deg",size:135} } → $cta
add_widget heading → $cta { title:"Pronto para começar?", header_size:"h2", title_color:"#ffffff" }
add_widget button  → $cta { text:"Falar no WhatsApp", link:{url:"https://wa.me/55...", is_external:"on"},
  background_background:"classic", background_color:"#ffffff", button_text_color:"#4f46e5", size:"lg" }
```

## 4. Depoimentos

Container raiz coluna + heading → container linha com wrap (`content_width:"full"`) → 3x container-card (`content_width:"full"`, width 31% / mobile 100%) → widget `testimonial` em cada card `{ testimonial_content, testimonial_name, testimonial_job, testimonial_image }`. Mesmo atalho de duplicar o primeiro card.

## 5. FAQ

```text
add_container raiz { content_width:"boxed", boxed_width:{unit:"px",size:800}, flex_direction:"column",
  padding:{top:"80",right:"24",bottom:"80",left:"24",unit:"px",isLinked:false} } → $faq
add_widget heading   → $faq { title:"Perguntas frequentes", header_size:"h2", align:"center" }
add_widget accordion → $faq { tabs:[
  {_id:"f1a2b3c", tab_title:"Pergunta 1?", tab_content:"<p>Resposta 1.</p>"},
  {_id:"d4e5f6a", tab_title:"Pergunta 2?", tab_content:"<p>Resposta 2.</p>"} ] }
```

## 6. Rodapé simples (dentro da página, para template canvas)

Container raiz `html_tag:"footer"`, fundo escuro, linha com `space-between` → containers filhos (`content_width:"full"`): esquerdo com heading (marca) + text-editor (descrição) → container direito com `icon-list` (`view:"inline"`, links) e `social-icons`. Segunda linha com `divider` + text-editor centralizado "© 2026 …".

---

## Âncoras e navegação
Para o botão `#contato` funcionar, defina `_element_id:"contato"` no container raiz da seção de destino (a chave é a mesma em containers e widgets).

## Checklist final de uma página
- [ ] Todo container-filho com `width` tem `content_width:"full"`.
- [ ] Valores de `align`/`position` copiados do arquivo do widget em `elementor/widgets/`.
- [ ] `get_page` bate com o plano (ordem, aninhamento).
- [ ] Todos os títulos grandes têm `_mobile`.
- [ ] Todas as linhas com colunas têm `flex_direction_mobile:"column"` ou largura 100% no mobile.
- [ ] Botões com link real (sem `#` solto).
- [ ] Imagens com `id` de mídia (não só URL externa).
- [ ] `regenerate_css` rodado; links de preview e do editor entregues.
- [ ] Página continua em rascunho, a menos que o usuário tenha pedido publicar.
