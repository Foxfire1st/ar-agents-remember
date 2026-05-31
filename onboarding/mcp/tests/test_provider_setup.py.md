# test_provider_setup.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/tests/test_provider_setup.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:50+02:00|
| lastVerifiedCommitHash | `c20a3292e667d227a3be0c1fb276f8a701df814f` |
| lastVerifiedCommitDate | 2026-05-31T14:17:11+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](../../../../../overview.md)

## Purpose

`test_provider_setup.py` verifies the package-local MCP provider setup helper used by benchmark and worktree preparation flows. It protects explicit provider settings requirements, the typed `ProviderSetupRequest` service entry point, CGC bundle path rewriting, and isolated worktree CGC settings so provider setup can seed or prepare context providers without mutating the main coordinator backend.

## Code Commentary

### Logic

The test module imports `agents_remember.providers.provider_setup` from
`mcp/src`. The explicit-settings tests assert that `settings_path()` rejects
missing provider settings (called as `settings_path(None)` with the single
settings-path argument, no separate root), the CLI parser requires
`--from-settings`, and
`run_provider_setup(ProviderSetupRequest)` accepts a side-effect-free typed
request with providers disabled. Provider setup reporting coverage asserts
dry-runs report unwritten summary paths, real runs write compact setup
summaries under `logs/providers/setup`, and recovered final watcher status is
reported separately from strict phase `ok`. CGC prepare fallback coverage
asserts that a missing seed source does not fail the whole prepare payload when
refresh fallback remains enabled and dry-run refresh is planned.

`test_rewrite_cgc_bundle_paths_rewrites_json_jsonl_and_text` builds a synthetic `.cgc` zip bundle containing JSON, JSONL, and text entries with source repository paths, runs `rewrite_cgc_bundle_paths`, then asserts that the rewritten bundle removes the source root and contains the target root.

`test_isolated_cgc_settings_targets_worktree_backend` builds a minimal provider
settings object and calls `isolated_cgc_settings`. It asserts that the isolated
settings point CGC roots at the target worktree repository, put CGC runtime and
FalkorDB data under the isolated provider runtime, write watcher logs under the
central workflow-local `logs/providers` tree, omit host `venvRoot` fields, and
derive isolated FalkorDB and runner container names. GrepAI isolated-settings
coverage also asserts that watch logs use `logs/providers/grepai/<instance>`
and that provider setup exposes isolated workflow settings only through the
canonical `isolatedProviderSettings` payload.
UTF-8 subprocess coverage monkey-patches `subprocess.run` and asserts `run_command` passes
`PYTHONUTF8=1`, `PYTHONIOENCODING=utf-8`, and `stdin=subprocess.DEVNULL` to
lifecycle children.

### Conventions

The tests use temporary directories and synthetic settings; they do not require Docker, FalkorDB, CGC, GrepAI, or network access. They call package-local helper and service functions directly. CLI coverage is limited to parser behavior for required settings, not lifecycle execution.

### Invariants And Boundaries

The tests protect provider setup boundaries: provider setup must not silently
fall back to coordinator `system/settings.json`, typed setup requests must work
without CLI round-tripping, setup summaries must make failed phases
diagnosable, CGC seed failure must not fail prepare when the existing refresh
fallback is enabled, seeded CGC bundles must not retain source checkout paths
after being adapted to a target worktree, worktree provider setup must isolate
runtime/data/log roots, and lifecycle subprocesses must run with UTF-8
environment overrides. These tests should stay side-effect free, should not
start provider watchers or containers, and must not reintroduce host executable
install fields into isolated provider settings.

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
| Explicit-settings coverage asserts missing provider settings are rejected, the parser requires `--from-settings`, and a typed `ProviderSetupRequest` can execute a disabled-provider dry run with setup summary metadata. | L20-L60 | [test_provider_setup.py](agents-remember-md/mcp/tests/test_provider_setup.py) |
| Setup reporting coverage asserts compact summary writes and recovered final status reporting while preserving strict failed-phase `ok=false`. | L62-L192 | [test_provider_setup.py](agents-remember-md/mcp/tests/test_provider_setup.py) |
| CGC prepare fallback coverage asserts a missing seed source still yields an overall successful dry-run payload when refresh fallback is enabled and `refresh-all` is planned. | L194-L235 | [test_provider_setup.py](agents-remember-md/mcp/tests/test_provider_setup.py) |
| The CGC bundle rewrite test builds JSON, JSONL, and text zip entries that contain a source path, calls `rewrite_cgc_bundle_paths`, then asserts the source path disappeared and the target path appears. | L102-L146 | [test_provider_setup.py](agents-remember-md/mcp/tests/test_provider_setup.py) |
| The isolated settings tests build synthetic CGC and GrepAI provider settings and assert target worktree roots, isolated runtime/data/log roots, no CGC `venvRoot` emission, canonical isolated setup payload shape, and derived container names. | L285-L626 | [test_provider_setup.py](agents-remember-md/mcp/tests/test_provider_setup.py) |
| The UTF-8 subprocess test monkey-patches `subprocess.run` and asserts `run_command` passes `PYTHONUTF8=1`, `PYTHONIOENCODING=utf-8`, and `stdin=subprocess.DEVNULL`. | L214-L237 | [test_provider_setup.py](agents-remember-md/mcp/tests/test_provider_setup.py) |
| Package-local provider setup owns the explicit settings check, typed setup request path, isolated CGC settings, command wrapper, and CGC bundle rewriting exercised by this test module. | L36-L127, L278-L407, L552-L633, L886-L894 | [provider_setup.py](agents-remember-md/mcp/src/agents_remember/providers/provider_setup.py) |

## Cross-Repo References

No sibling repository evidence is needed for these tests.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-31T12:50+02:00 — `test_settings_path_requires_explicit_provider_settings` now calls `provider_setup.settings_path(None)` (single settings-path arg) instead of `settings_path(root, None)` and drops its `TemporaryDirectory`, following `settings_path()` losing its leading `root` parameter; noted the single-arg call in Logic (1.0.0 review remediation).
- 2026-05-29T18:35+02:00: Replaced `assertIsNotNone` with `assert ... is not None` so the isolated-settings locals narrow before subscript; behavior-preserving (commit `0549b28`).
- 2026-05-28T14:21:08+02:00: Updated after provider setup tests asserted
  duplicate per-provider isolated settings payload keys are absent.
- 2026-05-28T13:40+02:00: Updated after provider setup tests removed CGC `venvRoot` from settings fixtures and isolated settings expectations.
- 2026-05-28T12:32+02:00: Updated after provider setup tests added setup summary reporting and central isolated provider log path assertions.
- 2026-05-24T05:48+02:00: Updated after provider setup tests added CGC seed failure plus refresh fallback coverage.
- 2026-05-24T00:04+02:00: Updated after provider setup tests added explicit settings requirements and typed `ProviderSetupRequest` service coverage.
- 2026-05-23T13:46+02:00: Updated after provider setup moved into `agents_remember.providers.provider_setup` and source scripts were removed.
- 2026-05-23T05:32+02:00: Updated after provider setup script tests switched from installed runtime scripts to top-level source/package-owned scripts.
- 2026-05-21T23:18+02:00: Updated after adding UTF-8 lifecycle child environment coverage.
- 2026-05-21T08:14+02:00: Created onboarding for provider setup unit tests and their isolated CGC settings coverage.
