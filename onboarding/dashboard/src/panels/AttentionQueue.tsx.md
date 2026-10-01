# dashboard/src/panels/AttentionQueue.tsx

## Governing Overview

[panels/ overview](overview.md)

## Purpose

The home-screen attention queue (note 06): the **server-ranked** list of what needs the human,
rendered through the dashboard's task-centric lens when a queued lifecycle has a bound task document.
"Open" couples into the detail view (the queue↔detail coupling). The queue also exposes a server-write
`Dismiss` / `Clear all` affordances for lifecycle-bound throwaway attention rows. Gate-open rows are
consumed by server-side gate cancellation/deletion; actionable-drift rows are dismissible repo-level
one-shots anchored by the drift snapshot timestamp. Other non-lifecycle alarms remain visible until
their source condition clears.

## Code Commentary

### Logic

Since L15 the panel's served ages advance LOCALLY: the wire carries stable forms without the volatile *Seconds fields, so the panel derives display ages from per-object arrival anchors (data/servedAges.ts) refreshed by a 10-second useNowMs ticker — the deliberate, disclosed deviation from the no-re-render ideal that replaced the per-second whole-payload churn.

Reads `selectQueue` (the reducer's `analytics.attentionQueue`, already severity-sorted) plus
`analytics.taskDocuments`. `taskForAttention` resolves a lifecycle-bound attention item to its
non-master task document when possible, `titleForAttention` promotes that task (`Task <id>: <title>`)
to the visible row title, and `detailForAttention` preserves the original attention title/detail as
secondary context. Each item is a `motion.li` (Motion enter/leave + layout reflow) styled by an `item`
Panda `cva` keyed on `severity` (alarm/warn/info border-left). A captured `lifecycleId` const drives
the "Open" `ghost` button. `canDismiss` limits per-row `Dismiss` and header `Clear all` to rows with
a lifecycle id, a gate-open `gateId`, or `kind === "actionable-drift"`; clicking either path first
calls `dashboardStore.suppressAttention(...)` so the row leaves the UI immediately, then posts
`postAttentionDismiss` with `itemId`, `kind`, nullable `lifecycleId`, and optional `gateId`. Failed
POSTs call `releaseAttention(...)`. Empty → a `muted` "queue clear".

### Conventions

Panda `css`/`cva`; the `Panel` chrome with a sizing `className` (`flex:0 1 auto; maxHeight:42%`). The
severity also drives a `<Dot>`, which is `aria-hidden` and therefore cannot carry the severity itself.
It is wrapped in a `severityMark` span that supplies the accessible name: `role="img"` plus
`aria-label={`Severity: ${q.severity}`}` (and the matching `title`), `data-testid="attn-severity"`.
The role is load-bearing — `aria-label` on a bare `<span>` names a `generic`, which ARIA prohibits
(axe-core `aria-prohibited-attr`, `serious`) and which no screen reader announces, so before the
wrapper carried a role the severity reached nobody. `LifecycleList`'s equivalent span needs no role
only because it sits inside React Aria's `role="option"`, whose name-from-content absorbs the label.
`severityMark` also takes the `flexShrink:0`, because the wrapper — not the `Dot` — is now the flex
item in the row.

### Invariants And Boundaries

The queue is computed server-side (never re-ranked here). Wait-times are formatted (`fmtWait`), never
computed from the clock. Dismissal stays source-scoped: lifecycle rows require a lifecycle target,
gate-open rows can be consumed by gate id, and actionable drift is the only targetless repo-level row
this component can dismiss. Provider/down/setup/start alarms remain fact-backed and cannot be dismissed
by this component. The severity must stay announced from a role that can hold a name: this panel's
mark has no surrounding widget role to inherit from, so the `role="img"` on `severityMark` is the only
thing putting the severity in the accessibility tree.

### 2026-07-24 Curator Delta

The kept-mounted attention rail is memoized and receives its visibility state. Its local age clock stops
while the full-bleed shell hides the rail, then refreshes when visible again; store updates still render
through the component's own subscription.

## Evidence

### Repo-Internal References

- The server-side attention queue this reads. [1]
- The `selectQueue` selector. [2]
- `canDismiss` admits lifecycle rows, gate-id gate rows, and actionable drift only. [3]
- `dismissItem` and `clearAll` optimistically suppress rows and release failed POSTs. [4]
- `severityMark` — the CSS style applied to the severity wrapper. [5]
- The `role="img"` / `aria-label` span rendered around the decorative `Dot`. [6]
- `Dot` is `aria-hidden`, so its consumers own the announced name. [7]
