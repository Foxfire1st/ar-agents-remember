# mcp/tests/test_lifecycle_operations.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_lifecycle_operations.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:46+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489` |
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Asynchronous lifecycle operation launch and cancellation authority.

## Code Commentary

### Logic

Starting returns queued immediately and an exact duplicate observes one launch. A contract lease excludes cross-kind or terminal mutation. Before the boundary, cancellation proves worker exit before releasing its authority. After commit proof, cancellation refuses with immutable-output recovery required and keeps approval claimed.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Public projection omits worker internals. An irreversible result cannot make spent approval reusable or turn cancellation into rollback.

### Todos

No file-local implementation change is requested by this reconciliation.

## Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain evidence applies to the file-local claims above. | N/A | N/A |

## Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

| Finding | Anchor | Source |
| --- | --- | --- |
| Start returns immediately and duplicate observes one launch. | `test_start_returns_immediately_and_duplicate_observes_one_launch` | mcp/tests/test_lifecycle_operations.py:40-57 |
| Contract lifecycle lease excludes cross kind and terminal mutation. | `test_contract_lifecycle_lease_excludes_cross_kind_and_terminal_mutation` | mcp/tests/test_lifecycle_operations.py:60-71 |
| Cancel before boundary proves exit before releasing worker authority. | `test_cancel_before_boundary_proves_exit_before_releasing_worker_authority` | mcp/tests/test_lifecycle_operations.py:74-135 |
| Cancel after boundary refuses without making approval reusable. | `test_cancel_after_boundary_refuses_without_making_approval_reusable` | mcp/tests/test_lifecycle_operations.py:138-162 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:46+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.

- 2026-09-04T10:05+02:00 — 260831-CCR-L18 Gate-5 memory pass: recorded the new operation-location developer-decision binding test. Verified at code commit f93ac631ca161e5880db3a937728cb256686b13b.

- 2026-09-03T12:30+02:00 -- 260831-CCR memory curation pass for 685f83c44055 (CCR-R22@v1/L22): recorded the certification_profile config mock in lifecycle operation dispatch tests.


- 2026-08-29T16:27+02:00 — Extended detached-launch forcing to require ownership transfer of the
  exact `Popen` object to the lifecycle reaper.

- 2026-08-25T15:44+02:00 — PDLS whole-system reconciliation updated the implementation summary
  above after source and requirement review. Verification remains closeout-owned.


- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this test card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1 candidate-11: rebound truthful `queueReleaseFailure`/`safeToReplace` dispatch forcing and the public irreversible-integrate cancellation relationship against accepted tree `4241908c`; verification metadata remains pinned until governed closeout.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: lifecycle-operation imports moved under
  `worktrees/integration/` and `TaskRef` under `application/task_docs/`; the lease-refusal test now
  drives `lease.__enter__()` explicitly and the `killpg` mock follows the moved module. Verified at code
  commit e5cb139f.
- 2026-08-16T07:05+02:00 — L4 Dagger repair: the closeout dispatch fixture now performs the real queued-to-running-to-completed journal transitions before starting integration, preserving cross-operation lease semantics.
- 2026-08-16T05:18+02:00 — Dagger fixture repair: integration worker dispatch carries the real absolute runtime settings path created by the shared contract fixture.
- 2026-08-16T04:06+02:00 — Dagger fixture repair: operation inputs reference a real workspace settings file and cancellation preview patches the canonical configured-contract resolver.
- 2026-08-15T23:38+02:00 — Reconciled the suite's L4 fixture and forcing role for protected integration branches, durable operation authority, external-memory parity, and recovery. Verification metadata remains closeout-owned.
- 2026-08-14T06:38+02:00 — L23 final candidate review: lifecycle-operation tests cover idempotent
  start/observe, conflicting fingerprints, detached recovery, monotonic terminal evidence, and the
  pre/post-claim boundary. Verification remains closeout-owned.

- 2026-08-13T09:05+02:00 — L23 curator: reviewed the operation-model import move and confirmed the
  tested lifecycle contract is unchanged; final provenance remains closeout-owned.

- 2026-08-12T16:54+02:00 — 260731-EFA-L23 installed-runtime repair: extended detached-launch proof
  to preserve the installed runtime `PYTHONPATH` and exclude unpublished task-checkout source, paired
  with the packaged-entry service-binding proof. Focused verification remains code-owned; memory
  provenance remains closeout-owned.

- 2026-08-12T16:52+02:00 — 260731-EFA-L23 packaged-worker repair: extended the existing parser/main
  regression to prove default worktree services are built and bound before worker dispatch. The
  focused test passes with configuration-owned xdist auto; verification provenance remains
  closeout-owned.

- 2026-08-12T15:19+02:00 — Created with L23's complete durable lifecycle operation forcing suite; verification provenance remains closeout-owned.
