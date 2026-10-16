# dashboard/src/panels/eventSummary.ts

## Governing Overview

[panels/ overview](overview.md)

## Purpose

Schema-aware Event River summary layer. It turns raw `ObserverEvent` envelopes into the small display
packet `EventRiver.tsx` needs: primary row label, optional task context, compact metadata, hover
diagnostics, raw diagnostic kind, and visibility/noise classification.

## Code Commentary

### Logic

`summarizeEvent(event)` dispatches directly on known kinds with no projection context, lifecycle label join or readiness gate.

- read.packet uses explicit file paths/repo facts and full-path hover.
- tool.completed uses explicit tool, caller, outcome and target fields; known roles get friendly labels, unknown roles/tasks remain verbatim.
- Unknown kinds, including retained historical lifecycle events, remain raw diagnostic kinds rather than guessed state changes. Their displayed context uses the explicit enclosure first and the repository only when no enclosure is present (`enclosure ?? repoId`); it does not repeat the repository beside the enclosure or reintroduce a task-state join.

No eventSummaryContextReady gate remains. Displaying a raw event does not depend on task, lifecycle or enclosure projection arrival.

Task/caller context comes from the event’s explicit fields, not task identity helper joins. formatEventTime uses Intl.DateTimeFormat and returns - for malformed timestamps.

### 260928-MIK-L114 Host-Path Caller Rows

`summarizeToolCompleted` divides on caller facts: rows carrying them show who called
(role and task, or chat with harness), the outcome as done / refused with code / reached
state, and the started or addressed role for role tools. Earlier-kind rows carry no caller
facts and keep their base ok/failed labels without inventing caller or lifecycle context. Unknown roles and tasks
render verbatim; only known roles keep friendly labels.

### Conventions

This module owns display translation only. It does not mutate raw events, infer payload values from
arbitrary strings, or parse serialized payload blobs. Known event summaries read documented fields;
fallbacks are intentionally honest and diagnostic.

### Invariants And Boundaries

- model displays as agent; raw actor/kind and trust stay visible.
- Explicit caller/target roles and legacy outcomes survive.
- Unknown kinds remain verbatim, without lifecycle/context handlers.

## Evidence

### Docs References

No external domain documentation applies; this is dashboard-local presentation logic over the
repository's observer event contract.

### Repo-Internal References

- The raw observer event envelope rendered by this formatter. [1]
- The Event River component consumes these summaries for rendering. [4]

- Unknown-event context prefers the explicit enclosure and otherwise the repository; the existing assertion checks enclosure presence and repository absence. [14]

### Cross-Repo References

No meaningful cross-repo references found.


## Current enclosure-only composition

Existing unknown-tool humanization statement remains correct. TOOL_LABELS loses cgc callers/callees/complexity/dependencies/symbol, drift_check, grepai_search and lifecycle gate/phase/resume/start entries. Old retained events are not deleted: those IDs now reach toolLabel mechanical humanization, with failure suffix/caller/outcome context unchanged.

### Maintenance boundaries

Removed tool labels take the ordinary mechanical humanization fallback; removing a label is not deleting event history. The only specialized event summarizers are read.packet and tool.completed; lifecycle phase/heartbeat/context handling is absent.

Source/test/fixture inspection is not a fresh mounted capture or a passing test run.
Historical provider-shaped input data and retained compatibility definitions do not
restore removed provider visuals or tool exposure.


- The current friendly-tool label map omits removed tool IDs; retained event history is not removed. [10]


- An unlisted tool ID uses mechanical humanization rather than reinstating removed tool exposure. [11]


- Only read.packet and tool.completed have specialized summary handlers; other kinds use the honest unknown-kind fallback. [12]


- The tool.completed formatter preserves explicit failure, caller, target and outcome facts without a task-state projection join. [13]
