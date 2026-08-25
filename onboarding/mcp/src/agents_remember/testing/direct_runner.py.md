# mcp/src/agents_remember/testing/direct_runner.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/testing/direct_runner.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-25T08:16+02:00 |
| lastVerifiedCommitHash | `cb6623775a04cbdeb0509dc26f08a8268189c3f6` |
| lastVerifiedCommitDate | `2026-08-25T08:12:56+02:00` |
| governingOverview | `overview.md` |

## Governing Overview

[Python testing boundary](overview.md)

## Purpose

Implements the only direct Python diagnostic command behind `./scripts/test-python`.

## Code Commentary

`run_direct_diagnostic` rejects flags, asks the sole classifier to admit the complete request,
prepares diagnostic-only bootstrap, scrubs the environment, forces the canonical config and
`-n=0`, and invokes pytest once with exactly the admitted nodes. It validates the child phase/node
report, rechecks the content-sealed binding after execution, and emits bounded stdout/stderr plus
`DiagnosticTestEvidence`. CLI help and every result state say non-certifying.

The runner deliberately knows nothing about how safety was established. The v2 classifier supplies
an exact eligible/refused value backed by the reviewed cohort manifest; the runner consumes that
typed value and never falls back to analyzing or accepting another selector.

## Invariants And Boundaries

- No fallback, subset retry, alternate config, or arbitrary pytest flag exists.
- A changed cohort file or configuration refuses before execution and cannot be auto-refreshed.
- Dagger admission is removed from the child environment.
- Missing, contradictory, or stale child evidence is infrastructure failure, not a test result.
- Only node outcomes and timing are retained; accepting consumers cannot use the payload.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The route classifies before executing once and rechecks the binding afterwards. | `run_direct_diagnostic` | mcp/src/agents_remember/testing/direct_runner.py:164-235 |
| The child command is serial and canonical. | `_pytest_command` | mcp/src/agents_remember/testing/direct_runner.py:270-294 |
| The report loader checks schema, exit code, exact node order, and outcomes. | `_load_phase_report` | mcp/src/agents_remember/testing/direct_runner.py:297-391 |

## Update History

- 2026-08-25T01:56+02:00 — Reconciled the runner with the explicit v2 content-sealed cohort and
  post-execution binding check; verification remains closeout-owned.
- 2026-08-24T21:23+02:00 — Created for 260824-PDLS.
