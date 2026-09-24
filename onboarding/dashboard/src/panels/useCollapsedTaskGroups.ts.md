# dashboard/src/panels/useCollapsedTaskGroups.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/useCollapsedTaskGroups.ts` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-12T12:58+02:00                           |
| lastVerifiedCommitHash | `2e11db883f77bb1bf2827ae537b5d1d564e020b3`       |
| lastVerifiedCommitDate | 2026-09-24T22:33:57+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels/ overview](overview.md)

## Purpose

Owns the Operations task-group disclosure preference — **both halves of it since 260921-ICR-L33**: the
keys the READER collapsed, and the keys the reader OPENED past a row's own default. Rows are expanded
on first use, an explicitly collapsed row stays collapsed, and a row the projection holds closed by
default (a master whose only children are its landed leaves) stays closed until the reader opens it —
and stays open afterwards. Both sets persist across dashboard refreshes and component remounts.

## Code Commentary

### Logic

`useCollapsedTaskGroups` initializes TWO `Set<string>`s from `localStorage` when running in a browser
(`readKeys`), otherwise returning empty sets for non-browser rendering. `operations.tasks.collapsed.v1`
keeps its published meaning — a key in it is a row the READER collapsed — and
`operations.tasks.opened.v1` is the second half 260921-ICR-L33 added: the keys the reader opened past a
row's own default. Keeping the two apart is what lets the default rule stay a function of the
projection (it can change as work lands or starts) without ever rewriting the reader's own choice.
The hook returns `{ collapsedKeys, openedKeys, setCollapsed }`. `setCollapsed(key, collapsed)` takes the
RESOLVED next state from the caller — the only layer that knows the row's default — and immutably adds
the key to one set and removes it from the other (`writeKeys`), so a key never lives in both and the
effective state is unambiguous whatever the projection does afterwards. The pre-260921-ICR-L33
`toggleCollapsed(key)` invert-on-call callback is gone: inverting in the hook cannot represent "open the
row the projection closed by default", because the hook does not know that default exists.

### Conventions

The hook follows the dashboard's small persisted-flag pattern: the storage key is versioned, the public
state is a `ReadonlySet`, and the hook returns a stable callback via `useCallback`.

### Invariants And Boundaries

- Unrecorded groups are expanded by default; a key present in neither set takes the row's own
default, which is `false` for every row except the auto-collapsed landed-master rows the list marks.
- A key lives in at most one of the two sets: `setCollapsed` adds to `collapsed` and deletes from
`opened` (or the reverse) in the same call, so the two can never contradict each other.
- Persistence is keyed by stable typed task-selection keys, never labels or array positions.
- The hook owns presentation preference only; it does not filter BY PHASE, clear selection, or mutate task data.
- The app-written v1 payload is intentionally trusted; no migration or corruption fallback is part of this leaf.

### Todos

None known for this leaf.

## 260921-ICR-L33 The Second Half Of The Collapse State

The v1 array was the whole of this hook's state for as long as every closed row was one the reader had
closed. `ICR-R33.4` broke that: the projection itself now holds some rows closed — a master with no
live worktree work, whose only children are its own landed leaves — and "the reader opened it" is not
representable in a set that only records collapses. The fix is a second array rather than a second
meaning for the first: `operations.tasks.opened.v1` records the opens, `operations.tasks.collapsed.v1`
keeps recording the collapses, and `LifecycleList`'s `rowIsCollapsed` resolves them against the row's
own default (explicit collapse wins; otherwise the default, overridden by an explicit open). The public
signature changed with it — `toggleCollapsed` became `setCollapsed(key, collapsed)` — because the
caller resolves the next state and the hook only stores it. **Nothing about the persistence contract
weakened:** both payloads are still the app-written v1 JSON arrays this hook trusts, keyed by stable
typed task-selection keys, and the hook still owns presentation preference only.

## Docs References

No relevant documentation found after checking the resolved `system/sources.md`; it has no configured
Domain Documentation entries. The storage behavior is a local application contract covered by tests.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain-documentation source was available for this local hook. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The parent list applies the hook only to BY REPO hierarchy visibility and leaves selection/detail separate. | `LifecycleListImpl` | dashboard/src/panels/lifecycle-list/LifecycleList.tsx:224-259 |
| Focused tests verify stable storage keys, remount persistence, independent nested state, and expanded defaults; the landed-master cases pin that a default-collapsed row opens, that its landed leaf is then reachable, and that a row carrying OTHER rows is never auto-collapsed. | "operations.tasks.collapsed.v1"; "holds a fully landed master closed by default and reaches its leaf when opened (R33.1/R33.4)"; "never closes a row that carries OTHER rows, even when its own work has all landed (R33.4)" | dashboard/src/panels/lifecycle-list/hierarchy.test.tsx:213-231; dashboard/src/panels/lifecycle-list/hierarchy.test.tsx:416-448; dashboard/src/panels/lifecycle-list/hierarchy.test.tsx:478-602 |
| The existing persisted-flag pattern was the worker's local implementation reference. | `usePersistedFlag` | dashboard/src/panels/file-viewer/usePersistedFlag.ts:6-25 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| The preference is local to the dashboard browser surface and has no cross-repository interface. | — | — |

## Update History

- 2026-09-24T23:30:00+02:00 — 260921-ICR-L33 curator (candidate `ar/260921-icr-l33-ar`, uncommitted; code base `86639933d61528387ce106dbd4d7a334bd468671` plus the working-tree delta; adversarial round 2 `verify-l33.md` = `pass`): **body update — the hook now owns both halves of the collapse state.** The Purpose, Logic, Invariants and the section above record `openedKeys`/`setCollapsed` and the new `operations.tasks.opened.v1` key; the sentence that described `toggleCollapsed` as the hook's single callback was false at this candidate and was corrected in place. The one range this pass moved (the focused-tests row, into a `hierarchy.test.tsx` this leaf grew) was re-derived against the candidate with the gate's own resolver. **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted and the governed closeout owns the real stamp.
- 2026-08-02T16:44:57+02:00 — L6 W1-B02 curator: repaired 3 repository-internal citations for the parent list, focused persistence tests, and persisted-flag reference.
- 2026-07-12T12:58+02:00 — Created for 260712-TRH-L3. Candidate source is uncommitted; verification metadata
  is pinned to the leaf base until closeout stamps the eventual code commit.
