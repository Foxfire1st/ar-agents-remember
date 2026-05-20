# test_context_providers.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `runtime/skills/U-01-core-skills/tests/test_context_providers.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-20T20:01+02:00                     |
| lastVerifiedCommitHash | `e4ae4955d888d3ce58b55b5ca99d20039cbcb214` |
| lastVerifiedCommitDate | 2026-05-20T20:01:26+02:00 |
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](../../../../../overview.md)

## Purpose

`test_context_providers.py` verifies the shared provider layout and patch helpers used by the provider lifecycle manager.

## Code Commentary

### Logic

The test module imports `agents_remember.context_providers` from the core-skill shared helper path. It checks that CGC runtime layout expansion produces a contained per-repo runtime root, shared provider venv, pinned requirements file, patch root, process env, and KuzuDB path. It verifies that `ensure_cgc_runtime_layout` writes pinned defaults and excludes process-only CGC runtime keys from persisted `.env`. It also covers forbidden source artifact detection, idempotent patch application, rejection of unexpected patch source text, stable repo id normalization, and stable patch id naming.

### Conventions

All tests use temporary directories and do not require CodeGraphContext to be installed. The patch tests use a small synthetic `cgcignore.py` snippet rather than mutating a real provider package.

### Invariants And Boundaries

The tests protect the core provider invariant: managed provider artifacts belong under `ar-coordination/providers/`, not inside indexed source repositories.

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
| The layout test asserts that CGC uses `providers/codegraphcontext/<repo-id>`, `.codegraphcontext/db/kuzu`, `providers/_venvs/codegraphcontext`, and `providers/requirements/codegraphcontext.txt`. | L30-L61 | [test_context_providers.py](agents-remember-md/runtime/skills/U-01-core-skills/tests/test_context_providers.py) |
| The default-layout test asserts the pinned requirement, config, persisted `.env` exclusions, `.cgcignore`, logs, and run directories. | L63-L83 | [test_context_providers.py](agents-remember-md/runtime/skills/U-01-core-skills/tests/test_context_providers.py) |
| Source artifact, patch idempotence, patch rejection, repo id, and patch id tests cover the provider containment and patch helper edge cases. | L85-L120 | [test_context_providers.py](agents-remember-md/runtime/skills/U-01-core-skills/tests/test_context_providers.py) |

## Cross-Repo References

No sibling repository evidence is needed for these tests.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-20T19:11+02:00: Created onboarding for the provider layout and patch helper unit tests. Verification metadata remains pinned to the current committed source revision until closeout commits these source changes.
