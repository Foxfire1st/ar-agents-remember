# dashboard/src/panels/Hangar.test.tsx

## Governing Overview

[panels overview](overview.md)

## Purpose

Hangar render/store assertions retain physical-worktree existence (either side admits), reopened-without-directory exclusion and full durable-command hover. Native owning task entries now supply status/qualified selection, not a lifecycle join.

## Code Commentary

### Logic

A typed enclosure fixture defaults both existence flags true. Teardown resets DOM/store; cases override flags or cleanup labels explicitly.

1. **Existence-only filter** — seeds a live enclosure, a memory-only one (`codeWorktreeExists: false`,
   `memoryWorktreeExists: true` — either side admits), and completed + abandoned ones with both flags
   false: exactly two `hangar-row`s survive and the panel title reads `Hangar · 2 worktrees`.
2. **Reopened-no-worktree hidden** — a `cleanup: "reopened"` enclosure with both flags false renders
   zero rows + the empty state: a reopened contract is a reset awaiting restart, not live work.
3. **Reopened-after-restart visible** — the same reopened contract with existence flags true renders
   again: existence, not the cleanup label, re-admits the row.
4. **Empty state** — every enclosure's worktrees physically gone → zero rows and the
   `/no live persistent worktrees/i` text.
5. **Durable current command** — a copied served operation supplies currentCommand, shown inline and complete in title. No hand-listed empty controls/effects fixture remains.
6. **Owning task entry** — a native entry bound to the worktree renders works and selects its qualified key, without a lifecycle join.

### Invariants And Boundaries

Seeded render/store assertions consume existence flags, never stat or delete worktrees. The copied served operation substitutes only currentCommand: inline/full-hover visibility is not execution or mutation. Native task selection checks its bound entry, not lifecycle-derived host state.

## Evidence

### Repo-Internal References


- The component under test (filters rows through `hasLiveWorktree`). [1]

- The shared existence-truth visibility selector. [2]
- Hangar tests seed and reset the shared dashboard store: existence cases set enclosures directly, while the owning-task case applies a snapshot with native task entries and their bound worktrees. The store carries tasks keyed by entry.key and enclosures keyed by enclosure, applies snapshots through applySnapshotState and resets through emptyWorkspace; it has no lifecycles store. [3]
- The `EnclosureNode` shape (incl. `codeWorktreeExists`/`memoryWorktreeExists`) the `enclosure(...)` factory fills. [4]
- The running-operation test copies `SERVED.enclosures.lifecycleOperation` and overrides currentCommand. Its assertions check that the full durable command appears inline and as the operation title; it does not author legalControls: [] or projectionEffects: [] in this fixture. [5]

## CCR-R18@v1 Fixture Envelope Fields

Historical CCR-L18 hand-listed operation version fields; current setup copies the served lifecycleOperation and overrides only currentCommand. Worktree-existence and full-command assertions are unchanged.
