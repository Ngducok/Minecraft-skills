# Evidence reference

Contracts describe intended applicability, not certified binary compatibility. Resolve exact version/build, toolchain and dependency coordinates. Inspect pinned APIs or native assets before using symbols/formats.

Source inspection checks documentation; it does not establish compile, runtime or client success. Rolling documentation may target a different release. Community design guidance and inferred balancing are not official mechanics.

## Sources

- [Paper Team API: versioned example](https://jd.papermc.io/paper/1.21.11/org/bukkit/scoreboard/Team.html) — registry ID `team`; inspected 2026-10-06. Presentation teams expose friendly-fire and collision options but do not replace authoritative group membership/permissions.
- [LuckPerms developer API](https://github.com/LuckPerms/LuckPerms/wiki/Developer-API) — registry ID `luckperms`; inspected 2026-10-06. Use provider APIs and context-sensitive permission queries; changes to account state need supported persistence.
- [WorldGuard protection queries](https://worldguard.enginehub.org/en/latest/developer/regions/protection-query/) — registry ID `worldguard`; inspected 2026-10-06. Use flag-aware protection queries; bypass handling is separate from region membership.
- [Using databases](https://docs.papermc.io/paper/dev/using-databases/) — registry ID `database`; inspected 2026-10-06. Embedded and standalone database choices differ; JDBC is an API and does not supply every database driver.
- [Safe dynamic MiniMessage replacements](https://docs.papermc.io/adventure/minimessage/dynamic-replacements/) — registry ID `minimessage`; inspected 2026-10-06. Use unparsed or component placeholders for untrusted strings rather than allowing formatting/action injection.

Shared source records: [knowledge/sources.json](../../../knowledge/sources.json).
