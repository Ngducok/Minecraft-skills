---
name: minecraft-task-classifier
description: "Classify Minecraft tasks into platforms, content, UI, mechanics or operations and select a minimal skill set."
---

# Task Classifier

First determine requested outcome: plugin/mod, content pack, world asset, player interaction, mechanics, diagnosis or deployment. Select core context and evidence guidance, then only the relevant platform and feature skills. Farming, economy and quests are optional mechanics, never defaults. Mixed tasks may need separate client/server targets. Read contracts before generation; empty verified_versions means no pre-certified release. Do not load every skill or treat routing as compatibility proof.

## Verification

Record inspected inputs, exact target and performed checks. Report unavailable build, runtime and client checks separately.


## Contract and evidence

Read [contract.json](contract.json) for applicability and required outputs; [REFERENCE.md](REFERENCE.md) for evidence and version limits. No listed verified release means resolve the target before generation. [examples/scenario.md](examples/scenario.md) contains a documented evaluation prompt, not proof that an agent passed.
