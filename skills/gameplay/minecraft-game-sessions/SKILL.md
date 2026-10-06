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

## Contract and evidence

Read [contract.json](contract.json) for applicability and required outputs; [REFERENCE.md](REFERENCE.md) for evidence and version limits. No listed verified release means resolve the target before generation. [tests/scenario.json](tests/scenario.json) contains a behavioral evaluation prompt, not proof that an agent passed.
