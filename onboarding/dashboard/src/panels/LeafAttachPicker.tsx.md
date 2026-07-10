# dashboard/src/panels/LeafAttachPicker.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/LeafAttachPicker.tsx`      |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-10T15:07+02:00 |
| lastVerifiedCommitHash | `0d5ce6784930aa4e9006ab4bbf2b788a3296abce`       |
| lastVerifiedCommitDate | 2026-07-10T22:30:19+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels overview](overview.md)

## Purpose

The **drill-down leaf picker** (Operations Integration L5, leaf-keyed chat registry): the control that
attaches a chat session to a task **leaf**. It is shared by the right-rail chat (`RailChat`) and the Chats
page (`Chats`). It replaces a native `<select>` — whose OS-rendered list was an unthemed white "flashbang"
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
align = "left" })` renders a trigger `<button>` (`{label} ▾`, `aria-haspopup="menu"`, `aria-expanded`,
testid `{testId}`) and, when open, a popover.

- **Props.** `tree: TaskTreeNode[]` is the recursive master→…→leaf hierarchy (built by
  `buildTaskTree` in `data/taskIdentity`); `onPick: (leafKey: string) => void` is the selection
  callback — fired with the chosen leaf's **qualified leaf key** (`repo/master/leaf-id`) when a leaf row
  is clicked; `contextMaster?: string` is the in-context master folder so the picker pre-drills to it on
  open; `label` is the trigger text + menu `aria-label`; `testId` prefixes every `data-testid`; `align`
  (`"left" | "right"`) decides which trigger edge the menu pins to.
- **Drill state.** `open` (bool), `path: TaskTreeNode[]` (the drilled master breadcrumb), and `coords`
  (the fixed-position anchor) are React state; `triggerRef` / `menuRef` are element refs. The current
  level is `here = path[path.length - 1]` (the deepest drilled master, or `undefined` at the root) and
  `level = here ? here.children : tree`. `drillInto(node)` pushes a master onto `path`, `back()` pops it,
  and `pick(leafKey)` closes the menu, clears `path`, and calls `onPick(leafKey)`.
- **Open + pre-drill.** `toggle()` opens/closes; on opening it sets `path` to `findMasterPath(tree,
  contextMaster)` when a `contextMaster` is given (so its leaves show first — "pre-selection via master")
  or `[]` otherwise, and measures the anchor.
- **Portaled, fixed popover.** When `open && coords`, the menu is rendered via `createPortal` into
  `document.body` with `position: fixed` so it escapes the rail's `overflow: hidden` (which was clipping
  it) and any ancestor stacking/transform context. `measure()` reads the trigger's bounding rect and pins
  the menu to the right edge (`align === "right"`, used by the right-rail) or the left edge (default, used
  by the Chats strip) so it never runs off-screen. A `useLayoutEffect` (active only while open)
  re-measures on `resize` / capturing `scroll`, and wires click-outside (the check spans **both** the
  trigger and the portaled menu, since the menu lives outside the component's DOM subtree) and `Escape`
  to close.
- **Rows.** Inside the menu: a sticky back button (`{testId}-back`, `‹ {here.title}`) when drilled; an
  empty note (`{testId}-empty`) reading "No sub-tasks here." when drilled into an empty master or "No
  tasks available yet." at the top level; otherwise each node in `level` renders either a **leaf** row
  (`role="menuitem"`, `{testId}-leaf`, `data-leaf-key`, `onClick` → `pick(node.leafKey)`) or a **master**
  row (`{testId}-master`, `data-master`, a ▸ chevron, `onClick` → `drillInto(node)`).

### Conventions

Co-located Panda `css()` (no global panel CSS); a dark `bgPanel` popover with amber accents matching the
cockpit. Plain React state + native `<button>`s rather than a React Aria overlay — keeps the drill flow
unit-testable without an overlay harness. `data-testid`s are all `{testId}`-prefixed so the two consumers
(`rail-attach-leaf-picker`, `chats-attach-leaf-picker`) get disjoint hooks. Node titles fall back to the
folder/leaf id inside the tree builder, so this component renders `node.title` directly.

### Invariants And Boundaries

- **Presentational + controlled.** It owns only ephemeral UI state (open / drill path / menu coords). It
  never reads a store, never fetches, and never performs the attach itself — selection is surfaced purely
  through the `onPick(leafKey)` callback; the consumer (`RailChat` / `Chats`) does the actual chat⇄leaf
  bind.
- **Tree is supplied, not built here.** The recursive hierarchy comes in as the `tree` prop; this
  component only navigates and renders it. Arbitrary nesting is handled generically — a nested master is
  just a master node sitting inside another master node.
- **Leaf key is opaque.** It passes `node.leafKey` straight through to `onPick` without parsing it.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The `TaskTreeNode` shape it drills and `findMasterPath` it pre-drills with (and `buildTaskTree` that produces the `tree` prop). | L104-L176 | [data/taskIdentity.ts](../data/taskIdentity.ts) |
| The right-rail consumer: builds the tree, passes `contextMaster` + `align="right"`, and attaches the free chat to the picked leaf via `onPick`. | L258, L329-L335 | [RailChat.tsx](RailChat.tsx) |
| The Chats-page consumer: builds the tree, passes `align="left"`, and attaches the active session to the picked leaf. | L316, L372-L378 | [Chats.tsx](Chats.tsx) |
| The render + drill interaction tests for this picker. | — | [LeafAttachPicker.test.tsx](LeafAttachPicker.test.tsx) |

## Cross-Repo References

No meaningful cross-repo references found. This is a self-contained presentational dashboard component.

## Update History

- 2026-07-10T15:07+02:00 — 260707-HFX2-L17: added explicit/preselected seat-role choice to leaf
  attach/move, disabled leaf selection until identity is known, and returned the leaf-role pair.

- 2026-06-30T00:00:00+02:00 — Operations Integration L5 (Sidebar chat): created — the dark drill-down leaf-attach
  picker. One Panda-themed popover (portaled to `document.body`, `position: fixed`, edge-pinned via
  `align`) navigates the recursive `TaskTreeNode` tree a level at a time: master rows drill in (with a
  "‹ back" breadcrumb), leaf rows fire `onPick(leafKey)`; `contextMaster` pre-drills via `findMasterPath`.
  Plain React state, no React Aria overlay. Shared by `RailChat` (align right) and `Chats` (align left).
  Verification metadata pinned until closeout stamps the L5 commit.
