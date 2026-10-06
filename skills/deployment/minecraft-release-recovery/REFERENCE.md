# Evidence reference

Contracts describe intended applicability, not certified binary compatibility. Resolve exact version/build, toolchain and dependency coordinates. Inspect pinned APIs or native assets before using symbols/formats.

Source inspection checks documentation; it does not establish compile, runtime or client success. Rolling documentation may target a different release. Community design guidance and inferred balancing are not official mechanics.

## Sources

- [Paper updates](https://docs.papermc.io/paper/updating/) — registry ID `update`; inspected 2026-10-06. Upgrade worlds and plugins with a restorable backup; source/build compatibility is separate from data compatibility.
- [Adventure resource-pack delivery](https://docs.papermc.io/adventure/resource-pack/) — registry ID `packs`; inspected 2026-10-06. Pack delivery uses URLs, identities and statuses; status replies are client-controlled and are not an integrity proof.
- [Minecraft usage guidelines](https://www.minecraft.net/en-us/usage-guidelines) — registry ID `usage`; inspected 2026-10-06. Review current first-party rules when the actual task concerns monetization, branding or distribution; no blanket legal clearance.

Shared source records: [knowledge/sources.json](../../../knowledge/sources.json).
