# mcp/src/agents_remember/serving/projections/native_attention.py

## Governing Overview

[overview](../overview.md)

## Purpose

Event-driven intake for the five native kinds: an initialized, completed, quiet file-backed kind refreshes only when
its own domain was invalidated, and keeps its last complete observation in between, while a cold or unfinished held or
pause acquisition resumes on the heartbeat, and permissions, stall clocks and the bound agents' turn-end stamps are derived on every pass. Nothing here
polls the host.

## Code Commentary

`NativeAttentionInput.read(config, *, host, task_entries, now, refreshed=None)` always derives permissions and the bound agents' turn-end stamps from retained host facts, and updates stall clocks (:151-167, :251). It acquires file-backed kinds on first look, full refresh or their invalidated domains; cold or unfinished held and pause acquisition also continues on the heartbeat. Initialized, completed file views remain retained on a quiet pass. Two domains carry the new file inputs: `attention-held` and `attention-controlplane`.

Permissions, held rows, pause facts and terminal notices each carry a completeness flag. A partial walk is incomplete, and an unreadable publication, hold store, activation record or notice store cannot establish that its previous visible facts ended. Stall clocks are a derived eligibility-and-continuity dictionary, with no fifth completeness flag: unknown host state, a boot change, bound work or an explicit pause breaks a task's interval. The notice read settles interrupted intents through `terminal_notice_recovery` before publishing the store's admitted occurrences.

Bounds come from the fact shapes rather than from this module: an entry allowance per refresh, the pause-record
heap and its completeness test, `MAX_PERMISSION_ITEMS`, `MAX_HELD_ITEMS`, `MAX_STALL_CLOCKS` and
`PARSED_FILE_BUDGET` for the parse cache.

### 20261023-L190-v2 The Turn Ends Come From The Same Publication

`_turn_ends` (:151-167) is a pure grouping of `HostActivitySnapshot.agents`: task key -> the sorted ISO `activity.eventAt` stamps of the seats bound to that task. It is the identity rule 7 needs for a stall (`observer/reducer_impl/_attention_native._interval_start`, :250-275) and it costs nothing on the read path — no file is opened, no domain is added to the invalidation map, and an age-only pass re-derives the same stamps. That is what keeps an acknowledged interval hidden across a reload: the stamp is a property of the publication, not of the reader's watch.

## Evidence boundary

Current source interpretation at the reviewed freeze; the retained inputs, incomplete-read behaviour and the
per-domain refresh are pinned by `mcp/tests/test_attention_native_inputs.py`,
`test_native_refresh_wiring.py` and `test_attention_quiescence.py`. No live-page witness and no CPU or resource
measurement: evidence item 6 is unrun and carried to L36, item 7 unrun.
