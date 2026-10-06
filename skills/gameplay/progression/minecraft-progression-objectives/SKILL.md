---
name: minecraft-progression-objectives
description: "Build Minecraft objectives, achievements, quests, scores, unlocks and reward balance for persistent or session-based games."
---

# Objectives, rewards and progression

Choose objective scope and evidence: player, team, match, world or account. Keep native advancements/scoreboards when they cover the goal; persistent XP and currency are optional.

- Define success conditions and observable server events. UI text or client claims must not establish completion.
- Reacquire advancement progress after datapack reload; do not retain references whose underlying advancement can be replaced.
- Distinguish criteria state from reward settlement. One-time, repeatable and round-scoped rewards need different identity/reset rules.
- Make progression reachable after failure, disconnect and team changes. Do not build mandatory daily gates or economic sinks into unrelated games.
- Balance time, challenge, risk and reward using measured scenarios. If currency exists, separate minted/burned resources from transfers; otherwise model scores, materials or unlocks.
- Detect replayed completion, farming one's own alternate targets and reset-based duplication where those paths affect the requested objective.
- Explain next actions and progress clearly without assuming a fixed language, rarity palette or RPG leveling scheme.

## Verification

Test partial completion, repeated events, disconnect, simultaneous team completion and reset. Model fastest and typical reward paths and verify exactly the intended settlement scope.

## Example request

Add adventure checkpoints and round scores without granting duplicate rewards after reconnect.

## Focused reference

Read [references/reward-cases.md](references/reward-cases.md) when handling the detailed cases above.

## Contract and evidence

Read [contract.json](contract.json) for applicability and required outputs; [REFERENCE.md](REFERENCE.md) for evidence and version limits. No listed verified release means resolve the target before generation. [examples/scenario.md](examples/scenario.md) contains a documented evaluation prompt, not proof that an agent passed.
