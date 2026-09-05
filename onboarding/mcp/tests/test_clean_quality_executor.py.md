# mcp/tests/test_clean_quality_executor.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_clean_quality_executor.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-05T06:14:14+00:00 |
| lastVerifiedCommitHash | `8f670ceecd75323600c873d40c47c4a1cc946ab3` |
| lastVerifiedCommitDate | 2026-09-05T06:48:24+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Tests the profile-declared clean executor boundary: exact staged candidate export, pinned Dagger invocation, shared runtime authority, typed failures, and atomic publication/recovery of complete report generations.

## Code Commentary

### Logic

Tests build small Git repositories and synthetic exported artifacts, inject a command runner and connection-only authority probe, then inspect the clean executor's returned result and durable publication state. The staged-candidate test binds the exact source export and separate ancestry input to one pipeline. Subsequent cases reject missing or contradictory profile/runtime/candidate authority and prevent invalid exports from replacing prior evidence.

Publication cases cover nested artifact directories, stale managed projections for non-applicable gates, incomplete-copy visibility, competing publishers, manifest/pruning failures and Git publication guards. Stream tests constrain chunk reads and progress windows. The fixtures track the current profile artifact inventory, including the additional suite result, so a changed profile affects these tests through real literal profile reads.

### Conventions

These are injected-runner boundary tests. They verify command and publication contracts without starting a real Docker engine or proving every in-container rail producer.

### Invariants And Boundaries

- No partial or invalid generation becomes the public current pointer.
- Exported failure remains authoritative; malformed exit status is not guessed.
- Candidate and runtime-authority identities remain exact.
- Fixture completeness must follow the declared artifact inventory without fabricating production evidence.

### Todos

Actual Gate-4 producer coverage belongs to real producer/consumer verification; these mocked exports do not discharge the missing producer obligation.

## Docs References

No external Domain Documentation source is configured for this repository. This card records repository-owned behavior from the source references below; no external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| External domain documentation is not configured. | N/A | N/A |

## Repo-Internal References

The cited source establishes the current contracts and boundaries described above. Source verification is documentation evidence, not acceptance of the implementation.

| Finding | Anchor | Source |
| --- | --- | --- |
| Exact staged source and one pinned pipeline | `test_exact_staged_candidate_is_passed_to_one_pinned_dagger_pipeline` | mcp/tests/test_clean_quality_executor.py:176-249 |
| Authority ownership and typed executor failures | `test_declared_host_authority_is_admitted_registered_and_released_without_docker`; `test_unavailable_admitted_executor_is_a_typed_gate_owned_failure`; `test_admitted_executor_start_failure_is_typed_and_gate_owned` | mcp/tests/test_clean_quality_executor.py:288-426 |
| Invalid exports and profile artifact publication | `test_exported_result_validation_rejects_missing_and_contradictory_authority`; `test_invalid_or_unowned_exports_never_replace_durable_evidence`; `test_not_applicable_gate_cleans_stale_managed_projection_without_requiring_it` | mcp/tests/test_clean_quality_executor.py:486-619 |
| Atomic publication and fail-closed generation checks | `test_report_generation_pointer_never_exposes_a_partial_copy`; `test_competing_report_publisher_reuses_the_complete_generation`; `test_report_manifest_verification_and_generation_pruning_fail_closed` | mcp/tests/test_clean_quality_executor.py:621-816 |
| Git guards, bounded stream behavior and native executor resolution | `test_report_publish_git_guard_and_streaming_progress_are_fail_closed`; `test_stream_reads_fixed_chunks_and_writes_at_most_two_progress_windows`; `test_profile_executor_resolution_uses_the_native_command_boundary` | mcp/tests/test_clean_quality_executor.py:818-1026 |

## Cross-Repo References

No separate cross-repository protocol is established by this file. The configured cross-repository allowance is empty; no external source is relied upon here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence is required for these file-local claims. | N/A | N/A |

## Update History

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
