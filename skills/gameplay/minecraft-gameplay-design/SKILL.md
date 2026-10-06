---
name: minecraft-gameplay-design
description: "Research or design Minecraft mechanics across survival, creative, adventure, PvP/PvE, minigames and technical play without imposing a genre."
---

# Gameplay contracts and mode selection

Translate the request into player goals, permitted actions, failure/recovery rules and persistence scope before selecting systems. Genre names are context, not implementation requirements.

- Identify what stays vanilla, what is configurable and what needs server/client code. Prefer a gamerule, datapack or existing plugin when it covers the goal.
- Define a short observable loop and test its first playable slice. Survival may need resource renewability; creative may need edit ownership; matches need lifecycle; adventure needs reachable objectives.
- Keep optional progression, currencies, rarity, classes and automation optional. Do not add them because a previous project used them.
- Research native mechanics on the target edition/runtime. Paper optimizations, modded rules and Bedrock differences can alter an apparently identical loop.
- Balance around actual time, risk, skill, fairness and accessibility for this mode. Borrow other games' patterns as hypotheses, not factual Minecraft rates.
- Route to only the relevant mechanic skills. No finite catalog proves coverage of every custom game; investigate unfamiliar rules before implementation.

## Verification

Run a representative player path from entry through success, failure and return. Document rules, measured results and untested mode/platform differences.

## Example request

Compare a vanilla survival extension and a round-based parkour game without assuming either needs RPG stats or money.

## Focused reference

Read [references/gameplay-matrix.md](references/gameplay-matrix.md) when handling the detailed cases above.

## Contract and evidence

Read [contract.json](contract.json) for applicability and required outputs; [REFERENCE.md](REFERENCE.md) for evidence and version limits. No listed verified release means resolve the target before generation. [tests/scenario.json](tests/scenario.json) contains a behavioral evaluation prompt, not proof that an agent passed.
