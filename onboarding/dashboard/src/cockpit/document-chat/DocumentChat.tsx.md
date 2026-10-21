# dashboard/src/cockpit/document-chat/DocumentChat.tsx

## Governing Overview

[Route overview](../../overview.md)

## Purpose

Compose the selected document’s bound launcher and shared native chat frame, with a tray dock for the visible column.

## Code Commentary

`DocumentChatImpl` combines the document state hook, native task array, bound role launcher and one shared frame in document page mode. The launcher appears when the known selection has no effective agent or the developer opens it; the Launch role control is offered when a target is shown. [1]

A pending document lookup retains the native screen under a holding line so it takes no input. An unreadable answer adds one actionable line with Retry beside that retained screen. A confirmed no-chat state hides the mounted wrapper with `display:none` and `aria-hidden`; returning to an effective agent reuses it. A documentless selection may target the matching Projects Architect. The state hook separately represents a review task whose canonical document is still pending or unknown, so that case is not treated as documentless. [2]

The component displays the shared warmup run line and the shown agent's pending, loading, failed or skipped state with its reason. A loaded agent adds no loading message.

For an active column whose state has an effective target and does not hide its frame wrapper, the component publishes that target for the tray's initial recipient choice. This publication does not wait for a native drawn-chat acknowledgement. The dock is a sibling immediately after the frame wrapper and uses the document channel. `preload` is passed to the shared frame so a closed review column can start the embedded application. [1] [2]

## Invariants And Boundaries

The memoized export avoids remounting the panel during parent rerenders. The bound launcher contributes no second chat frame. The dock observes the existing frame; its sibling placement does not move or key that frame. Selection reads, unbound-task handling and effective-agent choice remain in the document state hook. [3]

Warmup states describe observed loading work, not a guarantee that every agent is loaded. Hiding and holding the mounted frame are separate from native plugin display acknowledgement.


## Evidence

- The component composes document state, the launcher and shown-chat publication. [1]
- The view retains or hides the frame wrapper, forwards preload and places the document tray dock after it. [2]
- The export is memoized. [3]
- The hidden frame wrapper remains mounted. [4]
- The state owner distinguishes documentless and unresolved review-task scopes, and gates chat reads on active visibility. [5]
- Warmup wording preserves loaded, failed, skipped and pending meanings. [6]
