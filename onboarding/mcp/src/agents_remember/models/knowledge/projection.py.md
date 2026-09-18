# mcp/src/agents_remember/models/knowledge/projection.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge/projection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T06:05+02:00 |
| lastVerifiedCommitHash | `15fe8678fc0f87eaac4606952f179135ebe392c4` |
| lastVerifiedCommitDate | 2026-09-18T07:49:45+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l18` uncommitted source; base `e963a01c` |
| governingOverview | `mcp/src/agents_remember/models/overview.md` |

## Governing Overview

[models route overview](../../../overview.md)

## Purpose

The projection rule, and the whole of it is one property: **a projection may display an assessment,
and when it does the assessment's provenance and status travel with it** — its author, its exact
examined inputs and its recorded disposition.

## Code Commentary

### Logic

`AssessmentDisplay` carries the recorded `disposition` verbatim, the recorded `author`, the exactly
recorded `examined_inputs`, and a `status` drawn from `ASSESSMENT_STATUSES` — `current` or `stale`,
exhaustive on purpose. Its validator refuses a blank author and refuses a display with no examined
inputs, so a conclusion cannot be rendered without its basis. `status` is *measured from the examined
inputs* rather than stored beside them, which is why a stale assessment stays stale: nothing here
re-judges and no path upgrades a status.

`ProjectionRow.assessment` is `None` for an unassessed claim rather than an instance with empty
fields, because an instance with empty fields is a *present* assessment that happens to say nothing.
`assessment_display` is the one constructor and it derives the status from the row's recorded inputs.

### Invariants And Boundaries

- **Missing stays missing.** An unassessed claim renders as unassessed; there is no favourable
  default and no manufactured approval.
- **A disagreement is displayed, not resolved.** Picking a winner between two assessments would be a
  new interpretation rather than a rendering.
- **No field can hold a conclusion, a severity or a recommendation**, so a projection cannot acquire
  one by accident.
- **Nothing here persists, publishes or deletes.** The module imports no store, holds no handle and
  writes no file: a projection is derived and regenerable, never a second authority. Regenerating it
  is the only way it changes.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **The two statuses a displayed assessment can carry, exhaustive because the assessment either examined the inputs the row now rests on or it did not.** | `ASSESSMENT_STATUSES` | mcp/src/agents_remember/models/knowledge/projection.py:53-53 |
| **The display that refuses a conclusion without its basis: a recorded disposition, a named author and the exact examined inputs.** | `AssessmentDisplay` | mcp/src/agents_remember/models/knowledge/projection.py:56-92 |
| **The row whose missing assessment is `None` rather than an empty instance, and the one constructor that measures the status from the recorded inputs.** | `ProjectionRow`; `assessment_display` | mcp/src/agents_remember/models/knowledge/projection.py:94-120; mcp/src/agents_remember/models/knowledge/projection.py:122-148 |
| The models vocabulary this rule is built on. | `KnowledgeModel` | mcp/src/agents_remember/models/knowledge/base.py:1-58 |
| **The cases that measure the three consequences: a conclusion without its basis is refused, a missing assessment renders missing, and a stale assessment is never upgraded.** | `test_a_projection_display_refuses_a_conclusion_without_its_basis`; `test_a_projection_row_renders_a_missing_assessment_as_missing`; `test_a_stale_assessment_is_measured_from_its_examined_inputs_and_never_upgraded` | mcp/tests/test_knowledge_citation_bindings.py:377-431 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T06:05+02:00 — 260915-KS-L18 curator (uncommitted change set on `ar/260915-ks-l18`, base `e963a01c`): created this one-to-one card for the projection rule `KS-R18@v1` §3 introduces. It records the property the module exists to enforce — **a displayed assessment carries its disposition, its author and its exact examined inputs** — and the three consequences that are enforced rather than documented: a missing assessment is `None` on the row (an empty instance would be a *present* assessment saying nothing), a stale assessment is measured from its examined inputs and never upgraded, and there is no field for a conclusion, severity or recommendation, so a projection cannot acquire one by accident. The card also records that the module persists nothing and holds no store handle, which is what makes "a projection is derived and regenerable, never a second authority" structural rather than promised. Verification metadata advances to the leaf's base commit `e963a01c` because every cited construct was re-read against the working tree; the code commit does not exist yet and closeout owns that stamp.
