# dashboard/src/panels/LeafAttachPicker.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/LeafAttachPicker.tsx`      |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-07-24T13:17:17Z |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c`       |
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
| governingOverview      | `overview.md`                                    |

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

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The `TaskTreeNode` shape it drills and `findMasterPath` it pre-drills with (and `buildTaskTree` that produces the `tree` prop). | `TaskTreeNode`; `findMasterPath`; `buildTaskTree` | dashboard/src/data/taskIdentity.ts:133-139; dashboard/src/data/taskIdentity.ts:208-214; dashboard/src/data/taskIdentity.ts:218-225 |
| `RailChat` builds the nested task tree used by the attach picker from projected task documents. | "const leafTree = buildTaskTree(taskDocuments);" | dashboard/src/panels/RailChat.tsx:521-521 |
| `RailChat` renders the picker with right alignment and passes the selected leaf/role pair to its attach callback. | "import { LeafAttachPicker } from './LeafAttachPicker';"; "align=\"right\"" | dashboard/src/panels/RailChat.tsx:34-34; dashboard/src/panels/RailChat.tsx:1022-1029 |
| `RailChat` performs the server-first attach/move and applies the returned task-document-and-role assignment only after success; a taken seat leaves local state untouched. | "const result = await attachSessionToTask(sessionId, taskDocumentRef, seatRole);"; "sessionStore.getState().applyTaskAssignment(sessionId, taskDocumentRef, seatRole);"; "result === 'seat-taken'" | dashboard/src/panels/RailChat.tsx:533-541 |
| `ChatContextBar` builds the tree, restricts terminal role options when needed, and attaches/moves the focused session server-first. | `ChatContextBar` | dashboard/src/panels/session-cockpit/ChatContextBar.tsx:74-117 |
| Render/drill tests cover role selection, disabled leaf rows, and the two-argument callback. | "LeafAttachPicker drill-down" | dashboard/src/panels/LeafAttachPicker.test.tsx:35-134 |

## Cross-Repo References

No meaningful cross-repo references found. This is a self-contained presentational dashboard component.

## Current L5I Maintenance

The portaled leaf picker now measures the room above and below its trigger on every open/viewport
move, chooses the roomier vertical direction when space below is short, and applies that actual
available height. Horizontal placement remains edge-aware, preventing both rail clipping and a
fixed-height menu that runs off-screen.

## Update History
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: recorded the memoized measure hooks fix. Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B23 curator: rebased the `RailChat` rows to their
  source occurrences; exact non-fixing check returns zero findings.

- 2026-08-03T04:00:52+02:00 — 260731-EFA-L6 W3-B06 curator: curated 4 citation findings for the task-tree implementation and picker regression rows. Max-reviewer subject-binding addendum split the pooled RailChat row into exact tree, alignment/callback, and server-first attach behavior rows.

- 2026-07-24T13:17:17Z — Curator: documented viewport-aware vertical popover placement and its
  bounded height; verification fields remain pre-commit.

- 2026-07-18T16:02+02:00 — FEUI MX-FIX-3 / missing FEUI-L8 history repair: replaced the retired
  Chats consumer and one-argument callback with the landed `RailChat` + `ChatContextBar` ownership
  and `onPick(leafKey, seatRole)` contract. Leaf selection remains disabled until role identity is
  known, and both consumers attach/move server-first. This explicitly repairs the FEUI-L8
  duty-transfer edit that had no matching history entry. Verified against code commit
  `31f58834f86c0d98e26b0896e099a2403a8729ee`.

- 2026-07-10T15:07+02:00 — 260707-HFX2-L17: added explicit/preselected seat-role choice to leaf
  attach/move, disabled leaf selection until identity is known, and returned the leaf-role pair.

- 2026-06-30T00:00:00+02:00 — Operations Integration L5 (Sidebar chat): created — the dark drill-down leaf-attach
  picker. One Panda-themed popover (portaled to `document.body`, `position: fixed`, edge-pinned via
  `align`) navigates the recursive `TaskTreeNode` tree a level at a time: master rows drill in (with a
  "‹ back" breadcrumb), leaf rows fire `onPick(leafKey)`; `contextMaster` pre-drills via `findMasterPath`.
  Plain React state, no React Aria overlay. Shared by `RailChat` (align right) and `Chats` (align left).
  Verification metadata pinned until closeout stamps the L5 commit.
