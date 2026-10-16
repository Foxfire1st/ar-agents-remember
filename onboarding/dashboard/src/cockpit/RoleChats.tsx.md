# dashboard/src/cockpit/RoleChats.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

RoleChatsPane accepts the single served TaskEntry array and keeps canonical launcher intent, report takeover state and refresh generations, and composes the scope hook, run controls, options loader and persistent view. Stored requests and receipt actions belong to roleChatControls; the native-frame mount belongs to RoleChatsView.

## Code Commentary

The launcher is its row of controls: no execution, reply or report-path prose is rendered under them, and one failure line (a refused or unresolved start, an unreachable host, a failed options/catalog/report action, the launch lock) is the only text there. Canonical scope and request identity gate async options/results. Per-request active execution and saved retry selection survive in scoped tab storage; receipts drive frame targets and backend status/report fields. Result re-reads the execution, refreshes capabilities, steers the frame and opens the recorded report in the shared reader; the pane is hidden under the report takeover so the frame survives. Retry reuses the saved request; Revive uses the selected backend capability. Fast/provider-default disclosure keeps tier separate from effort.

## Invariants And Boundaries

Native tabs and launch intent are separate authorities. Unknown request state retains its actionable line, and a refused dispatch stays visible through automatic reads until an explicit successful action. Completed host status and report existence are not semantic acceptance. The dashboard draws no chat navigation of its own (MIK-R75 rules 7 to 10); the Parent pill gate belongs to the plugin, not this pane.

## Evidence

The current source and test assertions below establish the documented ownership; test citations do not claim a rerun in this pass.

- The pane composes canonical scopes, controls, options and the persistent view. [1]

- Selected Result/report reads retain UUID and live-target guards. [2]

- Start/Revive dispatch keeps exact request scope and retained retry identity. [3]
- The sole Chats destination mounts RoleChatsPane directly, has no Chats-mode selector or SessionsView child, and keeps the pane identity while hiding/showing the existing layer. [4]

## MIK-R95 Extracted Launcher And Bound Row

The launcher row is no longer defined here: `RoleLauncher` and `useRoleLaunchProgress` moved to `./role-launcher/`, and `RoleChatsPane` renders that shared component for the Chats page and for the document rail's bound selection. The pane coordinates launch intent and exact request identity through roleChatControls, options reads through roleChatOptionsLoader, and the failure line and frame through RoleChatsView. Its bound mode suppresses the known reference pickers; ordinary singleton and Projects roles mark an open execution running and offer no second start, while selected-task Investigator uses its explicit per-request policy, and adopts an existing saved Projects open request through `boundTasklessRequest` while an uncertain request keeps its exact identity. The canonical scopes are memoized from reference values by useRoleChatScopes; roleChatOptionsLoader owns the active, refresh and bound-request effect, and the controls enforce the selected UUID on Result application.

## Investigator scope and request identity

Selected sprint/master Investigators adopt and restore their exact saved request UUID from executions[], including a completed selection with a newer sibling. Automatic and manual Result/report, Retry and Revive retain that UUID and complete canonical document references through remount. The same persistent native frame and controls-only row remain in place; the selected document’s primary Manager/Orchestrator is refreshed separately and remains its coordinator.


- Options restoration selects the saved request rather than a newer sibling. [5]
