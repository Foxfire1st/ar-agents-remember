# mcp/src/agents_remember/worktrees/attention_terminal_notices.py

## Governing Overview

[overview](../overview.md)

## Purpose

The occurrence identity and the begin/confirm/discard wrapper the publishing routes share for the two terminal
notices, so all of them agree on what one occurrence is and which task it names.

## Code Commentary

`leaf_task` resolves a leaf enclosure's own task document and refuses an unresolved leaf instead of borrowing its master. For a series contract it instead names the series master's own document. Direct landing uses its immutable admitted leaf reference through `_direct_leaf`; its series enclosure is not the direct notice's subject. An unnameable subject produces no notice.

Identity is occurrence-scoped. Ordinary landed occurrences combine the resolved subject key and landed commit; abandonment uses that subject key. `direct_occurrence_at` adds the direct operation identity, including its recorded generation when present, so retries share an occurrence and distinct generations remain distinct. Generation `0` records `None`, rather than inventing a native generation.

`begin_landed_notice`, `begin_abandoned_notice` and `begin_direct_landed_notice` open the intent before the
native operation; `confirm_notice` publishes it and `discard_notice` drops it. A write failure never turns a
completed publication into a failure. Detail text is truncated here (`code_commit[:12]`, `exact_key[:16]`) and
capped at 280 by the store.

## Evidence boundary

Current source interpretation at the reviewed freeze; per-leaf subjects, generation identity and the
confirm/discard boundary are pinned by `mcp/tests/test_terminal_notice_subject.py`,
`test_attention_notice_publication.py` and `test_record_landing.py`. No live-page witness and no CPU or resource
measurement: evidence item 6 is unrun and carried to L36, item 7 unrun.
