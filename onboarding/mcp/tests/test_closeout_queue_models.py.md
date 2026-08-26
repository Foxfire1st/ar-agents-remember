# mcp/tests/test_closeout_queue_models.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_closeout_queue_models.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:48+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Owns the strict wire contract for closeout-door generations, disposable closeout projections, and
the public queue response. It keeps scheduling input, source-door truth, projection membership,
and operation-journal identity separate while bounding every persisted collection.

## Code Commentary

### Logic

The door tests accept only waiting, deferred, withdrawn, or claimed dispositions; require exact
operation identity only for a claimed generation; and refuse projection-only actions on the
source-publication request. The projection tests prove that invalid-empty contains no membership
or source identity, terminal empty is still valid-built, member reasons are bounded, and lifecycle
or commit evidence cannot leak into the disposable projection response.

### Invariants And Boundaries

- Door generations are source truth; projections are rebuildable scheduling views.
- A claimed door may reference journal-owned operation identity, but the queue never owns that
  lifecycle evidence.
- Every reason, source problem, member list, and response collection remains bounded.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Door dispositions, claimed-operation identity, and source/projection request separation are fail closed. | `CloseoutDoorModelTests` | mcp/tests/test_closeout_queue_models.py:85-124 |
| Invalid-empty and terminal valid-built projection states carry no illicit membership or lifecycle state. | `CloseoutProjectionModelTests` | mcp/tests/test_closeout_queue_models.py:127-195 |
| Projection member reasons and every persisted wire list are bounded. | `test_member_reasons_and_all_wire_lists_are_bounded` | mcp/tests/test_closeout_queue_models.py:163-195 |

## Current Contract — 260821 CLIVE Final

This is the current source-backed contract for this test card. It supersedes any earlier
queue-lifecycle, blocker-row, replan/drain, or compatibility-reader wording where present.

Forces strict wire invariants for door generations, projection members, projection service condition, bounded evidence, and task references.

### Current Invariants

- Projection condition is exactly valid-built or invalid-empty.
- Unknown, unbounded, or cross-plane lifecycle fields are rejected.

## Update History

- 2026-08-26T10:44:52+02:00 — No content impact: reviewed closeout source/projection package relocations; queue projection model forcing is unchanged.

- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: reconciled this test card to current source while preserving prior history and verification provenance.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-18T09:05+02:00 — Renamed the atomic 'barrier' concept to 'blocker' throughout (terminology unification; no behavioral change). Verification remains closeout-owned.

- 2026-08-15T14:05+02:00 — No content impact: corrected two nested invalid-state assertions to
  the earlier closed-queue quiescence invariant that the real model evaluates first.
- 2026-08-15T13:18+02:00 — No content impact: repository Ruff formatting changed only layout;
  strict request, state, memory-mode, and pending-WAL cases are identical.
- 2026-08-15T13:08+02:00 — No content impact: the invalid-status loop now uses a distinct derived
  payload name instead of overwriting its iteration binding; the exact cases remain identical.
- 2026-08-15T12:53+02:00 — L3 targeted-gate repair: expanded the focused model suite across the
  strict request, metadata, durable-state, memory-mode, and pending-WAL branch matrices.
- 2026-08-15T10:24+02:00 — Created by the L3 file-size repair from tests previously located in
  `test_closeout_queue.py`; assertions and imported production owners are unchanged.