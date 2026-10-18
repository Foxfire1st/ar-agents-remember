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

`ReviewScopeHeader` renders the record label (`recordLabelOf`), source inventory count or unavailable
state, and `Read-only`; then an optional currentness line, the joint sync/external movement state and
**one complete movement-facts block as open siblings**. The same selected-read status reaches both
movement renderers. Complete owner statements/reasons stay outside `ScopeMetadata`, including normal
objects and repeated renderings; their actual state/facts roots are marked semantic content.
`FamilyScope` remains marked open content with selected-subject state and limitations. The separate
`ScopeMetadata` retains task/comparison identities, code trees and command: answered metadata is a
closed provenance disclosure, while pending/unavailable metadata is open read-state content.

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
- Movement facts are hidden for pending/failed subjects, not for abnormal measurements in answered subjects; no closed duplicate is retained.
- Display only: no fetch, no local read state, no movement classification, and no control besides the identity disclosure.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.

- The module distinguishes task inventory/code trees from selected-subject comparison/currentness/family lines. [1]
- The header retains its record/inventory/test IDs and mounts the joint movement state and complete guarded facts openly, outside the metadata container. [2]
- Selected-subject scope lines become pending or unavailable statements rather than claiming the previous answer. [3]
- Reconstructed recorded endpoints take precedence over recorded/live task labels. [4]
- The actual workspace maps its ReadingStatus to pending/unavailable/null and passes that status to the header mount. [5]
- The header renders record label, inventory and scope while ScopeMetadata separately retains comparison identities/trees/command; the answered metadata container alone is default-closed provenance. [6]
- FamilyScope remains marked open content and withholds a previous payload limitation while the subject has no answer. [7]
- Selected-subject comparison/currentness/family derivation is payload display with explicit pending/failure guards, not a catalogue read or movement measurement. [8]
