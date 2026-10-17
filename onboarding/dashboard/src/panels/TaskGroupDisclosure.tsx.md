# dashboard/src/panels/TaskGroupDisclosure.tsx

## Governing Overview

[panels/ overview](overview.md)

## Purpose

The native disclosure control for Operations task-group rows. It exposes a compact, keyboard-operable
button for a group with visible descendants without turning disclosure activation into task selection.

## Code Commentary

### Logic

`TaskGroupDisclosure` receives the row label, collapsed state and a toggle callback. It renders a
native `button` with `type="button"`, an accurate Expand/Collapse accessible name, and
`aria-expanded={ !collapsed }`. Pointer-down, key-down, and click handlers stop propagation so the
button remains independent inside the ListBoxItem. Every click invokes the toggle callback, including a parent drawn open for a selected descendant; the parent list owns releasing that hold. aria-expanded describes the supplied collapsed value rather than forcing it locally. A transparent pseudo-element expands the pointer hit area into the adjacent gap without moving the glyph or neighboring marks.

### Conventions

Presentation composes the shared columnLook caret cell with local Panda hover/focus styling and the amber focus-visible treatment. The component owns no state and performs no persistence.

### Invariants And Boundaries

- The component does not select a task, mutate task state, or decide which rows have descendants.
- Parent `LifecycleList` supplies the stable key and owns collapse persistence.
- `aria-expanded` always describes the supplied collapsed state.

### Todos

None known for this leaf.

## Evidence

### Docs References

No relevant documentation found after checking the resolved `system/sources.md`; it has no configured
Domain Documentation entries. Accessibility semantics are proved by the native control and focused
repository tests.

No configured domain-documentation source was available for this local UI primitive.

### Repo-Internal References

- The native button always invokes the isolated disclosure callback; its transparent hit area extends beyond the unchanged glyph cell. [4]


- RowCaret mounts the disclosure only for a non-flat parent, passing actual collapsed state and a callback that delegates the held-state decision to the list. [1]


- The parent list mounts `TaskGroupDisclosure` for the descendant-bearing row. [2]


- Focused tests verify native button semantics, accessible names, aria-expanded state, and selection isolation. [3]


### Cross-Repo References

No meaningful cross-repo references found.

The control is local to the dashboard panels route and has no cross-repository interface.
