# mcp/tests/test_provider_current_state.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/tests/test_provider_current_state.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-28T19:52+02:00                     |
| lastVerifiedCommitHash | `bf3a3c4e310fb11032da885083d026a74a31ee9c` |
| lastVerifiedCommitDate | 2026-05-28T20:06:49+02:00|
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
provider aggregation, workflow-local instance paths for benchmarks, and
integration through `provider_status_packet()` plus
`provider_diagnostics_packet()`.

`ready_status_payload()` builds a small GrepAI plus CGC status packet with
running container-state summaries, one CGC repo watcher, and known uptime
seconds. Individual tests mutate that fixture to prove degradation and disabled
provider behavior without starting real providers.

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
| The disabled-provider regression proves disabled GrepAI is reported as disabled without poisoning aggregate readiness. | L105-L124 | [test_provider_current_state.py](agents-remember-md/mcp/tests/test_provider_current_state.py) |
| The workflow-local instance regression verifies benchmark scope/id paths under `logs/providers/status/benchmark/<instance>/current.json`. | L126-L155 | [test_provider_current_state.py](agents-remember-md/mcp/tests/test_provider_current_state.py) |
| The provider-status integration regression mocks watcher status and asserts `provider_status_packet()` writes current state and returns the file path while `provider_diagnostics_packet()` returns the full current-state payload. | L157-L174 | [test_provider_current_state.py](agents-remember-md/mcp/tests/test_provider_current_state.py) |
| Current-state projection and persistence are implemented in the provider current-state module. | L16-L277 | [current_state.py](agents-remember-md/mcp/src/agents_remember/providers/current_state.py) |

## Cross-Repo References

No sibling repository evidence is needed for these tests.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-28T19:52+02:00: Updated after provider current-state integration tests moved full current-state payload assertions to provider diagnostics.
- 2026-05-28T12:32+02:00: Created for provider current-state unit coverage.
