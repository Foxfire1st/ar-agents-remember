# ReviewExpressions.tsx

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

## Evidence

### Docs References

No Domain Documentation source is configured. The implementation-specific account is grounded in the repository source below.

No configured domain source could be checked.

### Repo-Internal References

The named constructs own this behavior; reads and validation use their existing callers and models.

- `ReviewExpressions` owns the behavior described above. [1]
- `expressionSelection` owns the behavior described above. [2]
- The layout and full-file controls, exported for the focused cards. [3]
- The centre mounts this view only when no cards read applies (a dataset review). [4]
- `ExpressionCard` owns the behavior described above. [5]

### Cross-Repo References

No independent cross-repository interface is introduced by this source.

No additional cross-repository evidence is required.
