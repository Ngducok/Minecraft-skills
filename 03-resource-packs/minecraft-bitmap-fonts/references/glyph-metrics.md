# Bitmap glyph geometry

Use when artwork wraps, clips, drifts or occupies a smaller hit area than expected.

Measure texture dimensions, provider row/column cells, nontransparent pixel bounds,
configured render height/ascent and actual cursor advance separately. Their values
are not interchangeable. Transparent padding may affect the visible center while
the renderer computes a different advance; inspect the target implementation or
measure a test glyph before relying on a formula.

Build a small diagnostic line with a baseline marker and one glyph at a time.
Compare visible left/right/top/bottom edges against native text and button bounds.
Test nonsquare artwork, sparse alpha, first/last cells and multiple GUI scales.
Large negative spacing can move pixels without making those pixels clickable.

Use namespaced font keys and stable private-use codepoints. Ensure every provider
row has the same number of codepoints and the texture divides into intended cells.
Check release-specific atlas/render limits before increasing texture size. Avoid
global replacement of the default font merely to draw one menu.

Record measured height, ascent, advance and alpha center in an asset-local fixture.
Reload the pack and inspect the client log; JSON parsing alone cannot prove visual
alignment or that the intended pack/font is active.
