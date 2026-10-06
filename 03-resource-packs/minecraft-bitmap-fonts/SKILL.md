---
name: minecraft-bitmap-fonts
description: "Create resource-pack font glyphs, custom GUI panels, icons or debug glyph advances, clipping and clickable text bounds."
---

# Bitmap fonts and glyph geometry

Inspect the target vanilla font providers and renderer limits before selecting glyph dimensions. Custom bitmap art has metrics; a visually transparent space is not automatically a drawable hit target.

- Track cell width/height, rendered height, ascent, alpha bounds and computed advance for every glyph. Do not assume square geometry or hardcode one atlas ceiling across versions.
- Split oversized art into supported cells and verify the exact sum of positive advances and negative spacing. Keep composed lines inside the native body's wrap width.
- Reserve namespaced fonts and private-use characters; inventory title, chat and Dialog layout apply different padding and line rules.
- Verify transparency thresholds, color multiplication, inherited shadow/italic and font fallback. Include complete and centered item art, with deliberate padding.
- Test labels with the actual font width table; localize before fitting. Use a small reusable overlay for repeated states instead of generating every combination of full-screen textures.

## Verification

Check atlas/cell bounds and expected advances programmatically. Render actual text/art and inspect native client clipping, wrap, focus and hit corners.

## Example request

A transparent font panel renders correctly but shifts every clickable area after the second glyph.

## Focused reference

Read [references/glyph-metrics.md](references/glyph-metrics.md) when handling the detailed cases above.

## Primary sources

Pin to the requested target release; rolling documentation may describe a newer API.

- [Paper Dialog API](https://docs.papermc.io/paper/dev/dialogs/)
- [Minecraft Java 1.21.9 pack changes](https://www.minecraft.net/en-us/article/minecraft-java-edition-1-21-9)
- [Microsoft game text guidance](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/101)
