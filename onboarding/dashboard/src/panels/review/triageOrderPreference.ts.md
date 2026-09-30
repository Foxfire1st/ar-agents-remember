# dashboard/src/panels/review/triageOrderPreference.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/triageOrderPreference.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T22:21:58+02:00 |
| lastVerifiedCommitHash | `3dc2ab0cf59cdc87ec478f6563d4ac6696871076`|
| lastVerifiedCommitDate | 2026-09-30T23:11:04+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

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

## Docs References

No domain documentation source is configured; the requirement packet `MIK-R33@v1` (adopting `ICR-R32@v1`) and the architect's rulings in `33_review-triage-order-and-change-kind-badges.json` live outside the code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's statement: browser-local, triage by default, no server state. | "It is a browser-local UI preference" | dashboard/src/panels/review/triageOrderPreference.ts:1-5 |
| The key and the read that falls back to triage. | `TREE_ORDER_KEY`; `readTreeOrder` | dashboard/src/panels/review/triageOrderPreference.ts:12-20 |
| The store and its hook. | `treeOrderStore`; `useTreeOrder` | dashboard/src/panels/review/triageOrderPreference.ts:35-47 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T22:21:58+02:00 — 260928-MIK-L33 curator (staged change set on `ar/260928-mik-l33`, code base `c052b2593b85d9baf425cc1d5c46f384b13fc9ea`; review R1 changes-required, R2 and R3 pass-with-notes, each followed by a fix round, with the merge round after MIK-L34): created this card for the new order-preference module of MIK-R33. The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
