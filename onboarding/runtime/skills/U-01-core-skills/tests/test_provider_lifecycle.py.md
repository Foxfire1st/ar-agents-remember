# test_provider_lifecycle.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `runtime/skills/U-01-core-skills/tests/test_provider_lifecycle.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-21T17:16+02:00                     |
| lastVerifiedCommitHash | `5ff4ed4ef94b5576a45059de8ac7c03e8c4c04a1` |
| lastVerifiedCommitDate | 2026-05-21T18:12:00+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](../../../../../overview.md)

## Purpose

`test_provider_lifecycle.py` verifies provider lifecycle parser behavior, process-namespace policy, and small command-output helpers that cannot be safely inferred from the generic provider-layout tests.

## Code Commentary

### Logic

The test module imports `runtime/scripts/provider-lifecycle.py` through `importlib.util` so it can exercise the script parser, render helpers, and handler functions directly. Render tests protect native CGC output streaming, the compact `run --lifecycle-json` payload path, and non-command result handling. `parse_cgc` builds the parser, parses a `cgc` command, normalizes CGC defaults, resolves paths, and stabilizes repo ids in the same shape the script uses before dispatch.

The tests assert that `cgc visualize` accepts named `--port` and `--context` options after the subcommand, that shared lifecycle options can still appear before the subcommand, that CGC and aggregate watcher commands default their coordinator root to the installed runtime root, that process namespace diagnostics report `durableForDaemons`, and that daemon/server actions reject ephemeral `--die-with-parent` namespaces. Dry-run coverage verifies an explicit long-running `cgc visualize --repo <repo> --port <port>` command. The CGC migration-boundary tests require `cgc run -- visualize ...` to fail with guidance to use `cgc visualize`, and also protect that bounded `cgc run` queries are still allowed in an ephemeral process namespace when the command itself is mocked. The GrepAI parser test protects the lifecycle contract that native `watch --background` output such as `PID 705881` is captured into managed state, while unrelated status text returns no PID.

### Conventions

The tests use temporary directories, dry-run/manual override arguments, and parser-only assertions, so they do not require CodeGraphContext, Docker, FalkorDB, GrepAI, or a configured coordinator. They focus on command shape and argument defaults, not live server startup.

### Invariants And Boundaries

The visualizer is a first-class long-running lifecycle command. It must not be hidden behind `cgc run`, because `run` is the bounded native-query escape hatch. Daemon/server policy must apply to `cgc visualize` and watcher management, but not to bounded `cgc run` queries. The installed provider lifecycle script should work without a repeated `--coordination-root` when invoked from its normal location. GrepAI managed status depends on the recorded watcher PID, so the start-output parser must only return a PID when GrepAI reports a concrete background process.

### Todos

None.

## Docs References

No external documentation is needed for these unit tests.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The module loads `provider-lifecycle.py` directly, and `parse_cgc` normalizes parsed CGC args the way the script's main path does. | L12-L18; L81-L91 | [test_provider_lifecycle.py](agents-remember-md/runtime/skills/U-01-core-skills/tests/test_provider_lifecycle.py) |
| Render tests assert that captured command output is streamed without wrapper text, successful `cgc run --json` still emits native output, and `run --lifecycle-json -- ...` preserves an explicit metadata path. | L21-L79 | [test_provider_lifecycle.py](agents-remember-md/runtime/skills/U-01-core-skills/tests/test_provider_lifecycle.py) |
| Parser tests assert that `visualize` accepts named options after the subcommand and still allows common lifecycle options before the subcommand. | L93-L129 | [test_provider_lifecycle.py](agents-remember-md/runtime/skills/U-01-core-skills/tests/test_provider_lifecycle.py) |
| Default-root parser tests assert that CGC and aggregate watcher commands infer the installed runtime root when `--coordination-root` is omitted. | L140-L155 | [test_provider_lifecycle.py](agents-remember-md/runtime/skills/U-01-core-skills/tests/test_provider_lifecycle.py) |
| Process namespace tests assert that ephemeral daemon actions raise clear errors, namespace status reports `durableForDaemons: false`, `cgc visualize` rejects non-dry-run server launch from that namespace, and bounded `cgc run` queries remain allowed when provider execution is mocked. | L157-L181; L183-L211; L270-L316 | [test_provider_lifecycle.py](agents-remember-md/runtime/skills/U-01-core-skills/tests/test_provider_lifecycle.py) |
| Handler tests assert that `cgc_visualize` dry-run emits an explicit long-running server command and that `cgc_run` rejects `visualize`. | L213-L268 | [test_provider_lifecycle.py](agents-remember-md/runtime/skills/U-01-core-skills/tests/test_provider_lifecycle.py) |
| The GrepAI parser test asserts that native watcher output with `PID <number>` returns that integer and unrelated status text returns no PID. | L318-L327 | [test_provider_lifecycle.py](agents-remember-md/runtime/skills/U-01-core-skills/tests/test_provider_lifecycle.py) |

## Cross-Repo References

No sibling repository evidence is needed for these tests.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-21T17:16+02:00: Updated after adding process namespace diagnostics/guard coverage and protecting that bounded `cgc run` queries are not blocked by the daemon namespace policy.
- 2026-05-21T15:42+02:00: Updated after adding parser coverage for defaulting `--coordination-root` to the installed runtime root.
- 2026-05-21T13:04+02:00: Updated after adding GrepAI native background watcher PID parsing coverage.
- 2026-05-21T12:40+02:00: Created onboarding for CGC visualizer lifecycle parser tests.
