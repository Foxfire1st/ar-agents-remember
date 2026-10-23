# mcp/src/agents_remember/observer/native_attention.py

## Governing Overview

[overview](../overview.md)

## Purpose

The five native fact shapes and the single place their bounds are named, where the reader and the builders both
read them.

## Code Commentary

`STALL_SECONDS = 900.0` is rule 4's settled stall predicate; v1 adds no user setting for it. Around it sit the
named caps: `MAX_PERMISSION_ITEMS = 128`, `MAX_HELD_ITEMS = 128`, `MAX_HELD_RECEIPTS = 64`,
`MAX_PAUSE_RECORDS = 256`, `MAX_TERMINAL_ITEMS = 64` and `MAX_STALL_CLOCKS = 2048`, with
`PARSED_FILE_BUDGET` derived from them (520) so a parser cache can be sized from the same numbers.

`NativeAttentionFacts` carries permissions, held rows, paused task keys, terminal notices and stall clocks, each
beside its own completeness flag, except the stall clocks, which carry no flag and are re-derived on every pass —
the shape that lets every consumer distinguish "nothing there" from "not read
completely". `PermissionWait` and `HeldMessage` are frozen value shapes: a held row carries the store's safe
reason and never the message text, and a permission wait carries the agent and prompt identities rather than any
prompt argument.

`observe_terminal_notices` reports each retained notice to the dismissal observer, and a notice acknowledgement
ends only when its occurrence leaves the retained set. `task_lineage` is the one definition of a task and its
master chain that the stall suppression reads.

## Evidence boundary

Current source interpretation at the reviewed freeze; the deadline, eligibility and suppression behaviour is
pinned by `mcp/tests/test_attention_native_kinds.py` and `test_attention_native_inputs.py`. No live-page witness
and no CPU or resource measurement: evidence item 6 is unrun and carried to L36, item 7 unrun.
