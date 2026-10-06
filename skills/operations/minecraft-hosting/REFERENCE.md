# Evidence reference

Contracts describe intended applicability, not certified binary compatibility. Resolve exact version/build, toolchain and dependency coordinates. Inspect pinned APIs or native assets before using symbols/formats.

Source inspection checks documentation; it does not establish compile, runtime or client success. Rolling documentation may target a different release. Community design guidance and inferred balancing are not official mechanics.

## Sources

- [Paper server requirements](https://docs.papermc.io/paper/getting-started/) — registry ID `paper-start`; inspected 2026-10-06. Version table separates Java 21-era Minecraft releases from Java 25-era releases; never copy current defaults into older targets.
- [Adventure resource-pack delivery](https://docs.papermc.io/adventure/resource-pack/) — registry ID `packs`; inspected 2026-10-06. Pack delivery uses URLs, identities and statuses; status replies are client-controlled and are not an integrity proof.
- [Velocity backend security](https://docs.papermc.io/velocity/security/) — registry ID `velocity-security`; inspected 2026-10-06. Offline backend authentication requires network isolation and trusted forwarding; forwarding alone is not a firewall.

Shared source records: [knowledge/sources.json](../../../knowledge/sources.json).
