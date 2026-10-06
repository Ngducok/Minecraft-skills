# Machine conservation cases

Use when processing inputs, queuing work or moving items between inventories.

For a simple illustrative recipe consuming two inputs to produce one output, track
input removed, reserved work, output pending and output delivered. Conservation
includes reservations and pending output, not only visible inventory slots.

Reserve one operation once; persist enough state to resume or reconcile. A full
output inventory must pause or retain pending output, not consume another input or
discard the product. Do not repeat completion on every tick after a failed insertion.

Exercise repeated clicks, hopper/external insertion, unload during work, restart at
completion, removed machine and team ownership change. Decide whether elapsed
offline time counts and cap catch-up so a long absence does not create unbounded
work. Simulation must preserve recipe and energy costs under faster tick batching.

Check item totals before/after each failure boundary, allowing only declared recipe
consumption/production. For multiple storage providers, document crash ambiguity
and reconcile; an in-memory flag is not exactly-once delivery across process failure.
