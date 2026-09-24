# dashboard/src/panels/lifecycle-list/landedLeaves.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/lifecycle-list/landedLeaves.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-24T23:30:00+02:00 |
| lastVerifiedCommitHash | `2e11db883f77bb1bf2827ae537b5d1d564e020b3` |
| lastVerifiedCommitDate | 2026-09-24T22:33:57+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**What a master's LANDED leaves are, and the one bound that keeps listing them a list** (`ICR-R33`,
260921-ICR-L33). The module is new in this leaf and exists because of a gap the delivered dashboard had:
`LifecycleList` admitted a leaf row only while its worktree physically existed, and closeout REMOVES the
worktree — so a master whose leaves had all landed rendered as a bare row and its finished work could
not be opened from the operations list at all (measured on the live projection at this leaf's base: a
33-leaf master rendered with 2 children, 31 landed leaves unreachable). The rules that make those leaves
reachable live here rather than inside the list component, because two of them are pure decisions and
one of them — the enclosure join — must not be duplicated.

The module's own header states the bound it is built around, and the bound is the reason it is not a
one-line change: the projection carries ~534 documents against ~57 entries, and *every rule below exists
to keep that gap a decision rather than an accident*.

## Code Commentary

### Logic

- **`leafRecordsLandedWork(doc)`** — a non-master document whose status is `Completed`. That is the
  durable record the requirement names ("a leaf whose task document records it as landed") and the only
  one that survives closeout. `DocStatus` is `planning | inProgress | Completed`, so this admits finished
  work only: a planned, reopened or abandoned leaf stays hidden exactly as it did before.
- **`childFactsByParent(docs, seriesList, docPaths, activeEnclosures)`** — what each row carries as
  children, read from the projection BEFORE any row is materialized, because a closed master's children
  are exactly the rows it does not build. A leaf is counted for the parent its series index resolves
  (`taskDocParentKey`), the same link the rendered rows nest by, so a landed leaf no index resolves is
  never floated to the top instead. Each child is counted once, as `live` (an active enclosure resolves
  it) or `landed` (`!live && leafRecordsLandedWork`).
- **`enclosureForDoc(doc, enclosures)`** — the list's ONE join, moved here so the admission rule (this
  module) and the row builders (the list) cannot disagree about which leaf is which. Enclosure leaf ids
  are lowercase directory names while doc ids are uppercase, so every comparison is case-insensitive;
  the joins are EXACT only, because since `task_reopen` a leaf keeps its exact id.
- **`rowChildFacts(facts)`** — the pair a row renders: `childCount` (live + landed) and `landedCount`.
- **`markAutoCollapsed(rows)`** — the default-collapse rule (R33.4), decided once the NON-landed rows
  exist. A row is held closed only when all three hold: it has landed children, `childCount ===
  landedCount` (every child it carries is one of its own landed leaves), **and** it carries no OTHER rows
  (`structuralChildren.get(row.key) ?? 0 === 0`). The third clause is load-bearing rather than defensive:
  a row that commands other masters, or that an orphaned lifecycle is nested under, would hide those
  rows' work behind a disclosure — measured on the live projection, one such command row owns a 161-row
  subtree (435 rows at the ceiling) including the very master under review.
- **`rowIsCollapsed(item, collapse)`** — the row's collapse state as the reader sees it. An explicit
  collapse wins; otherwise the row's own `autoCollapsed` default decides, and the reader's explicit open
  (`openedKeys`) overrides that default. The two sets live in `useCollapsedTaskGroups`.
- **`landedLeafDocs(input)`** — the pure materialization decision, in projection order: a document that
  is not already materialized, records landed work, resolves a parent that HAS a row, and whose parent is
  open. Everything else stays out, including the deliberate case of a landed leaf with no resolving
  series index ("it is not 'under its master' if there is no master to be under").

### Conventions

TypeScript, no React and no Panda: every export is a pure function or a type over the projection's own
node types (`EnclosureNode`, `SeriesNode`, `TaskDocNode`), importing `pathDir`/`pathStem`/
`taskDocParentKey` from `data/taskHierarchy` and `taskDocSelectionKey` from `data/taskIdentity`. The
module holds no state and reads no clock, so the list can re-derive it on every render and every rule in
it is directly unit-testable through the component.

### Invariants And Boundaries

- **Nothing here mutates the projection.** `markAutoCollapsed` writes only the in-render `OperationRow`
  values the list owns; the docs, enclosures and series nodes are read.
- **`leafRecordsLandedWork` is status-only and master-excluded by construction.** Widening it to, say,
  `abandoned` would admit work that was never landed — the point of the rule is that `Completed` is the
  durable record, and a reopened leaf returns to `planning` and drops out again.
- **The default-collapse rule never applies to a row that carries other rows.** Any future change to
  `markAutoCollapsed` that drops the `structuralChildren` exclusion re-opens the 161-row defect; the
  delivered case `never closes a row that carries OTHER rows, even when its own work has all landed
  (R33.4)` is the guard, and deleting the exclusion turns the full delivered suite from `1708 passed`
  into `1 failed | 1707 passed`.
- **No landed leaf is ever floated.** Materialization requires a resolved parent with a row; the
  boundary is pinned by `keeps a landed leaf that no series index resolves out of the list`, and one real
  leaf (`260713_turn-aware-expectation-supervision/05a_bootstrap-approval-hotfix.json`) is the residual
  instance of that class, deliberately not floating.
- **The module owns decisions, not rendering.** Counters reach the row through `rowChildFacts`, but how
  a closed master SAYS what it carries (`31/33 · inProgress · 31 landed`) is the list's `meta` text.

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured for this repository. This one-to-one card therefore relies on its direct agents-remember
source, the delivered cases and the leaf's own measurement rig.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The landed-leaf admission rule: what a task document must record to be a landed leaf at all. | `leafRecordsLandedWork` | dashboard/src/panels/lifecycle-list/landedLeaves.ts:31-33 |
| What each row carries as children, read before any row is materialized, counted for the parent the series index resolves. | `childFactsByParent`; `rowChildFacts` | dashboard/src/panels/lifecycle-list/landedLeaves.ts:56-77; dashboard/src/panels/lifecycle-list/landedLeaves.ts:97-104 |
| The one enclosure join, owned here so admission and the row builders cannot disagree. | `enclosureForDoc` | dashboard/src/panels/lifecycle-list/landedLeaves.ts:83-95 |
| The default-collapse rule and its row-carries-rows exclusion. | `markAutoCollapsed` | dashboard/src/panels/lifecycle-list/landedLeaves.ts:125-137 |
| The effective collapse predicate the list resolves rows through. | `rowIsCollapsed` | dashboard/src/panels/lifecycle-list/landedLeaves.ts:141-147 |
| The pure materialization decision, and the parent requirement that keeps an unindexed leaf out. | `landedLeafDocs` | dashboard/src/panels/lifecycle-list/landedLeaves.ts:164-177 |
| The list that consumes every rule here and owns the rendering. | `LifecycleListImpl`; `appendLandedLeafRows` | dashboard/src/panels/lifecycle-list/LifecycleList.tsx:235-271; dashboard/src/panels/lifecycle-list/LifecycleList.tsx:566-611 |
| The second half of the reader's collapse state this module's default is resolved against. | `useCollapsedTaskGroups`; `CollapseState` | dashboard/src/panels/useCollapsedTaskGroups.ts:24-30; dashboard/src/panels/useCollapsedTaskGroups.ts:37-51; dashboard/src/panels/lifecycle-list/landedLeaves.ts:14-17 |
| The delivered cases that measure this module's decisions through the real component. | "holds a fully landed master closed by default and reaches its leaf when opened (R33.1/R33.4)"; "shows a master's landed leaves beside its live ones without a click (R33.1)"; "never closes a row that carries OTHER rows, even when its own work has all landed (R33.4)"; "keeps a landed leaf that no series index resolves out of the list (R33.4)" | dashboard/src/panels/lifecycle-list/hierarchy.test.tsx:416-448; dashboard/src/panels/lifecycle-list/hierarchy.test.tsx:449-477; dashboard/src/panels/lifecycle-list/hierarchy.test.tsx:478-602; dashboard/src/panels/lifecycle-list/hierarchy.test.tsx:692-721 |
| The series index the parent join reads. | `taskDocParentKey` | dashboard/src/data/taskHierarchy.ts:58-66 |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and boundary review found no
cross-repository implementation source that governs its behaviour.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-09-24T23:30:00+02:00 — 260921-ICR-L33 curator (candidate `ar/260921-icr-l33-ar`, uncommitted; code base `86639933d61528387ce106dbd4d7a334bd468671` plus the working-tree delta; adversarial round 2 `verify-l33.md` = `pass`): **created — the landed-leaf rules get their own card (177 lines, new file).** The card records the admission rule, the child facts, the single enclosure join, the default-collapse rule with its row-carries-rows exclusion, the effective collapse predicate and the materialization decision, together with the bounds each one exists for and the four delivered cases that measure them through the real component. **Provenance:** this file did not exist at the stamp this card carries — the leaf's code base `86639933…`, the last real commit the reading was taken against — so every claim in it describes the working-tree candidate; the governed closeout owns the real stamp, and the case that the module's central guard is proved by mutation (not by argument) is recorded in the sibling `hierarchy.test.tsx` card and in the leaf's own verifier report.
