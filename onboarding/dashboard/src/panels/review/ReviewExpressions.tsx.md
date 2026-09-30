# ReviewExpressions.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/ReviewExpressions.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T22:35:02+02:00 |
| lastVerifiedCommitHash | `3dc2ab0cf59cdc87ec478f6563d4ac6696871076`|
| lastVerifiedCommitDate | 2026-09-30T23:11:04+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[overview.md](../overview.md)

## Purpose

Render actual bound source and test diffs directly after the selected intent in the central reading path.

**Since MIK-L31 this is the dataset (unconverted) review's expression view only.** For a tree comparison the centre
renders the focused expression cards (`ExpressionCards.tsx`, MIK-R31) instead of this file accordion; a dataset
review makes no tree read and still renders this component unchanged (review F8's narrowed claim). The one change
here is that `ExpressionControls` (the diff layout and full-file toggles) is exported, so the cards reuse the same
controls and state.

## Code Commentary

### Logic

The center supplies `linksIncomplete` from the selected family's real completeness state. Loaded linked-file counts and empty-expression copy describe only what has loaded, and incomplete scope points to roster continuation. Missing links do not assert absent stored attribution or unchanged expressions.

For selected invariants, expression selection also uses the exact retained revisions of the authoritative subject read. A confirmed no-family subject can still reach its registered source expressions through payload attribution; the full inventory remains independently reachable.

expressionSelection joins exact selected invariant revision IDs to attributed locations and member sources, then intersects those paths with the complete measured source inventory. A separately selected inventory file remains inspectable and is labelled outside selected intent when appropriate. Without semantic selection it opens the selected file or first inventory entry. ExpressionCard delegates bytes to SourceContent with the inventory exact before/after tree IDs. Layout, full-file disclosure and open path remain caller-owned state.

### Conventions

Use the existing owner interfaces and exact recorded identities; keep transient task evidence outside durable onboarding.

### Invariants And Boundaries

Linked expressions do not replace or filter the full source inventory in the rail. An unlisted source reference is not an invented changed file. The component reads no arbitrary dataset or working-tree path.

### Todos

None recorded. A partial or unavailable roster remains explicitly incomplete; the independent source explorer still reaches the complete change.

## Docs References

No Domain Documentation source is configured. The implementation-specific account is grounded in the repository source below.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain source could be checked. | — | — |

## Repo-Internal References

The named constructs own this behavior; reads and validation use their existing callers and models.

| Finding | Anchor | Source |
| --- | --- | --- |
| `ReviewExpressions` owns the behavior described above. | `ReviewExpressions` | dashboard/src/panels/review/ReviewExpressions.tsx:38-101 |
| `expressionSelection` owns the behavior described above. | `expressionSelection` | dashboard/src/panels/review/ReviewExpressions.tsx:152-180 |
| The layout and full-file controls, exported for the focused cards. | "export function ExpressionControls({" | dashboard/src/panels/review/ReviewExpressions.tsx:103-150 |
| The centre mounts this view only when no cards read applies (a dataset review). | `CenterExpressions` | dashboard/src/panels/review/FamilyReviewCenter.tsx:1003-1059 |
| `ExpressionCard` owns the behavior described above. | `ExpressionCard` | dashboard/src/panels/review/ReviewExpressions.tsx:182-239 |

## Cross-Repo References

No independent cross-repository interface is introduced by this source.

| Finding | Anchor | Source |
| --- | --- | --- |
| No additional cross-repository evidence is required. | — | — |

## Update History

- 2026-09-30T22:35:02+02:00 — 260928-MIK-L33 curator (staged change set on `ar/260928-mik-l33`, code base `c052b2593b85d9baf425cc1d5c46f384b13fc9ea`; review R1 changes-required, R2 and R3 pass-with-notes, each followed by a fix round, with the merge round after MIK-L34): No content impact: citation repair only; this document's own source is unchanged by MIK-L33. Rows citing MIK-L33's changed sources (`FamilyReviewCenter.tsx`) moved with the leaf's inserted lines: 1 passing row(s) normalised by the fixer. No claim wording changed, and no verification stamp was advanced.
- 2026-09-30T20:14:26+02:00 — 260928-MIK-L34 curator (staged change set on `ar/260928-mik-l34`, code base `904e804b07a598d5d6c66f06b7e67ddab64d9b8e`; reviews R1 to R3 changes-required, each followed by a fix round): No content impact: MIK-R34 inserted one import line in `FamilyReviewCenter.tsx`, so the fixer normalised the `CenterExpressions` row (`992-1048` → `993-1049`). The claim is unchanged. No stamp advanced.
- 2026-09-30T13:23:08+02:00 — 260928-MIK-L35 curator (staged change set on `ar/260928-mik-l35`, code base `ce4594231eac0b18950d22d6aee0d3b9f3eba3db`; review R1 changes-required, R2 pass-with-notes, R2-1 fixed): No content impact: the caller row into `FamilyReviewCenter.tsx`, which this leaf changed, was normalised by the installed fixer to where `CenterExpressions` now sits (`973-1029` → `992-1048`). Claim wording unchanged. No stamp advanced.
- 2026-09-30T10:05:09+02:00 — 260928-MIK-L31 curator (staged change set on `ar/260928-mik-l31`, code base `48f680d5b95b8cb6eafff4f1ccd19c8f32e8c48c`; review R3 pass-with-notes): body update. Purpose records that this is now the dataset review's expression view (a tree comparison renders MIK-R31's focused cards) and that `ExpressionControls` is exported for the cards; two rows added.

- 2026-09-27T00:59:43+00:00 — Replaced the resolved projection-gap note with the current loaded-link contract. Empty/partial copy no longer claims absent stored links; the complete source inventory and selected-subject source authority stay independent.
- 2026-09-26T21:21:39Z — Recorded the upstream continuation projection limit without reclassifying stored realizations as absent.
- 2026-09-26T21:09:29+00:00: Generated citation repair: `expressionSelection` repointed to dashboard/src/panels/review/ReviewExpressions.tsx:147-175. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T21:09:29+00:00: Generated citation repair: `ExpressionCard` repointed to dashboard/src/panels/review/ReviewExpressions.tsx:177-234. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T20:20:54Z — Reconciled authoritative subject reads, exact revision comparison and accessible selection behavior.

- 2026-09-26T19:49:05Z — Created the unified source-expression rendering card.
