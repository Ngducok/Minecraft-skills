# Reward and progression cases

Define completion evidence and scope before payout: player, team, round or world.
Test duplicate events, account reconnect, shared objectives and reset generation.
Criteria completion and reward issuance are distinct state transitions.

For sampled rewards, state per-item/stack/action semantics and persist the sampled
result when it must survive splitting/storage. Use deterministic test input for
range/probability invariants; do not assert exact production random frequencies.

Expected value uses joint outcome probability when yield/quality are correlated.
Measure time, effort, failures and supply in realistic beginner/typical/optimized
paths. Scores, materials, access and money have different balance goals. Currency
minting/burning differs from transfers; no universal inflation rate or price table.

Check reset/reclaim, repeat crafting and alternate-target loops against the
requested design. Intentionally repeatable progression is valid; quantify its
ceiling and prevent unintended duplicate settlement.
