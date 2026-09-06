# mcp/src/agents_remember/memory_quality/curator_checklist.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/curator_checklist.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `fbc89847233b1c5959f56475f2cb51f936d5ef0b` |
| lastVerifiedCommitDate | 2026-09-02T07:47:04+02:00|
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
commit cit:([`_render`, `_append_drift`], mcp/src/agents_remember/memory_quality/curator_checklist.py:181-237; mcp/src/agents_remember/memory_quality/curator_checklist.py:290-316).

Under CCR-R03@v1 `CuratorChecklist` now carries the exact `code_candidate_tree` and
`memory_candidate_tree`, and the attestation embeds the `memory-quality-attestation/v1` dependency
declaration built from the pair, both trees, and the rendered-report SHA-256 — so the checklist
attestation content-addresses exactly the candidate trees it inspected
cit:([`CuratorChecklist`, `write_curator_checklist`], mcp/src/agents_remember/memory_quality/curator_checklist.py:34-51; mcp/src/agents_remember/memory_quality/curator_checklist.py:88-173).

### Conventions

- The report filename is stable and contains no timestamp; generation time lives inside the file.
- Every list is sorted before rendering so identical inputs produce the same work order.
- Markdown cells collapse whitespace and escape table separators so finding text cannot corrupt
  the checklist layout.
- The attestation's dependency declaration is generated from the exact candidate trees and report
  digest, matching what the coherence observer re-requires.

### Invariants And Boundaries

- The checklist is operational, not onboarding, task state, or commit evidence.
- Only an untracked new card's missing provenance is closeout-owned. A tracked card with the same
  finding remains curator-actionable so historical debt cannot be hidden.
- `curatorActionableCount` is exactly repairable memory findings plus missing onboarding plus stale
  route indexes. Drift/source-change candidates remain explicit but cannot require a fabricated
  pre-commit verification stamp.
- The writer owns no quality classification, onboarding mutation, route-index mutation, or
  cleanup. It renders already-computed results and atomically publishes one file.
- The attestation binds the exact code/memory candidate trees; a changed tree produces a different
  dependency declaration and stales the attestation.

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
| A leaf scope derives the report path from the contract's worktree group; only a full scoped check requests rows and writes the checklist. | `resolve_leaf_memory_scope`; `_resolve_execution`; `_execute_memory_quality`; `_attach_curator_checklist` | mcp/src/agents_remember/application/memory_scope.py:107-131; mcp/src/agents_remember/application/memory_quality/controller.py:295-315; mcp/src/agents_remember/application/memory_quality/controller.py:318-360; mcp/src/agents_remember/application/memory_quality/controller.py:363-441 |
| Cleanup removes the reserved reports directory before it attempts to remove the enclosure. | `_removed_directories` | mcp/src/agents_remember/worktrees/modules/cleanup.py:532-559 |
| The checklist writer owns the enclosure report projection; deleted regression fixtures do not supply a current pass. | `write_curator_checklist` | mcp/src/agents_remember/memory_quality/curator_checklist.py:88-171 |
| R03 attestation dependency declaration source. | `memory_quality_attestation_dependencies` | mcp/src/agents_remember/models/lifecycles/curator_coherence.py:91-129 |

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

## MCAR-L02 Deterministic Attestation Source

The checklist renderer no longer embeds wall-clock time. Identical quality/candidate input now
reproduces identical Markdown and `ar-curator-memory-quality/v1` bytes, so a harmless rerun cannot
stale an accepted coherence generation. Changed findings or candidate tuples still change the
digest and correctly force republishing. The completion text points to the structured coherence
authority rather than a hand-authored report.

## MCAR-L03 Pair-Bound Attestation

The structured memory-quality attestation now carries the full exact pair identity, and its
generated checklist displays the contract and pair digest. The attestation therefore cannot be
reused for another valid checkout or branch pair.

## 260831-CCR-R03 Tree-Bound Attestation

The attestation now also declares the exact code/memory candidate trees it inspected, so changing
either tree stales the checklist attestation (worker handover:
notes/reports/260902-CCR-L03-worker-delivery.md).

## Update History

- 2026-09-04T01:48+02:00 — 260831-CCR-L08 Gate-5 memory pass: re-anchored the controller cells of the checklist row (resolve/execute/attach to 295-315/318-360/363-441, duplicate attach cell removed) shifted by the CCR-R08 +57-line controller insertion. Citation-only re-anchor; no content impact.

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for fbc89847233b1c5959f56475f2cb51f936d5ef0b (CCR-R03@v1/L03): recorded the candidate-tree fields on the checklist and the tree-bound attestation dependency declaration; prior sorting, atomic-write, and pair-binding prose preserved.

- 2026-08-29T21:46+02:00 — MCAR-L03: bound the curator worklist and structured attestation to the
  exact code/memory pair. Verification remains closeout-owned.

- 2026-08-29T08:52+02:00 — Removed timestamp entropy and redirected candidate disposition to the
  structured coherence authority. Verification remains closeout-owned.

- 2026-08-15T09:10+02:00 — L3 content update: documented the structured curator readiness
  attestation and rendered-report digest; verification remains closeout-owned.

- 2026-08-11T16:54+02:00 — Created for the enclosure-local, atomically overwritten curator
  memory-quality checklist and its repairable-versus-closeout-owned classification boundary.