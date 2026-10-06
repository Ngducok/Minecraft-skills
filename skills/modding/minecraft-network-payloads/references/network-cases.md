# Untrusted payload checks

Use when exposing mod/plugin messages, custom actions or remote gameplay requests.

The client requests an action; it does not authoritatively supply balance, damage,
ownership, reward, recipe output or permission. Bound encoded and decoded payload
sizes, collection lengths, numeric ranges and per-player request rates.

Test unknown IDs, invalid enum values, oversized strings, nonfinite numbers, missing
targets, dimension mismatch, impossible distance and a target removed before apply.
For valuable operations, test duplicate/replayed request IDs and stale session or
quote versions. Request deduplication must be scoped to account and operation.

Observe the target networking API's decode and handler thread contracts. Decode
into safe data; apply world/inventory effects on the current owner thread after
revalidation. Login/logout and region transfer can invalidate captured references.

Dedicated-server startup must not load client-only classes. Exercise malformed
messages without server crash, privilege gain, economic effects or unbounded log
spam. Protocol/version mismatch needs a supported failure path, not silent decoding
under a different schema.
