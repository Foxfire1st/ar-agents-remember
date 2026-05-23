# mcp/tests/test_integrity.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/tests/test_integrity.py`              |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-23T22:37+02:00                     |
| lastVerifiedCommitHash | `3417d47f1e76d37e9ba6e803c7b28afa4758da9c` |
| lastVerifiedCommitDate | 2026-05-23T23:06:47+02:00|
| governingOverview      | `../overview.md`                           |

## Governing Overview

[mcp/overview.md](../overview.md)

## Purpose

`test_integrity.py` verifies provider runner integrity manifests and the
provider status short-circuit that protects watcher/status calls from changed
or unrecorded provider runner files.

## Code Commentary

### Logic

The tests create temporary MCP settings, inspect the not-installed integrity
case, write a provider runner manifest, mutate a recorded runner file to ensure
the changed file is reported, and assert that provider status returns
`runnerIntegrityFailed` with a `runtime_install` recovery action when runner
files exist without a manifest.

### Conventions

The test inserts `mcp/src` and the test directory into `sys.path`, matching the
MCP test-suite pattern for importing the package under test and shared test
helpers without installing the package.

### Invariants And Boundaries

- Missing runner files plus no manifest is a clean `notInstalled` state.
- Changed recorded runner files must fail integrity.
- Provider status must not probe watchers when runner integrity fails.

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
| The second test writes a manifest, mutates a runner executable, and expects the changed runner file to be reported. | L33-L48 | [test_integrity.py](agents-remember-md/mcp/tests/test_integrity.py) |
| The third test verifies provider status returns `runnerIntegrityFailed` and recommends `runtime_install` for unrecorded runner files. | L50-L64 | [test_integrity.py](agents-remember-md/mcp/tests/test_integrity.py) |
| Provider status performs the runner integrity check before watcher status. | L38-L58 | [status.py](agents-remember-md/mcp/src/agents_remember/providers/status.py) |

## Cross-Repo References

No meaningful cross-repo boundary is documented here.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No sibling repository boundary is needed to explain this file. | n/a | n/a |

## Update History

- 2026-05-23T22:37+02:00: Created during quality-pass closeout after direct-closeout preview found the changed test lacked sidecar onboarding.
