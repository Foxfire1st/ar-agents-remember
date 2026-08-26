# mcp/src/agents_remember/memory_quality/curator_checklist.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/curator_checklist.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-15T09:10+02:00 |
| lastVerifiedCommitHash |  `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`|
| lastVerifiedCommitDate |  2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[memory quality overview](overview.md)

## Purpose

This module owns the curator's single enclosure-local memory-quality checklist. It turns the full
contract-scoped quality result, current-additions coverage, route-index preview, drift rows, and
report-only evidence into one deterministically ordered Markdown worklist that is atomically
replaced at `reports/curator-memory-quality.md`.

## Code Commentary

### Logic

`report_path_for` derives the reserved path from the worktree group. A full check separates
repairable findings from the one truthful closeout-only class: missing citation provenance on a
new, still-untracked onboarding card. It obtains the tracked set from the memory worktree rather
than treating every missing-provenance row as harmless historical debt
cit:([`report_path_for`, `split_commit_owned_findings`, `_tracked_onboarding_paths`], mcp/src/agents_remember/memory_quality/curator_checklist.py:53-76; mcp/src/agents_remember/memory_quality/curator_checklist.py:129-135).

`write_curator_checklist` sorts repair rows, missing sidecars, stale indexes, actionable drift
candidates, closeout-owned provenance, and noteworthy report-only rows before it derives the
zeroable curator count. It writes through `atomic_write_text`, so a reader sees the previous
complete checklist or the next complete checklist, never a partial report
cit:([`write_curator_checklist`], mcp/src/agents_remember/memory_quality/curator_checklist.py:79-126).
The renderer preserves the important distinction between a zeroable pre-closeout gate and dirty
source/real-commit evidence that must remain visible until governed closeout supplies a real
commit cit:([`_render`, `_append_drift`], mcp/src/agents_remember/memory_quality/curator_checklist.py:182-240; mcp/src/agents_remember/memory_quality/curator_checklist.py:293-319).

### Conventions

- The report filename is stable and contains no timestamp; generation time lives inside the file.
- Every list is sorted before rendering so identical inputs produce the same work order.
- Markdown cells collapse whitespace and escape table separators so finding text cannot corrupt
  the checklist layout.

### Invariants And Boundaries

- The checklist is operational, not onboarding, task state, or commit evidence.
- Only an untracked new card's missing provenance is closeout-owned. A tracked card with the same
  finding remains curator-actionable so historical debt cannot be hidden.
- `curatorActionableCount` is exactly repairable memory findings plus missing onboarding plus stale
  route indexes. Drift/source-change candidates remain explicit but cannot require a fabricated
  pre-commit verification stamp.
- The writer owns no quality classification, onboarding mutation, route-index mutation, or
  cleanup. It renders already-computed results and atomically publishes one file.

### Todos

None.

## Docs References

No Domain Documentation source is configured for this repository; the checklist contract is
package-owned.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The application layer decides when the report exists, and worktree cleanup owns its lifecycle.

| Finding | Anchor | Source |
| --- | --- | --- |
| A leaf scope derives the report path from the contract's worktree group; only a full scoped check requests rows and writes the checklist. | `resolve_leaf_memory_scope`; `_resolve_execution`; `_execute_memory_quality`; `_attach_curator_checklist` | mcp/src/agents_remember/application/memory_scope.py:91-143; mcp/src/agents_remember/application/memory_quality/controller.py:147-162; mcp/src/agents_remember/application/memory_quality/controller.py:165-190; mcp/src/agents_remember/application/memory_quality/controller.py:193-247 |
| Cleanup removes the reserved reports directory before it attempts to remove the enclosure. | `_removed_directories` | mcp/src/agents_remember/worktrees/modules/cleanup.py:532-559 |
| The enclosure regression proves same-path overwrite, one-file cardinality, component-count arithmetic, and subset-call non-interference. | `test_full_contract_check_replaces_one_enclosure_local_curator_report`; `test_subset_contract_check_does_not_replace_the_curator_report` | mcp/tests/test_memory_tool_enclosure_scope.py:242-269; mcp/tests/test_memory_tool_enclosure_scope.py:271-287 |

## Cross-Repo References

No cross-repository implementation owns this package-local report contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260815-DAG-L3 Structured Readiness Artifact

A full contract-scoped checklist write now atomically emits `curator-memory-quality.json` beside
the Markdown report. The attestation binds schema, checklist status and counts, the exact
source-change candidate rows, onboarding/report paths, and the SHA-256 of the rendered report;
the response exposes `attestationPath`.

## Update History

- 2026-08-15T09:10+02:00 — L3 content update: documented the structured curator readiness
  attestation and rendered-report digest; verification remains closeout-owned.

- 2026-08-11T16:54+02:00 — Created for the enclosure-local, atomically overwritten curator
  memory-quality checklist and its repairable-versus-closeout-owned classification boundary.