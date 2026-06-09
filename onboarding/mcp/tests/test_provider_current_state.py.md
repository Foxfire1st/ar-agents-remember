# mcp/tests/test_provider_current_state.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/tests/test_provider_current_state.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-10T06:20+02:00     |
| lastVerifiedCommitHash | `592274a52cec61d97521771c630272c72240ed01` |
| lastVerifiedCommitDate | 2026-06-10T01:38:42+02:00|
| governingOverview      | `../overview.md`                           |

## Governing Overview

[mcp/overview.md](../overview.md)

## Purpose

`test_provider_current_state.py` protects the MCP provider current-state
contract: provider status should show what is true now, not only what happened
during the last setup attempt.

## Code Commentary

### Logic

The test module uses synthetic settings and synthetic watcher status payloads.
It verifies Docker container state normalization, the current-state file path,
ready and degraded aggregate state, per-provider resource shape, disabled
provider aggregation, GrepAI no-workspace degradation, GrepAI no-workspace
restart/rebind recovery guidance, workflow-local instance paths for benchmarks,
and integration through `provider_status_packet()` plus
`provider_diagnostics_packet()`.

`ready_status_payload()` builds a small GrepAI plus CGC status packet with
running container-state summaries, one CGC repo watcher, a healthy GrepAI
`workspaceStatus`, and known uptime seconds. Individual tests mutate that fixture
to prove degradation and disabled provider behavior without starting real
providers. `test_current_state_reports_grepai_no_workspace_as_degraded` drops the
watcher's searchable workspace and asserts GrepAI reports `degraded` with
`indexingState: noWorkspace`, degrading the aggregate state.
`test_provider_status_reports_restart_recovery_for_grepai_no_workspace` then
mocks the same no-workspace status through the provider-status surface and
asserts both compact status and diagnostics return the
`provider_watchers(action='restart')` recovery action.

Readiness coverage from the 2.5.0/2.5.1 cycles pins the content-gated `ok`
contract: an `empty` CGC graph degrades the repo target, the provider, the
aggregate, and the global packet `ok` (with `partial` when other providers
remain ready), and yields a per-repo CGC restart recovery action; the
`indexing` transient stays ready at every level and instead feeds the compact
summary's `indexing` busy-target list. A `restarting` (crash-looping) watcher
container is not ready and degrades provider and global `ok`, and GrepAI
`initialScan` log markers map to `indexing`/`indexed`/`unknown` without
degrading readiness.

### Conventions

- Keep these tests side-effect free; do not require Docker, GrepAI, CGC, or
  network access.
- Use temporary directories for generated settings and status files.
- Mock watcher status when testing provider-status integration so the test
  focuses on current-state projection.

### Invariants And Boundaries

- Current state must not include setup history such as `lastSetup`.
- Disabled configured providers must not make the aggregate status fail.
- Worktree and benchmark provider scopes must write status under their own
  instance path.
- Provider status must persist current state and return the current-state file
  path in compact status; the full current-state payload belongs in diagnostics.

### Todos

None.

## Docs References

No external documentation is needed for these standard-library unit tests.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The Docker summary regression asserts container state, running flag, health, and integer uptime. | L24-L40 | [test_provider_current_state.py](agents-remember-md/mcp/tests/test_provider_current_state.py) |
| The current-truth regression writes current state, asserts `ready`, excludes `lastSetup`, checks the central status path, and verifies GrepAI watcher/resource fields. | L42-L74 | [test_provider_current_state.py](agents-remember-md/mcp/tests/test_provider_current_state.py) |
| The CGC degradation regression mutates one repo watcher to down and expects aggregate degraded state plus per-repo watcher/container details. | L76-L103 | [test_provider_current_state.py](agents-remember-md/mcp/tests/test_provider_current_state.py) |
| The disabled-provider regression proves disabled GrepAI is reported as disabled without poisoning aggregate readiness. | L157-L176 | [test_provider_current_state.py](agents-remember-md/mcp/tests/test_provider_current_state.py) |
| The GrepAI no-workspace regression drops the watcher's searchable workspace and expects GrepAI `degraded` with `indexingState: noWorkspace` plus a degraded aggregate. | L107-L127 | [test_provider_current_state.py](agents-remember-md/mcp/tests/test_provider_current_state.py) |
| Provider status and diagnostics both expose restart/rebind recovery guidance when the current projected GrepAI state is `noWorkspace`. | L129-L155 | [test_provider_current_state.py](agents-remember-md/mcp/tests/test_provider_current_state.py) |
| The workflow-local instance regression verifies benchmark scope/id paths under `logs/providers/status/benchmark/<instance>/current.json`. | L178-L208 | [test_provider_current_state.py](agents-remember-md/mcp/tests/test_provider_current_state.py) |
| The provider-status integration regression mocks watcher status and asserts `provider_status_packet()` writes current state and returns the file path while `provider_diagnostics_packet()` returns the full current-state payload. | L209-L230 | [test_provider_current_state.py](agents-remember-md/mcp/tests/test_provider_current_state.py) |
| Current-state projection and persistence are implemented in the provider current-state module. | L16-L277 | [current_state.py](agents-remember-md/mcp/src/agents_remember/providers/current_state.py) |

## Cross-Repo References

No sibling repository evidence is needed for these tests.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-06-10T06:20+02:00 — Body-quality pass: merged the 2.5.0/2.5.1 readiness coverage (content-gated ok, indexing busy list, restarting watcher, scan markers) into Logic (documentation only).
- 2026-06-10T05:30+02:00 — Added tests: restarting (crash-looping) watcher is not ready and degrades the provider/global ok; GrepAI `initialScan` markers map to indexing/indexed/unknown without degrading readiness; GrepAI indexing feeds the summary busy list.
- 2026-06-09T22:10+02:00 — Added tests for empty-graph degradation (repo target, provider, aggregate, and global packet `ok`/`partial`), the `indexing` transient staying ready at every level, the CGC per-repo restart recovery action, and the summary `indexing` busy-target list.
- 2026-06-04T22:15+02:00: Documented the provider-status regression that returns restart/rebind recovery guidance for GrepAI `noWorkspace` from both compact status and diagnostics.
- 2026-06-02T16:24+02:00: Added the `test_current_state_reports_grepai_no_workspace_as_degraded` regression (GrepAI reports `degraded` / `indexingState: noWorkspace` when the watcher has no searchable workspace) and noted that the ready fixture now includes a healthy `workspaceStatus`; reflected both in the Logic narrative and repo-internal references.
- 2026-05-28T19:52+02:00: Updated after provider current-state integration tests moved full current-state payload assertions to provider diagnostics.
- 2026-05-28T12:32+02:00: Created for provider current-state unit coverage.
