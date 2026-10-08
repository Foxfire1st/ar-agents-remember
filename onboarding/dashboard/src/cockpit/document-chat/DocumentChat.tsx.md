# dashboard/src/cockpit/document-chat/DocumentChat.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

The right rail's document chat: it composes the shared bound launcher and the shared native Paseo frame for the selected document.

## Code Commentary

`DocumentChatImpl` derives every visible value from `useDocumentChat` and renders three parts: a "Launch role" control only while an agent is shown, the shared `RoleChatsPane` launcher bound to the selection while no agent matches or the user opened it, and the shared `PaseoChatFrame` in document page mode. An unreadable host renders the shared `FrameUnavailable` notice with Retry instead of a start that cannot succeed. The frame element stays mounted and is only hidden while the selection is unresolved, so a ready frame survives a target switch; `memo` keeps the panel out of parent re-renders.

## Evidence

- The panel composes selection state, the bound launcher and the shared frame, exposing the launch control only when a target is shown. [1]
- The view hides the mounted frame while the selection is unresolved and shows the shared unavailable notice with Retry. [2]
- The exported panel is memoized so a parent re-render does not remount it. [3]
