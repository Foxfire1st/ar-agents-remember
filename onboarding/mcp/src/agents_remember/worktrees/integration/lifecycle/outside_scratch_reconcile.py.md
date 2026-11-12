# mcp/src/agents_remember/worktrees/integration/lifecycle/outside_scratch_reconcile.py

## Governing Overview

[overview](overview.md)

## Purpose

This module answers the one question the sweep may not guess: whether a generation has ended. It names the terminal owner as that authority, proves the two ways a generation can end, and attaches the resulting sweep to cleanup, abandon, finalize and the tool-server start. It sits beside `lifecycle_enclosure_terminal` rather than inside it because that module is imported by the location publisher, and the sweep itself reads locators through the publisher.

## Code Commentary

### Logic

- `reconcile_outside_scratch_roots` is the single caller of `outside_scratch.reconcile`, passing `generation_ended` as the `ended` predicate; `with_outside_scratch_reconcile` attaches the report to a terminal operation's answer under `outsideScratchReconcile`.
- `generation_ended` refuses a marker whose `contractPath` or `coordinationRoot` is not absolute, then accepts only when one proven record carries the marker's root path and generation and a `marker_sha256` equal to `outside_scratch.marker_identity(root)`.
- `_proven_generations` reads the address with `inspect_lifecycle_operation_locator` and proves exactly two ends: the live address when `observed.state` is `terminal-archived` and `terminal_cleanup_contract_authority` answers `cleanup-completed`, and every generation the manifest links as a collected predecessor.
- An archive-ready generation proves nothing: the archive is published before the destructive outputs, so its existence is never completion, and a state other than `terminal-archived` proves nothing either.
- `_ended_predecessors` follows `manifest.predecessorTerminal` for at most `MAX_PREDECESSOR_HOPS` (8), stopping at the first hop that does not prove rather than stepping past it; each hop must pass `_retained_archive` — archive and receipt inside the coordination root and outside the old group, that group gone, archive bytes equal to `link.terminalArchiveSha256`, both models parsing, and `_identities_agree` matching all thirteen fields against the link.
- `_generation_completed` prefers the completion record the finished cleanup wrote (`read_completion_record` plus `completion_agrees`); only when no record exists does it ask the predecessor's own address, so a replaced generation without a record is reported and never treated as ended.
- `_inside` compares every address against the resolved coordination root, so a link naming a path outside it, or one nested inside the group it outlived, proves nothing.
- `with_outside_scratch_reconcile` leaves a dry run untouched, returns the operation's own result unchanged when nothing was removed or reported, and on an exception publishes `{"removed": [], "reported": [{"path": "", "reason": "reconcile-failed: ..."}]}` instead of failing the operation.

## Invariants And Boundaries

- Deletion needs three agreeing proofs at once: the marker on disk, the retained contract record, and a `terminal-archived` locator.
- An archive, and a worktree group that merely stopped existing, are never completion evidence on their own.
- A root whose generation cannot be proved ended is reported with one reason and left untouched; a preview deletes nothing and adds nothing.
- Every proof is read from records retained under the coordination root; a relative path, an unresolvable locator or an unreadable manifest proves nothing.
- The pass is bounded by `MAX_ROOTS` and resumes from `.reconcile-cursor`, so a parent holding more roots than one pass is swept across passes rather than truncated.

## Evidence

- `mcp/tests/test_outside_scratch_root.py`: the completed-generation case publishes an enclosure, terminalises it and moves its contract to the completed cleanup cell, then proves the root is removed; the archive-ready case proves the same root is kept and reported as `generation-not-ended`.
- The successor case builds a real predecessor link and a completion record, deletes the predecessor's worktree group and rewrites the live address, then proves `_ended_predecessors` returns exactly that predecessor's root; removing the record alone makes the same call return nothing.
- Two further cases prove an active generation is reported and kept, and that `startup.start_outside_scratch_reconcile` runs the sweep off the handshake in its own thread.
