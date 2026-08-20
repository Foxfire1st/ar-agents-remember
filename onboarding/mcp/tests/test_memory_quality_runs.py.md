# mcp/tests/test_memory_quality_runs.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_memory_quality_runs.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-20T21:30+02:00 |
| lastVerifiedCommitHash | `de3a0fd9204f2e64755032274fb4e741bfddf6df` |
| lastVerifiedCommitDate | 2026-08-20T21:16:45+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Forcing suite for the bounded background run registry (`application/memory_quality_runs.py`) and
the async start/poll application wrappers (`application/memory_tools.py`), 260815-DAG-L15-R7.

## Code Commentary

### Logic

`MemoryQualityRunRegistryTests` drives the registry directly (module `_registry` cleared per test):
start → poll → completed with the identical result; a failed run reports the error text; single-flight
returns the active run's id/status for a concurrent same-key start; boundedness evicts completed runs
past the patched `MAX_QUALITY_RUNS`; TTL eviction drops stale completed runs and keeps fresh ones;
eviction with no completed runs is a no-op (running entries are never evicted).

`MemoryQualityApplicationWrapperTests` drives the application wrappers: `start_and_poll_wrappers_drive_a_background_run`
runs the real single-flight path with `_run_quality_check` mocked, asserting the started envelope
(`ok`, `status: started`, `runId`) and the completed poll carrying `ok: True` with the exact kwargs
forwarded; `poll_reports_an_unknown_run_as_run_not_found` pins the `ok: False`/`run-not-found`
envelope; `test_poll_wraps_running_and_failed_envelopes_with_ok` deterministically fills the registry
(direct `_QualityRun` entries, no threads) to cover the running/failed `ok=True` wrapper branches
(the gate-repair `ok`-header fix); `test_start_key_scopes_contract_path_and_checks` covers both
`_quality_run_key` branches (contract_path vs official, checks set vs empty).

### Invariants And Boundaries

- Registry tests manipulate the module `_registry` directly with `addCleanup` clearing — they never
  depend on thread timing for assertions.
- The wrapper tests mock only `_run_quality_check` (the slow real check), not the registry or the
  single-flight logic, so the concurrency contract is exercised for real.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The registry forcing tests. | `MemoryQualityRunRegistryTests` | mcp/tests/test_memory_quality_runs.py:13-97 |
| The application-wrapper forcing tests. | `MemoryQualityApplicationWrapperTests` | mcp/tests/test_memory_quality_runs.py:100-174 |
| The registry under test. | `start_quality_run`; `poll_quality_run`; `_evict_locked` | mcp/src/agents_remember/application/memory_quality_runs.py:37-71; mcp/src/agents_remember/application/memory_quality_runs.py:74-85; mcp/src/agents_remember/application/memory_quality_runs.py:88-99 |
| The wrappers under test. | `start_memory_quality_check_run`; `poll_memory_quality_check_run` | mcp/src/agents_remember/application/memory_tools.py:250-279; mcp/src/agents_remember/application/memory_tools.py:280-301 |

## Cross-Repo References

No cross-repo boundary applies to this forcing suite.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-20T21:30+02:00 — Created for 260815-DAG-L15-R7: the run-registry forcing suite
  (start/poll/completed/failed/single-flight/boundedness/TTL eviction) plus the application-wrapper
  tests covering the started/run-not-found/running/failed envelope branches and the key-scoping
  branches (extended in the gate-repair rounds). Verified at code commit de3a0fd9.
