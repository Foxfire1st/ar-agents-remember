# mcp/src/agents_remember/testing/pytest_phase_reporter.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/testing/pytest_phase_reporter.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T21:23+02:00 |
| lastVerifiedCommitHash | `b99501852bcfa5f499a25e7183063751f6133a28` |
| lastVerifiedCommitDate | 2026-08-24T21:21:58+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Python testing boundary](overview.md)

## Purpose

Produces the common `python-pytest-phase-report/v1` node/outcome and phase-timing record for direct
and Dagger routes without granting evidence authority.

## Code Commentary

One typed `_PhaseState` records session, collection, first-node, and outcome observations. At
session finish the controller writes a compact JSON report twice so the final payload also measures
its own reporting duration. Missing phases become `null`, preserving pytest's original exit instead
of masking a collection/usage error with a reporter exception.

## Invariants And Boundaries

- Workers do not race to publish the controller report.
- The recorded pytest exit code is the original exit code.
- Timing and outcome records are observations; authority comes from the route that publishes them.
- Missing timestamps are explicit `null`, never fabricated zero durations except execution after a
  completed empty collection.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| One state object owns all per-session observations. | `_PhaseState` | mcp/src/agents_remember/testing/pytest_phase_reporter.py:28-39 |
| Session finish writes a total report without changing exit status. | `pytest_sessionfinish`; `_duration` | mcp/src/agents_remember/testing/pytest_phase_reporter.py:82-114; mcp/src/agents_remember/testing/pytest_phase_reporter.py:159-163 |

## Update History

- 2026-08-24T21:23+02:00 — Created for 260824-PDLS; curator records the post-review total-report
  and single-state-object repair.
