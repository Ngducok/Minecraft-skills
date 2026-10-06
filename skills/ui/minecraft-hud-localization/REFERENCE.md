# Evidence reference

Contracts describe intended applicability, not certified binary compatibility. Resolve exact version/build, toolchain and dependency coordinates. Inspect pinned APIs or native assets before using symbols/formats.

Source inspection checks documentation; it does not establish compile, runtime or client success. Rolling documentation may target a different release. Community design guidance and inferred balancing are not official mechanics.

## Sources

- [Scoreboard Objective](https://jd.papermc.io/paper/1.21.11/org/bukkit/scoreboard/Objective.html) — registry ID `scoreboard`; inspected 2026-10-06. Native scoreboard supplies objectives and display slots; arbitrary pixel positioning is not part of this interface.
- [Adventure localization](https://docs.papermc.io/adventure/localization/) — registry ID `localization`; inspected 2026-10-06. Client resource-pack translation and server translation differ; rendering policy must identify which side owns the text.
- [Safe dynamic MiniMessage replacements](https://docs.papermc.io/adventure/minimessage/dynamic-replacements/) — registry ID `minimessage`; inspected 2026-10-06. Use unparsed or component placeholders for untrusted strings rather than allowing formatting/action injection.
- [Microsoft game contrast guidance](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/102) — registry ID `contrast-access`; inspected 2026-10-06. Contrast and non-color cues support readability and status recognition; screenshots alone do not establish full accessibility conformance.

Shared source records: [knowledge/sources.json](../../../knowledge/sources.json).
