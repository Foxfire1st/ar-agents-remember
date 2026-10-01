# dashboard/src/panels/Hangar.test.tsx

## Governing Overview

[panels overview](overview.md)

## Purpose

Vitest render tests for `Hangar` (260703-L11): they pin the **worktree-existence** visibility contract —
a row renders ONLY while a worktree physically exists (`hasLiveWorktree` over the projection's stat'ed
`codeWorktreeExists`/`memoryWorktreeExists`), never from a cleanup-state proxy. That covers the L9-reopen
defect (a `cleanup: reopened` contract with no worktrees rendered as live under the old
`ARCHIVED_CLEANUP` proxy) plus the as-before hiding of completed/abandoned enclosures whose worktrees
were reaped. The tests drive the panel through the real `dashboardStore` (the hangar reads `enclosures` /
`lifecycles` from the store), so they cover the filter end-to-end at the render layer.

## Code Commentary

### Logic

A local `enclosure(partial)` factory builds a full `EnclosureNode` from a minimal `{ enclosure }` plus
overrides, defaulting `cleanup: "pending"` **and** `codeWorktreeExists: true` / `memoryWorktreeExists:
true` (a live worktree), so a case only overrides the existence flags (and cleanup label) to mark a row
gone. `afterEach` runs `cleanup()` and `dashboardStore.getState().reset()` so cases don't leak state.
Five cases:

1. **Existence-only filter** — seeds a live enclosure, a memory-only one (`codeWorktreeExists: false`,
   `memoryWorktreeExists: true` — either side admits), and completed + abandoned ones with both flags
   false: exactly two `hangar-row`s survive and the panel title reads `Hangar · 2 worktrees`.
2. **Reopened-no-worktree hidden** — a `cleanup: "reopened"` enclosure with both flags false renders
   zero rows + the empty state: a reopened contract is a reset awaiting restart, not live work.
3. **Reopened-after-restart visible** — the same reopened contract with existence flags true renders
   again: existence, not the cleanup label, re-admits the row.
4. **Empty state** — every enclosure's worktrees physically gone → zero rows and the
   `/no live persistent worktrees/i` text.
5. **Durable current command** — a running closeout operation renders its projected
   `currentCommand` in the compact lifecycle badge and preserves that complete value in `title`.
   Its inline projection fixture carries the generated contract's required `legalControls: []` and
   `projectionEffects: []`; the test does not invent an advertised operation control or projection
   refresh effect merely to exercise command rendering.

### Invariants And Boundaries

Render + store state only; no backend, no gate posting, no WebSocket. The test treats the existence filter
as display-only: it seeds enclosure contracts and asserts they are *hidden*, never that they are deleted.
The existence flags themselves are server-stat'ed truth owned by the observer/projection layer
(`snapshots._enclosure_from_contract`); the tests only assert the client filters on them.
The command case is likewise projection/render coverage only: it seeds the already-durable
operation field and proves visibility, not execution or operation-state mutation. Its empty
`legalControls` and `projectionEffects` lists are fixture-contract conformance, not claims that live
operations never expose controls or projection refresh effects.

## Evidence

### Repo-Internal References

- The component under test (filters rows through `hasLiveWorktree`). [1]
- The shared existence-truth visibility selector. [2]
- The dashboard store the test seeds `enclosures` / `lifecycles` into and resets between cases. [3]
- The `EnclosureNode` shape (incl. `codeWorktreeExists`/`memoryWorktreeExists`) the `enclosure(...)` factory fills. [4]
- The running-operation fixture supplies required `legalControls: []` and `projectionEffects: []` while the assertion remains scoped to durable `currentCommand` rendering. [5]

## CCR-R18@v1 Fixture Envelope Fields

260831-CCR-L18 added `schemaVersion: "lifecycle-operation-projection/v1"` and `stateMatrixVersion: "lifecycle-operation-state-matrix/v1"` to the hand-built `lifecycleOperation` fixture inside the Hangar worktree-truth test, matching the generated mirror's now-required version literals. The worktree-existence visibility contract under test is unchanged.
