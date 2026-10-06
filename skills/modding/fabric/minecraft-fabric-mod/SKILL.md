---
name: minecraft-fabric-mod
description: "Create or maintain Fabric Minecraft Java mods, registries, entrypoints and client/server code separation."
---

# Fabric mod development

Pin game release, Fabric Loader/API, Loom, mappings and Java as one compatible toolchain. Do not paste a current-release example into an older mapping namespace without checking signatures.

- Identify logical side and physical distribution. Client screens/renderers must not be referenced from common code loaded by a dedicated server.
- Prefer public Fabric APIs/events; use mixins for a specific gap with narrow targets and an explicit version ceiling. Avoid broad overwrites when injection can preserve other mods' behavior.
- Keep registry identities stable and organize client assets versus server data. Registration timing must match the target lifecycle and built resource paths.
- Use loader-supported persistence/networking for shared state; do not assume a static singleton remains correct across different worlds or integrated-server restarts.
- Identify whether the mod is client-only, server-only or required on both sides. New registered content generally requires matching client understanding, unlike a server-side presentation-only plugin.
- Keep existing build wrappers/dependency management and add datagen only when it materially reduces repetitive asset/schema work.

## Verification

Run both development client and dedicated server. Build a distribution JAR, verify entrypoints/resources and test only the declared required-side installation.

## Example request

A Fabric feature works in singleplayer but crashes a dedicated server by loading a screen class.

## Contract and evidence

Read [contract.json](contract.json) for applicability and required outputs; [REFERENCE.md](REFERENCE.md) for evidence and version limits. No listed verified release means resolve the target before generation. [examples/scenario.md](examples/scenario.md) contains a documented evaluation prompt, not proof that an agent passed.
