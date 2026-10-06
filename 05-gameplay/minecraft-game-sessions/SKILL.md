---
name: minecraft-game-sessions
description: "Build Minecraft lobbies, queues, matches, rounds, spectator flows and isolated game sessions with reliable cleanup."
---

# Matches, rounds and session lifecycle

Separate account state, session membership and arena/world lifetime. Choose the smallest explicit state machine covering the requested game, such as waiting, active and ended.

- Define entry eligibility, team assignment, countdown, win/draw/abort rules and reconnect policy. Do not infer a competitive format when the game is cooperative.
- Scope timers, scores, callbacks and entities to a session ID/generation. Late tasks from a finished round must not affect its successor.
- Preserve player inventory, location, mode and other changed state according to the requested isolation contract. Persistent rewards and temporary kit state have different owners.
- Make completion and reward issuance idempotent. Simultaneous final events need one authoritative winner/settlement decision.
- Handle empty sessions, logout, plugin disable and failed reset with an explicit recovery path. Stop accepting entrants to an unsafe or half-reset arena.
- Coordinate spectators and visibility with server-side interaction rules; visual spectator treatment alone does not prevent interference.

## Verification

Test join/leave during countdown, simultaneous end conditions, reconnect, successive rounds and disable mid-round. Verify no leaked tasks, entities or temporary player state.

## Example request

Implement cooperative timed rounds that recover player state when the last participant disconnects.

## Focused reference

Read [references/session-cases.md](references/session-cases.md) when handling the detailed cases above.

## Primary sources

Pin to the requested target release; rolling documentation may describe a newer API.

- [Paper event listeners](https://docs.papermc.io/paper/dev/event-listeners/)
- [Paper scheduling](https://docs.papermc.io/paper/dev/scheduler/)
- [Using databases](https://docs.papermc.io/paper/dev/using-databases/)
- [Persistent data containers](https://docs.papermc.io/paper/dev/pdc/)
