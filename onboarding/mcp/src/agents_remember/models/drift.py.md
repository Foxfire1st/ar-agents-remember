# mcp/src/agents_remember/models/drift.py

## Governing Overview

[overview.md](overview.md)

## Purpose

`drift.py` defines the compact drift summary embedded in `ContextPacketV2`.

## Code Commentary

`DriftSummary` is strict and exposes the check status, optional total
and actionable counts, an optional report path, a bounded actionable sample, and
An optional error field is also part of the strict summary.

`status` is `DriftStatus`, **imported** from
`memory_quality.integrity.onboarding_drift_check.models`, the module
that produces it: `notChecked | checked | error`. This file used to declare its
own `DriftStatus = Literal["notChecked", "checked"]`, one of three hand-written
copies of the same vocabulary in the package, and the only one missing `error`.

**The diagnostic path was the one that crashed.** `run_drift_summary` returns
`{"status": "error", "error": ...}` when the onboarding root is missing. This
strict model rejected *both* halves — the status value and the `error` key — so
`include_drift=true` against a repo without onboarding raised out of the
`context_packet` tool instead of reporting why. `DriftCheckResponse`
(`models/memory.py`) had carried both all along; the summary embedded in the
context packet had not.

## Invariants And Boundaries

- Context-packet drift is a summary, not the full drift report.
- `status` is not declared here. It is `DriftStatus` from the drift-check
  models module, which is where `run_drift_summary` decides it; the same alias
  now also types `DriftCheckResponse.status`, so the two wire faces of one
  vocabulary cannot diverge.
- **A report-why field must be at least as wide as the failure it reports.** A
  strict model that omits the error member of a status enum turns its own
  diagnostic into an exception.
- Full memory quality workflows stay under the memory quality tools and reports.

## Evidence

### Repo-Internal References

- The strict `DriftSummary` model exposes status and the optional diagnostic error. [1]
- Context packet construction validates `_drift_packet` output with `DriftSummary.model_validate`; `_drift_packet` is typed as `DriftSummaryPacket`. [2]
- The onboarding drift model defines the `DriftStatus` and `DriftSummaryPacket` wire shapes. [3]
- Both wire models expose the shared `DriftStatus` and optional error diagnostic. [4]
