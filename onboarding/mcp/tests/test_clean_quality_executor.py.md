# mcp/tests/test_clean_quality_executor.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_clean_quality_executor.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T15:11:59+00:00 |
| lastVerifiedCommitHash | `c69d5171187fa1957025e393270db9f5a864ab14` |
| lastVerifiedCommitDate | 2026-09-06T16:32:29+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Tests the profile-declared clean executor boundary: exact staged candidate export, pinned Dagger invocation, shared runtime authority, typed failures, and atomic publication/recovery of complete report generations.

## Code Commentary

### Logic

Tests build small Git repositories and synthetic exported artifacts, inject a command runner and connection-only authority probe, then inspect the clean executor's returned result and durable publication state. The staged-candidate test binds the exact source export and separate ancestry input to one pipeline. Subsequent cases reject missing or contradictory profile/runtime/candidate authority and prevent invalid exports from replacing prior evidence.

Publication cases cover nested artifact directories, stale managed projections for non-applicable gates, incomplete-copy visibility, competing publishers, manifest/pruning failures and Git publication guards. Stream tests constrain chunk reads and progress windows. The pipeline assertion independently admits the actual profile against the exported Git tree and base, then compares the entire profile plan, profile source hash, profile digest and ordered compiled `publishedArtifacts`. The admitted plan is the oracle for selected sizes, required flags and ordering.

The staged source changes only `created.txt` and `tracked.txt`. The test reads the actual published source-selection artifact, requires its exact changed-path census to match the manifest and its ambient rail to be non-applicable, and asserts that no ambient export directory exists. Fake exports supply the frozen plan's canonical applicability bytes; comparison bases in real Git fixtures must resolve.

### Conventions

These are injected-runner boundary tests. They verify command and publication contracts without starting a real Docker engine or proving every in-container rail producer.

### Invariants And Boundaries

- No partial or invalid generation becomes the public current pointer.
- Exported failure remains authoritative; malformed exit status is not guessed.
- Candidate and runtime-authority identities remain exact.
- Fixture completeness must follow the declared artifact inventory without fabricating production evidence.

### Todos

Keep this injected-runner suite distinct from producer-backed publication tests and the separate live Dagger gate run. No unresolved producer absence is asserted here.

## Docs References

No external Domain Documentation source is configured. These are repository-owned implementation and verification contracts; no external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external domain source. | N/A | N/A |

## Repo-Internal References

These source owners establish the current behavior and the stated fixture boundaries.

| Finding | Anchor | Source |
| --- | --- | --- |
| The pipeline compares the actual admitted plan, compiled artifact inventory and source-selection evidence. | `_assert_exact_pipeline_publication` | mcp/tests/test_clean_quality_executor.py:133-207 |
| One pinned invocation receives exact staged source and ancestry. | `test_exact_staged_candidate_is_passed_to_one_pinned_dagger_pipeline` | mcp/tests/test_clean_quality_executor.py:209-303 |
| Injected authority admission, registration and release preserve owner identity. | `test_declared_host_authority_is_admitted_registered_and_released_without_docker` | mcp/tests/test_clean_quality_executor.py:342-423 |
| Missing executor resolution is a typed gate failure. | `test_unavailable_admitted_executor_is_a_typed_gate_owned_failure` | mcp/tests/test_clean_quality_executor.py:425-451 |
| Executor launch failure retains gate ownership. | `test_admitted_executor_start_failure_is_typed_and_gate_owned` | mcp/tests/test_clean_quality_executor.py:453-480 |
| Exported authority must agree with the candidate and profile. | `test_exported_result_validation_rejects_missing_and_contradictory_authority` | mcp/tests/test_clean_quality_executor.py:540-577 |
| Invalid exports preserve prior evidence. | `test_invalid_or_unowned_exports_never_replace_durable_evidence` | mcp/tests/test_clean_quality_executor.py:579-636 |
| Non-applicable gates remove only stale managed projections. | `test_not_applicable_gate_cleans_stale_managed_projection_without_requiring_it` | mcp/tests/test_clean_quality_executor.py:644-673 |
| The public pointer never exposes a partial generation. | `test_report_generation_pointer_never_exposes_a_partial_copy` | mcp/tests/test_clean_quality_executor.py:675-746 |
| Competing publication converges on complete bytes. | `test_competing_report_publisher_reuses_the_complete_generation` | mcp/tests/test_clean_quality_executor.py:748-768 |
| Manifest and pruning failures refuse publication. | `test_report_manifest_verification_and_generation_pruning_fail_closed` | mcp/tests/test_clean_quality_executor.py:770-870 |
| Git publication guards and stream refusals stay intact. | `test_report_publish_git_guard_and_streaming_progress_are_fail_closed` | mcp/tests/test_clean_quality_executor.py:872-975 |
| Stream reading remains bounded. | `test_stream_reads_fixed_chunks_and_writes_at_most_two_progress_windows` | mcp/tests/test_clean_quality_executor.py:977-1035 |
| Executor resolution uses the native command boundary. | `test_profile_executor_resolution_uses_the_native_command_boundary` | mcp/tests/test_clean_quality_executor.py:1072-1080 |

## Cross-Repo References

No separate cross-repository protocol is established by this file. In-tree fixture languages and Dagger SDK doubles remain same-repository evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence is required. | N/A | N/A |

## Update History

- 2026-09-06T15:11:59+00:00 — L33 pending candidate curation: Re-read the prepared source, corrected the artifact oracle to the actual admitted plan, documented exact non-applicable source-selection publication, and refreshed shifted anchors. Verification names the real prepared source commit c69d5171187fa1957025e393270db9f5a864ab14; this entry does not claim CCR acceptance.

- 2026-09-06T00:23:26+00:00 — L30 recovery: Reverified retained source or route ownership against actual candidate commit 97e8ed2e1fae21756c3ad995c30613d4fbfcc503; replaced the superseded private-candidate stamp.

- 2026-09-06T00:17+02:00 — Documented complete profile-owned publication equality instead of a stale artifact count and refreshed shifted assertions without implying live producer proof.

- 2026-09-05T06:14:14+00:00 — Refreshed the accumulated profile/export test contract and distinguished injected publication fixtures from proof of real artifact producers.

- 2026-09-04T10:05+02:00 - 260831-CCR-L12 Gate-5 memory pass for cfd09381 (CCR-R12@v4): recorded the host-authority admission/registration/release forcing case and probe doubles added to the clean-executor suite.

- 2026-09-03T12:30+02:00 -- 260831-CCR memory curation pass for 685f83c44055 (CCR-R22@v1/L22): recorded the profile-admission rewiring of the clean quality executor tests.

- 2026-08-31T04:50+02:00 — 260821-ARSPAWN-L5 independent-review repair: added the recursive
  nested-report publication, path-safety, digest verification, and lookup regression contract.
  Verification remains closeout-owned.

- 2026-08-29T16:27+02:00 — Added immutable publication and lookup proof for both canonical Python
  runtime artifacts.

- 2026-08-26T10:44:52+02:00 — Reconciled atomic causal-failure report publication and lookup with the candidate-bound quality generation.

- 2026-08-24T21:23+02:00 — Added candidate-bound schema-2 publication and evidence assertions.

- 2026-08-24T14:19+02:00 — 260821-DAGQC-L2: added strict manifest schema/error and parsed-snapshot artifact lookup coverage. Verification metadata remains pinned until architect-owned closeout.

- 2026-08-14T06:38+02:00 — L23 final candidate review: executor forcing cases cover fresh attempts,
  shared authoritative projections, fail-closed status, bounded live output, stale-report pruning,
  exact candidate bundles, and no direct-Docker/local fallback.

- 2026-08-12T15:19+02:00 — Created with L23 clean quality executor tests; verification provenance remains closeout-owned.
