# dashboard/src/panels/LeafAttachPicker.test.tsx

## Governing Overview

[panels overview](overview.md)

## Purpose

Vitest render + interaction tests for `LeafAttachPicker` (Operations Integration L5): they pin the
drill-down navigation contract over an **arbitrarily nested** task tree — masters list first, drilling a
master reveals its leaves and any nested masters, an in-context master pre-drills on open, and selecting a
leaf surfaces its leaf key through `onPick`. Because the picker uses plain React state (no React Aria
overlay), the tests drive it directly with `fireEvent.click`.

## Code Commentary

### 260707-HFX2-L17 Picker Identity Regressions

Tests prove leaves are disabled until role selection, explicit worker/reviewer choices reach
`onPick(leafKey, role)`, supplied identity preselects correctly, and restricted terminal options do
not expose agent roles.

### Logic

A shared `TREE` fixture encodes the nesting the picker must handle: `Operations Integration` (master) →
{ an `L5` leaf (`repo/ops/L5`), `Engine Room` (a **nested** master) → an `E1` leaf (`repo/engine/E1`) } —
i.e. "a master that is the leaf of another master". `TID = "attach-leaf-picker"` is the default testid
prefix. Four cases over `<LeafAttachPicker tree={TREE} onPick={vi.fn()} … />`:

1. **Masters-first, then drill** — clicking the trigger shows the top-level master row (`data-master ===
   "ops"`) and **no** leaf rows; clicking the master drills in, revealing a back row, the master's leaf
   (`data-leaf-key === "repo/ops/L5"`), and the nested `engine` master row.
2. **Attach at arbitrary depth** — open → drill `ops` → drill the nested `engine` master → click its only
   leaf; asserts `onPick` was called with `"repo/engine/E1"` (selection surfaces the qualified leaf key
   from a leaf nested two levels deep).
3. **Pre-drill to the in-context master** — rendered with `contextMaster="engine"`, opening lands already
   drilled into Engine Room: the back row text contains "Engine Room" and the visible leaf is
   `repo/engine/E1`, so the relevant leaves show immediately.
4. **Walk back up** — open → drill into a master → click the back row; the back row disappears and the top
   level (the `ops` master row) is shown again.

### Invariants And Boundaries

Render + interaction only; no store, no backend, no portal-overlay harness. The tests assert the public
contract (visible rows by testid, `onPick` payload) rather than internal drill state, and treat the leaf
key as opaque — they only check it round-trips through `onPick`.

## Evidence

### Repo-Internal References

- The component under test. [1]
- The `TaskTreeNode` type the `TREE` fixture is built against. [2]

## Current L5I Maintenance

The picker tests now cover the measured placement contract in addition to selection behavior,
including opening above the trigger when the lower viewport room cannot accommodate the menu.
