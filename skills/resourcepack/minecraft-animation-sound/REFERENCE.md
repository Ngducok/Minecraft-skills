# Evidence reference

Contracts describe intended applicability, not certified binary compatibility. Resolve exact version/build, toolchain and dependency coordinates. Inspect pinned APIs or native assets before using symbols/formats.

Source inspection checks documentation; it does not establish compile, runtime or client success. Rolling documentation may target a different release. Community design guidance and inferred balancing are not official mechanics.

## Sources

- [Display entities](https://docs.papermc.io/paper/dev/display-entities/) — registry ID `display`; inspected 2026-10-06. Displays provide visual transforms/interpolation; they do not automatically provide gameplay interaction or collision.
- [Adventure resource-pack delivery](https://docs.papermc.io/adventure/resource-pack/) — registry ID `packs`; inspected 2026-10-06. Pack delivery uses URLs, identities and statuses; status replies are client-controlled and are not an integrity proof.
- [Microsoft game contrast guidance](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/102) — registry ID `contrast-access`; inspected 2026-10-06. Contrast and non-color cues support readability and status recognition; screenshots alone do not establish full accessibility conformance.

Shared source records: [knowledge/sources.json](../../../knowledge/sources.json).
