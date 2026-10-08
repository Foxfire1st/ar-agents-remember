# dashboard/src/cockpit/RoleChats.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

RoleChatsPane owns canonical launcher intent, current role/document/request state and one persistent native chat frame.

## Code Commentary

The launcher is its row of controls: no execution, reply or report-path prose is rendered under them, and one failure line (a refused or unresolved start, an unreachable host, a failed options/catalog/report action, the launch lock) is the only text there. Canonical scope and request identity gate async options/results. Taskless active request and saved retry selection survive in tab storage; receipts drive frame targets and backend status/report fields. Result re-reads the execution, refreshes capabilities, steers the frame and opens the recorded report in the shared reader; the pane is hidden under the report takeover so the frame survives. Retry reuses the saved request; Revive uses the selected backend capability. Fast/provider-default disclosure keeps tier separate from effort.

## Invariants And Boundaries

Native tabs and launch intent are separate authorities. Unknown request state retains its actionable line, and a refused dispatch stays visible through automatic reads until an explicit successful action. Completed host status and report existence are not semantic acceptance. The dashboard draws no chat navigation of its own (MIK-R75 rules 7 to 10); the Parent pill gate belongs to the plugin, not this pane.

## Evidence

The current source and test assertions below establish the documented ownership; test citations do not claim a rerun in this pass.

| Finding | Anchor | Source at frozen tree |
| --- | --- | --- |
| Current source owner or exact assertion described above. | `RoleChatsPane` | `dashboard/src/cockpit/RoleChats.tsx:513-1071` |
| Current source owner or exact assertion described above. | `fetchExecutionResult` | `dashboard/src/cockpit/RoleChats.tsx:773-803` |
| Current source owner or exact assertion described above. | `dispatch` | `dashboard/src/cockpit/RoleChats.tsx:890-920` |
| The sole Chats destination mounts RoleChatsPane directly, has no Chats-mode selector or SessionsView child, and keeps the pane identity while hiding/showing the existing layer. | `directly shows one persistent Role chats pane without an old-chat selector` | `dashboard/src/cockpit/Cockpit.test.tsx:768-798` |

## MIK-R95 Extracted Launcher And Bound Row

The launcher row is no longer defined here: `RoleLauncher` and `useRoleLaunchProgress` moved to `./role-launcher/`, and `RoleChatsPane` renders that shared component for the Chats page and for the document rail's bound selection. The pane keeps launch intent, exact request identity, options/result reads and one failure line. Its bound mode suppresses the reference pickers it already knows, marks an open execution running and offers no second start, and adopts an existing saved Projects open request through `boundTasklessRequest` while an uncertain request keeps its exact identity. The document-scope effects stay keyed to the canonical scope and request.
