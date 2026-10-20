#!/usr/bin/env bash
#
# Build The Final Transaction to a single PDF.
#
#   build/make-pdf.sh [output.pdf]
#
# Requires pandoc and tectonic (pandoc's --pdf-engine=tectonic). Tectonic
# fetches its TeX bundle on first run, so the first build needs a network
# connection; later builds are cached.

set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

out="${1:-$repo_root/build/the-final-transaction.pdf}"

# Page setup. The defaults give a comfortable measure (about 66 characters
# a line) and an airy leading, which is what a novel wants; a draft set in
# 11pt on narrow margins comes out far denser than the book is meant to be.
# Override any of these from the environment to retune the build.
fontsize="${FONTSIZE:-12pt}"
geometry="${GEOMETRY:-inner=1.8in, outer=1.45in, top=1.6in, bottom=1.7in}"

# Title-page metadata. Change these if the book is renamed or the author
# writes under a different name.
title="The Final Transaction"
subtitle="A Novel"
author="$(git -C "$repo_root" config user.name || echo "The Author")"
date="First draft"

# Pick a book serif that is actually installed, so the script works on any
# machine. Charter is the nicest of these for a novel; the rest are
# fallbacks. If none is found, pandoc uses the LaTeX default (Latin Modern).
font_candidates=(
  "Charter"
  "Palatino"
  "Athelas"
  "Baskerville"
  "Iowan Old Style"
  "Georgia"
  "Times New Roman"
  "DejaVu Serif"
  "Liberation Serif"
)

font_args=()
if command -v fc-list >/dev/null 2>&1; then
  for candidate in "${font_candidates[@]}"; do
    if fc-list ":family=$candidate" family | grep -qix "$candidate"; then
      font_args=(-V "mainfont=$candidate")
      echo "Using font: $candidate"
      break
    fi
  done
fi

pandoc "$repo_root"/manuscript/*.md \
  --from=markdown+smart \
  --to=pdf \
  --pdf-engine=tectonic \
  --top-level-division=chapter \
  --lua-filter="$repo_root/build/chapter-prefix.lua" \
  --include-in-header="$repo_root/build/header.tex" \
  --number-sections \
  --toc \
  --toc-depth=1 \
  -V documentclass=book \
  -V classoption=openany \
  -V classoption=twoside \
  -V secnumdepth=0 \
  -V papersize=a4 \
  -V fontsize="$fontsize" \
  "${font_args[@]}" \
  -V "geometry=$geometry" \
  -V title="$title" \
  -V subtitle="$subtitle" \
  -V author="$author" \
  -V date="$date" \
  -o "$out"

echo "Wrote $out"
