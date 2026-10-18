# ReviewExpressions.tsx — retired renderer

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Retirement

The source was deleted. Its dataset-only file accordion, revision-to-location selection and file-card expansion no longer run; no equivalent accordion relocated. The original card and sidecar remain in their existing custody for retirement/history, not as an active implementation claim.

The separately reusable ExpressionControls presentation controls were extracted to ExpressionControls.tsx. That extraction does not preserve ReviewExpressions behavior. CenterExpressions now renders focused cards or the measured-tree-comparison explanation. SourceContent remains for expression-card Full file only.

## Retained Historical Account

The following account describes the removed implementation only. Its present-tense clauses and numbered reference labels are historical, not current product promises or live citations. The current retirement boundary and surviving owners are documented separately.

> # ReviewExpressions.tsx
>
> ## Governing Overview
>
> [overview.md](../overview.md)
>
> ## Purpose
>
> Render actual bound source and test diffs directly after the selected intent in the central reading path.
>
> **Since MIK-L31 this is the dataset (unconverted) review's expression view only.** For a tree comparison the centre
> renders the focused expression cards (`ExpressionCards.tsx`, MIK-R31) instead of this file accordion; a dataset
> review makes no tree read and still renders this component unchanged (review F8's narrowed claim). The one change
> here is that `ExpressionControls` (the diff layout and full-file toggles) is exported, so the cards reuse the same
> controls and state.
>
> ## Code Commentary
>
> ### Logic
>
> The center supplies `linksIncomplete` from the selected family's real completeness state. Loaded linked-file counts and empty-expression copy describe only what has loaded, and incomplete scope points to roster continuation. Missing links do not assert absent stored attribution or unchanged expressions.
>
> For selected invariants, expression selection uses the exact retained revisions of the authoritative subject read. A confirmed no-family subject can still use its registered source locations. Independent changed-file actions use All changes in the comparison viewer when a recorded tree comparison is available; without that range the action states `comparison_not_recorded`, rather than inventing an explorer or comparison.
>
> expressionSelection joins exact selected invariant revision IDs to attributed locations and member sources, then intersects those paths with the complete measured source inventory. A separately selected inventory file remains inspectable and is labelled outside selected intent when appropriate. Without semantic selection it opens the selected file or first inventory entry. ExpressionCard delegates bytes to SourceContent with the inventory exact before/after tree IDs. Layout, full-file disclosure and open path remain caller-owned state.
>
> ### Conventions
>
> Use the existing owner interfaces and exact recorded identities; keep transient task evidence outside durable onboarding.
>
> ### Invariants And Boundaries
>
> Linked expression selection does not redefine the complete source inventory. An unlisted source reference is not an invented changed file. The retained dataset expression renderer is not a full-inventory rail; current independent changed-file navigation is the comparison-page destination, with named refusal when no recorded range exists. This component reads no arbitrary dataset or working-tree path.
>
> ### Todos
>
> None recorded. A partial or unavailable roster remains explicitly incomplete; semantic continuation stays in the main reading area. Independent changed-file inspection belongs to the comparison page when its recorded range is available, not a source explorer.
>
> ## Evidence
>
> ### Docs References
>
> No Domain Documentation source is configured. The implementation-specific account is grounded in the repository source below.
>
> No configured domain source could be checked.
>
> ### Repo-Internal References
>
> The named constructs own this behavior; reads and validation use their existing callers and models.
>
> - `ReviewExpressions` owns the behavior described above. (historical reference 1)
> - `expressionSelection` owns the behavior described above. (historical reference 2)
> - The layout and full-file controls, exported for the focused cards. (historical reference 3)
> - The centre mounts this view only when no cards read applies (a dataset review). (historical reference 4)
> - `ExpressionCard` owns the behavior described above. (historical reference 5)
>
> ### Cross-Repo References
>
> No independent cross-repository interface is introduced by this source.
>
> No additional cross-repository evidence is required.
> - Dataset-only expression accordion in the central path (historical reference 6)
> - Shared diff layout and full-file controls for cards reuse (historical reference 7)
> - Revision-to-location join for the selected intent (historical reference 8)
> - Card byte delegation with exact inventory tree identities (historical reference 9)

## Evidence

- Surviving controls are independent presentation callbacks, not a relocated accordion. [10]
- CenterExpressions has no retired file-view fallback. [11]
