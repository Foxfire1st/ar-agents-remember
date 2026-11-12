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

`NativeAttentionFacts` carries permissions, held rows, paused task keys, terminal notices, stall clocks and —
since L190 v2 — the turn-end stamps of each task's bound agents, each beside its own completeness flag, except the
stall clocks and `turn_ends`, which carry no flag and are re-derived on every pass — the shape that lets every
consumer distinguish "nothing there" from "not read completely". `PermissionWait` and `HeldMessage` are frozen value shapes: a held row carries the store's safe
reason and never the message text, and a permission wait carries the agent and prompt identities rather than any
prompt argument.

`observe_terminal_notices` reports each retained notice to the dismissal observer, and a notice acknowledgement
ends only when its occurrence leaves the retained set; the three live kinds report their own ends from the
projection pass instead (`serving/projections/projection_inputs.py:750-787`), so this module stays the facts owner
and not the acknowledgement owner. `task_lineage` is the one definition of a task and its
master chain that the stall suppression reads.

### 20261023-L190-v2 Turn-End Stamps Name An Idle Interval

`turn_ends` (:93-97) maps a task key to the sorted published `eventAt` stamps of the agents bound to it, derived by
`serving/projections/native_attention._turn_ends` (:151-167) from the same host publication the stall clocks are
read beside. Its latest stamp is the native start of that task's idle interval, which is what rule 7 names a stall
occurrence by (`observer/reducer_impl/_attention_native._interval_start`, :250-275): a turn ends the interval and
moves the stamp, so the next interval is a different occurrence, while a restarted reader derives the identical
stamp from the identical publication and the developer's acknowledgement stays in force.

The field carries no completeness flag, for the same reason the stall clocks do not: a seat the publication gives
no transition contributes nothing rather than a guessed stamp, and the builder's fallback chain (a task's own
`eventAt`, then the reader's watch) is named there. The 900-second deadline is still counted on the reader's watch;
the stamp names the interval, it does not date the deadline.

## Evidence boundary

Current source interpretation at the reviewed freeze; the deadline, eligibility and suppression behaviour is
pinned by `mcp/tests/test_attention_native_kinds.py` and `test_attention_native_inputs.py`. No live-page witness
and no CPU or resource measurement: evidence item 6 is unrun and carried to L36, item 7 unrun.
