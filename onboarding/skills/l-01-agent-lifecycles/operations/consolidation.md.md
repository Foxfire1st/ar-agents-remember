# skills/l-01-agent-lifecycles/operations/consolidation.md

## Governing Overview

[overview](../overview.md)

## Purpose

Defines the operational workflow for a consolidation leaf pass, executed by the Consolidator over a leaf's `consolidationList` with an unchanged paired code tree.

## Code Commentary

Scopes the pass to one leaf's `consolidationList` with no route review and mandatory knowledge-gate plus coherence validation. The 5-step `Workflow` requires: checking `worktree_status` and `consolidationList` and persisting `consolidation_target` items via contract-scoped `memory_quality_check`; reading listed families together (guarantee + members) then loose rules against code, decisions, and cards while running only named or newly-linked proof tests with scratch temps; writing `stands`, corrected, or `unresolved` rows via mounted `knowledge_write` (`commit: false` then `commit: true`, no producer list) with `testsRun`/`testsNotRun`/`noProofRecorded` (zero-change passes land history alone); running clean-tree and integrity checks (`git status --porcelain`, `git diff --check`, `knowledge_integrity_check`, full `memory_quality_check` to `curatorActionableCount=0`/`ready-for-closeout`, and `knowledge_read(view="dependent", staleOnly=true, compact=true)`—full rows for evidence, 0 stale); running `curator_coherence` `prepare`->`publish`->`validate` when `coherence-required` (never re-validating post-closeout trees); and writing the pass report and sending the memory candidate to the sibling Reviewer via `role_message` (releasing the held Reviewer; naming files without pasting), repairing any findings via `knowledge_write` and re-running checks. `Notices` specifies when to notify the Manager, including `unresolved` and gap items routed onward to the Architect.

## Relationships

Composed by `skills/l-01-agent-lifecycles/composition-manifest.json` (`operations.consolidation`, `applies_to_roles: ["consolidator"]`) alongside `roles/consolidator.md` and packaged into `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/operations/consolidation.md`. Procedural detail lives in `reference/consolidation-pass.md`, while seat authority and prohibitions belong to `roles/consolidator.md`.

## Evidence

- The operation header scopes a consolidation pass to one leaf's `consolidationList` with an unchanged code tree, no route review, and mandatory knowledge-gate and coherence checks. [1]

- `## Workflow` orders worklist persistence, family-first reading and named proof-test execution, `knowledge_write` (`commit: false` -> `true`), clean-tree/integrity/stale checks, `curator_coherence`, and Reviewer handover via `role_message`. [2]

- `## Notices` directs Manager escalation for seat/delivery, authority, beyond-limit passes, disputes, reserved sync, and `unresolved`/gap items routed to the Architect. [3]
