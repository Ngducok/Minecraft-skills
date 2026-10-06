---
name: minecraft-bedrock-addons
description: "Create or debug Minecraft Bedrock behavior/resource packs and Script API add-ons; not Java datapacks or Paper plugins."
---

# Bedrock add-ons and scripts

Confirm Bedrock engine version, distribution and stable/preview API requirement. Java item-model JSON, Paper events and Fabric registry examples do not apply to a Bedrock add-on.

- Separate behavior pack, resource pack and script modules. Define unique manifest/module UUIDs, dependency linkage and engine/API compatibility from the target documentation.
- Use the appropriate namespace and schemas for custom blocks, items and entities. Client visuals and server behavior need consistent identifiers but distinct resource locations.
- Prefer stable Script API where it supports the requested mechanic. Experimental dependencies and world toggles must be disclosed as requirements, not switched on silently.
- Handle lifecycle and read-only/restricted execution phases using the supported events/scheduling contract. Defer mutations only through the target API's allowed mechanism.
- Keep player input validated server-side and persist state through supported data facilities. Do not assume preview methods are present on retail clients or hosted servers.
- Treat Geyser mappings as a separate integration path: a native Bedrock add-on does not automatically become a Java server feature.

## Verification

Import into a disposable matching Bedrock world, inspect content logs, restart and test supported server/client distribution. Verify pack UUID/dependency conflicts and missing experimental features.

## Example request

Build a stable Bedrock farming add-on without copying Java crop event or NBT code.

## Contract and evidence

Read [contract.json](contract.json) for applicability and required outputs; [REFERENCE.md](REFERENCE.md) for evidence and version limits. No listed verified release means resolve the target before generation. [examples/scenario.md](examples/scenario.md) contains a documented evaluation prompt, not proof that an agent passed.
