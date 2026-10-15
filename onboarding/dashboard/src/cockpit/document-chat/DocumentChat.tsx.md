# dashboard/src/cockpit/document-chat/DocumentChat.tsx

## Governing Overview

[Route overview](../../overview.md)

## Purpose

The right rail's document chat: it composes the shared bound launcher and the shared native Paseo frame for the selected document.

## Code Commentary

The pane displays the shared warmup run line and the shown agent's distinct pending, loading, failed or skipped reason. A loaded agent adds no loading message. These are observed warmup states, not a replacement chat frame or a claim that every agent is loaded.


`DocumentChatImpl` composes selection state, one bound launcher and one shared native frame in document page mode. The launcher appears only when the selection is known and has no effective agent, or the user opens it. A pending document lookup keeps the current native screen visible and passes a holding line into the frame so it takes no input. An unreadable lookup is an actionable one-line notice with Retry beside that retained screen, not a replacement unavailable view or a false empty selection.

Only confirmed no-chat hides the mounted wrapper with display:none and aria-hidden; returning to an effective agent reuses the same frame. No document selected still permits the matching Projects Architect as its effective target. `memo` prevents parent rerenders from remounting the panel. Hidden-state component assertions do not claim native keyboard or screen-reader traversal.
## Evidence

- The panel composes selection state, the bound launcher and the shared frame, exposing the launch control only when a target is shown. [1]
- Unknown selections keep the native screen visible under a holding line; unreadable answers add one-line Retry without replacing it. [2]
- The exported panel is memoized so a parent re-render does not remount it. [3]
- The hidden frame wrapper stays mounted behind display:none and aria-hidden. [4]
