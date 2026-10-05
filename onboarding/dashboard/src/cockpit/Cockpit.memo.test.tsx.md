# dashboard/src/cockpit/Cockpit.memo.test.tsx

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

These regressions preserve cockpit layer identity and the shell-driven reconciliation/visibility contract.

## Code Commentary

### Logic

The current Chats node is role-chats-pane. The same pane survives route switches while its parent display and aria-hidden change. SessionsView is removed from the current layer render-count account, while the remaining persistent layer counts retain their existing checks.

Memoized probes wrap real persistent panels and count parent-driven renders. The suite sweeps cockpit
views, preserves DOM identity and ARIA/display visibility, checks real prop changes still pass the memo
gate, and confirms the right-rail River/Chat switch remains interactive.

### Conventions

Mocks preserve the production export shape and use React's ordinary shallow memo comparison; store-driven
updates inside a panel are intentionally outside these parent-render counts.

### Invariants And Boundaries

The test guards tab-switch reconciliation cost without accepting unmount/remount as an optimization.
Same-node retention does not certify every native chat state; store-driven updates remain outside the parent-render counts.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory worktree's source registry; no external
documentation was invented.

No relevant external documentation is configured.

### Repo-Internal References

The current source extents below record the reviewed UI contract. Inline test names/facets are source-bound evidence; the installed writer cannot create typed proves from those call titles, and these citations do not claim such a proof or a rerun.

| Finding | Anchor | Source at frozen tree |
| --- | --- | --- |
| Current source owner or exact assertion described above. | `keeps the visibility/aria contract` | `dashboard/src/cockpit/Cockpit.memo.test.tsx:238-268` |
| Current source owner or exact assertion described above. | `role-chats-pane` | `dashboard/src/cockpit/Cockpit.memo.test.tsx:245-275` |
| Directly places RoleChatsPane in the persistent ViewLayer and supplies taskDocuments and series with active visibility. | `MainLayers` | `dashboard/src/cockpit/Cockpit.tsx:757-819` |

- The six counted persistent-panel `vi.mock` probes (`counts`, `CountedEngineRoom` … `CountedEventRiver`). [1]
- The keep-alive DOM-identity case (same `.rail--left` / `engine-room` / `role-chats-pane` nodes across switches). [2]
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
