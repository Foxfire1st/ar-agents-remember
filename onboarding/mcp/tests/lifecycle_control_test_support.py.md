# mcp/tests/lifecycle_control_test_support.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/lifecycle_control_test_support.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `99dc249bd507c20b09ece1169c2b1fa2af8e8c1b` |
| lastVerifiedCommitDate | 2026-09-02T05:53:10+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Provides public lifecycle-control helpers for tests that own a current generation.

## Code Commentary

### Logic

Builders preserve canonical generation, contract, worker, and control identity so tests do not hand-author partial journal state.

Since 260831-CCR (commit `99dc249b`) the completed-disposition authority helper
`publish_completed_disposition_task_authority` (line 39) builds the leaf through the real
JSON-primary store and stamps a current route review via
`build_route_review(contract, ResolvedTaskDocument(...), payload, now=...)` (line 87-93): the leaf
document is read/updated through `read_task_doc`/the task store when present or created through
`json_path_for` + `write_task_doc`, and the review is built with a fixed `now` instead of a
hand-authored candidate tree. The stamped `RouteReviewRecord` carries the canonical
`task-intent/v1` digest, so lifecycle-control tests exercise current intent-bound review evidence.

### Conventions

Tests execute production owners and use shared builders only for canonical setup. Scenario-specific
differences remain in the test so fixtures do not become a parallel implementation.

### Invariants And Boundaries

- The suite preserves loud negative cases and exact identity/refusal assertions; it does not obtain
  green through a fallback, allowlist, or weakened production threshold.
- Dagger owns certifying execution. Any direct execution remains bounded diagnostic evidence only.
- Completed-disposition fixtures publish current, intent-bound route reviews through the real
  build/stamp path, never hand-authored review rows.

### Todos

None recorded.

## Docs References

The configured Domain Documentation registry is empty. No external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain source is required for this repository-owned test contract. | `FIXTURE_GRADE_JUDGMENT` | mcp/tests/lifecycle_control_test_support.py:1-240 |

## Repo-Internal References

The test file is direct evidence for the production boundary named above.

| Finding | Anchor | Source |
| --- | --- | --- |
| The selected scenarios and assertions implement this test unit's forcing proof. | `FIXTURE_GRADE_JUDGMENT` | mcp/tests/lifecycle_control_test_support.py:1-240 |
| Completed-disposition task authority is built through the store and a fixed-now route review. | `publish_completed_disposition_task_authority`; `build_route_review` | mcp/tests/lifecycle_control_test_support.py:39-103; mcp/tests/lifecycle_control_test_support.py:87-93 |
| The typed candidate ref derived for the leaf document. | `document_ref` | mcp/tests/lifecycle_control_test_support.py:45-63 |

## Cross-Repo References

No cross-repository source is allowed by the resolved settings.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository reference applies. | `FIXTURE_GRADE_JUDGMENT` | mcp/tests/lifecycle_control_test_support.py:1-240 |

## CCR-R02@v2 Intent-Bound Fixture Reviews

Per `requirements/CCR-R02-v2-normative-task-intent-identity.md`, published reviews bind canonical
task intent; the fixture now writes leaf docs through the JSON-primary store and builds the review
through the production owner so lifecycle-control tests operate on current, intent-bound evidence.
Part of the landed L25 candidate `99dc249b`.

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for 99dc249bd507 (CCR-R02@v2/L25):
  the completed-disposition helper now builds the leaf through the task store and stamps a
  fixed-now, intent-bound route review via `build_route_review` over the resolved document.
  Verified at code commit 99dc249bd507c20b09ece1169c2b1fa2af8e8c1b.

- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.
