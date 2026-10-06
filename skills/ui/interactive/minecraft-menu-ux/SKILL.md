---
name: minecraft-menu-ux
description: "Review Minecraft menus, selectors, loadouts, crafting screens, shops and settings for readable state and reliable input."
---

# Menu usability across gameplay modes

Identify what the player is trying to accomplish and the actual rendering surface. Support the requested mode without assuming a shop, currency, rarity palette or fixed layout.

- Use recognizable names and distinguish available, hovered, focused, selected and disabled states with more than color. Keep long/localized names readable at supported GUI scales.
- Make card artwork and actual clickable area agree. Verify empty card space, edges, keyboard activation and controller/touch equivalents when applicable.
- Keep action labels, selected options and consequences derived from the same state. Quantities, costs, teams or loadouts must update together when those concepts exist.
- Choose explicit navigation appropriate to the content; arrows should communicate page versus scroll movement. Preserve selection or reset it visibly.
- Prefer stable native input over repeated screen recreation. Animation must not recenter the pointer, interrupt activation or hide commit state.
- Make cancel/exit semantics match the operation. Leaving a settings form, item escrow or match queue can have different cleanup requirements.

## Verification

Test first-use recognition, long names, rapid option changes, pointer corners, denied actions and exit on real supported clients. Report screenshot review separately from input testing.

## Example request

Redesign a team/loadout picker without turning it into a currency shop.

## Focused reference

Read [references/menu-review.md](references/menu-review.md) when handling the detailed cases above.

## Contract and evidence

Read [contract.json](contract.json) for applicability and required outputs; [REFERENCE.md](REFERENCE.md) for evidence and version limits. No listed verified release means resolve the target before generation. [examples/scenario.md](examples/scenario.md) contains a documented evaluation prompt, not proof that an agent passed.
