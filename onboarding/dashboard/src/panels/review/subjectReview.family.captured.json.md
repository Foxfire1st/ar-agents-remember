# subjectReview.family.captured.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/subjectReview.family.captured.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-28T16:55:00+02:00 |
| lastVerifiedCommitHash | `9b2f775f1ab0fca5f82b4f661785dd8216d4a8b3`|
| lastVerifiedCommitDate | 2026-09-28T17:43:09+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[overview.md](../overview.md)

## Purpose

Retain a captured family-selected response for subject-navigation regressions.

## Code Commentary

### Logic

The family response records its own selected family context and record-channel availability. It is paired with the invariant-selected response to prove a family read cannot establish a member assessment absence. The fixture is test evidence, not a current production dataset or invented authored judgment. The body is a real review-route response re-captured over HTTP (route bytes omit null fields); its receipt row in `subjectReview.capture-provenance.json` names the command, source tree, scenario and requests. Each of its 10 member sources carries the structured `locator`, `resolved_ranges` and `locator_state` fields; every locator here is a `file` locator, so the sources are `whole_file` on the exact recorded blob or `unresolved` otherwise, and none carries a range.

### Conventions

Keep captured provenance and exact input identities intact. Only the test harness selects these fixtures.

### Invariants And Boundaries

This source supplies scoped regression evidence, not semantic approval, execution certification or a replacement for the real mounted workflow.

### Todos

No additional work is asserted by this card.

## Docs References

No Domain Documentation source is configured; the fixture and regression source establish this local test contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain source could be checked. | — | — |

## Repo-Internal References

The named case or selected revision field is the direct source of this test input.

| Finding | Anchor | Source |
| --- | --- | --- |
| The case or fixture preserves its own selected input. | "revision_selection" | dashboard/src/panels/review/subjectReview.family.captured.json:76-79 |
| The member sources carry their structured locator state as the route emits it. | "locator_state" | dashboard/src/panels/review/subjectReview.family.captured.json:1-2323 |
| The receipt row naming this body's re-capture command, source tree and requests. | "subjectReview.family.captured.json" | dashboard/src/panels/review/subjectReview.capture-provenance.json:5-26 |

## Cross-Repo References

No independent cross-repository authority is introduced.

| Finding | Anchor | Source |
| --- | --- | --- |
| No additional cross-repository evidence is required. | — | — |

## Update History

- 2026-09-28T16:55:00+02:00 — 260921-ICR-L44 curator (uncommitted change set on `ar/260921-icr-l44`, code base `55c62237132eaa56b0df28ae5a8420a8dc05303d`): the body is now a real review-route response re-captured over HTTP (route bytes omit null fields), and its ten member sources carry the structured locator fields; recorded that, cited the locator state and the receipt row, and re-measured the selection range. No verification stamp was advanced.

- 2026-09-26T20:20:54Z — Created the scoped source/progression or selected-subject regression card.
