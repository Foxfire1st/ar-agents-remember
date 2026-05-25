# test_provider_lifecycle.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/tests/test_provider_lifecycle.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T15:12+02:00                     |
| lastVerifiedCommitHash | `a8ee8440dfa920d1153a4bb4bb43cc77534c3c90` |
| lastVerifiedCommitDate | 2026-05-25T15:22:52+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](../../../../../overview.md)

## Purpose

`test_provider_lifecycle.py` verifies provider lifecycle parser behavior, process-namespace policy, and small command-output helpers that cannot be safely inferred from the generic provider-layout tests.

## Code Commentary

### Logic

The test module imports `agents_remember.providers.provider_lifecycle` from `mcp/src`. Render tests protect native CGC output streaming, the compact `run --lifecycle-json` payload path, and non-command result handling. `parse_cgc` builds the parser, parses a `cgc` command, normalizes CGC defaults, resolves paths, and stabilizes repo ids in the same shape the lifecycle module uses before dispatch.

The tests assert that `cgc visualize` accepts named `--port` and `--context` options after the subcommand, that shared lifecycle options can still appear before the subcommand, that CGC and aggregate watcher commands default their coordinator root to the installed runtime root, that process namespace diagnostics report `durableForDaemons`, and that daemon/server actions reject ephemeral `--die-with-parent` namespaces. Dry-run coverage verifies an explicit long-running `cgc visualize --repo <repo> --port <port>` command. The CGC migration-boundary tests require `cgc run -- visualize ...` to fail with guidance to use `cgc visualize`, and also protect that bounded `cgc run` queries are still allowed in an ephemeral process namespace when the command itself is mocked. GrepAI tests protect native `watch --background` PID parsing, lifecycle-managed `grepai run -- search ...` command shape/env, rejection of native watcher control through `grepai run`, target-database readiness checks after `pg_isready`, adoption of already-running watchers, managed log-dir status probing, detached launcher startup that is left running when not ready, failed launcher reporting when no watcher appears, and aggregate watcher partial-result recovery actions.

F-04 service tests build a temporary lifecycle settings file and verify that
`providers.lifecycle_service` can run CGC and aggregate watcher dry-run/status
paths without going through the CLI `main(argv)` route.

### Conventions

The tests use temporary directories, dry-run/manual override arguments, and monkey-patched lifecycle functions, so they do not require CodeGraphContext, Docker, FalkorDB, GrepAI, or a configured coordinator. They focus on command shape, argument defaults, small lifecycle decisions, and aggregation behavior, not live server startup.

### Invariants And Boundaries

The visualizer is a first-class long-running lifecycle command. It must not be hidden behind `cgc run`, because `run` is the bounded native-query escape hatch. Daemon/server policy must apply to `cgc visualize` and watcher management, but not to bounded `cgc run` queries. The installed provider lifecycle script should work without a repeated `--coordination-root` when invoked from its normal location. GrepAI managed status depends on recorded watcher state, managed log-dir status commands, detached startup state, and target database readiness, so PID parsing, adoption, non-killing startup behavior, timeout reporting, and partial aggregation must remain explicit unit-test contracts.

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
| The module imports package-local provider lifecycle code from `mcp/src` and `parse_cgc` normalizes parsed CGC args the way the lifecycle main path does. | L12-L24; L81-L91 | [test_provider_lifecycle.py](agents-remember-md/mcp/tests/test_provider_lifecycle.py) |
| Service tests verify the typed lifecycle service can dispatch CGC and watcher operations from settings-owned config. | L112-L274 | [test_provider_lifecycle.py](agents-remember-md/mcp/tests/test_provider_lifecycle.py) |
| Render tests assert that captured command output is streamed without wrapper text, successful `cgc run --json` still emits native output, and `run --lifecycle-json -- ...` preserves an explicit metadata path. | L21-L79 | [test_provider_lifecycle.py](agents-remember-md/mcp/tests/test_provider_lifecycle.py) |
| Parser tests assert that `visualize` accepts named options after the subcommand and still allows common lifecycle options before the subcommand. | L93-L129 | [test_provider_lifecycle.py](agents-remember-md/mcp/tests/test_provider_lifecycle.py) |
| Default-root parser tests assert that CGC and aggregate watcher commands infer the installed runtime root when `--coordination-root` is omitted. | L140-L155 | [test_provider_lifecycle.py](agents-remember-md/mcp/tests/test_provider_lifecycle.py) |
| Process namespace tests assert that ephemeral daemon actions raise clear errors, namespace status reports `durableForDaemons: false`, `cgc visualize` rejects non-dry-run server launch from that namespace, and bounded `cgc run` queries remain allowed when provider execution is mocked. | L157-L181; L183-L211; L270-L316 | [test_provider_lifecycle.py](agents-remember-md/mcp/tests/test_provider_lifecycle.py) |
| Handler tests assert that `cgc_visualize` dry-run emits an explicit long-running server command and that `cgc_run` rejects `visualize`. | L213-L268 | [test_provider_lifecycle.py](agents-remember-md/mcp/tests/test_provider_lifecycle.py) |
| The GrepAI parser test asserts that native watcher output with `PID <number>` returns that integer and unrelated status text returns no PID. | L484-L493 | [test_provider_lifecycle.py](agents-remember-md/mcp/tests/test_provider_lifecycle.py) |
| GrepAI lifecycle tests assert that managed status probes include `--log-dir`, `grepai run -- search ...` uses managed workspace env, native watcher control is rejected from bounded run, PostgreSQL readiness proceeds from `pg_isready` to a target database query, already-running watchers are adopted without a new start command, detached starts can adopt a running watcher, startup can be reported pending without killing the launcher, failed launcher exits report recovery, and aggregate watcher results include partial state plus recovery actions. | L495-L850 | [test_provider_lifecycle.py](agents-remember-md/mcp/tests/test_provider_lifecycle.py) |

## Cross-Repo References

No sibling repository evidence is needed for these tests.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-25T15:12+02:00: Updated after GrepAI lifecycle tests switched from timeout-shaped `run_command` startup to detached `Popen` startup, added managed `--log-dir` probe coverage, and protected pending startup without killing the launcher.
- 2026-05-23T20:56+02:00: Updated after adding typed provider lifecycle service tests for F-04.
- 2026-05-23T13:46+02:00: Updated after provider lifecycle moved into `agents_remember.providers.provider_lifecycle` and source scripts were removed.
- 2026-05-23T05:32+02:00: Updated after provider lifecycle script tests switched from installed runtime scripts to top-level source/package-owned scripts.
- 2026-05-21T23:55+02:00: Updated after adding GrepAI `run -- search` command-shape coverage and native watcher-control rejection.
- 2026-05-21T23:18+02:00: Updated after adding tests for GrepAI target-database readiness, already-running watcher adoption, timeout-shaped watcher starts, and aggregate partial recovery actions.
- 2026-05-21T17:16+02:00: Updated after adding process namespace diagnostics/guard coverage and protecting that bounded `cgc run` queries are not blocked by the daemon namespace policy.
- 2026-05-21T15:42+02:00: Updated after adding parser coverage for defaulting `--coordination-root` to the installed runtime root.
- 2026-05-21T13:04+02:00: Updated after adding GrepAI native background watcher PID parsing coverage.
- 2026-05-21T12:40+02:00: Created onboarding for CGC visualizer lifecycle parser tests.
