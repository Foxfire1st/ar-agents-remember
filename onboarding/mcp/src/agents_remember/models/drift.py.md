# mcp/src/agents_remember/models/drift.py

## Governing Overview

[overview.md](overview.md)

## Purpose

`drift.py` defines the compact drift summary embedded in `ContextPacketV2`.

## Code Commentary

`DriftSummary` is strict and exposes the check status, optional total
and actionable counts, an optional report path, a bounded actionable sample, and an optional error field. For a converted tree it also carries what
was really measured — `basis`, `memoryRoot`, `codeRoot`, `sidecarCount`, `states`, `violationCount`,
`violationSample`, `reportOnlyCount` and `unreadableSidecars` — each optional and absent on legacy
results; legacy fields are never invented for a converted card, and vice versa.

`status` uses `DriftStatus`, declared in this module as
`Literal["notChecked", "checked", "error"]`. The drift packet model and
`models/memory.py` import this canonical declaration. This file's earlier
two-state declaration lacked `error`; the current declaration includes it.

`run_drift_summary` measures an absent onboarding collection as checked zero on converted memory. An existing non-directory onboarding path, legacy memory or a failed converted-tree measurement returns an error diagnostic. The strict summary accepts both the `error` status and its optional reason.

The earlier diagnostic failure belongs to model history. Before the three-state vocabulary and
optional `error` field were added, the producer's missing-root error packet could be rejected by
this strict model for both its status and its extra key; `DriftCheckResponse` already carried them.
That historical model repair does not describe the current absent-root behavior: converted readers
now measure the absent collection as checked zero. The remaining real error branches still need
the shared error status and diagnostic field.

## Invariants And Boundaries

- Context-packet drift is a summary, not the full drift report.
- `DriftStatus` is declared here and imported by the drift packet model and
  `DriftCheckResponse`; the producer emits members of that shared vocabulary.
  The context and tool wire faces therefore use the same three states.
- **A report-why field must be at least as wide as the failure it reports.** A
  strict model that omits the error member of a status enum turns its own
  diagnostic into an exception.
- Full memory quality workflows stay under the memory quality tools and reports.

## Evidence

### Repo-Internal References

- Context packet construction validates `_drift_packet` output with `DriftSummary.model_validate`; `_drift_packet` is typed as `DriftSummaryPacket`. [2]



- The onboarding drift model imports canonical `DriftStatus` and defines the `DriftSummaryPacket` wire shape. [3]

- Both wire models expose the shared `DriftStatus` and optional error diagnostic.  Anchor: "class DriftSummary"; "class DriftCheckResponse(ToolResponse):" [4]

- The strict `DriftSummary` model exposes status and the optional diagnostic error. [1]
- The summary carries the converted measurement fields beside the legacy ones. [5]
