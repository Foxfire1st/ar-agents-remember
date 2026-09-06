# mcp/tests/test_rail_evidence_publication.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_rail_evidence_publication.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T00:23:26+00:00 |
| lastVerifiedCommitHash | `97e8ed2e1fae21756c3ad995c30613d4fbfcc503` |
| lastVerifiedCommitDate | 2026-09-06T02:09:33+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Exercises actual producer reporting owners and exact capture bytes across rail binding, export, host publication and retained certificate consumption.

## Code Commentary

### Logic

An immutable SDK-contract double keeps command stdout/stderr separate from file bytes and executes only bounded hash/base64 utility operations. Tests prove that truncated UTF-8 tails remain exact binary bytes, observed empty output remains a real file, and unavailable streams retain partial diagnostics without certifying evidence. Terminal binding distinguishes failed, skipped and not-executed rails; a purported pass with missing required proof becomes a failure rather than fabricated evidence.

`_teardown_inputs` loads the actual clean-room runner with `runpy` in an isolated subprocess and uses its `RUN_COUNT`, `C10` checkpoint definition, `CheckpointRecorder`, `write_json` and summary writer. It serializes explicitly labeled checkpoint fixtures without invoking the scenario. The positive case executes the real teardown verifier and carries its exact proof bytes through emission, export, host generation publication and certificate evidence verification. Missing/failed checkpoints and the obsolete `C10` identity refuse without writing a proof; the actual checkpoint is `L5-C10`.

Provider tests execute the actual phase-reporting hooks over explicit terminal node observations and run the profile-declared pytest command/plugin against one temporary test. This verifies option ownership and persisted output, not the real provider workflow. Profile checks separately require JSON Playwright output, the provider phase-report path and the teardown `--proof` destination to be admitted finite Gate-4 publications.

### Conventions

Fixture fidelity is explicit: actual report serialization and publication owners run, while SDK transport and the clean-room scenario remain controlled fixtures. The live acceptance run is a separate obligation.

### Invariants And Boundaries

- Evidence binds retained bytes, including empty and non-UTF-8 tails.
- Hashing and export never mutate the shared next-rail container handle.
- Partial diagnostics do not become complete certifying evidence.
- The positive teardown fixture derives checkpoint identity from its producer; it does not copy the consumer spelling.
- Passing output requires actual proof bytes; missing, failed, skipped and unexecuted states stay distinct.

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
| Immutable transport doubles keep files and command streams distinct. | `_Container` | mcp/tests/test_rail_evidence_publication.py:59-112 |
| Binary truncation and subsequent container identity are preserved. | `test_capture_export_preserves_unicode_tail_and_the_next_rail_container` | mcp/tests/test_rail_evidence_publication.py:150-168 |
| Observed output streams produce actual retained files. | `test_observed_empty_and_both_output_streams_have_actual_retained_files` | mcp/tests/test_rail_evidence_publication.py:172-184 |
| Unavailable streams retain diagnostics without certification. | `test_unavailable_stream_is_partial_diagnostic_capture_without_certifying_evidence` | mcp/tests/test_rail_evidence_publication.py:187-201 |
| Terminal state and missing-proof semantics remain exact. | `test_terminal_binding_preserves_actual_failure_and_refuses_missing_proof` | mcp/tests/test_rail_evidence_publication.py:207-235 |
| The fixture invokes actual runner reporting owners without scenario execution. | `_teardown_inputs` | mcp/tests/test_rail_evidence_publication.py:238-285 |
| Real verifier bytes survive every export and host-consumption boundary. | `test_real_teardown_producer_bytes_reach_the_emitted_binding_and_export` | mcp/tests/test_rail_evidence_publication.py:288-353 |
| Missing input and failed checkpoints do not produce proof. | `test_teardown_refusal_never_writes_a_passing_proof` | mcp/tests/test_rail_evidence_publication.py:357-368 |
| The obsolete short checkpoint identity refuses. | `test_teardown_refuses_obsolete_checkpoint_identity` | mcp/tests/test_rail_evidence_publication.py:371-381 |
| The real reporter preserves failure observations. | `test_provider_reporter_persists_actual_terminal_node_facts` | mcp/tests/test_rail_evidence_publication.py:391-409 |
| The declared plugin owns its CLI option and writes actual pytest output. | `test_provider_command_loads_its_option_owner_and_writes_a_real_pytest_report` | mcp/tests/test_rail_evidence_publication.py:412-448 |
| Every repaired Gate-4 producer has a declared bounded publication. | `test_gate_four_profile_commands_admit_each_real_producer_publication` | mcp/tests/test_rail_evidence_publication.py:451-470 |

## Cross-Repo References

No separate cross-repository protocol is established by this file. In-tree fixture languages and Dagger SDK doubles remain same-repository evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence is required. | N/A | N/A |


## Update History

- 2026-09-06T00:23:26+00:00 — L30 recovery: Reverified retained source or route ownership against actual candidate commit 97e8ed2e1fae21756c3ad995c30613d4fbfcc503; replaced the superseded private-candidate stamp.

- 2026-09-06T00:17+02:00 — Created the producer-to-retention sidecar, documenting real reporting owners, exact binary capture and proof binding, and the limits of SDK/scenario fixtures.
