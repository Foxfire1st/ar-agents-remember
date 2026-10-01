# dashboard/src/panels/useCollapsedTaskGroups.ts

## Governing Overview

[panels/ overview](overview.md)

## Purpose

Owns the Operations task-group disclosure preference: the keys the READER collapsed. Rows are expanded
on first use, an explicitly collapsed row stays collapsed, and both persist across dashboard refreshes
and component remounts.

> **Corrected by the `260921-ICR-L34` curation, because the code this section described was reverted.**
> This card described the **two-set** state `260921-ICR-L33` introduced (`collapsedKeys` **and**
> `openedKeys`, with a `setCollapsed(key, collapsed)` that resolved the next state in the caller).
> Commit **`a9a1a41b`** — *"Revert L33's operations-list change; clear the pre-existing ruff-format
> red"*, a direct emergency commit with no curator pass behind it — restored this module to its
> 28-line pre-L33 bytes. There is **one** set again (`collapsedKeys`), the callback is
> `toggleCollapsed(key)`, and the second storage key `operations.tasks.opened.v1` does not exist. A
> reader who acted on the paragraph above would have written against an API that is in no tree.

## Code Commentary

### Logic

`useCollapsedTaskGroups` initializes ONE `Set<string>` from `localStorage` when running in a browser,
otherwise an empty set for non-browser rendering. `STORAGE_KEY` is
`operations.tasks.collapsed.v1`, and its published meaning is unchanged: a key in it is a row the
READER collapsed. The hook returns `{ collapsedKeys, toggleCollapsed }`; `toggleCollapsed(key)` inverts
that one key immutably and writes the whole set back
(`window.localStorage.setItem(STORAGE_KEY, JSON.stringify([...next]))`), behind the same
`typeof window === "undefined"` guard the initializer uses. **`openedKeys`, `setCollapsed` and
`CollapseState` exist nowhere in either tree** — the L33 additions were removed by the revert, not
renamed, and the card's former two-set description is deleted rather than re-worded, because a rename
would have been repairable and this was a deletion.

### Conventions

The hook follows the dashboard's small persisted-flag pattern: the storage key is versioned
(`…collapsed.v1`), the public state is a `ReadonlySet`, and the callback is stabilised with
`useCallback`.

### Invariants And Boundaries

- **One set, one meaning.** A key present in `collapsedKeys` is a row the reader collapsed; a key
  present in neither is expanded, which is the module's default.
- Persistence is keyed by stable typed task-selection keys, never labels or array positions.
- The hook owns presentation preference only; it does not filter BY PHASE, clear selection, or mutate
  task data.
- The app-written v1 payload is intentionally trusted; no migration or corruption fallback is part of
  this module.
- **Boundary: the default-collapse rule is not the hook's.** Whatever decides that a row starts closed
  lives in the list component, which is why the hook can stay one inverted set.

### Todos

None recorded. The module is at its pre-L33 shape.

## 260921-ICR-L33 The Second Half Of The Collapse State — **WITHDRAWN BY `a9a1a41b`**

> **This section's claim is no longer true of any tree, and the `260921-ICR-L34` curation is recording
> it rather than deleting the history.** L33 introduced a second persisted array,
> `operations.tasks.opened.v1`, and changed the hook's signature to `setCollapsed(key, collapsed)` so
> the caller could resolve a row's default. Commit **`a9a1a41b`** reverted the operations-list change —
> a direct emergency commit with no curator pass behind it — and the module is back to its 28-line
> pre-L33 shape: one array (`operations.tasks.collapsed.v1`), `toggleCollapsed(key)`, and no
> `openedKeys`, `setCollapsed` or `CollapseState` anywhere in the code tree. The paragraph below is kept
> as the record of what L33 did; **the body above is what the code does now.**

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

## Evidence

### Docs References

No relevant documentation found after checking the resolved `system/sources.md`; it has no configured
Domain Documentation entries. The storage behavior is a local application contract covered by tests.

No configured domain-documentation source was available for this local hook.

### Repo-Internal References

- The parent list applies the hook only to BY REPO hierarchy visibility and leaves selection/detail separate. [1]
- Focused tests verify stable storage keys, remount persistence, independent nested state, and expanded defaults. The landed-master cases this row used to name (`holds a fully landed master closed by default…`, `never closes a row that carries OTHER rows…`) **were deleted with the L33 revert** and no longer exist in `hierarchy.test.tsx`; the row now names the three cases the reverted file really carries. [2]
- The existing persisted-flag pattern was the worker's local implementation reference. [3]

### Cross-Repo References

No meaningful cross-repo references found.

The preference is local to the dashboard browser surface and has no cross-repository interface.
