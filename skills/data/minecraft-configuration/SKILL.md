---
name: minecraft-configuration
description: "Add or migrate Minecraft plugin/mod configuration, catalogs, probability tables and feature flags safely."
---

# Configuration validation and migration

Read existing configuration and its callers before changing the schema. Defaults are for absent values, not permission to ignore malformed files or replace a user's economy.

- Validate types, finite numbers, bounds, namespaced IDs, referenced materials and cross-field invariants. Probabilities must have an explicit normalization rule; reject negative prices and impossible stack sizes.
- Parse into a candidate immutable snapshot, validate completely and only then activate it. Runtime reload must retain the prior valid snapshot when the new file fails.
- Separate default resource templates from user data. Merge only necessary new keys; preserve unrelated settings and comments when the chosen tool supports them.
- Version migrations, back up changed data and make replay safe. Never interpret missing keys from a parsing error as a successful empty catalog.
- Feature flags need clear startup/runtime semantics and cleanup of owned tasks/state. Disabling production should not destroy already owed output or inventories.

## Verification

Test missing versus malformed files, unknown item IDs, invalid probabilities and failed reload. Verify the prior valid configuration still serves requests after rejection.

## Example request

Add a growth-rate setting without changing existing prices or silently accepting NaN.

## Contract and evidence

Read [contract.json](contract.json) for applicability and required outputs; [REFERENCE.md](REFERENCE.md) for evidence and version limits. No listed verified release means resolve the target before generation. [examples/scenario.md](examples/scenario.md) contains a documented evaluation prompt, not proof that an agent passed.
