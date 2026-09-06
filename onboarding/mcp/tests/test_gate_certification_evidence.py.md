# mcp/tests/test_gate_certification_evidence.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_gate_certification_evidence.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T00:23:26+00:00 |
| lastVerifiedCommitHash | `97e8ed2e1fae21756c3ad995c30613d4fbfcc503` |
| lastVerifiedCommitDate | 2026-09-06T02:09:33+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Forces exact retained publication consumption and live certificate-generation retention through real host publication, certificate-store and pruning owners.

## Code Commentary

### Logic

The suite builds a real temporary Git candidate with the shared gate helper, writes fixture rail bytes, publishes report generations and records certificates through production owners. An unchanged rerun must preserve original certificate bytes, creation provenance and the selected publication snapshot, even when a later storage generation exists. Selected generations survive pruning until the validated journal releases them.

Fault matrices remove, corrupt, enlarge or symlink report files and parent directories; alter payload SHA-256, sizes or references; and substitute valid foreign authority snapshots with identical artifact bytes. Recomputed foreign generations prove that matching bytes alone cannot rebind candidate, profile, plan, selection, executor, decoder or runtime authority. Invalid selected journals, capacity overruns, row identities, duplicate gates, malformed digests, cross-gate certificates and alternate existing result manifests must refuse without replacing the selected journal or releasing protected generations.

The host gate test deletes a required evidence file after a synthetic zero-return-code run and requires a refusal. Gate-4 missing-artifact cases preserve only the already-green Gates 1–3 prefix. Manifest roundtrips retain attestation and runtime inputs, while unsafe relative names and generation locators refuse before any filesystem open.

### Conventions

The 54 parameterized cases use actual host filesystem and certificate owners over synthetic producer bytes. They prove consumer and retention contracts; they do not substitute for a live Dagger producer run.

### Invariants And Boundaries

- Reuse reopens the original generation; current evidence is never silently substituted.
- Valid foreign semantic authority refuses even if every artifact byte matches.
- Malformed or unreadable selected state does not become an empty selection.
- Refusal preserves journal, pointer and protected generations as asserted by the owning case.
- Missing Gate-4 proof cannot mint a Gate-4 certificate or erase a valid earlier prefix.

### Todos

None recorded.

## Docs References

No external Domain Documentation source is configured. These are repository-owned implementation and verification contracts; no external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external domain source. | N/A | N/A |

## Repo-Internal References

These source owners establish the current behavior and the stated fixture boundaries.

| Finding | Anchor | Source |
| --- | --- | --- |
| Real candidate and production lane authority establish the fixture world. | `_arrange` | mcp/tests/test_gate_certification_evidence.py:59-75 |
| Unchanged semantic authority retains original certificate bytes, generation and provenance. | `test_unchanged_certificate_reuses_original_generation_and_provenance` | mcp/tests/test_gate_certification_evidence.py:104-133 |
| Generation retention follows validated selected certificates. | `test_selected_certificate_generation_survives_pruning_until_selection_releases_it` | mcp/tests/test_gate_certification_evidence.py:136-150 |
| Missing, corrupt, oversized and symlinked evidence refuses issuance. | `test_actual_evidence_fault_refuses_certificate_issuance` | mcp/tests/test_gate_certification_evidence.py:154-179 |
| Independently valid foreign authority cannot borrow identical artifact bytes. | `test_reuse_refuses_valid_foreign_authority_with_identical_artifact_bytes` | mcp/tests/test_gate_certification_evidence.py:295-308 |
| Unreadable and oversized journals preserve all live state. | `test_unavailable_selected_journal_refuses_publication_without_releasing_generations` | mcp/tests/test_gate_certification_evidence.py:380-414 |
| Invalid row identity and digest cases preserve the selected journal. | `test_invalid_selected_records_cannot_replace_a_live_journal` | mcp/tests/test_gate_certification_evidence.py:430-457 |
| A selected gate must match its actual certificate gate. | `test_selected_gate_cannot_claim_another_gates_certificate` | mcp/tests/test_gate_certification_evidence.py:460-471 |
| Existing result identity cannot be rebound to another certificate. | `test_reuse_refuses_certificate_rebound_to_another_existing_result` | mcp/tests/test_gate_certification_evidence.py:474-487 |
| The actual host gate refuses unavailable bytes despite a synthetic green process. | `test_actual_host_gate_refuses_green_process_with_unavailable_certificate_bytes` | mcp/tests/test_gate_certification_evidence.py:490-518 |
| Snapshot roundtrips retain all generation authority. | `test_exact_manifest_snapshot_roundtrips_all_generation_authority` | mcp/tests/test_gate_certification_evidence.py:536-555 |
| Unsafe report locators refuse before any file open. | `test_unsafe_retained_locator_refuses_before_opening_any_path` | mcp/tests/test_gate_certification_evidence.py:559-577 |
| Missing Gate-4 artifact retains only the valid earlier prefix. | `test_missing_required_gate_four_artifact_preserves_only_the_green_prefix` | mcp/tests/test_gate_certification_evidence.py:584-593 |

## Cross-Repo References

No separate cross-repository protocol is established by this file. In-tree fixture languages and Dagger SDK doubles remain same-repository evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence is required. | N/A | N/A |


## Update History

- 2026-09-06T00:23:26+00:00 — L30 recovery: Reverified retained source or route ownership against actual candidate commit 97e8ed2e1fae21756c3ad995c30613d4fbfcc503; replaced the superseded private-candidate stamp.

- 2026-09-06T00:17+02:00 — Created the retained-evidence regression sidecar with exact reuse, semantic binding, journal safety, locator confinement and prefix-preserving refusal boundaries.
