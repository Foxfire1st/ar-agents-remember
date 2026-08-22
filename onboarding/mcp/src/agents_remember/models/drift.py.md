# mcp/src/agents_remember/models/drift.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/models/drift.py`  |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-02T01:05+02:00                     |
| lastVerifiedCommitHash | `eb7ea60ab9919f009fef58f81afe5861aa1709da` |
| lastVerifiedCommitDate | 2026-08-22T11:44:33+02:00|
| governingOverview      | `overview.md`                              |

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The strict `DriftSummary` model exposes status and the optional diagnostic error. | `DriftSummary` | mcp/src/agents_remember/models/drift.py:13-23 |
| Context packet construction validates `_drift_packet` output with `DriftSummary.model_validate`; `_drift_packet` is typed as `DriftSummaryPacket`. | "drift=DriftSummary.model_validate"; "def _drift_packet"; "-> DriftSummaryPacket" | mcp/src/agents_remember/application/context_packet.py:105-105; mcp/src/agents_remember/application/context_packet.py:177-177; mcp/src/agents_remember/application/context_packet.py:181-181 |
| The onboarding drift model defines the `DriftStatus` and `DriftSummaryPacket` wire shapes. | "DriftStatus = Literal["; `DriftSummaryPacket` | mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/models.py:11-19; mcp/src/agents_remember/models/drift.py:11-11 |
| Both wire models expose the shared `DriftStatus` and optional error diagnostic. | "class DriftSummary"; "class DriftCheckResponse(ToolResponse):" | mcp/src/agents_remember/models/drift.py:13-14; mcp/src/agents_remember/models/memory.py:13-13 |
| These tests pin the drift diagnostic and both wire-model status validations. | `test_the_drift_error_diagnostic_survives_its_own_boundary`; `test_every_drift_status_validates_at_both_of_its_wire_models` | mcp/tests/test_wire_vocabulary_exhaustiveness.py:741-746; mcp/tests/test_wire_vocabulary_exhaustiveness.py:777-786 |

## Update History

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-04T13:54+02:00 — 260731-EFA-L6 S18-B13 curator: reissued whole-claim evidence for context validation and both drift wire-model faces for same-reviewer closure.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-01T09:31+02:00 — 260731-EFA-L4 curator: body corrected. The card described a model that
  "exposes whether drift was checked" plus counts, report path and sample — and that was the whole
  of it, which is precisely the defect: `DriftSummary` had no `error` member on `status` and no
  `error` field, while `run_drift_summary` returns `{"status": "error", "error": ...}` whenever
  the onboarding root is missing. `include_drift=true` against a repo without onboarding therefore
  raised a `ValidationError` out of the `context_packet` tool instead of reporting the reason —
  the diagnostic path was the one that crashed. `status` is now `DriftStatus` imported from
  `memory_quality.integrity.onboarding_drift_check.models` (the producer of the shared vocabulary:
  `notChecked | checked | error`), the local `DriftStatus = Literal["notChecked", "checked"]` is
  deleted, and `error: str | None = None` is declared. Added three invariants. The controller row
  gained `_drift_packet` with its new `DriftSummaryPacket` return type, and rows were added for the
  producing models module, for `models/memory.py` as the second wire face, and for the two
  exhaustiveness tests that pin it. Verification metadata pinned until closeout stamps the architecture slice.
  commit.
- 2026-05-28T19:52+02:00: Created for the context-packet drift summary model.
