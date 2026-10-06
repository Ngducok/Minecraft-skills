---
name: minecraft-recipes-loot
description: "Implement Minecraft crafting, furnace/processing recipes or loot tables while preserving custom item identity and preventing value loops."
---

# Recipes, loot and item provenance

Decide whether the task needs native data recipes, a plugin registration or modded recipe machinery. Keep one authoritative output definition and an explicit ingredient acceptance rule.

- Use namespaced recipe keys and inspect exact-choice/component matching support on the target. Matching only Material may accept renamed, forged or economically distinct items.
- Define catalyst, container remainder, durability and output-stack behavior. Shift-craft, recipe-book and automated crafting paths need the same restrictions as a manual craft.
- Build a value graph: inputs, outputs, by-products, buy/sell prices and time. Check cycles for item duplication and positive-profit conversion without meaningful cost.
- Keep loot probability, count ranges, conditions and attribution separate. Decide which roll occurs per entity, block, chest generation or player; reopening storage must not reroll loot.
- Avoid mixing a plugin replacement drop with still-enabled vanilla output. Select the authoritative event/loot mechanism and handle cancelled or protected actions.

## Verification

Test bulk crafting, container remainders, invalid custom ingredients, output capacity and repeatable loot access. Verify quantities and a no-profit buy/craft/sell cycle where required.

## Example request

Add a custom crop-processing recipe without allowing ordinary renamed wheat or shift-craft duplication.

## Contract and evidence

Read [contract.json](contract.json) for applicability and required outputs; [REFERENCE.md](REFERENCE.md) for evidence and version limits. No listed verified release means resolve the target before generation. [examples/scenario.md](examples/scenario.md) contains a documented evaluation prompt, not proof that an agent passed.
