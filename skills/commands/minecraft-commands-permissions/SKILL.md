---
name: minecraft-commands-permissions
description: "Implement Minecraft commands, arguments, suggestions and server-side permission checks on Paper or equivalent command platforms."
---

# Commands and action authorization

Choose the smallest existing command mechanism that supports the requested syntax. Use typed Brigadier arguments when they remove real parsing ambiguity; preserve working classic command handlers otherwise.

- Validate sender type, permission, argument ranges, target existence and world context. Suggestions must not leak private targets or become the only permission gate.
- Register Brigadier commands through the target Paper lifecycle API when applicable; do not assume a Paper bootstrap context exists in a classic plugin.
- Route command, menu and callback entry points into the same authorized operation. A hidden button or completed tutorial is not permission to bypass the server check.
- Separate administrative operations from ordinary gameplay permission defaults. Prefer an existing permission provider over manual rank-name comparisons.
- Treat player-provided text as data. Do not interpolate names or item strings into console commands or parsed formatting that can change actions.

## Verification

Exercise player, console and denied sender paths; malformed numbers, stale targets and tab completion. Ensure the same forbidden action is rejected through its GUI entry point.

## Example request

Create a purchase command with optional quantity and suggestions without allowing unauthorized console-equivalent actions.

## Contract and evidence

Read [contract.json](contract.json) for applicability and required outputs; [REFERENCE.md](REFERENCE.md) for evidence and version limits. No listed verified release means resolve the target before generation. [examples/scenario.md](examples/scenario.md) contains a documented evaluation prompt, not proof that an agent passed.
