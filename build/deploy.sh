#!/usr/bin/env bash
# Publish the built site/ folder to the gh-pages branch, which GitHub Pages serves.
#   python3 build/site.py && build/deploy.sh
# The branch holds one commit that is replaced each time, so old page images do not pile up.
set -euo pipefail
root="$(cd "$(dirname "$0")/.." && pwd)"
remote="$(git -C "$root" remote get-url origin)"
email="$(git -C "$root" config user.email)"; name="$(git -C "$root" config user.name)"
# The PDF and EPUB of each released part go to the "downloads" release, outside the 1 GB limit on the site.
if ls "$root"/build/downloads/* >/dev/null 2>&1; then
  gh release view downloads -R cameronsevern/the-human-empire >/dev/null 2>&1 ||
    gh release create downloads -R cameronsevern/the-human-empire --target main --title "Downloads" \
      --notes "The PDF and EPUB of each released part of The Human Empire. These files are replaced whenever a part is rebuilt."
  gh release upload downloads -R cameronsevern/the-human-empire --clobber "$root"/build/downloads/*
fi
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
