# dashboard/src/panels/AttentionQueue.tsx

## Governing Overview

[Panels overview](overview.md)

## Purpose

The server-ranked attention queue behind the bell in the Operations task-column head. The bell shows waiting count and the most pressing severity; opening it places the entries in a bounded scrollable Popover/Dialog over the tree without moving or shrinking that tree. Escape, an outside press or the bell closes the layer without dismissing its entries.

## Code Commentary

The bell reuses columnTabButton and an independently drawn panel-local BellIcon, not proposal code. Empty means no count and an accessible nothing-waiting label. Entry order remains selectQueue's server order; the bell finds its urgent tone independently of that order. AttentionQueueImpl measures a 0.62 bound of its owning column when opening and supplies Popover maxHeight; the layer recipe owns internal scrolling. AttentionLayer owns the entries, source-scoped actions and focus retention, not that measurement. Controls wrap within a narrow rail. Its ten-second served-age clock runs while the layer is mounted/open, not on the closed bell.

Waits start from server-served waitSeconds. [servedAges](../data/servedAges.ts.md) advances that value from the arrival stamp of the exact applied entry object, rather than deriving a fresh age from the render clock. An unanchored object uses its served value unchanged; a missing served value remains missing. Stable-equality identity reuse retains the original object and arrival anchor between real emissions.

Each plain li grid holds severity, cause, age and optional dismissal. Its second line shows the matching task document's short id/title; a lifecycle entry without such a document shows `lifecycle <id>`; a non-lifecycle entry shows its repository/lane. The lifecycle opener targets the same lifecycle even without a task document, and closes the layer. A non-master matching task document is preferred. Entries without dismissal keep the empty control's padding so their age aligns. The complete cause/location/severity/lane/age remains in the row hover.

canDismiss admits lifecycle rows, gate-open rows with a gate id, and actionable-drift one-shots. dismissAttentionItem and clearAllAttention optimistically suppress only the admitted entries and call postAttentionDismiss with itemId, kind, nullable lifecycleId and optional gateId; non-dismissed responses release the failed entries. Duplicate sends are guarded locally. Actionable-drift suppression is scoped to the triggering signal: the reducer retains a dismissal while signalTs is not newer than dismissedAt, and a newer snapshot/signal may surface the entry again. A missing signalTs remains suppressed while that emitted condition persists. Eligibility for an optimistic one-shot is not permanent acknowledgment of later drift. Provider/down/setup/start alarms remain visible until their source clears. Gate dismissal is source-scoped cancellation/deletion, not generic acknowledgment of any alarm. Removing a focused entry first focuses the Dialog so the keyboard can still close or traverse the layer.

Dot is decorative. Each severity wrapper must retain role=img and its Severity label: naming a bare generic span is prohibited and conveys nothing to a screen reader. The state wrapper inside the task ListBoxItem has a different naming owner (role=option); neither depends on hue alone. The old severity border, Motion row reflow, inline Panel sizing and separate Open-text buttons no longer describe this renderer.

The persistent bell is memoized with a stable callback; its own queue subscription still updates it. The former active-prop clock gate is historical: current layer lifetime gates age work, while LifecycleList separately controls hidden-rail collection work.

The layer's cause/title uses 0.8rem, matching task-page row text. Its item base, age and location/link use 0.72rem; dismissal inherits that base, and Clear all and the bell use columnTabButton at 0.72rem. These sizes replace proposal-scale text without changing layer geometry, queue ownership or actions. Dot remains a decorative 0.95em glyph, not ordinary text subject to the two-size census. Shared panel/header and empty-state typography retain their existing dashboard owners.

## Evidence

- Entry titles use 0.8rem; item-base, age and location/link text use 0.72rem, with dismissal inheriting the base. [16]
- Bell and Clear all take the column-specific 0.72rem tab recipe. [17]
- Task-page rows and smaller labels/counts supply the two text sizes. [18]

- Queue ownership, accessible bell and contained Popover/Dialog retain tree geometry and open the same lifecycle target. [8]
- The open layer maps server order, retains focus through entry removal and admits only source-scoped bulk dismissals. [9]
- Plain two-line entries retain accessible severity, full hover and exact lifecycle opening/dismissal. [10]

- Source-scoped dismissal and failed-response restoration remain explicit helpers. [11]

- The layer bound is a proportion of its owning column. [12]
- Mounted tests preserve lifecycle/drift payloads, protected alarms, empty/count/tone behavior and layer close without dismissal. [13]


- Dismissal suppression compares the triggering signal with its dismissal and permits newer signals to reappear. [14]

- Queue wait labels advance server-served values from applied-object arrival, without inventing missing ages. [15]
