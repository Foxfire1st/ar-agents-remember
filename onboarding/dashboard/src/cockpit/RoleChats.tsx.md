# dashboard/src/cockpit/RoleChats.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

RoleChatsPane owns canonical launcher intent, current role/document/request state and one persistent native chat frame.

## Code Commentary

One initially-open navigation boolean controls the first launcher button and outside-frame rail. Canonical scope and request identity gate async options/results. Taskless active request and saved retry selection survive in tab storage; result/dispatch receipts drive frame targets and backend status/report/reply fields. Retry reuses the saved request; Revive uses the selected backend capability. Fast/provider-default disclosure keeps tier separate from effort.

## Invariants And Boundaries

Native tabs and launch intent are separate authorities. Unknown request state retains identity, and refused dispatch remains visible through refresh. Completed host status and report existence are not semantic acceptance.

## Evidence

The current source and test assertions below establish the documented ownership; test citations do not claim a rerun in this pass.

| Finding | Anchor | Source at frozen tree |
| --- | --- | --- |
| Current source owner or exact assertion described above. | `RoleChatsPane` | `dashboard/src/cockpit/RoleChats.tsx:546-1077` |
| Current source owner or exact assertion described above. | `fetchExecutionResult` | `dashboard/src/cockpit/RoleChats.tsx:773-803` |
| Current source owner or exact assertion described above. | `dispatch` | `dashboard/src/cockpit/RoleChats.tsx:890-920` |
| The sole Chats destination mounts RoleChatsPane directly, has no Chats-mode selector or SessionsView child, and keeps the pane identity while hiding/showing the existing layer. | `directly shows one persistent Role chats pane without an old-chat selector` | `dashboard/src/cockpit/Cockpit.test.tsx:768-798` |
