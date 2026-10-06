# Domain selection

Resolve context first. Use catalog.json to locate named skills. Read only relevant contracts and references. Host-specific invocation syntax is optional.


## automation

- `minecraft-coworker`: Collaborate with a human or another coding agent on Minecraft work using clear ownership, evidence, concise updates and reviewable handoffs.
- `minecraft-evidence`: Verify Minecraft APIs, formats, mechanics and tool availability; avoid fabricated symbols, citations, compatibility and test results.
- `minecraft-subagents`: Coordinate authorized Minecraft subagent research, implementation or review with bounded tasks, separate edit ownership and parent verification.

## commands

- `minecraft-commands-permissions`: Implement Minecraft commands, arguments, suggestions and server-side permission checks on Paper or equivalent command platforms.

## core

- `minecraft-dependency-detection`: Resolve installed dependencies, pinned API artifacts and build-tool compatibility without speculative additions.
- `minecraft-platform-detection`: Distinguish Java server platforms, proxies, mod loaders and Bedrock execution environments.
- `minecraft-project-context`: Resolve project context before Minecraft changes. Inspect existing architecture, requested outcome and trust boundaries.
- `minecraft-scheduling`: Fix Minecraft scheduling, asynchronous I/O, task cancellation or Paper/Folia thread-ownership bugs.
- `minecraft-version-compatibility`: Select compatible Minecraft versions, loaders, Java toolchains and APIs when starting, upgrading or diagnosing a Minecraft project.
- `minecraft-version-detection`: Detect exact Minecraft releases, loader builds, Java and content formats from project artifacts.

## data

- `minecraft-configuration`: Add or migrate Minecraft plugin/mod configuration, catalogs, probability tables and feature flags safely.
- `minecraft-inventory-transactions`: Implement Minecraft item transfers, crafting commits, loadout swaps, trades and optional economy effects with loss/duplication protection.
- `minecraft-persistence`: Design or repair Minecraft player, island, item and transaction persistence, migrations and recovery after restart or crash.
- `minecraft-recipes-loot`: Implement Minecraft crafting, furnace/processing recipes or loot tables while preserving custom item identity and preventing value loops.

## datapack

- `minecraft-datapacks`: Create or debug Minecraft Java datapacks, functions, tags, predicates, advancements and target-version data registries.

## debugging

- `minecraft-performance`: Diagnose Minecraft tick lag, memory growth or plugin throughput using reproducible profiling and bounded workload design.

## deployment

- `minecraft-release-recovery`: Prepare Minecraft plugin/mod/pack releases, server upgrades, compatible data migrations and tested rollback plans.

## gameplay

- `minecraft-crafting-automation`: Implement or debug Minecraft crafting, redstone interactions, processing queues and storage logistics using native mechanics where possible.
- `minecraft-creative-building`: Build Minecraft creative/building workflows, selection tools, blueprints, batch edits and undo with ownership and bounded world changes.
- `minecraft-entity-ai`: Implement Minecraft mob/NPC/pet behavior, navigation, spawning and entity lifecycle on the chosen plugin/mod/add-on platform.
- `minecraft-exploration-content`: Implement Minecraft exploration routes, structures, encounters, discoveries and renewable resource locations without assuming a mining or RPG server.
- `minecraft-game-sessions`: Build Minecraft lobbies, queues, matches, rounds, spectator flows and isolated game sessions with reliable cleanup.
- `minecraft-gameplay-design`: Research or design Minecraft mechanics across survival, creative, adventure, PvP/PvE, minigames and technical play without imposing a genre.
- `minecraft-items-equipment`: Implement Minecraft item identities, equipment effects, durability, consumables, optional rarity and item lifecycle across gameplay modes.
- `minecraft-movement-abilities`: Implement Minecraft parkour, checkpoints, dashes, flight, mounts, teleportation and cooldown abilities with server-authoritative rules.
- `minecraft-survival-simulation`: Tune Minecraft survival simulation, growth, breeding, spawning, hunger, weather and renewable resources while preserving target-runtime behavior.
- `minecraft-teams-social`: Build Minecraft parties, teams, guilds, cooperative ownership and role changes with authoritative membership and scoped access.

## gameplay/combat

- `minecraft-combat-rules`: Implement Minecraft PvP/PvE damage, equipment effects, friendly fire, attribution and encounter rules without assuming an RPG stat system.

## gameplay/economy

- `minecraft-economy`: Design and implement genre-neutral Minecraft currencies, prices and transactional trading.

## gameplay/farming

- `minecraft-farming`: Implement optional plant or livestock systems without imposing farming on other game modes.

## gameplay/progression

- `minecraft-progression-objectives`: Build Minecraft objectives, achievements, quests, scores, unlocks and reward balance for persistent or session-based games.

## gameplay/quests

- `minecraft-quests`: Implement optional objectives and quest state with idempotent completion and recovery.

## integrations

- `minecraft-crossplay`: Assess or implement Java/Bedrock crossplay with Geyser/Floodgate, custom item mappings and equivalent player interactions.
- `minecraft-permission-providers`: Integrate LuckPerms or existing Minecraft permission services, contextual access and temporary/admin grants.
- `minecraft-plugin-apis`: Integrate existing Minecraft economy, island, protection or content plugins without redundant services or unsafe lifecycle assumptions.
- `minecraft-proxy-security`: Configure or debug Minecraft Velocity/Bungee-style proxy identity forwarding and protected backend connections.

## modding

- `minecraft-bedrock-addons`: Create or debug Minecraft Bedrock behavior/resource packs and Script API add-ons; not Java datapacks or Paper plugins.
- `minecraft-data-generation`: Generate Minecraft recipes, tags, loot, language files and models using Fabric/NeoForge datagen or an existing deterministic asset pipeline.
- `minecraft-network-payloads`: Design or debug Fabric/NeoForge custom network payloads, menu synchronization and validated client requests.

## modding/fabric

- `minecraft-fabric-mod`: Create or maintain Fabric Minecraft Java mods, registries, entrypoints and client/server code separation.

## modding/forge

- `minecraft-forge-mod`: Build Forge mods using version-matched MDK, registries, event buses and physical-side separation.

## modding/neoforge

- `minecraft-neoforge-mod`: Create or port NeoForge Minecraft Java mods, registries, event buses, data attachments and distribution-specific behavior.

## operations

- `minecraft-hosting`: Set up or debug Minecraft server startup, local/public resource-pack hosting, ports, scripts and restart behavior on Windows or Linux.

## resourcepack

- `minecraft-animation-sound`: Add or assess resource-pack texture animation, display-entity interpolation, menu motion and gameplay sound feedback.
- `minecraft-bitmap-fonts`: Create resource-pack font glyphs, custom GUI panels, icons or debug glyph advances, clipping and clickable text bounds.
- `minecraft-item-models`: Implement custom Minecraft Java item visuals, item-model definitions, texture atlases or model-selection components.
- `minecraft-pack-delivery`: Build, host or debug Minecraft Java resource-pack metadata, URLs, hashes, required-pack status and client compatibility.

## routing

- `minecraft-agent`: Route broad Minecraft development and research tasks to edition-appropriate platform, gameplay, UI, asset and operations skills.
- `minecraft-task-classifier`: Classify Minecraft tasks into platforms, content, UI, mechanics or operations and select a minimal skill set.

## server/paper

- `minecraft-paper-plugin`: Create or maintain Bukkit/Paper plugins, plugin descriptors, service boundaries and startup/shutdown behavior.

## server/purpur

- `minecraft-purpur-plugin`: Develop Purpur features while distinguishing inherited Paper APIs and Purpur-specific behavior.

## server/spigot

- `minecraft-spigot-plugin`: Build Spigot/Bukkit plugins with target-specific APIs and descriptors.

## server/velocity

- `minecraft-velocity-plugin`: Implement Velocity proxy plugins and secure proxy/backend integration.

## testing

- `minecraft-testing`: Test Minecraft plugin/mod/data changes with pure checks, matching isolated runtimes and real-client validation where needed.

## ui

- `minecraft-hud-localization`: Implement Minecraft sidebars, boss/action bars, item tooltips, rarity styling or localization with Adventure components.

## ui/dialog

- `minecraft-dialog-ui`: Build or debug Minecraft Java Dialog screens, custom actions, forms and resource-pack-backed Dialog artwork.

## ui/interactive

- `minecraft-menu-ux`: Review Minecraft menus, selectors, loadouts, crafting screens, shops and settings for readable state and reliable input.

## ui/inventory

- `minecraft-inventory-ui`: Create chest-style Minecraft menus or fix click, drag, shift-click and inventory-transfer behavior.

## worldbuilding

- `minecraft-claims`: Implement Minecraft island/region authorization or integrate protection checks for building, harvesting, fluids, entities and machines.
- `minecraft-map-design`: Design or validate Minecraft maps, arenas, hubs, adventure levels, creative plots and starter spaces for the chosen gameplay.
- `minecraft-schematics`: Generate, inspect or convert .litematic, .schem and vanilla structure NBT files and verify their imported blocks/entities.
- `minecraft-world-generation`: Create Minecraft void/custom worlds, dimension generators or safely replace an existing playable world.
