---
name: minecraft-hud-localization
description: "Implement Minecraft sidebars, boss/action bars, item tooltips, rarity styling or localization with Adventure components."
---

# HUD, tooltips and localized text

Choose the native surface by urgency and interaction: persistent scoreboard, transient action bar, progress boss bar or item-specific tooltip. Do not promise arbitrary placement from vanilla APIs.

- Keep semantic state server-side and presentation separate. Display stable labels and changed values rather than recreating every objective/team each tick.
- Use existing objective/team ownership conventions to avoid fighting another HUD plugin. Respect the target client's line limits and available number-format APIs.
- Pair rarity color with a written rarity or symbol. Put item name, useful properties and value in a stable hierarchy; hide implementation keys from player-facing lore.
- Choose client translations versus server rendering deliberately. Check locale fallback, format arguments and missing custom pack keys; preserve an explicit single-language requirement.
- Insert user text through literal/components or unparsed placeholders. Restrict executable click/hover actions to trusted templates. Tooltip skins require target-version sprite/nine-slice validation.

## Verification

Test missing translation, long labels, pack disabled and competing scoreboard updates. Measure readability at actual scale and verify color is not the sole rarity/status cue.

## Example request

Show region-specific farming progress without replacing another plugin scoreboard or exposing untranslated keys.

## Primary sources

Pin to the requested target release; rolling documentation may describe a newer API.

- [Scoreboard Objective](https://jd.papermc.io/paper/1.21.11/org/bukkit/scoreboard/Objective.html)
- [Adventure localization](https://docs.papermc.io/adventure/localization/)
- [Safe dynamic MiniMessage replacements](https://docs.papermc.io/adventure/minimessage/dynamic-replacements/)
- [Microsoft game contrast guidance](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/102)
