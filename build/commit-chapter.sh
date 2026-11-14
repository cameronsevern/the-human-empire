#!/bin/sh
# Check that a chapter's images exist, then commit its folder.  usage: commit-chapter.sh chapters/NN-name
d=$1
for f in $(grep -o 'images/[^)]*' "$d/chapter.md"); do test -f "$d/$f" || { echo "MISSING $f"; exit 1; }; done
title=$(head -1 "$d/chapter.md" | sed 's/^# //')
git add "$d" && git commit -q -m "Chapter $title Checked and illustrated

Co-Authored-By: Claude Fable 5.2 <noreply@anthropic.com>" && git log --oneline -1
