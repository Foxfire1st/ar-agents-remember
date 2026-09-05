# mcp/src/agents_remember/certification/telemetry/projection.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/telemetry/projection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T12:30:00+02:00 |
| lastVerifiedCommitHash | `2cd360d8f45ccdcf640dc9c5d14b941ac2f0f8eb` |
| lastVerifiedCommitDate | 2026-09-04T12:20:39+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[Certification overview](../overview.md)

## Purpose

Reconstructs the boundary and Gate 1-5 projections of one execution durably from the recorded
journal events, without rerunning any rail. The projection folds only the durable events to expose
the operation admission/finalization boundaries, per-gate and per-rail history, certificate
history, diagnostics, the operation terminal, and span totals for the journal/status/wait/
dashboard surfaces, carrying exactly the identities the events carry.

## Code Commentary

### Logic

The per-gate and cross-cutting projection models (`RailTelemetryProjection`,
`GateTelemetryProjection`, `BoundaryTelemetryProjection`, `DiagnosticTelemetryProjection`,
`OperationTerminalProjection`, and the root `TelemetryProjection` at `projection.py:75-175`) are frozen
contract models; the root projection requires exactly five gates and verifies its own
`projectionDigest` (`_verify_digest` at `projection.py:169-174`) so a rendered projection is
content-addressable. `project_execution_telemetry` (`projection.py:193-244`) folds the ordered
event stream: it refuses an empty stream, seeds five empty gates plus one boundary, and dispatches
each event to `_fold_boundary`, the gate-state fold (`_fold_gate_state` with per-kind branches
`_fold_gate_started`, `_fold_rail_started`, `_fold_rail_terminal`, `_fold_catalog_complete`,
`_fold_gate_pass`, `_fold_gate_fail`, `_fold_certificate_refused`, `_fold_gate_blocked`,
`_fold_certificate_invalidated`), the diagnostic fold (`_fold_diagnostic_state`), or the
operation-terminal fold (`_fold_operation_terminal`); rail history is then attached per gate, span
totals are aggregated, and the projection digest is computed over the draft minus the digest
field. `project_gate_history` (`projection.py:515-520`) exposes the exact history for one gate,
and `_replace` (`projection.py:521-537`) rebuilds frozen models with targeted updates.

### Conventions

The projection is derived data: it never infers a rail pass or a certificate authority that the
events do not already carry, and it stays byte-deterministic for the same event stream.

### Invariants And Boundaries

- An empty event stream is refused; the projection requires at least one event.
- The root projection always carries exactly five gates in Gate 1-5 order.
- Projection identity (execution kind/id, operation kind/generation or diagnostic nonce) comes
  from the first event; lastRevision comes from the last event.
- The projection digest must equal the digest of its own content, so tampering is detectable.
- The fold never reruns a rail and never alters the store.

### Todos

None recorded.

## Docs References

No Domain Documentation source is configured for this memory root; the governing documentary
artifact is the CCR-R16@v3 requirement packet, whose normative requirement states that cost, order,
zero-start barriers, recovery, and public state must be reconstructable without ephemeral-log
parsing - exactly what this projection fold provides. Task artifact paths are not repo-relative
citations, so this fact is recorded as prose here.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The fold turns the durable event stream into one lossless boundary/gate projection. | `project_execution_telemetry` | mcp/src/agents_remember/certification/telemetry/projection.py:193-244 |
| The projection model is digest-bound and requires exactly five gates. | `TelemetryProjection`; `_verify_digest` | mcp/src/agents_remember/certification/telemetry/projection.py:147-174 |
| Per-gate fold branches reconstruct rail history, catalogs, certificate decisions, blocking, and invalidation from events alone. | `_fold_gate_state`; `_fold_catalog_complete`; `_fold_certificate_invalidated` | mcp/src/agents_remember/certification/telemetry/projection.py:245-270; mcp/src/agents_remember/certification/telemetry/projection.py:324-340; mcp/src/agents_remember/certification/telemetry/projection.py:408-426 |
| Gate history for one gate is exposed without a full-stream fold. | `project_gate_history` | mcp/src/agents_remember/certification/telemetry/projection.py:515-520 |
| Span totals aggregate the events' spans without double counting overlap. | `aggregate_span_totals` | mcp/src/agents_remember/certification/telemetry/models.py:243-264 |

## Cross-Repo References

No cross-repository implementation boundary is owned here.

## Update History

- 2026-09-04T12:30+02:00 - 260831-CCR-L16 Gate-5: created for the CCR-R16@v3 durable
  reconstruction projection (leaf 260831-CCR-L16, certified commit
  `2cd360d8f45ccdcf640dc9c5d14b941ac2f0f8eb`). Verification stamp advanced to the certified code
  commit.
