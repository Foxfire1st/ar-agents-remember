# mcp/tests/test_final_codex_projection.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_final_codex_projection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T22:45+02:00 |
| lastVerifiedCommitHash | `54ff803a05209e06f732f2de1f90e2a71a069e08` |
| lastVerifiedCommitDate | 2026-09-04T22:31:30+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Standalone CCR-R14 lane-projection tests (leaf 260831-CCR-L14, code commit 54ff803a). Covers the readiness projection: an empty lane is not-started, a live attempt with no complete run is running, only the exact two-fresh-pass green run is certificate-ready, a one-pass/one-fail run stays red, and a changed plan marks a terminal run stale until a newer run binds the current plan. Fully standalone: imports only the leaf-local builder module and the package under test.

## Code Commentary

### Logic

`two_fresh` (lines 30-53) reserves, marks running, and publishes the two repetition slots, optionally failing the first. `FinalCodexProjectionTests` (lines 54-105) covers: an empty lane projecting not-started (55-61); a live attempt projecting running (62-71); the two-fresh-pass lane being certificate-ready (72-79); a one-pass/one-fail run staying red and never certificate-ready (80-87); a plan change staling the terminal run (88-100); and separate lane projections per candidate (101-105).

### Conventions

All projections are frozen models with verified digests; dispositions come from the closed vocabulary.

### Invariants And Boundaries

- Only the exact current two-fresh-pass run is certificate-ready.
- Red or stale lanes can never be certificate-ready, and one pass never compensates the other.
- An empty lane carries no manifest and no readiness.

### Todos

None.

## Docs References

No Domain Documentation source is configured for this memory root. CCR-R14@v3 (approved packet, leaf 14_final-real-codex-certification) requires the readiness projection semantics; task artifact paths are not repo-relative citations, so clauses are recorded as prose.

| Finding | Anchor | Source |
| --- | --- | --- |
| Only the exact two-fresh-pass lane projects certificate-ready. | `FinalCodexProjectionTests` | mcp/tests/test_final_codex_projection.py:54-105 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Exercises the lane readiness projection helpers. | `project_final_codex_lane`; `final_codex_certificate_ready` | mcp/src/agents_remember/certification/final_codex/projection.py:88-113; mcp/src/agents_remember/certification/final_codex/projection.py:116-125 |
| The shared leaf builders publish the two-fresh runs the projection reads. | `two_fresh`; `publish_run` | mcp/tests/test_final_codex_projection.py:30-53; mcp/tests/test_final_codex_models.py:480-494 |

## Cross-Repo References

No cross-repository evidence is required.

| Finding | Anchor | Source |
| --- | --- | --- |
| Every case is in-process and repository-neutral. | - | - |

## Update History

- 2026-09-04T22:45+02:00 - 260831-CCR-L14 Gate-5 memory pass: created this card for the new standalone CCR-R14 lane-projection suite delivered in code commit 54ff803a; anchors and ranges derived from the current worktree source and pinned to that commit (tree aff2e268968397ab8db042a782652957a3600dda).
