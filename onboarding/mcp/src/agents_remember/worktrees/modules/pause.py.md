# mcp/src/agents_remember/worktrees/modules/pause.py

## Governing Overview

[modules route overview](overview.md)

## Purpose

`pause.py` is the **entire stop-only pause route** for an atomic master. It owns one public-shape operation: release the master's atomic-series activation selection — or, when the master holds none, report that it is already stopped — write the pause fact into the master's contract-scoped activation record, publish nothing, and hand the turn back to the developer.

Its boundary **is** the feature. A caller who wants to stop a master must not be able to move a ref, create a commit, land anything or write a ledger row by reaching for the stop, so this module imports and calls none of the integration, landing, closeout or ledger planes and runs no Git at all.

## Code Commentary

`pause_result(args, current_contract)` is the whole entry point. It refuses to run against a contract that is not the one it was addressed with, then splits into five outcomes. First: **a contract that carries the removed mode is never paused** — it is refused with the opt-out refusal, whose way out is abandon and a fresh start, not control. Then the original four: **not a series contract** (`pause-requires-atomic-master`; a leaf pause must refuse rather than release its master's selection); **release refused and the master genuinely not vacant** (the release authority's own status explained through `_RELEASE_REFUSAL_DETAIL`); **already stopped** (only a re-observed `vacant` record becomes the `atomic-series-already-vacant` success, so a record that appeared, became unreadable, or names another master still refuses); and **released** (`state`/`status` `paused`, carrying the released record's source fact).

Both success payloads carry the same `_PAUSE_NEXT_STEP` — a summary and no `nextTool`/`nextArgs` — so the result proposes no continued execution. `_refusal_payload` mirrors that shape on the refusal side with `paused` false. Both success paths write that pause fact: the release is stamped with the release time through `release_atomic_series_selection(..., paused_at=...)`, and the already-stopped path re-marks the observed vacant record through `mark_atomic_series_pause`, so the record carries the explicit pause a stall suppression reads. The activation record is keyed per series contract, so releasing one master leaves every other master's record byte-identical. The stop is idempotent, and `worktree_checkpoint_landing` remains the separate, explicitly requested publication that is deliberately unreachable from here.

## Evidence


- Disabled contract refused before the kind check [14]


- Only a re-observed vacant record reports stopped [15]

- Refusals propose no next call either [16]
