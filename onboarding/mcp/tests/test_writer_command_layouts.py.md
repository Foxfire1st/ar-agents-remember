# mcp/tests/test_writer_command_layouts.py

## Governing Overview

[tests route overview](overview.md)

## Current source account — the real command from a primary checkout and from a linked worktree

The layouts are real Git shapes built in the test: a `.git` directory is the primary checkout and a `.git` file naming a gitdir is a linked worktree, so `resolve_checkout_location` and `require_linked` decide from the filesystem rather than a stub. The guard cases assert the primary location is refused as `primary checkout is refused` and the linked one is admitted and owns a coordination root under `provider-runtime`. A further case drives `leaf_write_report` with a `CommandRoute` carrying the guard clause, so the report itself is checked for the clause, the absolute `contractPath`, the mounted-route sentence, the absence of `--config`, no published question and unchanged memory.

The two end-to-end cases copy this candidate's package into the fixture checkout and run `python -m agents_remember.cli knowledge-ingest` as a subprocess with no guard or settings mock, probing first that no execution mode is declared, the package resolves inside the checkout, and discovery found the settings file. From the primary checkout the batch of one raise row and one ordinary row is refused with no written rows, no published question, `plannedBeforeRefusal` at 1, memory and task bytes unchanged. From a linked worktree the probe shows the disposable root and the configured root binding, the batch is refused on the contract-root mismatch (both roots and the settings file in the text, the binding line on stderr), nothing moves, and then the same hand-off without the raise row exits 0, writes the ordinary row and reads it back with the task tree still unchanged.

## Evidence Scope

This is a current source account, not an executed test, CODE/MEMORY grade, live producer grant or landing result. No Domain Documentation source is configured for this slice; no external-system guarantee is inferred.

## Evidence

- A real primary checkout refuses the whole batch with the guard clause and leaves memory and task bytes unchanged [1]
- A linked worktree refuses the batch on the disposable-root and contract-root mismatch, then the ordinary row alone commits and reads back [2]
