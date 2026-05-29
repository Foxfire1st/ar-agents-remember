# test_context_providers.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/tests/test_context_providers.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-29T07:19+02:00                     |
| lastVerifiedCommitHash | `e1382b9277d48f13b6a1cb065f2fa2638b36feba` |
| lastVerifiedCommitDate | 2026-05-29T07:08:19+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](../../../../../overview.md)

## Purpose

`test_context_providers.py` verifies the shared provider layout, settings expansion, runtime cleanup, and patch helpers used by the provider lifecycle manager.

## Code Commentary

### Logic

The test module imports `agents_remember.providers.context` from the MCP
package source path. It checks that CGC runtime layout expansion produces a
contained per-repo runner root, pinned requirements file, patch root, durable
`providers/data` FalkorDB backend root, FalkorDB process env, and isolated
HOME-like runtime directories without exposing host venv executable paths. It
verifies that `ensure_cgc_runtime_layout` writes pinned defaults, inherits
source `.gitignore` rules into the managed `.cgcignore`, and excludes
process-only CGC/FalkorDB runtime keys from persisted `.env`.

The provider-settings tests cover CGC multi-root settings expansion, root-level
`cgcignorePatterns`, rejection of configured code repository roots that do not
exist, and rejection of stale `venvRoot` settings. The cleanup test creates a
synthetic stale `my-app` runtime instance plus legacy `db`, `global`, and
`kuzu` artifacts under a configured runtime root, then verifies cleanup removes
only those generated artifacts while preserving the shared FalkorDB backend
data root. The GrepAI tests cover pin handling, workspace runtime paths,
explicit external and repo-internal memory roots, provider-owned mirror roots,
mirror sync exclusion of source `.grepai/`, provider-owned workspace config,
PostgreSQL store config, explicit Ollama endpoint/dimension defaults, central
`logs/providers/grepai` operator log layout, detection of `.grepai/` artifacts
in indexed roots, and removal of disposable `.grepai/` artifacts without
touching durable onboarding files. The remaining tests cover forbidden source
artifact detection, idempotent CGC patch application including the visualizer
repo-query and route patches, rejection of unexpected patch source text, stable
repo id normalization, and stable patch id naming.

CGC layout tests also cover that ambient host `FALKORDB_HOST` and
`FALKORDB_PORT` values do not alter default layout env or provider-settings
`hostPort=auto` expansion.

Windows-host coverage asserts that `to_container_path` strips a leading drive
letter (and is a no-op on POSIX paths), that the layout's
`container_runtime_root` / `container_code_repo_root` are driveless, and that
`env(for_container=True)` renders driveless path values and omits the host-only
Windows variables (`USERPROFILE`, `APPDATA`, `LOCALAPPDATA`) while leaving
non-path values unchanged.

### Conventions

All tests use temporary directories and do not require CodeGraphContext, GrepAI, Docker, FalkorDB, or PostgreSQL to be installed. The `my-app` directory name appears only as synthetic test data to prove stale generated runtime folders are removed; it is not intended live configuration. The GrepAI tests verify generated config text and path containment, not live indexing. The patch tests use small synthetic snippets rather than mutating a real provider package.

### Invariants And Boundaries

The tests protect the core provider invariant: managed provider artifacts belong
under `ar-coordination/providers/` and operator logs under
`ar-coordination/logs/`, not as durable source or memory data. They also
protect reinstall idempotence by proving stale generated runtime instances,
legacy embedded-backend files, and disposable GrepAI root artifacts can be
removed without touching shared backend data or onboarding files, and that
GrepAI's durable database data root is separate from provider-owned
config/state/mirror scaffolding.

The tests protect that provider backend env authority stays in settings/state,
not ambient host process variables.

The tests also protect the anti-slop boundary that `venvRoot` is no longer a
supported CGC settings field and managed CGC must not fall back to a
coordination-root host executable.

### Todos

- Add integration smoke tests once the environment can provide local CGC and GrepAI packages plus Docker backends without network setup.

## Docs References

No external documentation is needed for these unit tests.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The layout tests assert that CGC uses `providers/runners/codegraphcontext/<repo-id>`, a shared `providers/data/codegraphcontext/falkordb` backend root, `providers/requirements/codegraphcontext.txt`, patch root, and per-repo FalkorDB process env without host venv executable fields. | L89-L125 | [test_context_providers.py](agents-remember-md/mcp/tests/test_context_providers.py) |
| The default-layout test asserts the pinned requirement, config, managed `.cgcignore`, persisted `.env` exclusions, logs, run, HOME, APPDATA, and LOCALAPPDATA directories. | L145-L187 | [test_context_providers.py](agents-remember-md/mcp/tests/test_context_providers.py) |
| The cleanup test removes a synthetic stale `my-app` instance and legacy `db`, `global`, and `kuzu` artifacts while preserving the shared FalkorDB backend data root. | L188-L226 | [test_context_providers.py](agents-remember-md/mcp/tests/test_context_providers.py) |
| Provider-settings tests cover root expansion, per-root `cgcignorePatterns`, rejection of configured code repository paths that do not exist, and rejection of removed `venvRoot` settings. | L228-L338 | [test_context_providers.py](agents-remember-md/mcp/tests/test_context_providers.py) |
| GrepAI tests cover pin handling, workspace runtime and PostgreSQL data roots, central log roots, settings expansion across external and internal memory roots into provider-owned mirrors, mirror sync exclusion of source `.grepai/`, provider-owned workspace config, PostgreSQL store config, explicit Ollama endpoint/dimension defaults, detection of `.grepai/` artifacts in indexed memory roots, and disposable root artifact removal that preserves regular onboarding files. | L243-L445 | [test_context_providers.py](agents-remember-md/mcp/tests/test_context_providers.py) |
| Source artifact, patch idempotence, patch rejection, repo id, and patch id tests cover the remaining provider containment and patch helper edge cases, including the visualizer repo-query and route patches. | L423-L726 | [test_context_providers.py](agents-remember-md/mcp/tests/test_context_providers.py) |

## Cross-Repo References

No sibling repository evidence is needed for these tests.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-29T07:19+02:00: Added coverage for `to_container_path`, driveless `container_runtime_root` / `container_code_repo_root` properties, and `env(for_container=True)` (driveless path values, omitted host-only Windows env) for Windows-host provider support.
- 2026-05-28T13:40+02:00: Updated after CGC layout tests removed host venv executable expectations, added stale `venvRoot` rejection coverage, and removed venv module lookup tests.
- 2026-05-28T12:32+02:00: Updated after GrepAI context layout tests moved operator logs under `logs/providers/grepai`.
- 2026-05-25T19:16+02:00: Updated after tests imported the direct `providers.context` facade and provider context implementation moved into `context_modules/`.
- 2026-05-24T19:25+02:00: Added coverage that CGC FalkorDB host/port defaults ignore ambient host `FALKORDB_*` environment variables.
- 2026-05-23T17:50+02:00: Moved onboarding to `mcp/tests` after the tests moved out of `runtime/skills/U-01-core-skills/tests` and updated imports to the MCP package provider module.
- 2026-05-23T05:32+02:00: Updated provider layout expectations to `providers/runners` plus `providers/data`.
- 2026-05-21T23:18+02:00: Updated after adding GrepAI disposable root artifact removal coverage.
- 2026-05-21T13:22+02:00: Updated CGC patch tests for visualizer server route handling, CLI default-route propagation, CLI helper lookup, and the two new patch ids.
- 2026-05-21T12:40+02:00: Updated CGC patch tests for the visualizer repo-query patch, `viz/server.py` module lookup, and patch id stability.
- 2026-05-21T12:35+02:00: Updated GrepAI tests for provider-owned mirror-root expansion and mirror sync that excludes source `.grepai/` artifacts.
- 2026-05-21T12:20+02:00: Updated GrepAI workspace config test notes for explicit local Ollama endpoint and dimensions.
- 2026-05-21T11:50+02:00: Updated for GrepAI workspace-mode tests covering multi-root memory indexing, PostgreSQL data roots, provider-owned config, and `.grepai/` containment.
- 2026-05-21T02:10+02:00: Updated expected CGC backend data layout from provider-owned `_backends` to durable `provider-data/`.
- 2026-05-21T01:47+02:00: Updated for FalkorDB-only CGC layout, managed `.cgcignore` inheritance, missing-root rejection, stale runtime cleanup, GrepAI pin coverage, and the second CGC patch.
- 2026-05-20T19:11+02:00: Created onboarding for the provider layout and patch helper unit tests. Verification metadata remains pinned to the current committed source revision until closeout commits these source changes.
