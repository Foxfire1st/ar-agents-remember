# dashboard/src/panels/AttentionQueue.tsx

## Governing Overview

[Panels overview](overview.md)

## Purpose

The server-ranked attention queue behind the bell in the Operations task-column head. The bell shows waiting count and the most pressing severity; opening it places the entries in a bounded scrollable Popover/Dialog over the tree without moving or shrinking that tree. Escape, an outside press or the bell closes the layer without dismissing its entries.

## Code Commentary

The bell reuses columnTabButton and an independently drawn panel-local BellIcon, not proposal code. Empty means no count and an accessible nothing-waiting label. Entry order remains selectQueue's server order, which the reducer now serves newest first — by `waitSeconds` and then id, an entry without an age counting as zero (`observer/reducer_impl/_attention.py:80`) — and the bell finds its urgent tone independently of that order. AttentionQueueImpl measures a 0.62 bound of its owning column when opening and supplies Popover maxHeight; the layer recipe owns internal scrolling. AttentionLayer owns the entries, source-scoped actions, a Clear-all control gated only on the queue being non-empty, and focus retention, not that measurement. Controls wrap within a narrow rail. Its ten-second served-age clock runs while the layer is mounted/open, not on the closed bell.

Waits start from server-served waitSeconds. [servedAges](../data/servedAges.ts.md) advances that value from the arrival stamp of the exact applied entry object, rather than deriving a fresh age from the render clock. An unanchored object uses its served value unchanged; a missing served value remains missing. Stable-equality identity reuse retains the original object and arrival anchor between real emissions.

Each plain li grid holds severity, cause, server-served age and dismissal. Location is `entry.repoId`, falling back to `entry.lane`, without lifecycle/document matching; beside it every row renders the subject it can reach — a task control passing the row's exact served task key to the selection owner, and an agent control passing the row's exact agent target to the shell, with no invented task for a taskless agent. A row renders its × whatever the served `dismissible` flag says, so a live native cause shows one too; geometry, full hover and overlay closure remain presentation-owned.

A queue item dismisses by itemId and kind only, never lifecycle target or gateId; every row asks the server, the only early return being the duplicate guard on an id already in flight, and Clear all takes the whole queue and is hidden only when nothing is queued. Optimistic suppression is duplicate-guarded; failed replies restore entries and expose the failure notice. An actionable-drift acknowledgment suppresses the same complete actionable fingerprint; a different complete fingerprint can reappear. Missing fingerprints retain the acknowledgment. Every other kind hides exactly the occurrence it acknowledged: its record is reclaimed when a complete observation says that occurrence ended — an answered prompt, a delivered or withdrawn message, a bound turn — and the next occurrence of the same cause appears again (`observer/reducer_impl/_attention.py:78`, `observer/native_attention.py:93-97`, `controlplane/attention_dismissals.py:192-196`). Removing a focused entry first focuses the Dialog.

Dot is decorative. Each severity wrapper must retain role=img and its Severity label: naming a bare generic span is prohibited and conveys nothing to a screen reader. The state wrapper inside the task ListBoxItem has a different naming owner (role=option); neither depends on hue alone. The old severity border, Motion row reflow, inline Panel sizing and separate Open-text buttons no longer describe this renderer.

The persistent bell is a memoized component that now takes optional `onOpenTask`/`onOpenAgent` handlers from its column head; it holds no queue state of its own, and its own queue subscription still updates it. The former active-prop clock gate is historical: current layer lifetime gates age work, while LifecycleList separately controls hidden-rail collection work.

The layer's cause/title uses 0.8rem, matching task-page row text. Its item base, age and location use 0.72rem; dismissal inherits that base, and Clear all and the bell use columnTabButton at 0.72rem. These sizes replace proposal-scale text without changing layer geometry, queue ownership or actions. Dot remains a decorative 0.95em glyph, not ordinary text subject to the two-size census. Shared panel/header and empty-state typography retain their existing dashboard owners.

## Evidence


- Entry titles use 0.8rem; item-base, age and location text use 0.72rem, with dismissal inheriting the base. [16]

- Bell and Clear all take the column-specific 0.72rem tab recipe. [17]
- Task-page rows and smaller labels/counts supply the two text sizes. [18]



- Source-scoped dismissal and failed-response restoration remain explicit helpers. [11]


- The layer bound is a proportion of its owning column. [12]


- Actionable drift reappears on a different complete actionable fingerprint; missing fingerprints retain acknowledgment, and every other kind hides exactly the acknowledged occurrence, whose observed end reclaims the record before a new occurrence appears. [14]

- Queue wait labels advance server-served values from applied-object arrival, without inventing missing ages. [15]


- Rows render their location and a dismissal control on every entry - the published queue marks each row dismissible - and delegate task and agent controls to SubjectLinks only when the row names that subject and a handler is supplied. [19]
