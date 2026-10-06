---
name: minecraft-crossplay
description: "Assess or implement Java/Bedrock crossplay with Geyser/Floodgate, custom item mappings and equivalent player interactions."
---

# Geyser and cross-edition compatibility

Treat protocol bridging and visual/interaction parity as separate problems. Determine Java backend, Geyser/Floodgate builds, Bedrock clients and supported login/identity policy.

- Provide Bedrock pack assets and mappings deliberately; a Java resource pack is not automatically translated. Check the current custom-item mapping API version.
- Build a capability matrix for menus, input, custom blocks/items, tooltips and animations. Native Java-only Dialog behavior requires verification or an alternate flow for Bedrock players.
- Keep server-side inventory/economy rules identical across editions. Client presentation differences do not justify weaker validation.
- Resolve linked/unlinked identities with the installed authentication APIs. Do not guess Floodgate accounts solely from a username prefix.
- Test touch/controller input and limited screen space, not only mouse. Design an equivalent action path when a visual trick relies on Java font metrics.
- Handle pack acceptance/readiness through the correct edition's delivery path. Report missing parity explicitly rather than saying crossplay support is complete because login works.

## Verification

Run Java and Bedrock clients through purchase, sale, reconnect and custom item interactions. Inspect both pack logs and mapping failures.

## Example request

A Java custom crop shop needs a usable Bedrock path without changing its economic rules.

## Contract and evidence

Read [contract.json](contract.json) for applicability and required outputs; [REFERENCE.md](REFERENCE.md) for evidence and version limits. No listed verified release means resolve the target before generation. [examples/scenario.md](examples/scenario.md) contains a documented evaluation prompt, not proof that an agent passed.
