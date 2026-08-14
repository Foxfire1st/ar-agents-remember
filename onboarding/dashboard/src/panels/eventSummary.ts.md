# dashboard/src/panels/eventSummary.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/eventSummary.ts`           |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-28T05:38+02:00                           |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`       |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels/ overview](overview.md)

## Purpose

Schema-aware Event River summary layer. It turns raw `ObserverEvent` envelopes into the small display
packet `EventRiver.tsx` needs: primary row label, optional task context, compact metadata, hover
diagnostics, raw diagnostic kind, and visibility/noise classification.

## Code Commentary

### Logic

`buildEventSummaryContext` gathers the existing lifecycle, enclosure, and task-document identity
inputs from the dashboard store and precomputes `enclosuresByLifecycle` with
`groupEnclosuresByLifecycle` plus `taskDocsByLifecycle` from projected task documents. `summarizeEvent`
dispatches only on known event kinds:

- `read.packet` preserves the original full-path hover behavior and uses the read packet's
  facts-only `data.files[].path` and `data.repoId`.
- `tool.completed` reads the explicit `data.tool`, `data.ok`, and `data.tokens` fields, maps common
  MCP tool ids to readable action text, and keeps unknown tool ids on a mechanical humanized fallback.
- `lifecycle.phase-changed` reads `data.phase` and renders the destination phase through a fixed
  phase-label table.
- lifecycle block/gate rows read structured `ask.prompt`, `ask.question`, or `ask.ask` fields so the
  waiting request is the row's primary text.
- `lifecycle.heartbeat` returns `visibility: "hidden"` so the default river does not drown useful
  activity in liveness noise.
- unknown event kinds fall back to raw `event.kind` and raw diagnostic title text.

`eventSummaryContextReady(event, context)` is the display-shaping gate used by `EventRiver.tsx`.
Lifecycle-bound rows require a live lifecycle, an explicit event enclosure present in the enclosure map,
or at least one projected task document for the lifecycle. Enclosure-only rows require that enclosure
to exist. Unbound workspace rows remain immediately displayable. This keeps raw lifecycle ids from
painting during reload before the projection context catches up.

`lifecycleContext` reuses `taskDocsForLifecycle`, `findLifecycleEnclosure`, `taskLabel`, and
`taskDocumentLabel` so event rows share the same task/leaf labels as Operations and Detail. Its label
fallback order is live lifecycle projection, explicit event enclosure, direct task documents grouped
by lifecycle id, then the raw event enclosure/lifecycle id. That lets retained event-history rows keep
the task name even after the corresponding live lifecycle projection disappears. `formatEventTime`
uses `Intl.DateTimeFormat` and falls back to `-` for malformed timestamps; it does not slice ISO
strings.

### Conventions

This module owns display translation only. It does not mutate raw events, infer payload values from
arbitrary strings, or parse serialized payload blobs. Known event summaries read documented fields;
fallbacks are intentionally honest and diagnostic.

### Invariants And Boundaries

- Protocol actor `model` displays as `agent`; the raw actor remains available in the hover
  diagnostics.
- Trust provenance remains visible in row metadata and row colour.
- Task labels come from existing task identity helpers, not a second lifecycle-id-to-task-name
  resolver; raw lifecycle ids are display fallbacks only after projection, enclosure, and task-document
  labels are unavailable.
- Heartbeat events stay in the store and raw stream; only the default Event River render hides them.
- Lifecycle/enclosure-bound rows are displayable only after their summary context is ready; this is a
  presentation gate, not raw-event deletion.
- Raw unknown kinds must remain visible as raw kinds rather than guessed prose.

## Docs References

No external domain documentation applies; this is dashboard-local presentation logic over the
repository's observer event contract.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The raw observer event envelope rendered by this formatter. | `ObserverEvent` | dashboard/src/types/event.ts:9-22 |
| Existing task identity helpers reused for lifecycle-attached event labels, including task-document title fallback. | `findLifecycleEnclosure`, `taskLabel`, `taskDocsForLifecycle`, `taskDocumentLabel` | dashboard/src/data/taskIdentity.ts:253-260; dashboard/src/data/taskIdentity.ts:262-279; dashboard/src/data/taskIdentity.ts:281-286; dashboard/src/data/taskIdentity.ts:288-293 |
| Ambient lifecycle emits `tool.completed`, `read.packet`, lifecycle phase, and block events with explicit fields. | "\"tool.completed\","; "\"read.packet\", \"observed\", \"model\", repoId=repo_id, files=projected"; "self._emit_locked(\"lifecycle.phase-changed\", \"declared\", \"model\", phase=phase)"; "\"lifecycle.blocked\"," | mcp/src/agents_remember/observer/ambient.py:418-418; mcp/src/agents_remember/observer/ambient.py:452-452; mcp/src/agents_remember/observer/ambient.py:312-312; mcp/src/agents_remember/observer/ambient.py:217-217 |
| The Event River component consumes these summaries for rendering. | `eventSummaryContextReady`, `summarizeEvent` | dashboard/src/panels/EventRiver.tsx:62-73 |
| Focused render coverage proves lifecycle-only history rows use task document labels instead of raw lifecycle ids. | "uses task document labels when event history no longer has a live lifecycle row" | dashboard/src/panels/EventRiver.test.tsx:312-332 |
| `eventSummaryContextReady` gates lifecycle/enclosure-bound rows on available lifecycle, enclosure, or task-document context. | `eventSummaryContextReady` | dashboard/src/panels/eventSummary.ts:143-156 |
| `EventRiver` drops not-ready rows before calling `summarizeEvent`. | `eventSummaryContextReady`, `summarizeEvent` | dashboard/src/panels/EventRiver.tsx:62-73 |
| The reload-order regression covers a lifecycle-bound row hidden until task-document context arrives. | "uses task document labels when event history no longer has a live lifecycle row" | dashboard/src/panels/EventRiver.test.tsx:312-332 |

## Cross-Repo References

No meaningful cross-repo references found.

## Update History
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: reviewed this sidecar against the frontend-rail change set (strict-target lint remediation: complexity, max-lines-per-function, react-hooks, jsx-a11y, and import-cycle fixes). No content impact: behavior-preserving refactor; the file's responsibilities and the claims in this card remain current. Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-03T03:59:59+02:00 — Curated 14 citation claims (7 table rows, 7 source-form repairs): added exact anchors and source paths; scoped fixer generated the final ranges.

- 2026-06-28T05:38+02:00 — Task 29: added `eventSummaryContextReady`, the Event River display-shaping
  gate that suppresses lifecycle/enclosure-bound rows until lifecycle, enclosure, or task-document context
  exists. Verification metadata pinned until closeout stamps the task-29 code commit.
- 2026-06-26T19:40+02:00 — Task 20 lifecycle label follow-up: grouped projected
  task documents by lifecycle id and extended `lifecycleContext` so retained
  event-history rows without a live lifecycle projection render the task
  document title before using raw enclosure or lifecycle ids. Verification
  metadata pinned until closeout stamps the reopened task-20 code commit.
- 2026-06-26T18:14+02:00 — Created for task 20: introduced the schema-aware
  Event River summary layer for readable tool, lifecycle, gate, task-context,
  actor, time, heartbeat, and unknown-fallback presentation. Verification
  metadata pinned until closeout stamps the task-20 code commit.
