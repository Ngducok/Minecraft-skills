---
name: minecraft-release-recovery
description: "Prepare Minecraft plugin/mod/pack releases, server upgrades, compatible data migrations and tested rollback plans."
---

# Minecraft releases, backups and rollback

Identify the release unit: code, asset pack, schema or world version. Keep those versions and runtime requirements explicit; upgrading world data can make a binary-only downgrade unsafe.

- Build and validate before replacing installed files. Record artifact hashes and compatible platform/client combinations, not just a JAR filename.
- Back up consistent world, player, plugin and account data together when the change crosses those boundaries. Test restoration on an isolated runtime.
- Stage restart-required changes without pretending a plugin hot reload is equivalent. Avoid relying on /reload for classloader, task or storage cleanup.
- Deploy code and its required pack/hash as a coordinated change. A server running new item IDs with an old cached pack is a visible compatibility failure.
- Define a rollback trigger and whether data migration is reversible. Do not overwrite newer player progress with a stale backup merely because the previous binary works.
- Review current distribution/usage rules when publishing assets or monetized content. Treat this as task-specific review, not a blanket prohibition on ordinary server work.

## Verification

Exercise upgrade and restoration with representative saved items/profiles. Verify pack reachability, version logs and a minimal gameplay smoke check after restart.

## Example request

Release a custom-item update with a pack and schema migration while retaining a valid restore point.

## Contract and evidence

Read [contract.json](contract.json) for applicability and required outputs; [REFERENCE.md](REFERENCE.md) for evidence and version limits. No listed verified release means resolve the target before generation. [tests/scenario.json](tests/scenario.json) contains a behavioral evaluation prompt, not proof that an agent passed.
