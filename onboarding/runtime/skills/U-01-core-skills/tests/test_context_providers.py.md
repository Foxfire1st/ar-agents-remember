# test_context_providers.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `runtime/skills/U-01-core-skills/tests/test_context_providers.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-21T02:10+02:00                     |
| lastVerifiedCommitHash | `0462de46a1da1bf1997e3979f4cc5bc53d1132f6` |
| lastVerifiedCommitDate | 2026-05-21T08:30:44+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](../../../../../overview.md)

## Purpose

`test_context_providers.py` verifies the shared provider layout, settings expansion, runtime cleanup, and patch helpers used by the provider lifecycle manager.

## Code Commentary

### Logic

The test module imports `agents_remember.context_providers` from the core-skill shared helper path. It checks that CGC runtime layout expansion produces a contained per-repo runtime root, shared provider venv, pinned requirements file, patch root, provider-data FalkorDB backend root, FalkorDB process env, and isolated HOME-like runtime directories. It verifies that `ensure_cgc_runtime_layout` writes pinned defaults, inherits source `.gitignore` rules into the managed `.cgcignore`, and excludes process-only CGC/FalkorDB runtime keys from persisted `.env`.

The provider-settings tests cover multi-root settings expansion, root-level `cgcignorePatterns`, and rejection of configured code repository roots that do not exist. The cleanup test creates a synthetic stale `my-app` runtime instance plus legacy `db`, `global`, and `kuzu` artifacts under a configured runtime root, then verifies cleanup removes only those generated artifacts while preserving the shared FalkorDB backend data root. The remaining tests cover GrepAI pin handling, forbidden source artifact detection, idempotent CGC patch application, rejection of unexpected patch source text, stable repo id normalization, and stable patch id naming.

### Conventions

All tests use temporary directories and do not require CodeGraphContext to be installed. The `my-app` directory name appears only as synthetic test data to prove stale generated runtime folders are removed; it is not intended live configuration. The patch tests use small synthetic snippets rather than mutating a real provider package.

### Invariants And Boundaries

The tests protect the core provider invariant: managed provider artifacts belong under `ar-coordination/providers/`, not inside indexed source repositories. They also protect reinstall idempotence by proving stale generated runtime instances and legacy embedded-backend files can be removed without touching shared FalkorDB backend data.

### Todos

- Add an integration smoke test once the environment can provide a local CGC package without network setup.

## Docs References

No external documentation is needed for these unit tests.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The layout tests assert that CGC uses `providers/codegraphcontext/<repo-id>`, a shared `provider-data/codegraphcontext/falkordb` backend root, `providers/_venvs/codegraphcontext`, `providers/requirements/codegraphcontext.txt`, and per-repo FalkorDB process env. | L45-L90 | [test_context_providers.py](agents-remember-md/runtime/skills/U-01-core-skills/tests/test_context_providers.py) |
| The default-layout test asserts the pinned requirement, config, managed `.cgcignore`, persisted `.env` exclusions, logs, run, HOME, APPDATA, and LOCALAPPDATA directories. | L92-L126 | [test_context_providers.py](agents-remember-md/runtime/skills/U-01-core-skills/tests/test_context_providers.py) |
| The cleanup test removes a synthetic stale `my-app` instance and legacy `db`, `global`, and `kuzu` artifacts while preserving the shared FalkorDB backend data root. | L128-L160 | [test_context_providers.py](agents-remember-md/runtime/skills/U-01-core-skills/tests/test_context_providers.py) |
| Provider-settings tests cover root expansion, per-root `cgcignorePatterns`, and rejection of configured code repository paths that do not exist. | L163-L215 | [test_context_providers.py](agents-remember-md/runtime/skills/U-01-core-skills/tests/test_context_providers.py) |
| GrepAI pin, source artifact, patch idempotence, patch rejection, repo id, and patch id tests cover the provider containment and patch helper edge cases. | L217-L331 | [test_context_providers.py](agents-remember-md/runtime/skills/U-01-core-skills/tests/test_context_providers.py) |

## Cross-Repo References

No sibling repository evidence is needed for these tests.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-21T02:10+02:00: Updated expected CGC backend data layout from provider-owned `_backends` to durable `provider-data/`.
- 2026-05-21T01:47+02:00: Updated for FalkorDB-only CGC layout, managed `.cgcignore` inheritance, missing-root rejection, stale runtime cleanup, GrepAI pin coverage, and the second CGC patch.
- 2026-05-20T19:11+02:00: Created onboarding for the provider layout and patch helper unit tests. Verification metadata remains pinned to the current committed source revision until closeout commits these source changes.
