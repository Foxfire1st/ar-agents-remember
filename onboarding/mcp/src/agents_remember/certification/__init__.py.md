# mcp/src/agents_remember/certification/__init__.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/__init__.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-05T06:14:14+00:00 |
| lastVerifiedCommitHash | `288cdde8b3dc50950ea748f246a05e8162d41146` |
| lastVerifiedCommitDate | 2026-09-04T22:32:02+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Provides the repository-neutral public certification facade: canonical registry and plan operations, certificate storage and invalidation, exact-candidate lifecycle contracts, readiness projections, diagnostic and final-Codex lanes, measured replay, and telemetry contracts.

## Code Commentary

### Logic

Import blocks compose the owning modules; `__all__` names the supported public exports. The accumulated facade includes both final-Codex and replay surfaces, which were previously documented on separate sibling memory branches. Replay exports include frozen population/comparability, scenario evaluation, measured spans and comparison reports. Final-Codex exports retain the two-repetition certifying lane and its certificate compiler.

The facade exposes R05 admission/finalization and R16 telemetry builders, but importing those APIs does not connect them to a production closeout. The R11/R22 bridge is imported from `certification.certification_lane` by its consumers and is not re-exported here.

### Conventions

Keep algorithms, models and storage behavior in their owning modules. The facade selects public names; it does not become a second rail catalog or execution owner.

### Invariants And Boundaries

- Diagnostic output is structurally non-certifying and cannot satisfy a certification gate.
- Final-Codex and replay contracts keep their own identities and acceptance semantics.
- Public availability of lifecycle, telemetry and final-memory libraries is not evidence of production invocation.
- No rail execution, profile selection, memory scan or finalization starts when importing this facade.

### Todos

Production integration of typed lifecycle admission/finalization, closeout telemetry and final-memory executors remains incomplete in the inspected cumulative source. Those missing callers require implementation, not an onboarding stamp.

## Docs References

No external Domain Documentation source is configured for this repository. This card records repository-owned behavior from the source references below; no external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| External domain documentation is not configured. | N/A | N/A |

## Repo-Internal References

The cited source establishes the current contracts and boundaries described above. Source verification is documentation evidence, not acceptance of the implementation.

| Finding | Anchor | Source |
| --- | --- | --- |
| Core certificates and non-certifying diagnostics | `compile_certification_admission`; `ContentAddressedCertificateStore`; `DiagnosticManifestStore` | mcp/src/agents_remember/certification/__init__.py:3-37 |
| Final-Codex and typed lifecycle interfaces | `compile_final_codex_plan_record`; `compile_gate_four_certificate`; `compile_lifecycle_admission`; `compile_lifecycle_finalization` | mcp/src/agents_remember/certification/__init__.py:38-77 |
| Accumulated measured-replay surface | `compile_replay_freeze`; `measure_replay_run`; `require_comparable_replay_pair` | mcp/src/agents_remember/certification/__init__.py:104-144 |
| Telemetry imports and explicit public exports | `DurableTelemetryStore`; `compile_gate_started`; `compile_operation_terminal`; `__all__` | mcp/src/agents_remember/certification/__init__.py:155-341 |

## Cross-Repo References

No separate cross-repository protocol is established by this file. The configured cross-repository allowance is empty; no external source is relied upon here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence is required for these file-local claims. | N/A | N/A |

## Update History

- 2026-09-05T06:14:14+00:00 — Combined the final-Codex and replay facade account and made the difference between exported APIs and production wiring explicit.

- 2026-09-04T22:45+02:00 - 260831-CCR-L14 Gate-5 memory pass: re-anchored the facade rows to the verified current source (imports at lines 3-151 with the CCR-R14 final-codex block at 38-67 and `__all__` at 154-277) and recorded the CCR-R14 two-fresh final-codex facade exports (closed models, plan record, lane projection, CAS store, and bound Gate-4 certificate compiler). Verification stamp is the full leaf code commit `54ff803a05209e06f732f2de1f90e2a71a069e08` (tree `aff2e268968397ab8db042a782652957a3600dda`).

- 2026-09-04T22:23+02:00 - 260831-CCR-L17 Gate-5 memory pass: re-anchored the facade rows to the verified current source (imports at lines 3-154 with the R17 replay block at 72-104 and `__all__` at 157-283) and recorded the CCR-R17 measured-replay facade exports (freeze/population identity, comparability, span analysis, measured-run reduction, seventeen scenarios, and the pair comparison report). Verification stamp is the full leaf code commit `e84c004c37a4bad082e1a7f1bdc4bd062282a185` (tree `f97c4969d7ddb93eed75c80a4936fc05fab8e2eb`).

- 2026-09-04T17:50+02:00 - 260831-CCR-L13 Gate-5 memory pass: re-anchored the import/facade rows to the current source (imports at lines 18-47, __all__ at 124-219) and recorded the CCR-R13@v2 diagnostics facade exports (records, plan/lane projection, and store helpers). Verification stamp is the full leaf code commit 4ba18bb23ba90e201bb37341d61c0efc64161fcf (tree 631145bf3e0d5899b1dcbccf8c0d4a8257821f0d).

- 2026-09-04T12:30+02:00 - 260831-CCR-L16 Gate-5: facade widened to export the CCR-R16@v3
  durable gate and rail telemetry surface (telemetry import block plus `__all__` entries:
  ten telemetry models, twenty compile adapters, `span`, `aggregate_span_totals`,
  `project_execution_telemetry`, `project_gate_history`, `compile_telemetry_readiness`,
  `validate_execution_telemetry`); body and reference rows updated and re-anchored to
  the widened facade (import block `__init__.py:63-101`, `__all__` extent
  `__init__.py:104-181`). Verification stamp advanced to the certified commit
  `2cd360d8f45ccdcf640dc9c5d14b941ac2f0f8eb`.

- 2026-09-03T17:35+02:00 - 260831-CCR-L27 Gate-5 memory pass (src-a): re-anchored the two lifecycle import rows to the owning-module identifiers (`lifecycle_admission`, `lifecycle_recovery`) so each anchor resolves once in the facade, and widened the `__all__` row to its current extent. Verification remains pinned to the pre-commit source history until closeout.

- 2026-09-03T13:30+02:00 - 260831-CCR-L27 Gate-5 memory pass: re-anchored the two lifecycle import rows to identifier anchors present inside their cited ranges, and rewrote the Docs References task-artifact rows as prose (absolute ar-coordination paths are not repo-relative citations and carried no range). Verification remains pinned to the pre-commit source history until closeout.

- 2026-09-03T13:30+02:00 - 260831-CCR-L27 Gate-5 memory pass: re-anchored the two lifecycle
  import rows to identifier anchors present inside their cited ranges, and rewrote the
  Docs References task-artifact rows as prose (absolute ar-coordination paths are not
  repo-relative citations and carried no range). Verification remains pinned to the pre-commit
  source history until closeout.

- 2026-09-03T12:30+02:00 - 260831-CCR memory curation pass for 4e0ea4b3c493a2c89ca18367e89e4cb42ee8c5f3 (CCR-R05@v3/L05): facade widened to export the exact-candidate lifecycle admission and recovery/finalization contracts (`compile_lifecycle_admission`, `validate_lifecycle_admission_currentness`, `authorize_finalization_leg`, `compile_certification_recovery_record`, `compile_lifecycle_finalization`, `validate_lifecycle_finalization_currentness`); body updated, verification metadata rebased from `0506b57a` to the L05 owning commit.

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for 4e0ea4b3c493a2c89ca18367e89e4cb42ee8c5f3 (CCR-R05@v3/L05): facade widened to export the exact-candidate lifecycle admission and recovery/finalization contracts (`compile_lifecycle_admission`, `validate_lifecycle_admission_currentness`, `authorize_finalization_leg`, `compile_certification_recovery_record`, `compile_lifecycle_finalization`, `validate_lifecycle_finalization_currentness`); body updated, verification metadata rebased from `0506b57a` to the L05 owning commit.

- 2026-09-01T03:11+02:00 - Created for the public certification-contract facade. Verification remains closeout-owned until the source candidate is committed.

- 2026-09-01T03:11+02:00 — Created for the public certification-contract facade. Verification remains closeout-owned until the source candidate is committed.

- 2026-09-01T03:11+02:00 - Created for the public certification-contract facade. Verification
  remains closeout-owned until the source candidate is committed.
