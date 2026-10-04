# Regenerar a referência do Elementor

A pasta `references/elementor/` foi gerada a partir do código-fonte oficial do Elementor. Quando sair uma versão nova, regenere:

```bash
git clone --depth 1 https://github.com/elementor/elementor.git
./run.sh ./elementor
```

Requer `php` (8.1+) e `python3`. Nada é instalado e nenhum WordPress é necessário: o script carrega os arquivos de widget com dublês mínimos das classes do Elementor/WordPress e registra cada `add_control`, `add_responsive_control` e `add_group_control` que eles chamam.

Arquivos:
- `gen_stubs.py`: gera os dublês, lendo constantes reais (`Controls_Manager`, cores/tipografia globais, breakpoints) do repositório.
- `base.php.inc`: classes base que capturam os controles.
- `wp.php`: funções do WordPress usadas durante o registro.
- `run.php` / `run_groups.php`: executam o registro de widgets/elementos e de grupos e exportam JSON.
- `gen.py`: transforma o JSON nos arquivos Markdown.

Os widgets `html` e `shortcode` são ignorados de propósito (o WSP MCP bloqueia esses tipos).
