# test_context_providers.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `runtime/skills/U-01-core-skills/tests/test_context_providers.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-23T05:32+02:00                     |
| lastVerifiedCommitHash | `00aae9dad3d8740e10a41ab285f87ecab8608745` |
| lastVerifiedCommitDate | 2026-05-21T23:53:08+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](../../../../../overview.md)

## Purpose

`test_context_providers.py` verifies the shared provider layout, settings expansion, runtime cleanup, and patch helpers used by the provider lifecycle manager.

## Code Commentary

### Logic

The test module imports `agents_remember.context_providers` from the core-skill shared helper path. It checks that CGC runtime layout expansion produces a contained per-repo runner root, shared provider venv, pinned requirements file, patch root, durable `providers/data` FalkorDB backend root, FalkorDB process env, and isolated HOME-like runtime directories. It verifies that `ensure_cgc_runtime_layout` writes pinned defaults, inherits source `.gitignore` rules into the managed `.cgcignore`, and excludes process-only CGC/FalkorDB runtime keys from persisted `.env`.

The provider-settings tests cover CGC multi-root settings expansion, root-level `cgcignorePatterns`, and rejection of configured code repository roots that do not exist. The cleanup test creates a synthetic stale `my-app` runtime instance plus legacy `db`, `global`, and `kuzu` artifacts under a configured runtime root, then verifies cleanup removes only those generated artifacts while preserving the shared FalkorDB backend data root. The GrepAI tests cover pin handling, workspace runtime paths, explicit external and repo-internal memory roots, provider-owned mirror roots, mirror sync exclusion of source `.grepai/`, provider-owned workspace config, PostgreSQL store config, explicit Ollama endpoint/dimension defaults, detection of `.grepai/` artifacts in indexed roots, and removal of disposable `.grepai/` artifacts without touching durable onboarding files. The remaining tests cover forbidden source artifact detection, idempotent CGC patch application including the visualizer repo-query and route patches, CGC module lookup helpers including the CLI helper, rejection of unexpected patch source text, stable repo id normalization, and stable patch id naming.

### Conventions

All tests use temporary directories and do not require CodeGraphContext, GrepAI, Docker, FalkorDB, or PostgreSQL to be installed. The `my-app` directory name appears only as synthetic test data to prove stale generated runtime folders are removed; it is not intended live configuration. The GrepAI tests verify generated config text and path containment, not live indexing. The patch tests use small synthetic snippets rather than mutating a real provider package.

### Invariants And Boundaries

The tests protect the core provider invariant: managed provider artifacts belong under `ar-coordination/providers/`, not as durable source or memory data. They also protect reinstall idempotence by proving stale generated runtime instances, legacy embedded-backend files, and disposable GrepAI root artifacts can be removed without touching shared backend data or onboarding files, and that GrepAI's durable database data root is separate from provider-owned config/log/state/mirror scaffolding.

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
| The layout tests assert that CGC uses `providers/runners/codegraphcontext/<repo-id>`, a shared `providers/data/codegraphcontext/falkordb` backend root, `providers/_venvs/codegraphcontext`, `providers/requirements/codegraphcontext.txt`, and per-repo FalkorDB process env. | L67-L113 | [test_context_providers.py](agents-remember-md/runtime/skills/U-01-core-skills/tests/test_context_providers.py) |
| The default-layout test asserts the pinned requirement, config, managed `.cgcignore`, persisted `.env` exclusions, logs, run, HOME, APPDATA, and LOCALAPPDATA directories. | L115-L153 | [test_context_providers.py](agents-remember-md/runtime/skills/U-01-core-skills/tests/test_context_providers.py) |
| The cleanup test removes a synthetic stale `my-app` instance and legacy `db`, `global`, and `kuzu` artifacts while preserving the shared FalkorDB backend data root. | L154-L187 | [test_context_providers.py](agents-remember-md/runtime/skills/U-01-core-skills/tests/test_context_providers.py) |
| Provider-settings tests cover root expansion, per-root `cgcignorePatterns`, and rejection of configured code repository paths that do not exist. | L189-L241 | [test_context_providers.py](agents-remember-md/runtime/skills/U-01-core-skills/tests/test_context_providers.py) |
| GrepAI tests cover pin handling, workspace runtime and PostgreSQL data roots, settings expansion across external and internal memory roots into provider-owned mirrors, mirror sync exclusion of source `.grepai/`, provider-owned workspace config, PostgreSQL store config, explicit Ollama endpoint/dimension defaults, detection of `.grepai/` artifacts in indexed memory roots, and disposable root artifact removal that preserves regular onboarding files. | L243-L422 | [test_context_providers.py](agents-remember-md/runtime/skills/U-01-core-skills/tests/test_context_providers.py) |
| Source artifact, patch idempotence, CGC module lookup, patch rejection, repo id, and patch id tests cover the remaining provider containment and patch helper edge cases, including the visualizer repo-query patch, visualizer route patches, `viz/server.py` lookup, and `cli/cli_helpers.py` lookup. | L423-L679 | [test_context_providers.py](agents-remember-md/runtime/skills/U-01-core-skills/tests/test_context_providers.py) |

## Cross-Repo References

No sibling repository evidence is needed for these tests.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

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
