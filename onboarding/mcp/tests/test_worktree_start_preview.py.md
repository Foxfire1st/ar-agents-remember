# mcp/tests/test_worktree_start_preview.py

## Governing Overview

[Nearest governing overview](overview.md)

## Purpose

Registered public operation proofs for exact planned-parent preview, no startup-state materialization, truthful journal/ref facts and unchanged durable apply — plus the proof that the removed opt-out mode never previews.

## Code Commentary

The canonical confined fixtures use real temporary code and external-memory repositories and the registered MCP/application/start/bootstrap path. `PreviewFixture` builds every world external-memory; the repeated first-leaf preview is parametrized only by commanded versus uncommanded parentage and asserts complete startup-owned state, refs, worktrees, contents and real index bytes stay identical with no parent publication. `test_disabled_start_is_refused_before_any_publication` pins the L50 refusal: both preview and real run with `memory_mode="disabled"` answer `memory-opt-out-refused` at the top of `worktree_start`, before any branch, worktree, contract or task binding exists, so the world is byte-identical afterwards and no parent contract was published. The partial-bootstrap case drives one genuine journal before and after its helper creates the exact memory ref (`would-create` then `existing`), with actual apply recovering that journal; rejection, foreign-parent, invalid-input, changed-source and organizational cases remain separate operations.

## Evidence

- Fixture world is always external-memory [7]
- First-leaf preview repeatable without publication, commanded or not [8]
- Disabled mode refused in preview and real run, world unchanged [9]
- Partial bootstrap read-only, then apply recovers the same journal [10]
