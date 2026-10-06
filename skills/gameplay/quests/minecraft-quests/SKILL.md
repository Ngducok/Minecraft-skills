---
name: minecraft-quests
description: "Implement optional objectives and quest state with idempotent completion and recovery."
---

# Quests

Define objective events, participant scope, repeatability, prerequisites and reward transaction. Store stable IDs and schema versions; display text is not identity. Count authorized events once, resist reconnect/party credit duplication and distinguish acceptance from completion. Persist completion/reward entitlement and define recovery if delivery fails. Test abandon, repeat, disconnect, multiplayer attribution and migration; do not force linear quests into sandbox play.

## Verification

Record inspected inputs, exact target and performed checks. Report unavailable build, runtime and client checks separately.


## Contract and evidence

Read [contract.json](contract.json) for applicability and required outputs; [REFERENCE.md](REFERENCE.md) for evidence and version limits. No listed verified release means resolve the target before generation. [examples/scenario.md](examples/scenario.md) contains a documented evaluation prompt, not proof that an agent passed.
