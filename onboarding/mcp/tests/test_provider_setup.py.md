# test_provider_setup.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/tests/test_provider_setup.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-24T00:04+02:00                     |
| lastVerifiedCommitHash | `7a12e014c773612105fb91e897c94c9808a61527` |
| lastVerifiedCommitDate | 2026-05-23T23:56:58+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](../../../../../overview.md)

## Purpose

`test_provider_setup.py` verifies the package-local MCP provider setup helper used by benchmark and worktree preparation flows. It protects explicit provider settings requirements, the typed `ProviderSetupRequest` service entry point, CGC bundle path rewriting, and isolated worktree CGC settings so provider setup can seed or prepare context providers without mutating the main coordinator backend.

## Code Commentary

### Logic

The test module imports `agents_remember.providers.provider_setup` from `mcp/src`. The explicit-settings tests assert that `settings_path()` rejects missing provider settings, the CLI parser requires `--from-settings`, and `run_provider_setup(ProviderSetupRequest)` accepts a side-effect-free typed request with providers disabled.

`test_rewrite_cgc_bundle_paths_rewrites_json_jsonl_and_text` builds a synthetic `.cgc` zip bundle containing JSON, JSONL, and text entries with source repository paths, runs `rewrite_cgc_bundle_paths`, then asserts that the rewritten bundle removes the source root and contains the target root.

`test_isolated_cgc_settings_targets_worktree_backend` builds a minimal provider settings object and calls `isolated_cgc_settings`. It asserts that the isolated settings point CGC roots at the target worktree repository, put CGC runtime and FalkorDB data under the isolated provider runtime, reuse the coordinator's shared CGC venv, and derive an isolated FalkorDB container name. UTF-8 subprocess coverage monkey-patches `subprocess.run` and asserts `run_command` passes `PYTHONUTF8=1`, `PYTHONIOENCODING=utf-8`, and `stdin=subprocess.DEVNULL` to lifecycle children.

### Conventions

The tests use temporary directories and synthetic settings; they do not require Docker, FalkorDB, CGC, GrepAI, or network access. They call package-local helper and service functions directly. CLI coverage is limited to parser behavior for required settings, not lifecycle execution.

### Invariants And Boundaries

The tests protect five provider setup boundaries: provider setup must not silently fall back to coordinator `system/settings.json`, typed setup requests must work without CLI round-tripping, seeded CGC bundles must not retain source checkout paths after being adapted to a target worktree, worktree CGC setup must isolate runtime state plus backend data while reusing installed dependencies, and lifecycle subprocesses must run with UTF-8 environment overrides. These tests should stay side-effect free and should not start provider watchers or containers.

### Todos

- Add lifecycle fixture coverage only when there is a side-effect-free provider lifecycle fixture that does not require Docker or network access.

## Docs References

No external documentation is needed for these standard-library unit tests.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The test module imports package-local provider setup code from `mcp/src`, extending the loaded `agents_remember` package path when needed. | L12-L24 | [test_provider_setup.py](agents-remember-md/mcp/tests/test_provider_setup.py) |
| Explicit-settings coverage asserts missing provider settings are rejected, the parser requires `--from-settings`, and a typed `ProviderSetupRequest` can execute a disabled-provider dry run. | L20-L54 | [test_provider_setup.py](agents-remember-md/mcp/tests/test_provider_setup.py) |
| The CGC bundle rewrite test builds JSON, JSONL, and text zip entries that contain a source path, calls `rewrite_cgc_bundle_paths`, then asserts the source path disappeared and the target path appears. | L56-L100 | [test_provider_setup.py](agents-remember-md/mcp/tests/test_provider_setup.py) |
| The isolated settings test builds synthetic CGC provider settings and asserts the target worktree root, isolated runtime root, shared venv, isolated backend data root, and derived container name. | L102-L166 | [test_provider_setup.py](agents-remember-md/mcp/tests/test_provider_setup.py) |
| The UTF-8 subprocess test monkey-patches `subprocess.run` and asserts `run_command` passes `PYTHONUTF8=1`, `PYTHONIOENCODING=utf-8`, and `stdin=subprocess.DEVNULL`. | L168-L191 | [test_provider_setup.py](agents-remember-md/mcp/tests/test_provider_setup.py) |
| Package-local provider setup owns the explicit settings check, typed setup request path, isolated CGC settings, command wrapper, and CGC bundle rewriting exercised by this test module. | L36-L127, L278-L407, L552-L633, L886-L894 | [provider_setup.py](agents-remember-md/mcp/src/agents_remember/providers/provider_setup.py) |

## Cross-Repo References

No sibling repository evidence is needed for these tests.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-24T00:04+02:00: Updated after provider setup tests added explicit settings requirements and typed `ProviderSetupRequest` service coverage.
- 2026-05-23T13:46+02:00: Updated after provider setup moved into `agents_remember.providers.provider_setup` and source scripts were removed.
- 2026-05-23T05:32+02:00: Updated after provider setup script tests switched from installed runtime scripts to top-level source/package-owned scripts.
- 2026-05-21T23:18+02:00: Updated after adding UTF-8 lifecycle child environment coverage.
- 2026-05-21T08:14+02:00: Created onboarding for provider setup unit tests and their isolated CGC settings coverage.
