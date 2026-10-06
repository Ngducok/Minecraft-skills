# Evidence reference

Contracts describe intended applicability, not certified binary compatibility. Resolve exact version/build, toolchain and dependency coordinates. Inspect pinned APIs or native assets before using symbols/formats.

Source inspection checks documentation; it does not establish compile, runtime or client success. Rolling documentation may target a different release. Community design guidance and inferred balancing are not official mechanics.

## Sources

- [VaultAPI author repository](https://github.com/MilkBowl/VaultAPI) — registry ID `vault`; inspected 2026-10-06. Vault bridges economy providers; withdrawal responses and provider availability must be checked.
- [BentoBox documentation](https://docs.bentobox.world/en/latest/) — registry ID `bentobox`; inspected 2026-10-06. Existing island/blueprint infrastructure should be evaluated before writing a complete island platform.
- [WorldGuard protection queries](https://worldguard.enginehub.org/en/latest/developer/regions/protection-query/) — registry ID `worldguard`; inspected 2026-10-06. Use flag-aware protection queries; bypass handling is separate from region membership.
- [Paper plugin descriptors](https://docs.papermc.io/paper/dev/plugin-yml/) — registry ID `plugin-yml`; inspected 2026-10-06. Plugin metadata, API compatibility, commands and permission defaults belong in the correct descriptor.

Shared source records: [knowledge/sources.json](../../../knowledge/sources.json).
