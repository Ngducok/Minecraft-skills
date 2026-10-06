---
name: minecraft-purpur-plugin
description: "Develop Purpur features while distinguishing inherited Paper APIs and Purpur-specific behavior."
---

# Purpur Plugin

Pin exact Purpur build and upstream Paper version. Use Paper API for portable behavior; use Purpur API only when needed and declare that platform requirement. Inspect actual purpur.yml defaults rather than assume vanilla mechanics. Test requested behavior on Purpur, including restart and disabled-feature paths. Do not advertise Paper support for code importing Purpur-only symbols.

## Verification

Record inspected inputs, exact target and performed checks. Report unavailable build, runtime and client checks separately.


## Contract and evidence

Read [contract.json](contract.json) for applicability and required outputs; [REFERENCE.md](REFERENCE.md) for evidence and version limits. No listed verified release means resolve the target before generation. [tests/scenario.json](tests/scenario.json) contains a behavioral evaluation prompt, not proof that an agent passed.
