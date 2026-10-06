---
name: minecraft-dialog-ui
description: "Build or debug Minecraft Java Dialog screens, custom actions, forms and resource-pack-backed Dialog artwork."
---

# Native Dialog menus

Confirm the target client and server expose the needed Dialog API. Choose native bodies/inputs/buttons first; bitmap-font composition is a deliberate visual workaround, not a general browser UI system.

- Define entry, browsing, quantity, review, commit and exit states. Derive every label and total from the same current selection.
- Bind callbacks to player identity, session/version and bounded lifetime. Recheck permission, item identity, price and capacity at execution; stale or replayed callbacks must not trade again.
- Preserve native focus/keyboard behavior where possible. Identify client-owned warning and layout controls instead of promising arbitrary pixel positioning or mouse tracking.
- Avoid repeated close/open or scheduled redraws for animation; verify actual cursor behavior when replacing a Dialog. Use native interpolation only on surfaces that support it.
- For custom font panels, measure advances, row height, centering and drawable hit bounds. Click testing must include tile corners, empty tile space and text itself.

## Verification

Check native creation and stale actions on a matching server. Review an actual client at relevant GUI scales, including Escape, pointer movement and pack failure. Artwork previews are separate evidence.

## Example request

A resource-pack Dialog only responds when its text is clicked; align drawable hit bounds with the intended card.

## Focused reference

Read [references/dialog-review.md](references/dialog-review.md) when handling the detailed cases above.

## Contract and evidence

Read [contract.json](contract.json) for applicability and required outputs; [REFERENCE.md](REFERENCE.md) for evidence and version limits. No listed verified release means resolve the target before generation. [tests/scenario.json](tests/scenario.json) contains a behavioral evaluation prompt, not proof that an agent passed.
