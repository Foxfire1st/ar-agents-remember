# dashboard/src/panels/AttentionQueue.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/AttentionQueue.tsx`        |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-01T09:20+02:00                           |
| lastVerifiedCommitHash | `e52edaf5b655f495580efd93306afdf922b19b51`       |
| lastVerifiedCommitDate | 2026-08-01T11:01:51+02:00|
| governingOverview      | `overview.md`                                    |

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

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The server-side attention queue this reads. | — | [observer/reducer.py](agents-remember/mcp/src/agents_remember/observer/reducer.py) |
| The `selectQueue` selector. | L37-L46 | [data/selectors.ts](../data/selectors.ts) |
| `canDismiss` admits lifecycle rows, gate-id gate rows, and actionable drift only. | L122-L128 | [AttentionQueue.tsx](AttentionQueue.tsx) |
| `dismissItem` and `clearAll` optimistically suppress rows and release failed POSTs. | L146-L178 | [AttentionQueue.tsx](AttentionQueue.tsx) |
| `severityMark` — the wrapper that carries the severity's accessible name, and why the role is required. | L41-L49 | [AttentionQueue.tsx](AttentionQueue.tsx) |
| The `role="img"` / `aria-label` span rendered around the decorative `Dot`. | L222-L230 | [AttentionQueue.tsx](AttentionQueue.tsx) |
| `Dot` is `aria-hidden`, so its consumers own the announced name. | L118-L126 | [grammar/Dot.tsx](../grammar/Dot.tsx) |

## Update History

- 2026-08-01T09:20+02:00 — 260731-EFA-L4 curator: documented the `severityMark` wrapper — the `Dot`
  is `aria-hidden`, so the severity is now announced from a `role="img"` span with
  `aria-label="Severity: …"`; recorded why the role (not the label) is the fix, and that `flexShrink`
  moved to the wrapper because it is now the flex item. Repaired three stale citations against the
  current source: `selectQueue` L23-L32 → L37-L46 (the old range covered `hasLiveWorktree` and the
  `EMPTY_QUEUE` cache fields, not the selector), `canDismiss` L103-L118 → L122-L128 (the old range
  covered `titleForAttention`/`detailForAttention`/`dismissPayload`), and the dismiss row
  L126-L158 → L146-L178, renamed to the actual symbols `dismissItem`/`clearAll`.

- 2026-07-24T13:17:50Z — Documented memoized hidden-rail age behavior. Verification hash/date remain
  pinned to the pre-commit source stamp.

- 2026-07-07T10:50+02:00 — L15: served ages advance locally (servedAges anchors + 10s ticker); volatile fields no longer arrive on the wire. Verification metadata pinned until closeout stamps the L15 commit.

- 2026-07-07T05:30+02:00 — 260703-L15 S1: item wait times now advance locally —
  `fmtWait(servedAgeSeconds(q, q.waitSeconds, nowMs))` with a panel-level `useNowMs()` (10 s
  tick), because the change gate no longer re-serves the queue every tick just to age the waits.
  Verification metadata pinned until closeout stamps the L15 commit.
- 2026-06-28T07:32+02:00 — Task 29 S7 follow-up: `Dismiss`/`Clear all` now hide rows immediately via
  store-level optimistic suppression, release failed POSTs, and include targetless actionable-drift rows
  as the repo-level one-shot dismiss case. Verification metadata pinned until closeout stamps the task-29
  code commit.
- 2026-06-28T03:05+02:00 — Task 28 S5.2: `Dismiss` and `Clear all` now target only lifecycle-bound attention rows through `postAttentionDismiss`; non-lifecycle alarms no longer render dismissal controls. Verification metadata pinned until closeout stamps the task-28 code commit.
- 2026-06-25T14:02+02:00 — Task 24 reopened: `Clear` now includes stale gate-open rows with only `gateId`, posting a gate-id-only cancel instead of hiding or ignoring them.
- 2026-06-25T13:10+02:00 — Task 23/24: added the `Clear` gate-interaction action, backed by targeted cancel writes instead of local hiding.
- 2026-06-25T07:17+02:00 — Task 19: attention rows now resolve lifecycle-bound queue items through `analytics.taskDocuments` so the visible title is task-centric while the original lifecycle/gate attention text remains in detail. Verification metadata pinned until closeout stamps the task-19 code commit.
- 2026-06-15T17:00 — Created for slice 5d: migrated onto `Panel` + Panda `cva`. Verification metadata
  pinned until closeout stamps the 5d code commit.
