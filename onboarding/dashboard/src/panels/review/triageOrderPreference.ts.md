# dashboard/src/panels/review/triageOrderPreference.ts

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**The family tree's order choice (MIK-R33, ICR-R32@v1 rule 8): triage order by default, or pure authored order.** A
browser-local UI preference (`review.tree-order.v1`) in the house persisted-store idiom (vanilla zustand seeded from
localStorage, as `intentDiffPreference.ts`); no server state is added.

## Code Commentary

### Logic

- `readTreeOrder` returns `authored` only for that stored value; any other value, absent storage or a throwing storage
  gives `triage`.
- `treeOrderStore.setOrder` writes the value (a storage failure is swallowed, so the control still works for the page's
  lifetime) and updates the store; `useTreeOrder` subscribes the tree, the controls and the centre.

### Conventions

47 lines; the key is versioned.

### Invariants And Boundaries

If storage is unavailable, triage order applies (rule 8); nothing here is review state.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured; the requirement packet `MIK-R33@v1` (adopting `ICR-R32@v1`) and the architect's rulings in `33_review-triage-order-and-change-kind-badges.json` live outside the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module's statement: browser-local, triage by default, no server state. [1]
- The key and the read that falls back to triage. [2]
- The store and its hook. [3]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
