# mcp/src/agents_remember/worktrees/integration/terminal_cleanup_completion.py

## Governing Overview

[overview](overview.md)

## Purpose

This module writes and reads the record that says a generation's cleanup finished, for generations whose own contract no longer exists to be asked. A successor replaces a predecessor's address and the predecessor's group is deleted with its contract, so the operation that completed is the only witness left, and it writes that witness beside its terminal archive. The sweep reads the record back to prove a predecessor ended by completion rather than by a folder that vanished.

## Code Commentary

### Logic

- `completion_record_path` derives the address from `terminal_enclosure_archive_paths`: `SUFFIX` is `.cleanup-complete.json`, so the record sits beside `<publicationRequestId>.json` and its receipt under `controlplane/lifecycle-enclosure-archives`.
- `write_completion_record` asks `inspect_lifecycle_operation_locator` for the generation's address first, and returns an empty path without writing when there is no locator — a generation that never reached the progression has nothing to attest.
- The payload carries `schemaVersion` set to `SCHEMA` (`terminal-cleanup-completion/1.0`), `state` set to `cleanup-completed`, the `publicationRequestId` taken from the locator rather than from the contract, `cleanupOperation`, the resolved `contractPath`, and `outsideScratch` copied from `outside_scratch.recorded_root(completed)` as path, generation and markerSha256, or `null` when the completed contract records no root.
- The write goes through `atomic_write_text` with sorted keys and a trailing newline; an `OSError` returns an empty path rather than raising, so the cleanup or abandon that called it still publishes its own answer.
- The callers are the completed operations that will lose the ability to answer later: `cleanup.py` writes `worktree_cleanup` once its contract is published, and `abandon.py` writes `worktree_abandon`.
- `read_completion_record` accepts only a dict whose `schemaVersion` equals `SCHEMA`, whose `state` is `cleanup-completed` and whose `publicationRequestId` equals the one asked for; a missing, unreadable or unparsable file is `None`.
- `completion_agrees` is the sweep's check of that record against the evidence it was found through: `publicationRequestId`, `cleanupOperation` and `contractPath` must all match.

## Invariants And Boundaries

- No record exists without a terminal locator, so a generation that never reached `terminal-archived` is never attested as completed.
- The record names one publication request, one operation and one contract path; a record from another generation or another verb does not agree and is not evidence.
- Reading is all or nothing: a wrong schema, a wrong state or another request id makes the record invisible to the sweep.
- Writing never raises; a failed write returns an empty path and leaves the sweep to report the root it cannot prove.
- The record sits in the coordination root's archive directory, outside the worktree group it describes, so deleting that group does not take the evidence with it.

## Evidence

- `mcp/tests/test_outside_scratch_root.py`: the successor case writes a record through `write_completion_record` for a completed generation, deletes the predecessor's worktree group and rewrites the live address, and `_ended_predecessors` still returns exactly the predecessor's root.
- The same case deletes the record file and proves `_ended_predecessors` returns nothing, so neither the archive nor the vanished group is doing the proving.
- The live-address path the sweep takes when no record exists is covered by the completed-generation case, which reaches `cleanup-completed` through the locator with no record present.
