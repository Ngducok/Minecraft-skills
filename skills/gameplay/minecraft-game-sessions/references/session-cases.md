# Session lifecycle probes

Give each session/round a stable identity or generation. Exercise join, leave,
disconnect, spectator entry, countdown cancellation, active completion, draw/abort
and reset. Delayed work from generation N must not mutate generation N+1.

Test two completion events in one tick and repeated completion callbacks. Settle
the outcome once under one owner. For permanent rewards use the persistent claim
scope; temporary score alone is not a crash-safe settlement log.

Capture only state the session changes, such as inventory, game mode or flight.
Test capacity conflicts and disconnect during restoration. Restore state according
to the isolation contract rather than erasing legitimate persistent progress.

Assert no owned timers/entities remain after finish/disable and no player remains
in a half-reset world. These probes do not establish client presentation or durable
recovery unless those boundaries are exercised separately.
