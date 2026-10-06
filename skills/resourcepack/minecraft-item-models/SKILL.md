---
name: minecraft-item-models
description: "Implement custom Minecraft Java item visuals, item-model definitions, texture atlases or model-selection components."
---

# Item models, components and textures

Determine whether the target uses legacy model overrides or newer client item definitions. Separate gameplay identity from the visual model key; a model swap does not create a new registered material on a vanilla server.

- Prefer supported ItemMeta/component APIs for the target platform. Keep persistent product identity separate from mutable display names, lore and resource-pack paths.
- Trace item definition to model to textures and atlas membership. Do not mix item/block atlas resources inside a model when the target release forbids it.
- Verify transforms in GUI, hand, dropped and frame contexts. Correct source alpha bounds before compensating for a tiny or off-center icon in GUI layout.
- For modded registry items, route registration through the chosen loader instead of emulating new content with server-only metadata.
- Keep fallback material readable without the pack. A missing texture or outdated component must not bypass item validation or silently become valuable produce.

## Verification

Validate every JSON reference, namespace and texture path. Check target clients in GUI and hand, including resource reload and missing pack.

## Example request

A custom crop model is invisible in the shop but visible in hand; trace the client-item definition and atlas.

## Contract and evidence

Read [contract.json](contract.json) for applicability and required outputs; [REFERENCE.md](REFERENCE.md) for evidence and version limits. No listed verified release means resolve the target before generation. [examples/scenario.md](examples/scenario.md) contains a documented evaluation prompt, not proof that an agent passed.
