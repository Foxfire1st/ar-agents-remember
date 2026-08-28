# mcp/tests/test_causal_quality_preflight.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_causal_quality_preflight.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T07:20+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[MCP test overview](overview.md)

## Purpose

Forces the quality wrapper to continue with the independently runnable pytest population after a
valid causal-owner failure, while falling back to unsuppressed safe mode when the causal subprocess
or its report contract is broken.

## Code Commentary

### Logic

A synthetic runner records every quality command. One test returns a valid failed causal report and
requires pytest to receive that report for exact-node suppression. Two safe-mode tests cover a
failed preflight with no report and a nominally successful preflight with invalid JSON; both require
pytest to run without the suppression option and the overall gate to stay failed.

### Conventions

The test uses the real `CheckConfig` and Dagger admission token but replaces subprocess execution,
so it proves orchestration order and arguments without minting quality acceptance.

### Invariants And Boundaries

- A valid failed causal report permits independent continuation but never converts the gate to
  success.
- Missing, malformed, or contradictory causal evidence disables suppression; it does not disable
  pytest.
- Safe mode must be louder and broader than a valid suppression route, never silently narrower.

### Todos

None.

## Docs References

No Domain Documentation source is configured; this is an internal wrapper contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external documentation is required for this forcing test. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| A valid failed causal report reaches pytest while the overall quality result remains failed. | `test_owned_causal_failure_runs_independent_pytest_population` | mcp/tests/test_causal_quality_preflight.py:20-55 |
| Missing or invalid reports disable suppression and still run the selected pytest population. | `test_broken_preflight_disables_suppression_and_runs_selected_pytest`; `test_success_exit_without_valid_report_also_uses_safe_mode` | mcp/tests/test_causal_quality_preflight.py:57-112 |
| The fixture uses the real quality configuration and explicit failed-report vocabulary. | `_quality_config`; `_failed_causal_payload` | mcp/tests/test_causal_quality_preflight.py:115-168 |
| Continuation policy is centralized in its dedicated owner rather than duplicated in the test. | `evaluate_preflight_result` | mcp/test_support/agents_remember_test_support/code_quality/causal_continuation.py:48-73 |

## Cross-Repo References

No meaningful cross-repository boundary applies.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external process contract is asserted beyond the repository-owned wrapper. | — | — |

## Update History

- 2026-08-28T06:28+02:00 — PDLS wave 005 curator: created the missing sidecar for causal
  continuation and fail-safe unsuppressed execution.
