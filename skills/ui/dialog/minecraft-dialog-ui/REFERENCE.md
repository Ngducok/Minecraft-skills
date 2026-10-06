# Evidence reference

Contracts describe intended applicability, not certified binary compatibility. Resolve exact version/build, toolchain and dependency coordinates. Inspect pinned APIs or native assets before using symbols/formats.

Source inspection checks documentation; it does not establish compile, runtime or client success. Rolling documentation may target a different release. Community design guidance and inferred balancing are not official mechanics.

## Sources

- [Paper Dialog API](https://docs.papermc.io/paper/dev/dialogs/) — registry ID `dialog`; inspected 2026-10-06. Native Dialog bodies, inputs and custom callbacks are supported; implementation must be checked against target version.
- [Adventure resource-pack delivery](https://docs.papermc.io/adventure/resource-pack/) — registry ID `packs`; inspected 2026-10-06. Pack delivery uses URLs, identities and statuses; status replies are client-controlled and are not an integrity proof.
- [Microsoft game text guidance](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/101) — registry ID `text-access`; inspected 2026-10-06. Readability depends on actual rendered size and display conditions, not only logical font size.

Shared source records: [knowledge/sources.json](../../../../knowledge/sources.json).
