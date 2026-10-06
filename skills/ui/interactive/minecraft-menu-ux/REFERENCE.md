# Evidence reference

Contracts describe intended applicability, not certified binary compatibility. Resolve exact version/build, toolchain and dependency coordinates. Inspect pinned APIs or native assets before using symbols/formats.

Source inspection checks documentation; it does not establish compile, runtime or client success. Rolling documentation may target a different release. Community design guidance and inferred balancing are not official mechanics.

## Sources

- [Paper Dialog API](https://docs.papermc.io/paper/dev/dialogs/) — registry ID `dialog`; inspected 2026-10-06. Native Dialog bodies, inputs and custom callbacks are supported; implementation must be checked against target version.
- [Custom InventoryHolders](https://docs.papermc.io/paper/dev/custom-inventory-holder/) — registry ID `inventory`; inspected 2026-10-06. Menu identity can be carried by a holder rather than guessed from display titles.
- [Microsoft game text guidance](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/101) — registry ID `text-access`; inspected 2026-10-06. Readability depends on actual rendered size and display conditions, not only logical font size.
- [Microsoft game contrast guidance](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/102) — registry ID `contrast-access`; inspected 2026-10-06. Contrast and non-color cues support readability and status recognition; screenshots alone do not establish full accessibility conformance.

Shared source records: [knowledge/sources.json](../../../../knowledge/sources.json).
