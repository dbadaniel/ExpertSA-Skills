#!/usr/bin/env bash
# Regenera references/elementor/ a partir de um checkout do repositório elementor/elementor.
# Uso: ./run.sh /caminho/para/elementor   (requer php >= 8.1 e python3)
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
export ELEMENTOR_SRC="$(cd "${1:?informe o caminho do repositório do Elementor}" && pwd)"
export WORK="$(mktemp -d)"; export OUT="$HERE/../../references/elementor"
export EVER="$(grep -m1 'Version:' "$ELEMENTOR_SRC/elementor.php" | awk '{print $NF}')"
python3 "$HERE/gen_stubs.py"
W="$ELEMENTOR_SRC/includes"
php "$HERE/run.php" "$W/widgets/common-base.php" "$W/elements/container.php" "$W/elements/section.php" "$W/elements/column.php" \
  $(ls "$W"/widgets/*.php | grep -v -e common -e html.php) > "$WORK/out_all.json" 2> "$WORK/err.txt" || true
php "$HERE/run_groups.php" > "$WORK/groups.json" 2>> "$WORK/err.txt" || true
grep -v id_base "$WORK/err.txt" || true
mkdir -p "$OUT/widgets"; python3 "$HERE/gen.py"
echo "Referência regenerada para Elementor $EVER em $OUT"
