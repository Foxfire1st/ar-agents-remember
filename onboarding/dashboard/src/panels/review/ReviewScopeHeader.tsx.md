# dashboard/src/panels/review/ReviewScopeHeader.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/ReviewScopeHeader.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-28T21:46:34+02:00 |
| lastVerifiedCommitHash |  `ae2fd5c864aa2609ae45b5c7dbbaa693569aefc6`|
| lastVerifiedCommitDate |  2026-09-28T22:11:57+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The review workspace's scope header: which task comparison this is, its source inventory, and — behind a
"Comparison details" disclosure — its identities. Extracted from `ReviewWorkspace.tsx` in `260921-ICR-L48`
(L47-R1-F5 file budget) and taught one new thing: while the selected subject is pending or could not be
read, the lines that describe **one subject's read** say so instead of describing the previous subject's
read under the new selection (`ICR-R26` isolation under a retained shell).

## Code Commentary

### Logic

`ReviewScopeHeader` renders the record label (`recordLabelOf`), the task's source inventory count (or
"Source inventory unavailable"), and "Read-only"; then an optional currentness line; then the disclosure
with the task identifiers, the comparison line, the before → after code trees and the family-context line.

**Two kinds of line.** The inventory, the code trees and the record label are the **task's**, whichever
subject is selected, so they always come from the payload the workspace is mounted over. The comparison
identity, currentness and family-context lines describe **one subject's read**; `subjectScopeOf(payload,
status)` returns them. With `status === 'pending'` they read "being read" and currentness is omitted; with
`status === 'unavailable'` they read "could not be read" / "No family context was read"; with `null` (the
payload answers the subject) they are the payload's own: currentness only when `staleness.state` is not
`current` (stale → "Comparison has changed · refresh before relying on this view."; not measured →
"Currentness not measured · inspect the comparison details."), the comparison reference and policy, and
`families_returned of families_total · state`.

`recordLabelOf` distinguishes reconstructed recorded endpoints (`history:reconstructed-recorded-endpoints`
limitation) from a recorded and a live task comparison.

### Conventions

Panda `css` for styles, one module-level `muted` constant. Test ids are the contract and are unchanged by
the extraction: `review-scope-header`, `review-scope-record`, `review-currentness-status`,
`review-scope-task`, `review-scope-comparison`, `review-scope-families`. `status` is derived by the
workspace from its `reading` (`null`, `'pending'`, `'unavailable'`).

### Invariants And Boundaries

- While the selected subject has no answer, no line of this header states the previous subject's
  comparison reference, currentness or family context.
- Task-level facts (inventory, trees, record) are never withheld while a subject is pending.
- Display only: no read, no state, no control besides the disclosure.

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
| **The module's own statement of which lines are the task's and which describe one subject's read.** | "The inventory and code trees are the task's whichever subject is" | dashboard/src/panels/review/ReviewScopeHeader.tsx:1-4 |
| The header and its test ids. | `ReviewScopeHeader`; `review-scope-header`; `review-scope-comparison`; `review-scope-families` | dashboard/src/panels/review/ReviewScopeHeader.tsx:10-69 |
| The subject-bound lines, replaced while pending or unavailable. | `subjectScopeOf`; "is being read"; "could not be read" | dashboard/src/panels/review/ReviewScopeHeader.tsx:71-106 |
| The record label. | `recordLabelOf`; "Reconstructed from recorded endpoints" | dashboard/src/panels/review/ReviewScopeHeader.tsx:108-112 |
| The workspace mounts it with a status derived from `reading`. | `ReviewScopeHeader`; `status=` | dashboard/src/panels/review/ReviewWorkspace.tsx:237-244 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-28T21:46:34+02:00 — 260921-ICR-L48 curator (uncommitted candidate tree `ac73216e2a763b72844a63b8c36c81f9a8b5f0e8` over code base `cb1b942af60a7ed5006ac992075d2bf96aeb9fa7`): **created this one-to-one card for the scope header extracted from `ReviewWorkspace.tsx`.** The render and its test ids moved unchanged; `recordLabelOf` moved with it; the new `status` input and `subjectScopeOf` replace the subject-bound lines while the selected subject is pending or unavailable (the worker's E6 event found the previous subject's comparison reference still shown while pending, and this is its fix). The verification hash and date are blank because no commit contains this file yet; closeout owns the stamp.
