---
name: minecraft-permission-providers
description: "Integrate LuckPerms or existing Minecraft permission services, contextual access and temporary/admin grants."
---

# Permission providers and contexts

Use the installed supported provider rather than parallel rank lists. Identify user/group context, server/world scope and whether the task reads permissions or changes stored permission data.

- Query effective permissions under the correct context; a node stored on an account is not necessarily effective in the current world/server.
- Use player UUIDs and provider APIs. Do not derive authorization from chat prefixes, scoreboard teams or operator-looking names.
- Keep database/future-based account loading outside the tick path, then apply gameplay changes under the correct thread and recheck session validity.
- For temporary grants, define duration and context precisely. Persist through the provider when modifying account data; a local cached flag is not a global grant.
- Register dependencies honestly and handle provider absence/reload. A missing permission provider must not silently elevate players.
- Read-only inspection does not authorize granting global wildcard permissions or operator status. Make requested changes scoped and reviewable.

## Verification

Test inherited/group permissions, world contexts, temporary expiry and player reconnect. Ensure denied GUI/command paths remain denied.

## Example request

Grant access to one farm action in one world without granting a global admin permission.

## Contract and evidence

Read [contract.json](contract.json) for applicability and required outputs; [REFERENCE.md](REFERENCE.md) for evidence and version limits. No listed verified release means resolve the target before generation. [examples/scenario.md](examples/scenario.md) contains a documented evaluation prompt, not proof that an agent passed.
