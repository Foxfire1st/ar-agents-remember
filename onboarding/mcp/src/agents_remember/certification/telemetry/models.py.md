# mcp/src/agents_remember/certification/telemetry/models.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/telemetry/models.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T12:30:00+02:00 |
| lastVerifiedCommitHash | `2cd360d8f45ccdcf640dc9c5d14b941ac2f0f8eb` |
| lastVerifiedCommitDate | 2026-09-04T12:20:39+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[Certification overview](../overview.md)

## Purpose

The CCR-R16@v3 durable boundary, gate, and rail telemetry event schema and its closed
vocabularies. Every event carries executionKind, executionId, a monotonic eventRevision, the
candidate / R22 profile / applicable R11 plan, the consumed runtime identity, timestamp, bounded
evidence references, and the always-present certificateDisposition / certificateId /
gateResultManifestId keys. A closeout-generation event requires operation kind and the public
generation with a null diagnostic nonce; a diagnostic-run event requires the R13 nonce and can
never acquire gate, certificate, delivery, approval, or finalization authority. The exhaustive
event matrix, certificate refusal codes, and terminal result classes are closed vocabularies.

## Code Commentary

### Logic

The module defines the closed type vocabularies first: `TelemetryExecutionKind`, `CertificateDisposition`,
`CertificateRefusalCode`, `TerminalResultClass`, `RailTerminalDisposition`, `TelemetrySpanKind`,
`PassFailAborted`, and the twenty-four-member `EventKind` literal (`models.py:39-107`), plus the
derived kind partitions `CONTROL_EVENT_KINDS`, `DIAGNOSTIC_ONLY_EVENT_KINDS`, `CLOSEOUT_EVENT_KINDS`,
`CERTIFICATE_REFUSAL_CODES`, and `TERMINAL_RESULT_CLASSES` (`models.py:113-148`).
`MatrixCell` (`models.py:152-188`) models one exhaustive-matrix row (disposition plus
certificate/manifest ID cardinality) and `EVENT_MATRIX` (`models.py:160-185`) maps all
twenty-four kinds to their cell. `GateCitation` (`models.py:189-200`) binds the attempt / catalog
revision / catalog manifest identity triple. `TelemetrySpan` and `SpanTotals` with
`aggregate_span_totals` (`models.py:218-264`) model separately timed spans whose active time never
exceeds wall time. `CatalogCounts`/@TICK@@CatalogRailRecord`/`catalog_manifest_digest`
(`models.py:294-343`) make the ordered terminal set and counts content-addressable.
`R21DependencyDecision` (`models.py:344-368`) and `FinalizationAuthorityRecord`
(`models.py:369-378`) carry the R21 reuse and finalization authority facts. The
`_PayloadKindBase` subclasses (`models.py:379-671`) define one immutable payload per event kind;
each payload validates its own shape (for example `GateStartedPayload` requires the exact green
predecessor prefix, `RailStartedPayload` requires a positive attempt repetition, and
`GateCatalogCompletePayload` requires canonical ordered records whose derived counts match).
`TelemetryEvent` (`models.py:673-851`) is the root frozen model; its model validators enforce the
execution identity contract (`_verify_execution_identity`), the eventKind-to-payload kind
agreement and closeout/diagnostic envelope partition (`_verify_kind_payload`), the matrix ID
cardinality (`_verify_id_cardinality`), the exact gate/rail identity and payload-shape rules
(`_verify_event_shape`), catalog manifest digest binding (`_verify_catalog_payload_digest`), the
Gate-4 certifying-rail rule (`_verify_gate_four_shape`), and the operation-terminal manifest rule
(`_verify_operation_terminal`). `dispositions_for_event_kind` and `event_matrix_cell`
(`models.py:853-920`) expose the closed matrix to the other layers.

### Conventions

All events and payloads are frozen contract models; all vocabularies are closed Literals, tuples,
or frozensets with no open-ended extension point.

### Invariants And Boundaries

- A diagnostic-run event can never acquire gate, certificate, delivery, approval, or
  finalization authority.
- Certificate disposition is exactly not-applicable, pending, published, reused, refused, or
  invalidated; IDs are digest strings only where the matrix permits and null otherwise.
- gateResultManifestId must equal the digest of the ordered terminal set and counts for catalog
  events and must cite the exact catalog manifest for decisions.
- Event revisions are monotonic and positive; rail repetition counts are positive.
- The module carries schema only: it never persists events or validates streams.

### Todos

None recorded.

## Docs References

No Domain Documentation source is configured for this memory root; the governing documentary
artifact is the CCR-R16@v3 requirement packet, whose execution-identity and exhaustive-event-matrix
sections normatively define the vocabularies and cardinalities this schema encodes. Task artifact
paths are not repo-relative citations, so this fact is recorded as prose here.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The exhaustive matrix fixes one disposition and ID cardinality per event kind. | `EVENT_MATRIX`; `MatrixCell` | mcp/src/agents_remember/certification/telemetry/models.py:160-185; mcp/src/agents_remember/certification/telemetry/models.py:152-158 |
| The root event enforces execution identity, envelope partition, matrix cardinality, exact gate/rail identity, and digest binding. | `TelemetryEvent` | mcp/src/agents_remember/certification/telemetry/models.py:673-851 |
| Per-kind payloads validate their own shape before an event may carry them. | `GateStartedPayload`; `GateCatalogCompletePayload`; `RailStartedPayload` | mcp/src/agents_remember/certification/telemetry/models.py:405-417; mcp/src/agents_remember/certification/telemetry/models.py:444-498; mcp/src/agents_remember/certification/telemetry/models.py:418-434 |
| Content-addressed catalog and decision models keep manifest identities deterministic. | `catalog_manifest_digest`; `CatalogRailRecord` | mcp/src/agents_remember/certification/telemetry/models.py:330-343; mcp/src/agents_remember/certification/telemetry/models.py:308-329 |
| The adapters compile events against exactly these matrix cells. | `_base_event` | mcp/src/agents_remember/certification/telemetry/adapters.py:584-612 |

## Cross-Repo References

No cross-repository implementation boundary is owned here.

## Update History

- 2026-09-04T12:30+02:00 - 260831-CCR-L16 Gate-5: created for the CCR-R16@v3 telemetry event
  schema and closed vocabularies (leaf 260831-CCR-L16, certified commit
  `2cd360d8f45ccdcf640dc9c5d14b941ac2f0f8eb`). Verification stamp advanced to the certified code
  commit.
