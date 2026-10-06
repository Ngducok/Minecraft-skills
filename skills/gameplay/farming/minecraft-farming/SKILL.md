---
name: minecraft-farming
description: "Implement optional plant or livestock systems without imposing farming on other game modes."
---

# Farming

Define lifecycle and ownership before adding growth or yield rules. Inspect vanilla mechanics on the target platform; account for chunk unload, server downtime, random ticks and offline limits. Treat metadata quality, mutation or weight as server-owned state and persist it before value transfer. Cap production assumptions, avoid per-plant synchronous tasks and test deterministic seeds, harvest duplication and restart. Keep economy integration optional.

## Verification

Record inspected inputs, exact target and performed checks. Report unavailable build, runtime and client checks separately.


## Contract and evidence

Read [contract.json](contract.json) for applicability and required outputs; [REFERENCE.md](REFERENCE.md) for evidence and version limits. No listed verified release means resolve the target before generation. [examples/scenario.md](examples/scenario.md) contains a documented evaluation prompt, not proof that an agent passed.
