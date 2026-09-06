# mcp/tests/test_gate_certification_records.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_gate_certification_records.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T00:23:26+00:00 |
| lastVerifiedCommitHash | `97e8ed2e1fae21756c3ad995c30613d4fbfcc503` |
| lastVerifiedCommitDate | 2026-09-06T02:09:33+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Tests the quality-gate record seam, admission freeze, typed result/certificate publication, exact-candidate recovery and refusal behavior.

## Code Commentary

### Logic

The extracted `gate_certification_test_support.py` fixtures create a minimal Git checkout with the current profile, write actual fixture report bytes and build synthetic green catalogs containing their exact file references, digests and sizes for every planned rail. The gate runner is replaced with a fixture producer, allowing tests to observe that admission exists before execution and that the record seam can mint the chain from a complete payload.

Four real-store corruption cases independently combine admission/certificate objects with invalid semantic digests or valid objects stored at the wrong content address. The wrong-address fixture first validates the full model after recomputing its semantic digest, so the refusal specifically proves address validation. Corrupt bytes are preserved and no green certificate is reused.

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

No external Domain Documentation source is configured. These are repository-owned implementation and verification contracts; no external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external domain source. | N/A | N/A |

## Repo-Internal References

These source owners establish the current behavior and the stated fixture boundaries.

| Finding | Anchor | Source |
| --- | --- | --- |
| The extracted helper writes exact fixture evidence and artifact bindings. | `_gate_catalog` | mcp/tests/gate_certification_test_support.py:109-162 |
| The injected executor outcome uses real host publication over synthetic producer bytes. | `_green_outcome_factory` | mcp/tests/gate_certification_test_support.py:165-203 |
| Admission exists before the injected run and certificates cover the complete green prefix. | `test_gate_seam_freezes_admission_before_gate_one_and_mints_gate_one_four` | mcp/tests/test_gate_certification_records.py:102-120 |
| Unchanged reruns reuse canonical content-addressed objects. | `test_gate_seam_is_idempotent_across_an_unchanged_rerun` | mcp/tests/test_gate_certification_records.py:122-141 |
| Invalid semantic digests and wrong addresses refuse for both admissions and certificates. | `test_corrupt_exact_authority_refuses_reuse` | mcp/tests/test_gate_certification_records.py:145-181 |
| An absent catalog cannot create certificates. | `test_gate_seam_without_gate_catalog_records_admission_only` | mcp/tests/test_gate_certification_records.py:183-238 |
| Candidate mismatch refuses. | `test_records_candidate_tree_mismatch_is_refused` | mcp/tests/test_gate_certification_records.py:265-271 |
| Malformed catalog entries refuse. | `test_records_malformed_catalog_entries_are_refused` | mcp/tests/test_gate_certification_records.py:273-282 |
| Missing evidence blocks a green certificate. | `test_records_green_gate_without_run_evidence_is_refused` | mcp/tests/test_gate_certification_records.py:322-342 |
| Undeclared artifacts are not accepted. | `test_records_undeclared_artifact_bindings_are_refused` | mcp/tests/test_gate_certification_records.py:344-395 |
| A contradictory observed rail yields a terminal red manifest without a green certificate. | `test_records_contradictory_red_catalog_publishes_terminal_manifest` | mcp/tests/test_gate_certification_records.py:397-418 |
| Missing memory execution ports refuse. | `test_records_bound_memory_rails_port_missing_is_refused` | mcp/tests/test_gate_certification_records.py:432-450 |
| Unknown rail terminal status refuses. | `test_records_unknown_terminal_status_is_refused` | mcp/tests/test_gate_certification_records.py:452-472 |
| Unrelated store errors propagate. | `test_records_persist_raises_on_non_collision_store_error` | mcp/tests/test_gate_certification_records.py:555-588 |
| Recovery consumes an exact published green generation. | `test_gate_recover_path_records_green_generation` | mcp/tests/test_gate_certification_records.py:655-723 |

## Cross-Repo References

No separate cross-repository protocol is established by this file. In-tree fixture languages and Dagger SDK doubles remain same-repository evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence is required. | N/A | N/A |


## Update History

- 2026-09-06T00:23:26+00:00 — L30 recovery: Reverified retained source or route ownership against actual candidate commit 97e8ed2e1fae21756c3ad995c30613d4fbfcc503; replaced the superseded private-candidate stamp.

- 2026-09-06T00:17+02:00 — Moved fixture ownership references to the extracted helper, documented real retained fixture bytes and the four semantic-digest/address corruption refusals, and refreshed all shifted record-seam anchors.

- 2026-09-05T06:14:14+00:00 — Created the record-seam test account and documented the synthetic payload boundary that previously obscured missing producers.
