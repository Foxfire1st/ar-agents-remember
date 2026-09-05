# mcp/tests/test_gate_certification_records.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_gate_certification_records.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-05T06:14:14+00:00 |
| lastVerifiedCommitHash | `668d710bf2a9898fb706614163462ff346d986b7` |
| lastVerifiedCommitDate | 2026-09-05T02:45:47+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Tests the quality-gate record seam, admission freeze, typed result/certificate publication, exact-candidate recovery and refusal behavior.

## Code Commentary

### Logic

The fixtures create a minimal Git checkout with the current profile and build synthetic green catalogs containing evidence and required artifacts for every planned rail. The gate runner is replaced with a fixture producer, allowing tests to observe that admission exists before execution and that the record seam can mint the chain from a complete payload.

Further cases cover unchanged reruns, absent catalogs, unsupported repositories, wrong candidate trees, malformed entries, non-green dispositions, unplanned gates, missing evidence, undeclared artifacts, contradictory rail statuses and absent memory service ports. Tests also inspect journal loading and decoder-artifact read errors. Recovery cases bind a published generation to exact gate identity.

### Conventions

The synthetic catalog deliberately supplies the data shape required by the consumer. Its existence cannot prove the real executor emits the same shape or that every artifact has a production writer.

### Invariants And Boundaries

- Freeze must precede Gate 1.
- Missing observations or artifact bindings must refuse certification rather than generate placeholder digests.
- Non-green outcomes have no green certificate.
- Recovery binds the current exact candidate and published manifest.
- A green fixture covering Gates 1–4 is consumer contract evidence, not terminal master certification.

### Todos

Retain producer-backed integration coverage for all required Gate-4 artifacts; these fixtures cover the consumer side of that obligation.

## Docs References

No external Domain Documentation source is configured for this repository. This card records repository-owned behavior from the source references below; no external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| External domain documentation is not configured. | N/A | N/A |

## Repo-Internal References

The cited source establishes the current contracts and boundaries described above. Source verification is documentation evidence, not acceptance of the implementation.

| Finding | Anchor | Source |
| --- | --- | --- |
| Synthetic complete catalogs and injected run outcome | `_gate_catalog`; `_green_outcome_factory` | mcp/tests/test_gate_certification_records.py:117-222 |
| Freeze-before-run, idempotence and admission-only behavior | `test_gate_seam_freezes_admission_before_gate_one_and_mints_gate_one_four`; `test_gate_seam_is_idempotent_across_an_unchanged_rerun`; `test_gate_seam_without_gate_catalog_records_admission_only` | mcp/tests/test_gate_certification_records.py:250-346 |
| Candidate, payload and artifact refusal cases | `test_records_candidate_tree_mismatch_is_refused`; `test_records_malformed_catalog_entries_are_refused`; `test_records_green_gate_without_run_evidence_is_refused`; `test_records_undeclared_artifact_bindings_are_refused`; `test_records_contradictory_red_catalog_publishes_terminal_manifest` | mcp/tests/test_gate_certification_records.py:373-552 |
| Port/status/currentness and store-error handling | `test_records_bound_memory_rails_port_missing_is_refused`; `test_records_unknown_terminal_status_is_refused`; `test_records_persist_raises_on_non_collision_store_error` | mcp/tests/test_gate_certification_records.py:566-722 |
| Recovered generation recording | `test_gate_recover_path_records_green_generation` | mcp/tests/test_gate_certification_records.py:789-857 |

## Cross-Repo References

No separate cross-repository protocol is established by this file. The configured cross-repository allowance is empty; no external source is relied upon here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence is required for these file-local claims. | N/A | N/A |

## Update History

- 2026-09-05T06:14:14+00:00 — Created the record-seam test account and documented the synthetic payload boundary that previously obscured missing producers.
