# dashboard/src/panels/eventSummary.ts

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

## Evidence

### Docs References

No external domain documentation applies; this is dashboard-local presentation logic over the
repository's observer event contract.

### Repo-Internal References

- The raw observer event envelope rendered by this formatter. [1]
- Existing task identity helpers reused for lifecycle-attached event labels, including task-document title fallback. [2]
- Ambient lifecycle emits `tool.completed`, `read.packet`, lifecycle phase, and block events with explicit fields. [3]
- The Event River component consumes these summaries for rendering. [4]
- Focused render coverage proves lifecycle-only history rows use task document labels instead of raw lifecycle ids. [5]
- `eventSummaryContextReady` gates lifecycle/enclosure-bound rows on available lifecycle, enclosure, or task-document context. [6]
- `EventRiver` drops not-ready rows before calling `summarizeEvent`. [7]
- The reload-order regression covers a lifecycle-bound row hidden until task-document context arrives. [8]

### Cross-Repo References

No meaningful cross-repo references found.
