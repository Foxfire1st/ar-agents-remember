# Host-free turn-ended decision tests

[Governing plugin overview](../overview.md)

## Contract

Synthetic role facts, timelines and a controlled sender exercise silent-turn notifications without a host. The line carries the ended turn's own last line, shortened to 300 characters, with `no text`/`unreadable` cases; explicit delivered returns suppress notices while a refused or failed one gives the line; permission waits, running descendants and a parent that is in a turn defer them, and the suite separates a parent whose provider is known to steer (delivered at once) from an unknown provider (held), asserting that the running turn is not replaced. Turn-local custody, an archived or missing parent waking the current Manager, a held line moving on archive, and the once-only missing-agent log are covered. Retry, overlap, restart and archive cases qualify held-line ownership and loss prevention; bounded historical stores and whole-line batching are asserted. Ordering is its own subject: lines are delivered in the order their turns ended across a requeue, across an in-flight earlier flush and across a Manager rebind, the second batch is not sent into the turn the first batch started, and a real failed send keeps the debt and is retried once, in order. Provider history is shown reclaimed on archive and capped at its named limit, evicting the oldest and leaving the absent identity unknown. The size assertion checks the source constant, not settings reload. The contributed-handler case invokes the actual registerParentWakeEvents against a mock event registry and host sender, checks its five registered names, turn/permission gates and the steer option it passes. This remains a synthetic composition, not live SDK callback payload, plugin-load or cross-harness wakeup proof.

## Evidence

- The host-free suite retains suppression/deferral/retry/restart controls and adds actual parent-wake registration against a mock registry with explicit steer sends. [1]
