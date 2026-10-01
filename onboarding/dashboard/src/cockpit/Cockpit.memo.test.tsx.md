# dashboard/src/cockpit/Cockpit.memo.test.tsx

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

Render-count regression coverage for the cockpit's persistent, hidden-not-unmounted layers.

## Code Commentary

### Logic

Memoized probes wrap real persistent panels and count parent-driven renders. The suite sweeps cockpit
views, preserves DOM identity and ARIA/display visibility, checks real prop changes still pass the memo
gate, and confirms the right-rail River/Chat switch remains interactive.

### Conventions

Mocks preserve the production export shape and use React's ordinary shallow memo comparison; store-driven
updates inside a panel are intentionally outside these parent-render counts.

### Invariants And Boundaries

The test guards tab-switch reconciliation cost without accepting unmount/remount as an optimization.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory worktree's source registry; no external
documentation was invented.

No relevant external documentation is configured.

### Repo-Internal References

- The seven `vi.mock` render-count probes (`counts`, `CountedEngineRoom` … `CountedEventRiver`). [1]
- The keep-alive DOM-identity case (same `.rail--left` / `engine-room` / `sessions-view` nodes across switches). [2]
- The persistent layer layout is declared once for Chats. [3]
- The file layer reuses the persistent layout. [4]
- The Operations layer reuses the persistent layout. [5]
- The Engine Room layer reuses the persistent layout. [6]
- The shell hides each layer through display and aria-hidden while retaining its children. [7]
- The Engine Room instance remains mounted. [8]
- The Operations reader remains mounted. [9]
- The File Viewer remains mounted and receives visibility as active. [10]
- Chats remains mounted; takeover suppresses its active state. [11]

| The current series sub-task model owns optional createdAt; the historical fixture split below records why that distinction matters. | "export interface SeriesSubTaskNode {" | dashboard/src/types/projection.ts:561-568; dashboard/src/types/projection.ts:560-560 |

### Cross-Repo References

No meaningful cross-repository references found.

- This is dashboard-local test coverage. [12]
