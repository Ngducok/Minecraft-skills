# Dialog interaction review

Use when choosing Dialog layout or diagnosing mouse/focus complaints.

Separate client-owned controls, server callbacks and pack artwork. Resource packs
do not supply arbitrary JavaScript, CSS layouts or continuous mouse-coordinate
events. Verify native APIs against the actual client/server release.

Test the entire clickable rectangle, not only the text. Decorative glyph advance
does not prove the drawable pixels match button bounds. Compare corners, center,
keyboard activation and focus outline at multiple GUI scales. Do not remove native
focus affordances without an equally usable keyboard path.

Record cursor position before category, page and quantity changes. If updates
replace the screen, distinguish client recentering from layout drift. Prefer a
native state update when available; otherwise reduce transitions and explain the
limit. Texture animation can add visual motion but cannot fix screen recreation.

Check long names, unavailable pack, insufficient funds, capacity changes and stale
callbacks. ESC should exit when supported; exit must invalidate pending callbacks.
Treat screenshot alignment and successful client interaction as separate checks.
