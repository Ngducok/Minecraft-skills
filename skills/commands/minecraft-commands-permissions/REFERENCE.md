# Evidence reference

Contracts describe intended applicability, not certified binary compatibility. Resolve exact version/build, toolchain and dependency coordinates. Inspect pinned APIs or native assets before using symbols/formats.

Source inspection checks documentation; it does not establish compile, runtime or client success. Rolling documentation may target a different release. Community design guidance and inferred balancing are not official mechanics.

## Sources

- [Paper command registration](https://docs.papermc.io/paper/dev/command-api/basics/registration/) — registry ID `commands`; inspected 2026-10-06. Lifecycle registration supports Brigadier commands; classic descriptors and Paper bootstrapping are distinct choices.
- [Paper plugin descriptors](https://docs.papermc.io/paper/dev/plugin-yml/) — registry ID `plugin-yml`; inspected 2026-10-06. Plugin metadata, API compatibility, commands and permission defaults belong in the correct descriptor.
- [Safe dynamic MiniMessage replacements](https://docs.papermc.io/adventure/minimessage/dynamic-replacements/) — registry ID `minimessage`; inspected 2026-10-06. Use unparsed or component placeholders for untrusted strings rather than allowing formatting/action injection.

Shared source records: [knowledge/sources.json](../../../knowledge/sources.json).
