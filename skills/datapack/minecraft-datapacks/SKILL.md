---
name: minecraft-datapacks
description: "Create or debug Minecraft Java datapacks, functions, tags, predicates, advancements and target-version data registries."
---

# Java datapack development

Identify Minecraft release, datapack format and intended loading mechanism before writing files. Datapacks modify server data; resource packs supply assets. Bedrock behavior-pack instructions are a different system.

- Use namespaced IDs and target-version folder names/schema. Old plural directory conventions, execute syntax and item NBT examples may be incompatible with a newer release.
- Separate one-time initialization from recurring work. Tick functions need bounded selectors and scoped tags; never scan every entity for a small local mechanic.
- Design repeatability around reload and world restart. Scoreboards, storage and tags must initialize without erasing progress or duplicating rewards.
- Prefer native predicates, recipes, loot and advancements when they express the rule. Use a plugin/mod for persistence or interactions the datapack cannot implement reliably.
- Keep datapack enablement and plugin discovery lifecycle explicit. Do not silently replace another pack's registry entries; identify pack priority and namespace conflicts.

## Verification

Load on a disposable matching world, inspect parsing logs and list enabled packs. Exercise load/tick functions twice, reload and restart without duplicating state.

## Example request

Port an old datapack to a newer release without resetting player quest state.

## Contract and evidence

Read [contract.json](contract.json) for applicability and required outputs; [REFERENCE.md](REFERENCE.md) for evidence and version limits. No listed verified release means resolve the target before generation. [tests/scenario.json](tests/scenario.json) contains a behavioral evaluation prompt, not proof that an agent passed.
