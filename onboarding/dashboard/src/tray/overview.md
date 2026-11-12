# dashboard/src/tray/ — Reference Tray

## Governing Overview

[Dashboard overview](../overview.md)

## What This Area Is

The tray collects references, selected passages, pasted images and notes for one developer message to each chosen existing AR chat. Object picks retain structured identity; their written opening forms are resolved by the backend rather than copied from displayed object text.

## Hot Path Summary

AddToTray and pickBuilders collect objects. SelectionOffer/useSelectionOffer collect dashboard text only after an explicit click; the trusted frame channel supplies chat passages with their recorded origin. trayStore owns admission, target defaults and Send settlement. TrayDock/TrayPanel present the same collection beside a chat frame or in a corner. traySend calls the developer-message routes; TraySent displays their per-target outcomes and log.

## Construction And Ownership

pickKey deduplicates the exact kind, comparison/tree/side/path/range/revision identity. The first pick chooses only the initial target: its source chat for a chat passage, the published shown-chat target for another pick, or none. Explicit target choices win and later picks do not redirect them. The document column publishes its active, non-hidden bound target; that publication is not a native drawn-chat acknowledgement. On the Chats page, a drawn frame uses its plugin report once one arrives. Recipient discovery is paged and preserves known rows while an incomplete listing leaves missing seats unknown.

Metadata, notes, text and targets persist per browser origin; image bytes use digest-keyed IndexedDB with a live memory copy. A storage failure leaves live content and a visible non-persistence warning. Preferences set copy-on-highlight and positive count/image/message bounds locally. The backend enforces its own independent request and decoded-byte limits.

The dock is outside the existing iframe and follows its native composer measurements while reserving its drawn height. When a composer report carries the message box's own left and width, the column dock takes that left and width for itself — the frame supplies only the origin — with no minimum and no clamp; a report without the pair keeps the frame-wide placement. In Operations, where the frame is the column, that is a measured inset: the retained case puts the tray that spanned the 300 px column at the box's left 16 and width 268, 16 px in from each side and 32 px narrower, at both 1920 and 1440. Unreadable composer geometry has the named below-frame placement. Without a visible chat dock it uses the page corner. New picks show the minimized Attached counter unless the tray is already expanded. The expanded pick list has bounded scrolling while the message and Send remain visible; close retains the collection behind its edge pill.

On a review page with its chat column closed, a pick reveals only the minimized tray line and leaves the column closed. Explicitly opening the full tray opens that column. Its first pick can wait for the column’s published chat; choosing targets, removing the last pick without an explicit target choice or leaving the review ends the wait.

An ordinary Send captures an immutable snapshot and submits one composed message per remaining live target after archived or placeholder explainer recipients are separated. The backend resolves reference/provenance forms and files the complete message and hashed picks before native send or hold. Delivered and held outcomes are counted as sent without conflating those states. A refusal keeps the snapshot for its failed targets; picks added during the send survive settlement. The bounded sent log follows each message's own held end and retains the durable files.

A Send aimed at an archived or placeholder explainer first asks that leaf’s fixed-target first-request form to open with the current text. If no live target remains, no role-chat post or settlement occurs and the collection stays; a mixed selection continues through ordinary live-target posting and settlement. This handoff is not reported as native delivery. The minimized line’s head also expands on a click, Enter or space outside a nested control; the nested button, link, input, textarea, select and listed ARIA control targets retain their own actions, so Close does not also expand. The existing closed-column minimized-pick rule remains separate from the explicit first-request signal that opens its matching column.

## Invariants And Boundaries

Hosted object ⊕ controls stay quiet until their own host is hovered or focused, have accessible names and read “✓ in tray” after collection. An inactive nested host keeps its idle control quiet while an outer host is active. An unhosted AddToTray remains visible; deduplication still belongs to the store/key.

Collection controls preserve selection and ordinary copy. Highlight alone never adds. Explicit note editing may focus its input. Only the File Viewer's own line gutter collects file-line references; excerpt panes do not gain that gutter.

The tray neither navigates the host chat nor creates a role. Native origin/window trust, parser validation and bridge teardown remain the frame owners' duties. The pinned chat DOM adapter reads the selected row's recorded time and names a broken read; it does not fabricate a timestamp or page the timeline. Later asynchronous held loss is represented by the filed message and log, without automatic restoration of browser picks.

**L184.** The tray's send result says held · rate limited with the time left in one compact unit, and the full view adds the exact reset with date and zone.

## Evidence

- Collection admission, first-target choice and snapshot settlement [1]

- Exact structured reference identity [2]

- Per-target developer send and explicit outcome parsing [3]

- One dock outside the retained frame, its column placement at the message box's own left and width. [4]

- A hosted idle object control follows its own hover/focus host; the named taken control and repeated click remain explicit. [5]

- The Chats pane publishes the chat its own frame reports showing, and nothing else: a frame that has not reported a chat yet names none, and while a placeholder stands in for the frame it publishes nothing. [6]


- A review pick stays minimized with the column closed; explicit expansion opens it, while one pending target default ends on user choice, empty automatic collection or leaving review. [7]

- A Send aimed at an archived or placeholder explainer first asks that leaf’s fixed-target first-request form to open with the current text. If no live target remains, no role-chat post or settlement occurs and the collection stays; a mixed selection continues through ordinary live-target posting and settlement. This handoff is not reported as native delivery. The minimized line’s head also expands on a click, Enter or space outside a nested control; the nested button, link, input, textarea, select and listed ARIA control targets retain their own actions, so Close does not also expand. The existing closed-column minimized-pick rule remains separate from the explicit first-request signal that opens its matching column. [8]
