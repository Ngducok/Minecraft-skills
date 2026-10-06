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

## Primary sources

Pin to the requested target release; rolling documentation may describe a newer API.

- [Paper AdvancementProgress: versioned example](https://jd.papermc.io/paper/1.21.11/org/bukkit/advancement/AdvancementProgress.html)
- [Scoreboard Objective](https://jd.papermc.io/paper/1.21.11/org/bukkit/scoreboard/Objective.html)
- [Paper event listeners](https://docs.papermc.io/paper/dev/event-listeners/)
- [Persistent data containers](https://docs.papermc.io/paper/dev/pdc/)
- [Using databases](https://docs.papermc.io/paper/dev/using-databases/)
