# Evidence reference

Contracts describe intended applicability, not certified binary compatibility. Resolve exact version/build, toolchain and dependency coordinates. Inspect pinned APIs or native assets before using symbols/formats.

Source inspection checks documentation; it does not establish compile, runtime or client success. Rolling documentation may target a different release. Community design guidance and inferred balancing are not official mechanics.

## Sources

- [MockBukkit author repository](https://github.com/MockBukkit/MockBukkit) — registry ID `mockbukkit`; inspected 2026-10-06. Mock API coverage does not prove packet behavior, native registries or client rendering.
- [Paper server requirements](https://docs.papermc.io/paper/getting-started/) — registry ID `paper-start`; inspected 2026-10-06. Version table separates Java 21-era Minecraft releases from Java 25-era releases; never copy current defaults into older targets.
- [Paper Dialog API](https://docs.papermc.io/paper/dev/dialogs/) — registry ID `dialog`; inspected 2026-10-06. Native Dialog bodies, inputs and custom callbacks are supported; implementation must be checked against target version.

Shared source records: [knowledge/sources.json](../../../knowledge/sources.json).
