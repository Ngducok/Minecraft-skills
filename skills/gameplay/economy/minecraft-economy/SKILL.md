---
name: minecraft-economy
description: "Design and implement genre-neutral Minecraft currencies, prices and transactional trading."
---

# Economy

Identify currency provider, sources, sinks and unit of account before pricing. Estimate net emission per active player-hour under plausible automation; record assumptions and sensitivity, not guaranteed inflation. Calculate quantities and total cost server-side with bounded arithmetic. Validate balance, inventory capacity and offer revision at commit; prevent replay/duplication. Define rollback/recovery for debit-item delivery failure and avoid floating-point currency unless provider semantics require it. Simulate adversarial trading and restart recovery.

## Verification

Record inspected inputs, exact target and performed checks. Report unavailable build, runtime and client checks separately.


## Contract and evidence

Read [contract.json](contract.json) for applicability and required outputs; [REFERENCE.md](REFERENCE.md) for evidence and version limits. No listed verified release means resolve the target before generation. [examples/scenario.md](examples/scenario.md) contains a documented evaluation prompt, not proof that an agent passed.
