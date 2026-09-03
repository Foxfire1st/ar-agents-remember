# mcp/tests/test_closeout_queue_task_doc_status.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_closeout_queue_task_doc_status.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `3e276f2b2052b641afbee180a472259f21b500df` |
| lastVerifiedCommitDate | 2026-09-02T14:46:34+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[governing overview](overview.md)

## Purpose

Proves task-document completion routes through the closeout queue quiescence owner and forces the
L04 mutation-classified projection scope: task truth publishes first, scope is resolved before
publication, and evidence/audit-only deltas select no task-driven projection refresh.

## Code Commentary

The production task-doc publisher is exercised so an in-flight queue candidate prevents an
otherwise terminal status publication. The L04 additions build real sprint/leaf documents and
assert classifier-gated scope selection: reference/statusNote edits resolve an empty scope, a
completion edit resolves the affected sprint, a contract lifecycle restamp resolves no scope, an
empty scope publishes without opening the queue store, and a scope-refusal (unclassified delta)
happens before any task publication side effect. Event ordering in
`test_scope_preflight_precedes_task_first_fixed_order_invalidation` pins the
validated/sources/resolved/task-published sequence.

## Invariants And Boundaries

- The suite exercises production owners rather than copying their state-transition logic.
- Refusal cases assert no unauthorized Git, contract, queue, task, or memory mutation.
- Crash/retry cases retain exact durable identity and expected-old facts.
- Scope resolution precedes publication; a scope refusal or unclassified delta never writes task truth.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The focused suite owns task-first publication and per-scope projection-effect containment. | `TaskFactPublicationTests` | mcp/tests/test_closeout_queue_task_doc_status.py:132-370 |
| Scope refusals and empty scopes happen before any publication side effect. | `test_scope_refusal_happens_before_task_publication`; `test_empty_projection_scope_publishes_without_queue_churn` | mcp/tests/test_closeout_queue_task_doc_status.py:193-212; mcp/tests/test_closeout_queue_task_doc_status.py:214-227 |
| Evidence/audit-only, completion, and lifecycle-restamp deltas select exact scopes. | `test_evidence_and_audit_only_delta_selects_no_task_driven_scope`; `test_completion_delta_selects_the_affected_sprint`; `test_contract_lifecycle_restamp_selects_no_task_driven_scope` | mcp/tests/test_closeout_queue_task_doc_status.py:229-244; mcp/tests/test_closeout_queue_task_doc_status.py:246-256; mcp/tests/test_closeout_queue_task_doc_status.py:258-278 |

## Docs References

No configured Domain Documentation or cross-repository source applies to this repository-local forcing suite.

## Cross-Repo References

No meaningful cross-repository boundary is exercised.

## Current Contract — 260821 CLIVE Final + L04 Mutation Scope

This is the current source-backed contract for this test card. It supersedes any earlier
queue-lifecycle, blocker-row, replan/drain, or compatibility-reader wording where present.

Forces task-first publication across zero, one, and multiple sprint scopes with machine-readable invalidation/rebuild effects, and now proves the classifier gates which changes select any scope at all.

### Current Invariants

- Task truth persists even when projection refresh fails.
- Every affected scope reports its exact prior state, invalidation, rebuild result, and next action.
- A mutation that does not invalidate projections publishes task truth with zero queue churn.

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for
  3e276f2b2052b641afbee180a472259f21b500df (CCR-R04@v1/L04): recorded the L04 scope-classification
  forcing cases — scope-before-publication ordering, refusal-before-write, empty-scope
  no-queue-churn, evidence/audit-only no-scope, completion sprint scope, and lifecycle-restamp
  no-scope. Verification is pinned to the owning commit.

- 2026-08-26T10:44:52+02:00 — No content impact: reviewed the closeout-projection package relocation; task-doc status projection forcing is unchanged.

- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: reconciled this test card to current source while preserving prior history and verification provenance.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.

- 2026-08-15T23:38+02:00 — 260815-DAG-L4: created queue-owned task completion forcing onboarding from the frozen integration-authority candidate. Verification remains closeout-owned.
