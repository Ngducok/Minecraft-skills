---
name: minecraft-data-generation
description: "Generate Minecraft recipes, tags, loot, language files and models using Fabric/NeoForge datagen or an existing deterministic asset pipeline."
---

# Versioned data generation and validation

Use the existing generator/build setup if present. Add datagen when repeated target-version schemas justify it; a small hand-authored file does not need a new generator framework.

- Select the correct registry lookup and provider APIs for the target loader/version. Keep generated output separate from hand-authored assets to avoid overwriting custom work.
- Make the input catalog authoritative for IDs and shared values. Validate references across recipes, tags, models, textures, languages and custom item definitions.
- Produce deterministic content and stable ordering; identify unavoidable ZIP timestamps separately from semantic changes.
- Detect generated/handwritten ID collisions and stale artifacts when catalog entries are removed. Do not delete arbitrary neighboring files as cleanup.
- Inspect logical side: assets are client presentation and data is server behavior. A generated recipe cannot repair a missing client model.
- Run the game's load/reload validation after schema checks. The generator compiling successfully only establishes provider execution, not that the target client/server accepts its output.

## Verification

Regenerate twice and compare semantic outputs. Remove one catalog item and verify only owned stale resources disappear. Load generated recipes/models on the matching game.

## Example request

Unify item definitions and recipes while keeping manually painted textures untouched.

## Primary sources

Pin to the requested target release; rolling documentation may describe a newer API.

- [Fabric data generation](https://docs.fabricmc.net/develop/data-generation/setup)
- [Paper recipes](https://docs.papermc.io/paper/dev/recipes/)
- [Paper data components](https://docs.papermc.io/paper/dev/data-component-api/)
