# mcp/tests/test_code_quality_environment_guard.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_code_quality_environment_guard.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-14T11:48:55+02:00 |
| lastVerifiedCommitHash | `aeca9a2839c965218a61a3040e15cb84367ebeca` |
| lastVerifiedCommitDate | 2026-08-14T13:35:55+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Prove that every direct Python quality-wrapper entry refuses before parsing or planning unless the
live process carries the matching Dagger nonce/file attestation, and that accepted entry selects
the wrapper's fixed native scratch root independently of durable report placement.

## Code Commentary

### Logic

`CodeQualityEnvironmentGuardTests` calls the production `check.main` boundary. Missing and
mismatched attestations must return failure before `build_parser` is called and must explain the
host-execution refusal. The accepted-path cases isolate environment sanitization and require
`native_subprocess_environment` to receive `QUALITY_TEMP_ROOT`, whether or not the caller supplies
an enclosure-owned progress-report path.

### Conventions

The refusal cases use the production guard with temporary on-disk evidence. Accepted-path cases
patch only the guard and downstream quality runner so the test remains about entry authorization
and native scratch-root selection, not the quality suite itself.

### Invariants And Boundaries

- Parser, targeted-scope, and retry-proof planning are unreachable before Dagger attestation.
- An environment nonce without the matching file is not acceptance authority.
- Durable report placement does not become the subprocess temporary directory.
- The suite itself runs only inside the repository's Dagger-attested Python acceptance graph.

### Todos

None recorded.

## Docs References

The resolved Dagger-only execution contract is recorded in `system/tools.md` and
`system/git-workflow.md`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Missing or mismatched attestation refuses before parser construction. | `test_direct_wrapper_refuses_before_targeted_or_retry_planning_without_attestation`; `test_direct_wrapper_refuses_a_mismatched_dagger_attestation_before_planning` | mcp/tests/test_code_quality_environment_guard.py:16-51 |
| Accepted entry always supplies the fixed native scratch root, with or without a durable report path. | `test_main_uses_the_report_environment_to_select_its_native_temp_root`; `test_main_without_a_report_uses_the_native_default_temp_root` | mcp/tests/test_code_quality_environment_guard.py:53-86 |
| Production authorization is shared by the wrapper and pytest collection. | `require_dagger_test_environment` | mcp/src/agents_remember/code_quality/dagger_environment.py:36-48 |

## Cross-Repo References

No external repository supplies or overrides this acceptance guard.

## Update History

- 2026-08-14T11:48:55+02:00 — Created for the R42 file-size extraction. Preserved the direct
  refusal and native-temp regressions formerly housed in `test_code_quality_check.py`; final source
  verification remains closeout-owned.
