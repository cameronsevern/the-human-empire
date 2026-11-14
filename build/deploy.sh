#!/usr/bin/env bash
# Publish the built site/ folder to the gh-pages branch, which GitHub Pages serves.
#   python3 build/site.py && build/deploy.sh
# The branch holds one commit that is replaced each time, so old page images do not pile up.
set -euo pipefail
root="$(cd "$(dirname "$0")/.." && pwd)"
remote="$(git -C "$root" remote get-url origin)"
email="$(git -C "$root" config user.email)"; name="$(git -C "$root" config user.name)"
tmp="$(mktemp -d)"; trap 'rm -rf "$tmp"' EXIT
cp -r "$root/site/." "$tmp/"
touch "$tmp/.nojekyll"
cd "$tmp"
git init -q -b gh-pages
git config user.email "$email"; git config user.name "$name"
git add -A
git commit -q -m "Site as of $(date +%Y-%m-%d)"
git push -q --force "$remote" gh-pages
echo "published $(du -sh . | cut -f1) to gh-pages"
