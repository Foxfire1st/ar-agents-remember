# mcp/tests/lifecycle_control_test_support.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/lifecycle_control_test_support.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-14T20:00+02:00 |
| lastVerifiedCommitHash | `bb65a2073228c5e143b055a470f39c6c9e2f4d9d` |
| lastVerifiedCommitDate | 2026-09-14T19:36:04+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Provides public lifecycle-control helpers for tests that own a current generation.

## Code Commentary

### Logic

Builders preserve canonical generation, contract, worker and control identity. Existing door scheduling provenance supplies the judgment ID when present; the explicit standalone case detaches only the asserted singleton fixture sprint through the task store before returning master-scoped caller authority. This support module has no collected tests and does not itself establish coverage.

Since 260831-CCR (commit `99dc249b`) the completed-disposition authority helper
`publish_completed_disposition_task_authority` (line 40) builds the leaf through the real
JSON-primary store and stamps a current route review via
`build_route_review(contract, ResolvedTaskDocument(...), payload, now=...)` (lines 92-107): the leaf
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
| No external domain source is required for this repository-owned test contract. | `FIXTURE_GRADE_JUDGMENT` | mcp/tests/lifecycle_control_test_support.py:1-255 |

## Repo-Internal References

The helper source establishes fixture construction; retained consumer assertions determine actual protection.

| Finding | Anchor | Source |
| --- | --- | --- |
| The fixed fixture judgment is used only when no selected door supplies scheduling provenance. | `FIXTURE_GRADE_JUDGMENT` | mcp/tests/lifecycle_control_test_support.py:1-255 |
| Completed-disposition task authority is built through the store and a fixed-now route review. | "def publish_completed_disposition_task_authority(" | mcp/tests/lifecycle_control_test_support.py:40-199 |
| Completed task authority derives the typed candidate reference inside the store-backed publication. | "def publish_completed_disposition_task_authority(" | mcp/tests/lifecycle_control_test_support.py:40-199 |

## Cross-Repo References

No cross-repository source is allowed by the resolved settings.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository reference applies. | `FIXTURE_GRADE_JUDGMENT` | mcp/tests/lifecycle_control_test_support.py:1-255 |

## CCR-R02@v2 Intent-Bound Fixture Reviews

Per `requirements/CCR-R02-v2-normative-task-intent-identity.md`, published reviews bind canonical
task intent; the fixture now writes leaf docs through the JSON-primary store and builds the review
through the production owner so lifecycle-control tests operate on current, intent-bound evidence.
Part of the landed L25 candidate `99dc249b`.

## Update History

- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the live-door swap is the
  frozen change and the earlier entry records it. Re-checked the fixture-judgment fallback at
  `:48-50` and the fixed-`now` review builder at `:92-107`: they hold. No wording changed.
  Verification metadata remains closeout-owned.
- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification):
  `mcp/tests/lifecycle_control_test_support.py` changed since the recorded verification commit.
  Re-read the card against the frozen on-disk source and re-checked its claims and cited ranges:
  nothing this card asserts is falsified by the change, so no wording changed. Verification metadata
  remains closeout-owned; no verification stamp advanced.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the source gained the
  `live_closeout_door` import and now reads the door live. Re-derived the helper line references and
  every cited range against the current source (the module is now 255 lines). No claim text changed;
  verification metadata remains closeout-owned.
- 2026-09-09T02:42:21+02:00 — CCR-L24 inherited/current-source reconciliation 2026-09-09: Re-read the current card purpose, logic, invariants, and cited route against the frozen candidate source; no content or route change was required, and the existing claim bytes remain accurate. source-sha256=2cb7e45718692cdac660fd95989334e883bcef26b048e34ee0290ecfd5dc59e3; verification metadata remains unchanged because commit-owned realization is pending.


- 2026-09-06T23:08:28+00:00 — Reconciled retained source behavior and fixture limitations for IAS recovery; prior verification pins retained.

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for 99dc249bd507 (CCR-R02@v2/L25):
  the completed-disposition helper now builds the leaf through the task store and stamps a
  fixed-now, intent-bound route review via `build_route_review` over the resolved document.
  Verified at code commit 99dc249bd507c20b09ece1169c2b1fa2af8e8c1b.

- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.
