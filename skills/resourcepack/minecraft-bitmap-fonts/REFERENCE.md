# Evidence reference

Contracts describe intended applicability, not certified binary compatibility. Resolve exact version/build, toolchain and dependency coordinates. Inspect pinned APIs or native assets before using symbols/formats.

Source inspection checks documentation; it does not establish compile, runtime or client success. Rolling documentation may target a different release. Community design guidance and inferred balancing are not official mechanics.

## Sources

- [Paper Dialog API](https://docs.papermc.io/paper/dev/dialogs/) — registry ID `dialog`; inspected 2026-10-06. Native Dialog bodies, inputs and custom callbacks are supported; implementation must be checked against target version.
- [Java Edition 1.21.9 release notes](https://www.minecraft.net/en-us/article/minecraft-java-edition-1-21-9) — registry ID `release-1219`; inspected 2026-10-06. Official rolling documentation; resolve target release before using symbols.
- [Microsoft game text guidance](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/101) — registry ID `text-access`; inspected 2026-10-06. Readability depends on actual rendered size and display conditions, not only logical font size.

Shared source records: [knowledge/sources.json](../../../knowledge/sources.json).
