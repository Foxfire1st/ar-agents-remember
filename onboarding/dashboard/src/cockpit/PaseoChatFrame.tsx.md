# dashboard/src/cockpit/PaseoChatFrame.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

The component owns one native embedded chat document and an external AR navigation rail, with distinct frame/control/catalog/agent notices.

## Code Commentary

The descriptor is read on first activation and explicit Retry. A stable controller consumes execution targets and trusted plugin messages. Catalog data is grouped against current taskDocuments/series; navigationOpen is controlled by the launcher. The iframe generation drives replacement, while ready navigation retains src and exact frame-origin clipboard policy.

## Invariants And Boundaries

Normal view/rail hiding preserves the frame; Retry and the existing unavailable-control URL path may replace a generation. Catalog failure disables navigation rather than claiming valid empty data.

## Evidence

The current source and test assertions below establish the documented ownership; test citations do not claim a rerun in this pass.

| Finding | Anchor | Source at frozen tree |
| --- | --- | --- |
| Current source owner or exact assertion described above. | `useFrameController` | `dashboard/src/cockpit/PaseoChatFrame.tsx:146-176` |
| Current source owner or exact assertion described above. | `useFrameDescriptor` | `dashboard/src/cockpit/PaseoChatFrame.tsx:195-225` |
| Current source owner or exact assertion described above. | `EmbeddedFrame` | `dashboard/src/cockpit/PaseoChatFrame.tsx:296-342` |
| A fresh page installs no bridge or write watcher before the exact embed-list pair confirms its parent, then installs a bridge only on the settled page. | `listed frame: the AR look and the channel, once the list has confirmed the parent` | `dashboard/src/cockpit/paseoPluginClient.test.ts:775-805` |
| The sole Chats destination mounts RoleChatsPane directly, has no Chats-mode selector or SessionsView child, and keeps the pane identity while hiding/showing the existing layer. | `directly shows one persistent Role chats pane without an old-chat selector` | `dashboard/src/cockpit/Cockpit.test.tsx:768-798` |
