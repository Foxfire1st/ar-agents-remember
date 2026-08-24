# mcp/src/agents_remember/testing/direct_runner.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/testing/direct_runner.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T20:55+02:00 |
| lastVerifiedCommitHash | `77bc614506b8b50937aed6846523547d36045947` |
| lastVerifiedCommitDate | 2026-08-24T20:41:34+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Python testing boundary](overview.md)

## Purpose

Implements the only direct Python diagnostic command behind `./scripts/test-python`.

## Code Commentary

`run_direct_diagnostic` rejects flags, classifies the complete request, prepares diagnostic-only
bootstrap, scrubs the environment, forces the canonical config and `-n=0`, and invokes pytest once
with exactly the admitted nodes. It validates the child phase/node report, rechecks candidate
currency, and emits bounded stdout/stderr plus `DiagnosticTestEvidence`. CLI help and every result
state say non-certifying.

## Invariants And Boundaries

- No fallback, subset retry, alternate config, or arbitrary pytest flag exists.
- Dagger admission is removed from the child environment.
- Missing, contradictory, or stale child evidence is infrastructure failure, not a test result.
- Only node outcomes and timing are retained; accepting consumers cannot use the payload.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The route classifies before executing once. | `run_direct_diagnostic` | mcp/src/agents_remember/testing/direct_runner.py:165-228 |
| The child command is serial and canonical. | `_pytest_command` | mcp/src/agents_remember/testing/direct_runner.py:289-325 |
| The report loader checks schema, exit code, exact node order, and outcomes. | `_load_phase_report` | mcp/src/agents_remember/testing/direct_runner.py:328-415 |

## Update History

- 2026-08-24T20:55+02:00 — Created for 260824-PDLS.
