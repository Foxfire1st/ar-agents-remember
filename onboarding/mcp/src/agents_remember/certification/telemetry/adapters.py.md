# mcp/src/agents_remember/certification/telemetry/adapters.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/telemetry/adapters.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T12:30:00+02:00 |
| lastVerifiedCommitHash | `2cd360d8f45ccdcf640dc9c5d14b941ac2f0f8eb` |
| lastVerifiedCommitDate | 2026-09-04T12:20:39+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[Certification overview](../overview.md)

## Purpose

Compiles immutable CCR-R16@v3 telemetry events from the owner-produced R11/R20/R21/R22 objects of
the five-gate closeout domain. Every adapter builds one `TelemetryEvent` whose certificate disposition,
certificate identity, and gate-result-manifest identity come from the closed exhaustive
`EVENT_MATRIX` table, so an adapter can never publish an authority it does not own. Catalog manifest
identities are the digest of the ordered terminal set and counts; rail results, gate
certificates, admission manifests, finalization authorities, reuse plans, and invalidation
decisions are bound by their exact content digests.

## Code Commentary

### Logic

`TelemetryExecutionContext` (`adapters.py:93-107`) is the frozen execution-coherent identity every
compiled event is bound to: execution kind/id, monotonic event revision, and - for closeout
generations - operation kind and public generation, or - for diagnostic runs - the R13 nonce,
plus optional candidate, profile, and occurrence timestamp. The twenty public compile adapters
each take the context plus one owned domain object and return the exact event kind:
`compile_admission_started`/`compile_admission_refused`/`compile_candidate_admitted` bind the admission boundary
(`adapters.py:123-165`), `compile_gate_started`/`compile_rail_started`/`compile_rail_terminal` bind gate and rail
identity (`adapters.py:166-235`), `compile_gate_catalog_complete`/`compile_gate_pass_published`/
`compile_gate_pass_reused`/`compile_gate_fail` bind the complete-catalog decisions
(`adapters.py:236-356`), and `compile_certificate_refused`/`compile_gate_blocked`/
`compile_certificate_invalidated` bind refusal/block/invalidation events (`adapters.py:357-432`).
`compile_diagnostic_started`/`compile_diagnostic_terminal` bound diagnostic runs
(`adapters.py:433-463`); the finalization group (`compile_finalization_started`,
`compile_finalization_boundary_resumed`, `compile_finalization_completed`, `compile_execution_disposition`,
`compile_operation_terminal`) binds boundary/terminal state (`adapters.py:464-548`);
`compile_reuse_dependency_decision` projects the R21 dependency decision
(`adapters.py:549-566`). `span` (`adapters.py:567-583`) builds one separately timed span
(Dagger is an executor span, never a gate). `_base_event` (`adapters.py:584-612`) applies the matrix cell,
attaches optional identity fields, requires candidate and profile, and constructs the event;
`_authority_record`, `_catalog_counts`, `_terminal_disposition`, and
`_finding_from_result` are the digest/disposition projection helpers shared by the adapters.

### Conventions

Adapters are the only place domain objects cross into the telemetry vocabulary; the models layer
never sees R11/R20/R21/R22 objects.

### Invariants And Boundaries

- An adapter can never publish a certificate disposition, certificate id, or manifest id the
  exhaustive matrix does not grant to its event kind.
- Catalog manifest identities must equal the digest of the ordered terminal set plus counts.
- Certificate, rail, and runtime identities are bound by exact content digests; nothing is
  inferred from filenames, wall time, or caller-supplied strings.
- Diagnostic-run adapters never attach gate/certificate/delivery/approval/finalization authority.

### Todos

None recorded.

## Docs References

No Domain Documentation source is configured for this memory root; the governing documentary
artifact is the CCR-R16@v3 requirement packet, whose exhaustive event matrix defines the legal
context/outcome and required payload for every event kind the adapters compile. Task artifact
paths are not repo-relative citations, so this fact is recorded as prose here.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Execution-coherent identity is fixed before any event is compiled. | `TelemetryExecutionContext` | mcp/src/agents_remember/certification/telemetry/adapters.py:93-107 |
| Admission, gate/rail, catalog-decision, refusal/block/invalidation, diagnostic, and finalization adapters map owned domain objects into events. | `compile_candidate_admitted`; `compile_gate_pass_published`; `compile_rail_terminal`; `compile_finalization_completed` | mcp/src/agents_remember/certification/telemetry/adapters.py:148-165; mcp/src/agents_remember/certification/telemetry/adapters.py:279-304; mcp/src/agents_remember/certification/telemetry/adapters.py:210-235; mcp/src/agents_remember/certification/telemetry/adapters.py:498-513 |
| Every event is assembled through one matrix-driven base path that requires candidate and profile. | `_base_event` | mcp/src/agents_remember/certification/telemetry/adapters.py:584-612 |
| Separate spans carry executor time without ever becoming gate evidence. | `span`; `TelemetrySpan` | mcp/src/agents_remember/certification/telemetry/adapters.py:567-583; mcp/src/agents_remember/certification/telemetry/models.py:218-234 |
| The event kind vocabulary the adapters emit is fixed by the models layer. | `EventKind`; `EVENT_MATRIX` | mcp/src/agents_remember/certification/telemetry/models.py:82-107; mcp/src/agents_remember/certification/telemetry/models.py:160-185 |
| The facade exposes the full adapter set. | `compile_*`; `span` | mcp/src/agents_remember/certification/telemetry/__init__.py:3-27 |

## Cross-Repo References

No cross-repository implementation boundary is owned here.

## Update History

- 2026-09-04T12:30+02:00 - 260831-CCR-L16 Gate-5: created for the CCR-R16@v3 event-compile
  adapters (leaf 260831-CCR-L16, certified commit
  `2cd360d8f45ccdcf640dc9c5d14b941ac2f0f8eb`). Verification stamp advanced to the certified code
  commit.
