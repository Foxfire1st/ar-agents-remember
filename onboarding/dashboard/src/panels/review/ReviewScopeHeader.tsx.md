# dashboard/src/panels/review/ReviewScopeHeader.tsx

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

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- **The module's own statement of which lines are the task's and which describe one subject's read.** [1]
- The header and its test ids. [2]
- The subject-bound lines, replaced while pending or unavailable. [3]
- The record label. [4]
- The workspace mounts it with a status derived from `reading`. [5]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
