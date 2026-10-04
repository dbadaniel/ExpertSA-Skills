import json, os, re
D=json.load(open(os.environ['WORK']+'/out_all.json')); G=json.load(open(os.environ['WORK']+'/groups.json'))
OUT=os.environ['OUT']
os.makedirs(OUT+'/widgets',exist_ok=True)
UI={'heading','raw_html','divider','alert','deprecated_notice','notice','button','hidden','promotion_control','section','tab','tabs','popover_toggle'}
POP={'typography':('typography','custom'),'box-shadow':('box_shadow_type','yes'),'text-shadow':('text_shadow_type','yes'),'text-stroke':('text_stroke_type','yes'),'css-filter':('css_filter','custom')}
SW={'background':'background','border':'border'}
def j(v,n=90):
    s=json.dumps(v,ensure_ascii=False)
    return s if len(s)<=n else s[:n]+'…'
def esc(s): return str(s).replace('|','\\|').replace('\n',' ')
def opts(a):
    o=a.get('options')
    if isinstance(o,dict) and o: 
        ks=list(o.keys()); return ', '.join('`%s`'%k for k in ks[:14])+(' …' if len(ks)>14 else '')
    return ''
def cond(a):
    c=a.get('condition')
    if isinstance(c,dict) and c: return esc(j(c,70))
    return ''
def row(key,a,resp):
    t=a.get('type','')
    if t in UI and t!='hidden': return None
    if t=='hidden': return None
    d=a.get('default','')
    extra=[]
    if a.get('size_units'): extra.append('units: '+','.join(a['size_units']) if isinstance(a['size_units'],list) else '')
    if a.get('return_value') and t=='switcher': extra.append('ligado=`%s`'%a['return_value'])
    if a.get('global',{}).get('default'): extra.append('global padrão `%s`'%a['global']['default'])
    o=opts(a)
    return '| `%s` | %s | %s | %s | %s | %s |'%(key,t,'sim' if resp else '',esc(o+(' · ' if o and extra else '')+' · '.join(x for x in extra if x)),esc(j(d,60)) if d not in ('',None,[],{}) else '',cond(a))
def group_line(c):
    gt=c['kind'].split(':',1)[1]; name=c['id']; a=c['args']
    keys=[k for k in G.get(gt,{}).keys() if not k.startswith('_')]
    exc=a.get('exclude',[]) or []
    keys=[k for k in keys if k not in exc]
    sw=''
    if gt in POP: sw='liga com `%s_%s: "%s"`'%(name,POP[gt][0],POP[gt][1])
    elif gt in SW: sw='liga com `%s_%s` (%s)'%(name,SW[gt], '"classic"/"gradient"' if gt=='background' else '"solid"/"dashed"/…')
    shown=[k for k in keys if k not in (SW.get(gt),)]
    if gt=='background': shown=[k for k in shown if not k.startswith(('slideshow','video','play_','privacy'))][:14]
    ks=', '.join('`%s_%s`'%(name,k) for k in shown)
    return '| `%s_*` | **grupo %s** (ver groups.md) | | %sChaves: %s | | %s |'%(name,gt,(sw+'. ') if sw else '',ks,cond(a))
HDR='| Chave | Tipo | Resp. | Opções / notas | Padrão | Condição |\n|---|---|---|---|---|---|'
TABN={'content':'Conteúdo','style':'Estilo','advanced':'Avançado','layout':'Layout'}
def render(title, ctrls, note=''):
    lines=['# %s\n'%title]
    if note: lines.append(note+'\n')
    cur=None
    for c in ctrls:
        sec=(c.get('tab') or 'content', (c.get('section') or {}).get('label','') )
        if sec!=cur:
            cur=sec; lines.append('\n## %s › %s\n\n%s'%(TABN.get(sec[0],sec[0]),esc(sec[1]),HDR))
        k=c['kind']; a=c['args']
        state=' (%s)'%c['state'] if c.get('state') else ''
        if k.startswith('group:'): lines.append(group_line(c)+(' '+state if state else '')); continue
        r=row(c['id'],a,k=='responsive' or a.get('responsive'))
        if not r: continue
        if state: r=r.replace('| `%s` |'%c['id'],'| `%s`%s |'%(c['id'],esc(state)),1)
        lines.append(r)
        if a.get('type')=='repeater' and isinstance(a.get('fields'),list):
            lines.append('\n**Itens do repeater `%s`** (cada item precisa de `_id` único de 7 hex):\n\n%s'%(c['id'],HDR))
            for f in a['fields']:
                fa=f.get('args',f) if isinstance(f,dict) else {}
                fid=f.get('id') or fa.get('name')
                if f.get('kind','').startswith('group:'): lines.append(group_line(f)); continue
                rr=row(fid,fa,f.get('kind')=='responsive')
                if rr: lines.append(rr)
            lines.append('\n'+HDR)
    txt='\n'.join(lines)
    txt=re.sub(r'\n\n'+re.escape(HDR)+r'(?=\n\n|\n*$)','',txt)
    return txt+'\n'
SKIP={'html','shortcode','sidebar','wp-widget-'}
index=[]
for cls,v in D.items():
    n=v.get('name')
    if cls.endswith('Container'): fn,title='container.md','Container (flexbox/grid) — `elType: "container"`'
    elif cls.endswith('Element_Section'): fn,title='legacy-section.md','Section (layout legado) — `elType: "section"`'
    elif cls.endswith('Element_Column'): fn,title='legacy-column.md','Column (layout legado) — `elType: "column"`'
    elif n=='common-base': fn,title='advanced-common.md','Aba Avançado comum a TODOS os widgets'
    elif n in ('common','common-optimized') or n in SKIP or not n: continue
    else: fn,title='widgets/%s.md'%n,'Widget `%s`'%n
    note='Gerado do código-fonte do Elementor '+os.environ.get('EVER','?')+' (`%s`). O site pode ter outra versão: em caso de dúvida, confirme com `wsp_elementor_get_widget_schema`.'%v['file']
    open(OUT+'/'+fn,'w').write(render(title,v['controls'],note))
    index.append((fn,n or cls,len(v['controls'])))
print('\n'.join('%s %s %d'%x for x in index))

# groups.md
GL=['# Grupos de controles (prefixo + campo)\n','Um grupo é um conjunto de chaves com prefixo comum. Se um widget tem o grupo `typography` com nome `title_typography`, as chaves ficam `title_typography_font_size`, `title_typography_font_weight` etc. O **interruptor** do grupo precisa ser enviado junto, senão o Elementor ignora os outros campos.\n',
'| Grupo | Interruptor (chave = `<nome>_<campo>`) |','|---|---|',
'| typography | `<nome>_typography: "custom"` |','| background | `<nome>_background: "classic"` ou `"gradient"` (ou `"video"`/`"slideshow"` em containers) |','| border | `<nome>_border: "solid"` (`dashed`, `dotted`, `double`, `groove`, `none`) |','| box-shadow | `<nome>_box_shadow_type: "yes"` |','| text-shadow | `<nome>_text_shadow_type: "yes"` |','| text-stroke | `<nome>_text_stroke_type: "yes"` |','| css-filter | `<nome>_css_filter: "custom"` |','| flex-container / grid-container / image-size / flex-item | sem interruptor |','']
for g,fields in G.items():
    GL.append('\n## %s\n\n%s'%(g,HDR))
    for k,a in fields.items():
        if k.startswith('_') or k.startswith(('slideshow','video','play_','privacy')): continue
        r=row('<nome>_'+k,a,a.get('responsive'))
        if r: GL.append(r)
open(OUT+'/groups.md','w').write('\n'.join(GL)+'\n')
