# mcp/src/agents_remember/models/drift.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/models/drift.py`  |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-01T09:31+02:00                     |
| lastVerifiedCommitHash | `e52edaf5b655f495580efd93306afdf922b19b51` |
| lastVerifiedCommitDate | 2026-08-01T11:01:51+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`drift.py` defines the compact drift summary embedded in `ContextPacketV2`.

## Code Commentary

`DriftSummary` (L13-L23) is strict and exposes the check status, optional total
and actionable counts, an optional report path, a bounded actionable sample, and
— since 260731-EFA-L4 — an optional `error` (L23).

`status` is `DriftStatus`, **imported** from
`memory_quality.integrity.onboarding_drift_check.models` (L14 there), the module
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

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Context packet construction validates drift output through this model; `_drift_packet` (L169-L180) is now typed `-> DriftSummaryPacket`. | [context_packet.py](agents-remember/mcp/src/agents_remember/controllers/context_packet.py) |
| `DriftStatus` (L14) and the `DriftSummaryPacket` TypedDict (L17-L20) this model is the wire face of. | [onboarding_drift_check/models.py](agents-remember/mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/models.py) |
| The second wire face of the same alias — `DriftCheckResponse.status`, which already carried `error` on both halves. | [memory.py](agents-remember/mcp/src/agents_remember/models/memory.py) |
| `test_the_drift_error_diagnostic_survives_its_own_boundary` and `test_every_drift_status_validates_at_both_of_its_wire_models` pin this. | [test_wire_vocabulary_exhaustiveness.py](agents-remember/mcp/tests/test_wire_vocabulary_exhaustiveness.py) |

## Update History

- 2026-08-01T09:31+02:00 — 260731-EFA-L4 curator: body corrected. The card described a model that
  "exposes whether drift was checked" plus counts, report path and sample — and that was the whole
  of it, which is precisely the defect: `DriftSummary` had no `error` member on `status` and no
  `error` field, while `run_drift_summary` returns `{"status": "error", "error": ...}` whenever
  the onboarding root is missing. `include_drift=true` against a repo without onboarding therefore
  raised a `ValidationError` out of the `context_packet` tool instead of reporting the reason —
  the diagnostic path was the one that crashed. `status` is now `DriftStatus` imported from
  `memory_quality.integrity.onboarding_drift_check.models` (L14 there:
  `notChecked | checked | error`), the local `DriftStatus = Literal["notChecked", "checked"]` is
  deleted, and `error: str | None = None` is declared (L23). Added three invariants. Citations:
  `DriftSummary` pinned to L13-L23 and `error` to L23; the controller row gained `_drift_packet`
  L169-L180 with its new `DriftSummaryPacket` return type, and rows were added for the producing
  models module (L14, L17-L20), for `models/memory.py` as the second wire face, and for the two
  exhaustiveness tests that pin it. Verification metadata pinned until closeout stamps the L4
  commit.
- 2026-05-28T19:52+02:00: Created for the context-packet drift summary model.
