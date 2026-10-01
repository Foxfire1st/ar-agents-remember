# dashboard/src/panels/LeafAttachPicker.tsx

## Governing Overview

[panels overview](overview.md)

## 260731-EFA-L8 Change

The react-hooks-first remediation memoized the `measure` callback
(`useCallback`) and added it to the effect dependency array; picker behavior is
unchanged.

## Purpose

The **drill-down leaf picker** (Operations Integration L5, leaf-keyed chat registry): the control that
attaches a chat session to a task **leaf**. Its current consumers are the contextual right-rail chat
(`RailChat`) and the full-page cockpit duty bar (`session-cockpit/ChatContextBar`). It replaces a native
`<select>` — whose OS-rendered list was an unthemed white "flashbang"
and dumped every leaf of every series into one flat list. The task hierarchy nests arbitrarily (a master
can itself be a sub-task of another master), so a single grouped list cannot express it; instead one
Panda-themed popover navigates the recursive tree a level at a time — a master row drills **in** (a
"‹ back" breadcrumb returns), a leaf row **attaches**. When a master is in context the picker opens
pre-drilled to it. It deliberately uses plain React state (no React Aria overlay) so it stays trivially
testable: click the trigger, drill, click a leaf.

## Code Commentary

### 260707-HFX2-L17 Explicit Seat Role Picker

The popover now pairs the leaf drill-down with a seat-role chip row. Leaf buttons stay disabled
until a role is selected; spawned/previously typed sessions may preselect a role, untyped
hand-opened harnesses require an operator choice, and plain terminal consumers restrict options to
`terminal`. `onPick` returns both the opaque leaf key and selected role.

### Logic

`LeafAttachPicker({ tree, onPick, contextMaster, label = "Attach to leaf", testId = "attach-leaf-picker",
align = "left", seatRole, roleOptions = ATTACH_SEAT_ROLES })` renders a trigger `<button>` (`{label} ▾`, `aria-haspopup="menu"`, `aria-expanded`,
testid `{testId}`) and, when open, a popover.

- **Props.** `tree: TaskTreeNode[]` is the recursive master→…→leaf hierarchy (built by
  `buildTaskTree` in `data/taskIdentity`); `onPick: (leafKey: string, seatRole: string) => void` is the
  selection callback; `seatRole` optionally preselects current identity; `roleOptions` defaults to the
  attachable seat-role catalog and can be restricted (the terminal duty bar uses `['terminal']`).
  `contextMaster?: string` pre-drills to the in-context master; `label` is the trigger text + menu
  `aria-label`; `testId` prefixes every `data-testid`; `align` (`"left" | "right"`) decides which trigger
  edge the menu pins to.
- **Drill state.** `open` (bool), `path: TaskTreeNode[]` (the drilled master breadcrumb), and `coords`
  (the fixed-position anchor) are React state; `triggerRef` / `menuRef` are element refs. The current
  level is `here = path[path.length - 1]` (the deepest drilled master, or `undefined` at the root) and
  `level = here ? here.children : tree`. `drillInto(node)` pushes a master onto `path`, `back()` pops it,
  and `pick(leafKey)` refuses without a selected role; otherwise it closes the menu, clears `path`, and
  calls `onPick(leafKey, selectedRole)`.
- **Open + pre-drill.** `toggle()` opens/closes; on opening it sets `path` to `findMasterPath(tree,
  contextMaster)` when a `contextMaster` is given (so its leaves show first — "pre-selection via master")
  or `[]` otherwise, and measures the anchor.
- **Portaled, fixed popover.** When `open && coords`, the menu is rendered via `createPortal` into
  `document.body` with `position: fixed` so it escapes the rail's `overflow: hidden` (which was clipping
  it) and any ancestor stacking/transform context. `measure()` reads the trigger's bounding rect and pins
  the menu to the right edge (`align === "right"`, used by `RailChat`) or the left edge (default, used
  by `ChatContextBar`) so it never runs off-screen. A `useLayoutEffect` (active only while open)
  re-measures on `resize` / capturing `scroll`, and wires click-outside (the check spans **both** the
  trigger and the portaled menu, since the menu lives outside the component's DOM subtree) and `Escape`
  to close.
- **Rows.** Inside the menu: a sticky back button (`{testId}-back`, `‹ {here.title}`) when drilled; an
  empty note (`{testId}-empty`) reading "No sub-tasks here." when drilled into an empty master or "No
  tasks available yet." at the top level; otherwise each node in `level` renders either a **leaf** row
  (`role="menuitem"`, `{testId}-leaf`, `data-leaf-key`, disabled until a role is selected, `onClick` →
  `pick(node.leafKey)`) or a **master**
  row (`{testId}-master`, `data-master`, a ▸ chevron, `onClick` → `drillInto(node)`).

### Conventions

Co-located Panda `css()` (no global panel CSS); a dark `bgPanel` popover with amber accents matching the
cockpit. Plain React state + native `<button>`s rather than a React Aria overlay — keeps the drill flow
unit-testable without an overlay harness. `data-testid`s are all `{testId}`-prefixed so the two consumers
(`rail-attach-leaf-picker` for `RailChat`, `chats-attach-leaf-picker` for `ChatContextBar`) get disjoint
implementation hooks; the `chats-*` prefix is not evidence of a retired component. Node titles fall back to the
folder/leaf id inside the tree builder, so this component renders `node.title` directly.

### Invariants And Boundaries

- **Presentational + controlled.** It owns only ephemeral UI state (open / drill path / menu coords /
  selected role). It never reads a store, never fetches, and never performs the attach itself — selection
  is surfaced through `onPick(leafKey, seatRole)`. `RailChat` and `ChatContextBar` then perform the
  server-first attach/move and apply local assignment only after acceptance.
- **Tree is supplied, not built here.** The recursive hierarchy comes in as the `tree` prop; this
  component only navigates and renders it. Arbitrary nesting is handled generically — a nested master is
  just a master node sitting inside another master node.
- **Leaf key is opaque.** It passes `node.leafKey` straight through to `onPick` without parsing it.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- The `TaskTreeNode` shape it drills and `findMasterPath` it pre-drills with (and `buildTaskTree` that produces the `tree` prop). [1]
- `RailChat` builds the nested task tree used by the attach picker from projected task documents. [2]
- `RailChat` renders the picker with right alignment and passes the selected leaf/role pair to its attach callback. [3]
- `RailChat` performs the server-first attach/move and applies the returned task-document-and-role assignment only after success; a taken seat leaves local state untouched. [4]
- `ChatContextBar` builds the tree, restricts terminal role options when needed, and attaches/moves the focused session server-first. [5]
- Render/drill tests cover role selection, disabled leaf rows, and the two-argument callback. [6]

### Cross-Repo References

No meaningful cross-repo references found. This is a self-contained presentational dashboard component.

## Current L5I Maintenance

The portaled leaf picker now measures the room above and below its trigger on every open/viewport
move, chooses the roomier vertical direction when space below is short, and applies that actual
available height. Horizontal placement remains edge-aware, preventing both rail clipping and a
fixed-height menu that runs off-screen.
