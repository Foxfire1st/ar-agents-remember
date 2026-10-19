# Host-free turn-ended decision tests

[Governing plugin overview](../overview.md)

## Contract

Synthetic role facts, timelines and a controlled sender exercise the whole silent-turn decision without a host. The line carries the ended turn's own last line, shortened to 300 characters, with `no text`/`unreadable` cases; explicit delivered returns suppress notices while a refused or failed one gives the line; permission waits, running descendants and a parent that is in a turn defer them, and the suite separates a parent whose provider is known to steer (delivered at once) from an unknown provider (held). Turn-local custody, an archived or missing parent waking the current Manager, a held line moving on archive, and the once-only missing-agent log are covered. Retry, overlap, restart and archive cases qualify held-line ownership; bounded historical stores and whole-line batching are asserted. Ordering is delivered in the order the turns ended across a requeue, an in-flight earlier flush and a Manager rebind.

The leaf rule is its own group: a completed leaf turn with no hand-off sends the seat one message after the 60-second wait and its parent no line; the third and fourth sends give the parent the counted line and the seat nothing; the third end's marked line leaves only at the end of its own wait and a turn start inside that wait cancels it; an archived or permission-waiting seat at the wait's end gets nothing and a row is written. Each non-silent end (failed, canceled, permission, child in a turn, archived, reply to a waiting sender) leaves the seat alone with its reason, a replaced timeline falls back to the last `user_message`, and a child is found by its `paseo.parent-agent-id` label even when its turn began before the plugin loaded. A hand-off, or a turn begun by another agent's message, resets the run; the plugin's own message does not. A Manager turn is never sent back. Hand-off recognition is exercised on the five exact captured rows from `fixtures/evidence-rows.json` — the L104 Curator's escaped answer included — and on rows of each other form built as the pinned mappers build them, including the four Hermes title forms, a cut answer, a shell row that only mentions `role_message`, and a `role_start` row, which is no leaf hand-off.

The size assertion checks the source constants, not settings reload. The contributed-handler case invokes the actual `registerParentWakeEvents` against a mock event registry and host sender. The suite remains a host-free composition: it consumes captured row values, not live SDK callbacks, and proves no plugin load, live delivery or cross-harness wakeup.

## Evidence

- The host-free suite retains suppression/deferral/retry/restart controls and adds actual parent-wake registration against a mock registry with explicit steer sends. [1]
