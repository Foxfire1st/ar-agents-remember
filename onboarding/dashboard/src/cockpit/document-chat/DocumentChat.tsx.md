# dashboard/src/cockpit/document-chat/DocumentChat.tsx

## Governing Overview

[Route overview](../../overview.md)

## Purpose

Compose ordinary document chat or the leaf review's explainer chrome over one persistent native frame and tray dock.

## Code Commentary

In ordinary document mode, `DocumentChatImpl` combines the document state hook, native task array, bound role launcher and one shared frame in document page mode. The launcher appears when the known selection has no effective agent or the developer opens it; the Launch role control is offered when a target is shown. [1]

In ordinary document mode, a pending document lookup retains the native screen under a holding line so it takes no input. An unreadable answer adds one actionable line with Retry beside that retained screen. A confirmed no-chat state hides the mounted wrapper with `display:none` and `aria-hidden`; returning to an effective agent reuses it. A documentless selection may target the matching Projects Architect. The state hook separately represents a review task whose canonical document is still pending or unknown, so that case is not treated as documentless. [2]

Ordinary document mode displays the shared warmup run line and the shown agent's pending, loading, failed or skipped state with its reason. A loaded agent adds no loading message.

For an ordinary active column whose state has an effective target and does not hide its frame wrapper, the component publishes that target for the tray's initial recipient choice. This publication does not wait for a native drawn-chat acknowledgement. The dock is a sibling immediately after the frame wrapper and uses the document channel. `preload` is passed to the shared frame so a closed review column can start the embedded application. [1] [2]

## Invariants And Boundaries

The memoized export avoids remounting the panel during parent rerenders. The bound launcher contributes no second chat frame. The dock observes the existing frame; its sibling placement does not move or key that frame. Ordinary selection reads, unbound-task handling and effective-agent choice remain in the document state hook; explainer mode uses its own column state and disables those ordinary reads. [3]

Warmup states describe observed loading work, not a guarantee that every agent is loaded. Hiding and holding the mounted frame are separate from native plugin display acknowledgement.


## Evidence

- The export is memoized. [3]
- The state owner distinguishes documentless and unresolved review-task scopes, and gates chat reads on active visibility. [5]
- Warmup wording preserves loaded, failed, skipped and pending meanings. [6]

Compose ordinary document-chat chrome or the review leaf's explainer chrome above one persistent native frame and one tray dock. Ordinary documents retain their bound launcher, warmup and held-frame behavior. An explainer target disables ordinary document discovery and uses useExplainerColumn instead: resolveDocumentFrameProps supplies the explainer's frame target and showFrame state, while ColumnChrome displays its placeholder, form, progress or header. Pending unbound review identity retains the screen under its wait line; known missing identity displays the named problem. The frame wrapper remains keyed persistent-chat-frame across modes and the sibling TrayColumnDock remains persistent-tray-dock. Ordinary visible targets publish via documentShownChat; explainer targets publish through columnState, including a placeholder identity when no seat exists.

- Compose ordinary document-chat chrome or the review leaf's explainer chrome above one persistent native frame and one tray dock. Ordinary documents retain their bound launcher, warmup and held-frame behavior. An explainer target disables ordinary document discovery and uses useExplainerColumn instead: resolveDocumentFrameProps supplies the explainer's frame target and showFrame state, while ColumnChrome displays its placeholder, form, progress or header. Pending unbound review identity retains the screen under its wait line; known missing identity displays the named problem. The frame wrapper remains keyed persistent-chat-frame across modes and the sibling TrayColumnDock remains persistent-tray-dock. Ordinary visible targets publish via documentShownChat; explainer targets publish through columnState, including a placeholder identity when no seat exists. [7]

- DocumentChatImpl chooses ordinary document state or the leaf explainer state; the ordinary branch publishes its effective shown target, while explainer publication is owned by columnState. [1]

- DocumentChatImpl composes ordinary or explainer chrome over the same persistent frame wrapper, takes visibility/target/preload from resolveDocumentFrameProps and places the document tray dock after that wrapper. [2]

- The persistent-chat-frame wrapper stays mounted in DocumentChatImpl across ordinary document and explainer modes; a hidden phase sets display:none and aria-hidden instead of unmounting it. [4]
