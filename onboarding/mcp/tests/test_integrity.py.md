# mcp/tests/test_integrity.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/tests/test_integrity.py`              |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-28T19:52+02:00                     |
| lastVerifiedCommitHash | `bf3a3c4e310fb11032da885083d026a74a31ee9c` |
| lastVerifiedCommitDate | 2026-05-28T20:06:49+02:00|
| governingOverview      | `../overview.md`                           |

## Governing Overview

[mcp/overview.md](../overview.md)

## Purpose

`test_integrity.py` verifies provider runner integrity manifests for the current
Docker-owned provider model.

## Code Commentary

### Logic

The tests create temporary MCP settings, inspect the not-installed integrity
case, prove that legacy CodeGraphContext venv files are ignored by current
manifests, and assert that provider status does not short-circuit on those
legacy venv files. The status-success regression now reads compact
`provider_status_packet()` output for provider state and uses
`provider_diagnostics_packet()` for integrity detail.

### Conventions

The test inserts `mcp/src` and the test directory into `sys.path`, matching the
MCP test-suite pattern for importing the package under test and shared test
helpers without installing the package.

### Invariants And Boundaries

- Missing watched runner files plus no manifest is a clean `notInstalled`
  state.
- Current `_bin` and `_venvs` files are not part of the watched runner surface
  because CGC and GrepAI execution is Docker-owned.
- Provider status must proceed to watcher status when only legacy host venv
  files exist, and compact status plus diagnostics should preserve the
  summary/detail split.

### Todos

None.

## Docs References

No external documentation is needed for this unit-test file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation is needed for the test behavior. | n/a | n/a |

## Repo-Internal References

The test file and provider status module are the direct evidence.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The test imports provider integrity helpers, provider status packet, and shared config fixtures. | L8-L20 | [test_integrity.py](agents-remember-md/mcp/tests/test_integrity.py) |
| The first test records the missing-manifest/no-runner-files state as `notInstalled`. | L23-L31 | [test_integrity.py](agents-remember-md/mcp/tests/test_integrity.py) |
| The second test writes an empty current manifest while legacy CGC venv files exist and verifies later venv edits remain ignored. | L33-L48 | [test_integrity.py](agents-remember-md/mcp/tests/test_integrity.py) |
| The third test verifies provider status proceeds instead of returning `runnerIntegrityFailed` when only legacy CGC venv files exist, then reports ready current state through compact status and integrity detail through diagnostics. | L50-L90 | [test_integrity.py](agents-remember-md/mcp/tests/test_integrity.py) |
| Provider status performs the runner integrity check before watcher status. | L38-L58 | [status.py](agents-remember-md/mcp/src/agents_remember/providers/status.py) |

## Cross-Repo References

No meaningful cross-repo boundary is documented here.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No sibling repository boundary is needed to explain this file. | n/a | n/a |

## Update History

- 2026-05-28T19:52+02:00: Updated after provider integrity tests split compact provider status assertions from diagnostics integrity assertions.
- 2026-05-28T12:32+02:00: Updated after integrity status coverage switched to current-state-derived provider state.
- 2026-05-26T12:51+02:00: Updated after integrity tests stopped treating CodeGraphContext host venv files as watched runner authority.
- 2026-05-25T18:07+02:00: Updated after integrity tests switched changed/unrecorded runner cases to CGC venv files because `_bin` is no longer a watched provider path.
- 2026-05-23T22:37+02:00: Created during quality-pass closeout after direct-closeout preview found the changed test lacked sidecar onboarding.
