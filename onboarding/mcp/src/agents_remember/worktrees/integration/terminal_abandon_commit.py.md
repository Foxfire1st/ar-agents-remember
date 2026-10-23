# mcp/src/agents_remember/worktrees/integration/terminal_abandon_commit.py

## Governing Overview

[overview](../overview.md)

## Purpose

One native abandonment commit owner for two explicit successful-result receipts: an archive-generation receipt beside its archive, and an admitted no-remains receipt retained beside its canonical contract. Both use the same bounded lease, final atomic write and precommit restoration; neither creates an independent history.

## Code Commentary

`TerminalAbandonCommitRecord` keeps the strict archive-generation schema and path. `NoRemainsAbandonCommitRecord` requires `authorityKind="no-remains"`, the exact contract path, lifecycle identity, canonical committed-contract SHA-256 and terminal note. Both models are frozen with `extra="forbid"`; the required note may be empty and is bounded at 4096 characters. The 16 KiB serialized-receipt bound applies on read and publication.

`terminal_abandon_commit(original, committed)` selects the no-remains route only through the original contract's canonical admission predicate. Its receipt address is `contract_path.with_suffix('.abandon-committed.json')`, retained with that contract; it claims no archive or generation. Other inputs require the exact validated abandonment archive and its archive-generation receipt. Each branch permits only the final cleanup/note amendment. A missing archive does not select the no-remains route.

The owner holds one lease through publication and restoration. `NativeAbandonCommit.publish` writes the receipt as the native guard's final commit operation; before commitment, restoration can remove the uncommitted receipt. The nonwaiting reader returns no proof while that lease is held. No-remains recovery requires the exact typed receipt matching abandoned cleanup, path, lifecycle, terminal note and canonical final-contract hash. The hash uses the native writer's canonical publication serialization; it is not an arbitrary-format file-tamper guarantee. A predicate or cleanup cell alone proves nothing.

## Evidence boundary

Current source interpretation at the reviewed freeze; the abandonment crash matrix and the receipt/archive
distinction are pinned by `mcp/tests/test_terminal_notice_commit_recovery.py` and
`mcp/tests/test_attention_notice_publication.py`. No live-page witness and no CPU or resource measurement:
evidence item 6 is unrun and carried to L36, item 7 unrun.
