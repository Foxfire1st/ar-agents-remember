# mcp/src/agents_remember/controlplane/attention_notices.py

## Governing Overview

[overview](../overview.md)

## Purpose

The bounded, disposable terminal-notice store: its schema, the one baseline cut it carries, the pending intents
of interrupted publications, the confirmed occurrences a reader publishes, and the pruning and quarantine rules
that keep all of it bounded.

## Code Commentary

The store is `<coordination_root>/controlplane/attention-notices.json`, written whole under
`ATTENTION_NOTICE_OWNERSHIP` and never appended; a write failure is logged and never raised, so a notice failure
cannot fail the native publication it follows.

**The cut.** On the write that creates the store, `_rewrite` reads a UTC timestamp under the notice-file lock and stores it as `StoreCut.at`, with `sequence=1`. Confirmation and successful settlement read their timestamps under the same lock, replace the intent's earlier `at`, and assign a monotonically increasing notice sequence. `published()` orders by notice sequence and admits a row only if both its sequence and timestamp meet the stored cut. This is the notice store's creation and admission order: native contract and journal commits occur between begin and confirm outside this lock. The cut is retained on ordinary reload and restart, so retained unacknowledged occurrences keep their identity. A missing or unreadable store is created with a fresh cut, without scanning historical terminal records; unreadable bytes are quarantined before replacement. A store without a cut publishes nothing. `RETIRED_STORE_KEYS = frozenset({"baseline"})` is tolerated on read because the previous format carried that unused key.

**Observation.** A missing file, a readable store that holds nothing, and bytes this build cannot interpret are
three different observations (`NoticeStoreState`), and only the third is quarantined — its bytes moved to a
`.torn.` sibling — so an unreadable store never reads as an empty one.

**Bounds.** `MAX_TERMINAL_NOTICES = 64`, `MAX_PENDING_NOTICES = 16`, `MAX_NOTICE_DETAIL = 280` characters and
`MAX_NOTICE_STORE_BYTES = 64 * 1024`, enforced over the exact document about to be written — confirmed rows and
interrupted intents measured through the same serialization the writer publishes, because a cap measured on one
representation and applied to another is not a cap.

## Evidence boundary

Current source interpretation at the reviewed freeze; the cut, quarantine, three-state observation and the
bounds are pinned by `mcp/tests/test_attention_notice_store.py` and `test_terminal_notice_recovery.py`. No
live-page witness and no CPU or resource measurement: evidence item 6 is unrun and carried to L36, item 7 unrun.
