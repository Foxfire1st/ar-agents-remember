# test_provider_setup.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `runtime/skills/U-01-core-skills/tests/test_provider_setup.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-21T08:14+02:00                     |
| lastVerifiedCommitHash |                                            `0462de46a1da1bf1997e3979f4cc5bc53d1132f6`|
| lastVerifiedCommitDate |                                            2026-05-21T08:30:44+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](../../../../../overview.md)

## Purpose

`test_provider_setup.py` verifies the shared provider setup helper used by installer, benchmark, and worktree preparation flows. It protects CGC bundle path rewriting and isolated worktree CGC settings so provider setup can seed or prepare context providers without mutating the main coordinator backend.

## Code Commentary

### Logic

The test module imports `runtime/scripts/provider-setup.py` directly with `importlib.util.spec_from_file_location`, because the script filename contains a hyphen and is not importable as a normal Python module. `test_rewrite_cgc_bundle_paths_rewrites_json_jsonl_and_text` builds a synthetic `.cgc` zip bundle containing JSON, JSONL, and text entries with source repository paths, runs `rewrite_cgc_bundle_paths`, then asserts that the rewritten bundle removes the source root and contains the target root.

`test_isolated_cgc_settings_targets_worktree_backend` builds a minimal provider settings object and calls `isolated_cgc_settings`. It asserts that the isolated settings point CGC roots at the target worktree repository, put CGC runtime and FalkorDB data under the isolated provider runtime, reuse the coordinator's shared CGC venv, and derive an isolated FalkorDB container name.

### Conventions

The tests use temporary directories and synthetic settings; they do not require Docker, FalkorDB, CGC, GrepAI, or network access. The test imports the script under the module name `provider_setup` and calls helper functions directly rather than shelling out through the CLI.

### Invariants And Boundaries

The tests protect two provider setup boundaries: seeded CGC bundles must not retain source checkout paths after being adapted to a target worktree, and worktree CGC setup must isolate runtime state plus backend data while reusing installed dependencies. These tests should stay side-effect free and should not start provider watchers or containers.

### Todos

- Add CLI-level provider setup smoke coverage once a local test fixture can run lifecycle commands without Docker or network dependency.

## Docs References

No external documentation is needed for these standard-library unit tests.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The test module imports `runtime/scripts/provider-setup.py` directly using `importlib.util.spec_from_file_location` and executes the loaded module before defining test cases. | L12-L21 | [test_provider_setup.py](agents-remember-md/runtime/skills/U-01-core-skills/tests/test_provider_setup.py) |
| The CGC bundle rewrite test builds JSON, JSONL, and text zip entries that contain a source path, calls `rewrite_cgc_bundle_paths`, then asserts the source path disappeared and the target path appears. | L22-L54 | [test_provider_setup.py](agents-remember-md/runtime/skills/U-01-core-skills/tests/test_provider_setup.py) |
| The isolated settings test builds synthetic CGC provider settings and asserts the target worktree root, isolated runtime root, shared venv, isolated backend data root, and derived container name. | L56-L109 | [test_provider_setup.py](agents-remember-md/runtime/skills/U-01-core-skills/tests/test_provider_setup.py) |
| `provider-setup.py` owns `isolated_cgc_settings` and `rewrite_cgc_bundle_paths`, the two helpers exercised by this test module. | L119-L172, L359-L534 | [provider-setup.py](agents-remember-md/runtime/scripts/provider-setup.py) |

## Cross-Repo References

No sibling repository evidence is needed for these tests.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-21T08:14+02:00: Created onboarding for provider setup unit tests and their isolated CGC settings coverage.
