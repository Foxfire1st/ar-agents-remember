# mcp/src/agents_remember/worktrees/modules/quality/certification_records.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/modules/quality/certification_records.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-05T06:14:14+00:00 |
| lastVerifiedCommitHash | `668d710bf2a9898fb706614163462ff346d986b7` |
| lastVerifiedCommitDate | 2026-09-05T02:45:47+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[Governing route overview](../overview.md)

## Purpose

Connects the profile-backed quality gate to R21 admission, terminal result manifests and certificates. It consumes verified published generation data and records refusals when the supplied rail evidence cannot support certification.

## Code Commentary

### Logic

prepare_certification_records currently supports only repository id agents-remember. It loads the exact profile, compiles the repository plan against the supplied candidate tree, obtains memory rails through the bound service port, and persists admission under the enclosure's certification-records directory before execution.

record_published_generation checks candidate-tree equality, reads the payload's gate catalog and processes entries in catalog order while accumulating predecessor certificates. Missing gate catalogs produce admission-only/empty gate records. Non-green dispositions remain terminal records. A green entry must contain every planned rail with recognized status and actual evidence/artifact bindings; missing evidence, unplanned gates and invalid manifests are journaled as typed refusals.

Valid result manifests are stored content-addressably. Only green manifests produce certificates bound to the admission and predecessor chain. The current journal is atomically replaced; load_execution_records returns None for absent, malformed or wrong-schema admission data. Admission publication has explicit content-address-collision handling; this should not be confused with independent proof of an unchanged whole run.

### Conventions

Keep memory-domain imports behind CertificationMemoryRailsPort. Executor data is the observation source; never fabricate bindings to satisfy a declared artifact.

### Invariants And Boundaries

- Candidate tree must match the published generation.
- Green pipeline disposition does not excuse missing rail artifacts or evidence.
- Non-green/invalid gates publish no reusable certificate.
- The gate.py caller currently discards the returned refused list; outer quality success can coexist with missing certificates.
- This module does not call typed lifecycle admission/finalization, durable telemetry or the final Gate-5 executor.
- Ordinary failed runs do not reach this helper through the current gate.py success path.

### Todos

Three Gate-4 required artifacts lack production bindings in the inspected source. Complete refusal propagation and all-terminal-outcome production integration remain unresolved.

## Docs References

No external Domain Documentation source is configured for this repository. This card records repository-owned behavior from the source references below; no external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| External domain documentation is not configured. | N/A | N/A |

## Repo-Internal References

The cited source establishes the current contracts and boundaries described above. Source verification is documentation evidence, not acceptance of the implementation.

| Finding | Anchor | Source |
| --- | --- | --- |
| Repository guard, admission freeze and catalog recording | `prepare_certification_records`; `record_published_generation` | mcp/src/agents_remember/worktrees/modules/quality/certification_records.py:156-242 |
| Atomic journals and green-only manifest/certificate publication | `load_execution_records`; `journal_gate_records`; `_record_gate` | mcp/src/agents_remember/worktrees/modules/quality/certification_records.py:245-338 |
| Payload-bound rail observations and required service port | `_terminal_results`; `_bound_memory_rails` | mcp/src/agents_remember/worktrees/modules/quality/certification_records.py:357-451 |
| Admission persistence and collision handling | `_persist_admission`; `_is_content_address_collision` | mcp/src/agents_remember/worktrees/modules/quality/certification_records.py:474-496 |

## Cross-Repo References

No separate cross-repository protocol is established by this file. The configured cross-repository allowance is empty; no external source is relied upon here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence is required for these file-local claims. | N/A | N/A |

## Update History

- 2026-09-05T06:14:14+00:00 — Created the exact production record-consumer account, including refusal journaling and unresolved composition/propagation boundaries.
