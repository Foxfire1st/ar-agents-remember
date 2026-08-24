# mcp/tests/test_worktree_integrate_quality_gate.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_worktree_integrate_quality_gate.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:48+02:00 |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb` |
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Integration-seam suite for leaf closeout-proof reuse versus master/full code-quality altitude.

## Code Commentary

### Logic

Leaf integration returns the explicit `certified-at-leaf-closeout` result without calling the
quality decider or executor. Series integration builds the `QualityGateTarget` and uses the full
gate, host-managed when no explicit cap is configured. Dry-run reports without executing and a
master refusal prevents merge. Source-tip cases distinguish unchanged from moved tips, prove a move after
quality blocks before memory replay, and prove the second post-memory recheck blocks immediately
before merge. The memory replay unit matrix pins existing scratch-branch refusal, checkout failure,
rebase conflict, and successful content/ledger rewrite so those legacy helper branches remain
covered without restoring integration-time replay for stale leaf ancestry.

### Conventions

Test-only evidence uses deterministic fakes/fixtures and exercises the owning seam directly.

### Invariants And Boundaries

Acceptance ownership is contract-kind based: leaf integration never reruns targeted acceptance,
while master integration owns full acceptance and carries the worktree group. No
integration mutation occurs after a failed quality gate or either post-quality source movement
check. A stale leaf must sync before integration; replay helpers do not bypass that admission gate.

## Docs References

No Domain Documentation source is configured for this repository-local regression contract.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Current suite declaration anchoring this card. | `integration_contract` | mcp/tests/test_worktree_integrate_quality_gate.py:61-186 |

## Cross-Repo References

No cross-repository implementation source governs this test module.

## L23 Final Candidate Disposition

Integration forcing proves leaf no-rerun versus full master Dagger altitude, mandatory task-derived
diff base, complete pre/post-quality lineage rechecks, pinned source tips, and failure atomicity
before any source ref moves.

## R39 Integration Forcing Evidence

The integration suite now proves leaf integration reuses closeout acceptance without invoking a
gate, while master integration owns full acceptance and blocks before merge on a missing
self-owned wrapper or failed Dagger result. Leaf mode cannot be requested from the integration
gate selector.

## R43 Self Versus Consumer Wrapper Policy

The altitude suite now proves both arms at master integration: Agents Remember without its
self-owned wrapper blocks before merge, while a consumer repository without an opted-in wrapper
reports `wrapper-unavailable` and remains non-blocking. The full gate still runs once when present.

## 260815-DAG-L4 Integration-Authority Forcing

This task extends this suite's production-bound fixtures or assertions for task-derived protected-ref ownership, durable closeout/integration authority, external-memory parity, and fail-closed recovery. The suite continues to exercise the real owner named in its existing purpose; the L4 delta adds exact negative or crash/retry evidence rather than a test-only bypass.

## 260821-CLIVE-L2 Current Regression Contract

The current forcing seams include `test_git_fixture_helper_surfaces_command_failures`, `test_external_recovery_proves_the_exact_task_memory_head`, `test_completed_integration_recovery_must_match_exactly`, `test_integrate_result_refuses_completed_contract_without_durable_recovery`. The L2 additions force public worktree consumers through closed configured-contract admission, mutation-owner reread, journal recovery, and fail-closed destructive cleanup.

### Reconciled Source Evidence

| Finding | Citations | Source Path |
| --- | --- | --- |
| The current test source exercises `test_git_fixture_helper_surfaces_command_failures`, `test_external_recovery_proves_the_exact_task_memory_head`, `test_completed_integration_recovery_must_match_exactly`, `test_integrate_result_refuses_completed_contract_without_durable_recovery`. | L220-L222; L224-L241; L243-L291; L293-L312 | `mcp/tests/test_worktree_integrate_quality_gate.py` |

## Current Contract — 260821 CLIVE Final

This is the current source-backed contract for this test card. It supersedes any earlier
queue-lifecycle, blocker-row, replan/drain, or compatibility-reader wording where present.

Forces altitude-aware integration quality admission, certification, dry-run behavior, external-memory recovery, and protected integration execution.

### Current Invariants

- The quality result is journaled certification evidence, not a queue field.
- Dry-run is pure; apply revalidates exact inputs and protected refs before the irreversible edge.

## Update History

- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: reconciled this test card to current source while preserving prior history and verification provenance.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this test card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-20T05:12+02:00 — L11 landed-wave refresh: the leaf-segment graph-model commit
  (f2e2f4b9) touched this source; card re-verified against the current file, verification stamp
  advanced to f2e2f4b9. Body unchanged — the documented contract still holds.


- 2026-08-17T12:30+02:00 — No content impact: L5 extends the suite for the altitude-routed organizational full gate; the documented quality-gate ownership is unchanged.

- 2026-08-16T07:05+02:00 — L4 review repair: completed apply without a durable recovery tuple now refuses before queue completion; read-only completed preview remains non-mutating.
- 2026-08-16T05:18+02:00 — Dagger fixture repair: the post-memory source-move unit case executes its publication callback through an isolated queue-owner seam with a valid operation key, retaining the real two-stage source recheck.
- 2026-08-16T04:06+02:00 — Dagger fixture repair: series gates use a real approved closeout commit, queue-claim mocks isolate pre-merge memory blockers, and source movement patches exact named-ref reads.
- 2026-08-15T23:38+02:00 — Reconciled the suite's L4 fixture and forcing role for protected integration branches, durable operation authority, external-memory parity, and recovery. Verification metadata remains closeout-owned.

- 2026-08-15T11:07+02:00 — No content impact: corrected the synthetic task root to the canonical
  coordination hierarchy required by queue scope resolution; quality-gate assertions are unchanged.
- 2026-08-14T12:13:26+02:00 — R43 curator: added the consumer-master non-blocking counterpart to
  the self-repository missing-wrapper refusal. Verification remains closeout-owned.

- 2026-08-14T11:27+02:00 — R39 curator: replaced leaf rerun expectations with certified-commit
  reuse and master-only full enforcement. Verification remains closeout-owned.
- 2026-08-14T09:37+02:00 — Reopened L23 cadence proof: the leaf seam asserts zero quality-decider
  and executor calls, while the series seam retains the single full Dagger run and refusal boundary.
- 2026-08-14T06:40+02:00 — L23 final candidate review: integration tests prove targeted leaf versus
  full master Dagger altitude, mandatory diff base, pre/post-quality lineage rechecks, pinned source
  tips, and failure atomicity before refs move.

- 2026-08-13T12:53+02:00 — L23 Dagger-rail coverage: recorded exact source-tip unchanged/moved
  behavior, both post-quality/pre-merge rechecks, and the complete memory replay helper branch
  matrix. Verification provenance remains closeout-owned.


- 2026-08-13T08:40+02:00 — L23 integration-gate repair: added the post-quality source-tip movement refusal and proved memory replay plus source merge remain untouched. Verification metadata remains closeout-owned.

- 2026-08-12T07:10+02:00 — 260731-EFA-L24 curator: added the
  absent-cap/host-managed integration proof while retaining explicit settings-
  cap and altitude-routing coverage. Verification metadata remains pinned
  until closeout stamps L24.

- 2026-08-11T19:58+02:00 — Reconciled `test_worktree_integrate_quality_gate.py` with its current structural task/seat, tool-vocabulary, or quality-boundary regression contract and removed stale exact-id/leaf implications where present.
- 2026-08-08T02:00+02:00 — 260731-EFA-L17 curator: created this file-level
  onboarding card for the new integration-altitude suite; content derived from
  the current worktree source. Verification metadata pinned until closeout
  stamps the 260731-EFA-L17 commit.
