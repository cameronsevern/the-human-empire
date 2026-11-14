#!/usr/bin/env bash
# Generate the final illustration for one toolbox page with Codex's image tool.
# Usage: toolbox/draw/generate.sh 05-sickle sickle
# Reads toolbox/<dir>/prompt.txt (the subject and labels) and toolbox/draw/style.txt,
# attaches the code-drawn schematic toolbox/<dir>/<name>.png as the layout reference,
# and writes toolbox/<dir>/<name>-gen.png. Set CODEX_MODEL to use a different Codex model.
set -euo pipefail
dir=$1; name=$2
root=$(cd "$(dirname "$0")/.." && pwd)
style=$(cat "$root/draw/style.txt"); subject=$(cat "$root/$dir/prompt.txt")
codex exec ${CODEX_MODEL:+-m "$CODEX_MODEL"} -s workspace-write -C "$root" "Use your image generation tool to make ONE illustration and save it as the PNG file $dir/$name-gen.png (inside the current directory), replacing any existing file of that name. Do not create, edit or delete any other file. The attached image is a plain schematic of the same subject: keep its content, layout idea and label wording, but redraw it as a richer illustration. $style Subject: $subject" -i "$root/$dir/$name.png" < /dev/null
