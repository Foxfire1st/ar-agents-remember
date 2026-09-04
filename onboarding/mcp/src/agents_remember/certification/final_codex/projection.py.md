# mcp/src/agents_remember/certification/final_codex/projection.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/final_codex/projection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T22:45+02:00 |
| lastVerifiedCommitHash | `54ff803a05209e06f732f2de1f90e2a71a069e08` |
| lastVerifiedCommitDate | 2026-09-04T22:31:30+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[Certification contract overview](../overview.md)

## Purpose

Readiness projection for the two-fresh-no-retry final real-Codex Gate-4 lane (leaf 260831-CCR-L14, code commit 54ff803a). The projection answers one question per exact candidate: is the lane empty (not-started), is a live attempt running, is the terminal run a current two-fresh-pass eligible for its certificate, is it red (any failed/aborted/hard-failure/retried composition), or is it stale (the run no longer binds the current frozen plan)? Diagnostic evidence never satisfies this lane: it neither unblocks nor blocks here.

## Code Commentary

### Logic

- `FinalCodexLaneDisposition` (lines 34-40) is the closed disposition vocabulary: not-started, running, two-fresh-pass, red, stale.
- `FinalCodexLaneProjection` (lines 45-68) is the frozen projection with a self-verified `projectionDigest`; its validator (`_verify_shape`) refuses a not-started lane carrying a manifest/readiness, a running lane without an incomplete live attempt, and any terminal shape that violates `_require_terminal_projection` (lines 71-85: two-fresh-pass requires aggregate green plus certificate readiness; red/stale can never be certificate-ready).
- `project_final_codex_lane` (lines 88-113) reads the newest run manifest from the store: empty lane projects not-started; an incomplete live attempt projects running; a terminal run that no longer binds the current plan projects stale; a current terminal run projects two-fresh-pass only when the aggregate is green, else red.
- `final_codex_certificate_ready` (lines 116-125) is the boolean readiness gate used by the run controller before certificate compilation.
- `_run_is_current` (lines 128-142) compares the attempt's bound plan identity against the current plan record.

### Conventions

Projections are frozen models with content digests; the disposition vocabulary is closed and never extends.

### Invariants And Boundaries

- An empty lane has no scenario step, no owner, and no certificate.
- A terminal run is two-fresh-pass only when both repetitions passed with distinct fresh identities, retryCount zero, and the run is current for the frozen plan.
- Any red, partial, aborted, hard-failure, or stale run blocks certificate readiness and can never be compensated by the other repetition.
- Diagnostic evidence never unblocks and never blocks this lane.

### Todos

None.

## Docs References

The approved CCR-R14@v3 requirement packet and the leaf doc 14_final-real-codex-certification govern this module; task-artifact paths are not repo-relative citations, so clauses are recorded as prose here.

| Finding | Anchor | Source |
| --- | --- | --- |
| Two-fresh-pass requires a current green aggregate and flips certificate readiness on. | `project_final_codex_lane` | mcp/src/agents_remember/certification/final_codex/projection.py:88-113 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The projection reads the newest candidate run manifest from the durable store. | `FinalCodexManifestStore`.`manifest` | mcp/src/agents_remember/certification/final_codex/store.py:72-75 |
| The run manifest aggregate and completeness drive the terminal dispositions. | `aggregate`; `complete` | mcp/src/agents_remember/certification/final_codex/models.py:392-404 |
| The frozen plan identity comes from the plan record. | `FinalCodexPlanRecord` | mcp/src/agents_remember/certification/final_codex/models.py:173-199 |
| Content digests use the shared certification digest helper. | `content_digest` | mcp/src/agents_remember/certification/digests.py:1-80 |

## Cross-Repo References

No cross-repository implementation boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| The projection stays repository-neutral and never consults repository-selected engines. | `CandidateIdentity` | mcp/src/agents_remember/certification/models.py:1-200 |

## Update History

- 2026-09-04T22:45+02:00 - 260831-CCR-L14 Gate-5 memory pass: created this card for the new CCR-R14 final-codex lane readiness projection delivered in code commit 54ff803a; anchors and ranges derived from the current worktree source and pinned to that commit (tree aff2e268968397ab8db042a782652957a3600dda).
