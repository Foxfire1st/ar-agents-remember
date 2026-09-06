# mcp/tests/test_gate_certification_records.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_gate_certification_records.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T15:11:59+00:00 |
| lastVerifiedCommitHash | `c69d5171187fa1957025e393270db9f5a864ab14` |
| lastVerifiedCommitDate | 2026-09-06T16:32:29+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Tests full-run admission freezing, typed terminal publication, selected original rendering and exact candidate/profile refusal at the quality-gate record seam.

## Code Commentary

### Logic

The shared `gate_certification_test_support.py` fixtures create real temporary Git checkouts, observe the candidate tree and comparison base, and admit the configured profile. They write fixture report bytes and synthesize applicable rail outcomes; planned non-applicable rails retain exact source-selection evidence and zero starts. Environment census bytes come from the production census over temporary fixture files. The injected executor lets the suite observe admission before execution and the actual record owner issue the complete Gates 1–4 chain.

Four real-store corruption cases independently combine admission/certificate objects with invalid semantic digests or valid objects stored at the wrong content address. The wrong-address fixture first validates the full model after recomputing its semantic digest, so the refusal specifically proves address validation. Corrupt bytes are preserved and no green certificate is reused.

Unchanged fresh reruns preserve original content-addressed bytes. Preparation must retain the complete frozen profile for another registered repository; an absent profile or memory-rail port refuses for any repository. Missing Git bases and commit objects supplied as tree identities refuse before record publication. Unsupported dispositions, incomplete catalogs, unplanned gates, unknown statuses and undeclared artifacts cannot synthesize terminal observations. An absent catalog leaves the admission record but raises without writing gate records; a complete contradictory failed rail catalog retains a red terminal without a green certificate.

The decoder cases use selected fixture publications and preserve existing gate-record bytes on non-object input. Selected rendering consumes the supplied frozen run and original typed references; it does not discover recovery authority through a current report pointer. A changed index or repository identity refuses without replacing records or the pointer. The separate admission-summary loader tests only its missing/malformed presentation behavior.

### Conventions

The shared fixture performs real Git observation, filesystem publication and certificate-store operations with injected rail execution. Its environment census is real over fixture files, while its passing rail outcomes do not prove live Dagger execution or every production artifact writer.

### Invariants And Boundaries

- Freeze must precede Gate 1.
- Missing observations or artifact bindings must refuse certification rather than generate placeholder digests.
- Non-green outcomes have no green certificate.
- Selected rendering binds the current exact candidate and supplied original publications.
- A configured repository profile and actual Git source observation are required regardless of repository name.
- A green fixture covering Gates 1–4 is consumer contract evidence, not terminal master certification.

### Todos

Keep producer-backed Gate-4 coverage alongside these consumer tests; this suite alone does not prove live rail production.

## Docs References

No external Domain Documentation source is configured. These are repository-owned implementation and verification contracts; no external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external domain source. | N/A | N/A |

## Repo-Internal References

These source owners establish the current behavior and the stated fixture boundaries.

| Finding | Anchor | Source |
| --- | --- | --- |
| The extracted helper writes exact fixture evidence and artifact bindings. | `_gate_catalog` | mcp/tests/gate_certification_test_support.py:124-255 |
| The injected executor outcome uses real host publication over fixture reports. | `_green_outcome_factory` | mcp/tests/gate_certification_test_support.py:258-297 |
| Admission exists before the injected run and certificates cover the complete green prefix. | `test_gate_seam_freezes_admission_before_gate_one_and_mints_gate_one_four` | mcp/tests/test_gate_certification_records.py:108-126 |
| Unchanged reruns reuse canonical content-addressed objects. | `test_gate_seam_is_idempotent_across_an_unchanged_rerun` | mcp/tests/test_gate_certification_records.py:128-174 |
| Invalid semantic digests and wrong addresses refuse for both admissions and certificates. | `test_corrupt_exact_authority_refuses_reuse` | mcp/tests/test_gate_certification_records.py:178-209 |
| An absent catalog raises after admission and writes no gate-record journal. | `test_gate_seam_without_gate_catalog_refuses_certification` | mcp/tests/test_gate_certification_records.py:211-266 |
| Candidate mismatch refuses. | `test_records_candidate_tree_mismatch_is_refused` | mcp/tests/test_gate_certification_records.py:325-331 |
| Malformed catalog entries refuse. | `test_records_malformed_catalog_entries_are_refused` | mcp/tests/test_gate_certification_records.py:333-344 |
| Missing evidence blocks a green certificate. | `test_records_green_gate_without_run_evidence_is_refused` | mcp/tests/test_gate_certification_records.py:382-402 |
| Undeclared artifacts are not accepted. | `test_records_undeclared_artifact_bindings_are_refused` | mcp/tests/test_gate_certification_records.py:404-455 |
| A contradictory observed rail yields a terminal red manifest without a green certificate. | `test_records_contradictory_red_catalog_publishes_terminal_manifest` | mcp/tests/test_gate_certification_records.py:457-478 |
| Missing memory execution ports refuse. | `test_records_bound_memory_rails_port_missing_is_refused` | mcp/tests/test_gate_certification_records.py:492-513 |
| Unknown rail terminal status refuses. | `test_records_unknown_terminal_status_is_refused` | mcp/tests/test_gate_certification_records.py:515-535 |
| Unrelated store errors propagate. | `test_records_persist_raises_on_non_collision_store_error` | mcp/tests/test_gate_certification_records.py:618-656 |
| Selected rendering preserves the supplied original certificate objects. | `test_gate_recover_path_records_green_generation` | mcp/tests/test_gate_certification_records.py:703-716 |
| Another registered repository retains its full frozen profile and typed stored run. | `test_another_registered_repository_retains_its_complete_actual_profile` | mcp/tests/test_gate_certification_records.py:292-323 |
| Missing profile authority refuses for every repository. | `test_records_prepare_refuses_missing_profile_for_any_repository` | mcp/tests/test_gate_certification_records.py:278-290 |
| Missing bases and commit-as-tree selectors refuse before records or Git mutation. | `test_records_prepare_refuses_unobservable_git_source_authority` | mcp/tests/test_gate_certification_records.py:719-741 |
| Moved candidate or repository identity preserves selected objects and the pointer. | `test_selected_renderer_refuses_moved_target_without_replacing_originals` | mcp/tests/test_gate_certification_records.py:744-771 |
| Unreadable selected decoder artifacts refuse. | `test_gate_record_helper_refuses_unreadable_artifact` | mcp/tests/test_gate_certification_records.py:674-686 |
| Non-object decoder input preserves existing gate records. | `test_gate_record_helper_refuses_non_object_payload` | mcp/tests/test_gate_certification_records.py:688-701 |
| Unsupported dispositions and non-object rail observations remain explicit refusals. | `test_records_unsupported_dispositions_and_junk_rails_are_refused` | mcp/tests/test_gate_certification_records.py:346-370 |

## Cross-Repo References

No separate cross-repository protocol is established by this file. In-tree fixture languages and Dagger SDK doubles remain same-repository evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence is required. | N/A | N/A |

## Update History

- 2026-09-06T15:11:59+00:00 — L33 pending candidate curation: Re-read the prepared source, replaced obsolete summary/pointer recovery claims with full frozen-run and selected-original behavior, documented generic profile and Git-source refusals, and refreshed current test anchors. Verification names the real prepared source commit c69d5171187fa1957025e393270db9f5a864ab14; this entry does not claim CCR acceptance.

- 2026-09-06T00:23:26+00:00 — L30 recovery: Reverified retained source or route ownership against actual candidate commit 97e8ed2e1fae21756c3ad995c30613d4fbfcc503; replaced the superseded private-candidate stamp.

- 2026-09-06T00:17+02:00 — Moved fixture ownership references to the extracted helper, documented real retained fixture bytes and the four semantic-digest/address corruption refusals, and refreshed all shifted record-seam anchors.

- 2026-09-05T06:14:14+00:00 — Created the record-seam test account and documented the synthetic payload boundary that previously obscured missing producers.
