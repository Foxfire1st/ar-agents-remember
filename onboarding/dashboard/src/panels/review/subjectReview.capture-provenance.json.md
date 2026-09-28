# subjectReview.capture-provenance.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/subjectReview.capture-provenance.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-28T16:55:00+02:00 |
| lastVerifiedCommitHash | `9b2f775f1ab0fca5f82b4f661785dd8216d4a8b3`|
| lastVerifiedCommitDate | 2026-09-28T17:43:09+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[overview.md](../overview.md)

## Purpose

Bind each selected-subject test fixture to its actual application-owner response and capture evidence.

## Code Commentary

### Logic

The manifest carries fixture hashes, original response names, provenance artifacts and their hashes, and the captured source tree. It states that disposable-repository responses are test evidence; the assessed case has ambiguous heads and the successor pair is genuinely unique.

The manifest now carries two kinds of entry. The `family` and `invariant` entries describe **real review-route bodies re-captured over HTTP**: each names its own `captured_source_tree`, capture time, command, route, capture-record path and digest, selection rule, structural signature, attempts, scenario and requests, and its `scope` says route bytes omit null fields. The re-capture was needed so these bodies carry each member source's structured `locator`, `resolved_ranges` and `locator_state`. The remaining entries (`successorFamily`, `successorInvariant`, `noFamily`) are still the exact application-owner responses with their original response names and provenance hashes; no route can serve them because they were produced over a hand-built resolution with no leaf enclosure, and they carry no member source. The top-level `captured_source_tree` still describes those owner-produced entries.

The re-capture command names a producer script under the task's notes, outside the repository; it is task-local evidence with an expiry, so re-running it later means re-creating an equivalent producer rather than invoking a tracked tool.

### Conventions

Keep response identities and capture provenance unchanged; tests consume these as captured inputs.

### Invariants And Boundaries

These fixtures are not current project knowledge, new authored judgments or mounted-product acceptance. Missing evidence, ambiguous selection and confirmed absence retain different meanings.

### Todos

No additional work is asserted by this card.

## Docs References

No Domain Documentation source is configured; source and captured responses provide this local test evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain source could be checked. | — | — |

## Repo-Internal References

The case or captured property below records the input this card describes.

| Finding | Anchor | Source |
| --- | --- | --- |
| The case or response retains its declared selected input. | "captured_source_tree" | dashboard/src/panels/review/subjectReview.capture-provenance.json:2-6 |
| **The re-captured family entry: its own source tree, command, route, capture record, selection rule, signature and requests.** | "subjectReview.family.captured.json"; "l44_recapture_review_fixtures.py" | dashboard/src/panels/review/subjectReview.capture-provenance.json:5-26 |
| **The re-captured invariant entry, with the same producer facts.** | "subjectReview.invariant.captured.json" | dashboard/src/panels/review/subjectReview.capture-provenance.json:27-48 |
| The manifest scope distinguishing re-captured route bodies from unchanged owner-produced responses. | "real review-route bodies re-captured" | dashboard/src/panels/review/subjectReview.capture-provenance.json:71-71 |

## Cross-Repo References

Capture provenance names disposable repository evidence; it grants no production knowledge authority.

| Finding | Anchor | Source |
| --- | --- | --- |
| No additional production cross-repository contract is asserted. | — | — |

## Update History

- 2026-09-28T16:55:00+02:00 — 260921-ICR-L44 curator (uncommitted change set on `ar/260921-icr-l44`, code base `55c62237132eaa56b0df28ae5a8420a8dc05303d`): the `family` and `invariant` entries now describe real route re-captures (own source tree, command, route, capture record, selection rule, signature, attempts, scenario, requests) while the other entries remain owner-produced responses; recorded the two entry kinds, the task-local producer's expiry and the new scope sentence, with rows. No verification stamp was advanced.

- 2026-09-26T20:40:46Z — Created the captured subject-selection regression/provenance card.
