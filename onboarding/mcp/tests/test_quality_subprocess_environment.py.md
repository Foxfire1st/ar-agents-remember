# mcp/tests/test_quality_subprocess_environment.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_quality_subprocess_environment.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T07:20+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Pure regression proof that nested candidate tests cannot inherit and overwrite an outer
quality-wrapper invocation's retry cache or progress evidence.

## Code Commentary

### Logic

The test constructs one representative environment containing every outer-only retry/report
control plus the Dagger admission, CI invocation, attempt nonce, memory cap, and ordinary `PATH`.
It asserts the closed outer-only set is absent from the child and every semantic/process value is
preserved exactly.

### Invariants And Boundaries

- The assertion compares the complete child mapping, so silently stripping an additional semantic
  value fails.
- The proof is pure and isolated from the admission-bound wrapper suite.
- Environment isolation prevents evidence-location collision; it does not change retry identity or
  candidate semantics.

### Todos

None.

## Docs References

No external domain documentation governs this repository-owned process boundary.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Only outer retry/report controls are removed while admission and semantic values survive. | `test_outer_retry_controls_do_not_leak_into_candidate_tests` | mcp/tests/test_quality_subprocess_environment.py:6-29 |
| The production owner defines the exact closed set. | `OUTER_INVOCATION_ONLY`; `child_environment` | mcp/test_support/agents_remember_test_support/code_quality/quality_subprocess_environment.py:9-25 |

## Cross-Repo References

None.

## Update History

- 2026-08-27T18:33+02:00 — Created with the nested quality-environment isolation repair.
  Verification metadata remains empty until governed closeout.
