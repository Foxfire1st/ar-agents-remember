# mcp/src/agents_remember/certification/telemetry/adapters.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/telemetry/adapters.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T12:30:00+02:00 |
| lastVerifiedCommitHash | `602143bd1d48226f4d53b83ff7c5002a695dcdff` |
| lastVerifiedCommitDate | 2026-09-09T00:26:24+02:00|
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
| Execution-coherent identity is fixed before any event is compiled. | `TelemetryExecutionContext` | mcp/src/agents_remember/certification/telemetry/adapters.py:91-103 |
| Admission telemetry derives the candidate-admitted event from its owned inputs. | "def compile_candidate_admitted" | mcp/src/agents_remember/certification/telemetry/adapters.py:147-162 |
| Pass telemetry derives the publication event from its owned gate evidence. | "def compile_gate_pass_published" | mcp/src/agents_remember/certification/telemetry/adapters.py:278-301 |
| Rail telemetry projects the terminal rail observation. | "def compile_rail_terminal" | mcp/src/agents_remember/certification/telemetry/adapters.py:209-232 |
| Finalization telemetry projects completion from its owned finalization inputs. | "def compile_finalization_completed" | mcp/src/agents_remember/certification/telemetry/adapters.py:497-510 |
| Every event is assembled through one matrix-driven base path that requires candidate and profile. | `_base_event` | mcp/src/agents_remember/certification/telemetry/adapters.py:583-609 |
| Separate spans carry executor time without ever becoming gate evidence. | "def span("; "class TelemetrySpan(FrozenContractModel)" | mcp/src/agents_remember/certification/telemetry/adapters.py:566-580; mcp/src/agents_remember/certification/telemetry/models.py:220-234 |
| The event kind vocabulary the adapters emit is fixed by the models layer. | `EventKind`; `EVENT_MATRIX` | mcp/src/agents_remember/certification/telemetry/models.py:82-107; mcp/src/agents_remember/certification/telemetry/models.py:160-185 |
| The facade exposes the full adapter set through its explicit export table. | `__all__` | mcp/src/agents_remember/certification/telemetry/__init__.py:105-197 |

## Cross-Repo References

No cross-repository implementation boundary is owned here.

## Update History

- 2026-09-09T02:49:53+02:00 — CCR-L38 bounded inherited claim reconciliation: replaced generic type-use anchors with the exact span helper and model declarations. Source hashes: mcp/src/agents_remember/certification/telemetry/adapters.py=18cc9d511188ad2d835419acd6dd1251260c3233d06e1454291aa53a4ecb9ecd, mcp/src/agents_remember/certification/telemetry/models.py=482cc098f1f2cae2165a6beb91e524251af79a7c1bfc31071f63a928da255cf6; verification metadata remains unchanged.

- 2026-09-09T02:42:21+02:00 — CCR-L24 inherited/current-source reconciliation 2026-09-09: Re-read the current card claims against the frozen candidate source and repaired exact citation coordinates (span→566-580; __all__ export table→105-197). Preserved claim prose; source-sha256=18cc9d511188ad2d835419acd6dd1251260c3233d06e1454291aa53a4ecb9ecd; verification metadata remains unchanged because commit-owned realization is pending.

- 2026-09-09T02:42:21+02:00 — CCR-L24 inherited citation follow-up: corrected the retained `span` body citation to the current definition range `566-580` after the first reconciliation history entry; source-sha256=18cc9d511188ad2d835419acd6dd1251260c3233d06e1454291aa53a4ecb9ecd. Verification metadata remains unchanged because commit-owned realization is pending.

- 2026-09-06T22:41:21+00:00: Generated citation repair: `TelemetryExecutionContext` repointed to mcp/src/agents_remember/certification/telemetry/adapters.py:91-103. No content impact: mechanical anchor-range projection bound to citation source snapshot 250eac92295fa399589ccf1c9726bfb4cd28a1a0b20dca126769403fba09b52d; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-06T22:41:21+00:00: Generated citation repair: `_base_event` repointed to mcp/src/agents_remember/certification/telemetry/adapters.py:583-609. No content impact: mechanical anchor-range projection bound to citation source snapshot 250eac92295fa399589ccf1c9726bfb4cd28a1a0b20dca126769403fba09b52d; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-04T12:30+02:00 - 260831-CCR-L16 Gate-5: created for the CCR-R16@v3 event-compile
  adapters (leaf 260831-CCR-L16, certified commit
  `2cd360d8f45ccdcf640dc9c5d14b941ac2f0f8eb`). Verification stamp advanced to the certified code
  commit.
