# dashboard/src/panels/LeafAttachPicker.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/LeafAttachPicker.test.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-10T15:07+02:00 |
| lastVerifiedCommitHash | `fdff55f2921d7aaa8ba240c11087d02c15a170d7`       |
| lastVerifiedCommitDate | 2026-07-10T15:53:23+02:00|
| governingOverview      | `overview.md`                                    |

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

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The component under test. | — | [LeafAttachPicker.tsx](LeafAttachPicker.tsx) |
| The `TaskTreeNode` type the `TREE` fixture is built against. | — | [data/taskIdentity.ts](../data/taskIdentity.ts) |

## Update History

- 2026-07-10T15:07+02:00 — 260707-HFX2-L17: expanded drill-down tests with mandatory/preselected
  seat role and restricted role-option behavior.

- 2026-06-30T00:00:00+02:00 — Operations Integration L5 (Sidebar chat): created — drill-down navigation tests over a
  nested master→leaf tree: masters list before leaves, drilling reveals a master's leaves + nested
  masters, an in-context master pre-drills on open, walking back returns to the top level, and selecting a
  leaf calls `onPick` with the qualified leaf key (incl. a leaf two levels deep). Verification metadata
  pinned until closeout stamps the L5 commit.
