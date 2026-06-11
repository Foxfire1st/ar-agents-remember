# test_carryover.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_carryover.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-10T09:45+02:00                     |
| lastVerifiedCommitHash | `610b8568b6517a78a80d35583101b32ed396e2a7`                                  |
| lastVerifiedCommitDate | 2026-06-11T15:49:54+02:00|

## Purpose

Tests for branch-memory carryover planning and apply (`memory/carryover.py`),
focused on the issue #56 route-overview candidate and index-regeneration
behavior.

## Code Commentary

### Logic

`CarryoverFixture` builds a real code repo (main + landed `task/one` branch
touching `src/app/feature.py`), a ledgered official memory repo, and a source
memory tree with the feature sidecar. Plan tests prove: a differing route
overview whose route covers a landed path becomes a `route-overview` candidate
keyed by the normalized route and is `review-required`; a route without landed
paths produces no candidate; identical branch/official content (root route `.`)
auto-carries for metadata re-verification; sidecar candidates keep the
`file-sidecar` default kind. `EntityCatalogCarryoverTests` proves the
`entity-catalog` kind: identical catalogs yield no candidate, differing
catalogs are review-required keyed by the literal `entity-catalog`, and a
carried catalog reports `entity_fingerprint_validation` (`validated` for a
correct `git-blob-set-v1` row, `mismatch` with per-entity detail otherwise).
`MemoryOnlyDocCarryoverTests` proves the `memory-only-doc` kind against a
git clone of official memory (`clone_memory`, real worktree shape): a
re-verified doc auto-carries only when the source object at its verification
commit matches official AND official memory left it untouched since the
merge-base; source divergence, an independent official change, or a plain
(non-git) source memory each force review-required; diff-covered paths are
not duplicated as memory-only candidates. Apply tests prove: an explicitly included
overview is copied, restamped to the official head, and official-side
`overview.index.json` files are regenerated and committed
(`route_index_refresh.state == "refreshed"`); a non-official checkout skips
index regeneration with a reported reason; a no-carry apply reports the
skipped index refresh.

`MemoryMainAdvanceTests` (issue #54) prove `memory_main_advance`: a carried-over
apply from a non-main official checkout fast-forwards `main` to the cycle
branch tip; the `ledger-mapped-head` path advances too; a main checkout reports
`already-current`; a diverged main is reported and left untouched; a repo
without a `main` branch reports `skipped`.

### Invariants And Boundaries

Self-contained git/onboarding fixtures (no imports from other test modules);
exercises the service API (`build_plan_for_request` /
`apply_carryover_for_request`), not the CLI adapters. The legacy sidecar
evidence-tier coverage stays in `test_worktree_support.py`'s c-11 tests.

## Docs References

No external documentation is needed for this standard-library test.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Module under test. | [carryover.py](agents-remember/mcp/src/agents_remember/memory/carryover.py) |
| Evidence-tier and ledger-mapping carryover coverage lives beside the worktree tests. | [test_worktree_support.py](agents-remember/mcp/tests/test_worktree_support.py) |

## Update History

- 2026-06-11T15:05+02:00 — Added `EntityCatalogCarryoverTests` and `MemoryOnlyDocCarryoverTests` (8 tests) plus `write_entity_catalog`/`clone_memory`/`candidates_of_kind` helpers; `MemoryOnlyDocCarryoverTests` uses a git clone of official memory so the merge-base evidence path is exercised like a real worktree.
- 2026-06-10T09:45+02:00 — Issue #54 sub-task C: added `MemoryMainAdvanceTests` (5 tests: ff from non-main checkout, ledger-mapped-head ff, already-current, diverged untouched, missing-main skipped).
- 2026-06-10T05:50+02:00 — Created with the route-overview carryover candidates and guarded index regeneration (issue #56 sub-task 3).
