# test_provider_lifecycle.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/tests/test_provider_lifecycle.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-27T00:41+02:00                     |
| lastVerifiedCommitHash | `767790a0a90c9cdc97eb3e291d42622aced82a14` |
| lastVerifiedCommitDate | 2026-05-27T01:14:04+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](../../../../../overview.md)

## Purpose

`test_provider_lifecycle.py` verifies provider lifecycle parser behavior,
process-namespace policy, provider-owned lifecycle modules, and small
command-output helpers that cannot be safely inferred from the generic
provider-layout tests.

## Code Commentary

### Logic

The test module imports `agents_remember.providers.lifecycle` from `mcp/src`,
then imports CGC, GrepAI, watcher, and process-status modules from the
provider-first package layout. Render tests protect native CGC output
streaming, the compact `run --lifecycle-json` payload path, and non-command
result handling. They also protect Compose auto-port rendering so configured
`auto` ports become valid empty published-port syntax. `parse_cgc` builds the
parser, parses a `cgc` command, normalizes CGC defaults, resolves paths, and
stabilizes repo ids in the same shape the lifecycle module uses before
dispatch.

The tests assert that `cgc visualize` accepts named `--port` and `--context` options after the subcommand, that shared lifecycle options can still appear before the subcommand, that CGC and aggregate watcher commands default their coordinator root to the installed runtime root, that process namespace diagnostics report `durableForDaemons`, and that daemon/server actions reject ephemeral `--die-with-parent` namespaces. Dry-run coverage verifies an explicit Dockerized long-running `cgc visualize --repo <repo> --port <port>` command against the `agents-remember/codegraphcontext:<pin>` runner image on the shared CGC Docker network. The generated runner patch script has a regression guard so replacements are embedded as Python data rather than `json.loads({...})`. The CGC migration-boundary tests require `cgc run -- visualize ...` to fail with guidance to use `cgc visualize`, and also protect that bounded `cgc run` queries are still allowed in an ephemeral process namespace when the command itself is mocked. GrepAI tests protect the Docker-only boundary: direct non-settings GrepAI `run` calls return unsupported instead of trying host binaries, settings-backed bounded GrepAI queries use `docker exec ar-grepai-watcher grepai ...` without host `_bin`, and GrepAI start dry-run includes managed Compose migration, the managed network, Postgres backend, Ollama embedder, runner image/container, container DSN, container project path, and container Ollama endpoint. CGC dry-run coverage also asserts project migration for the backend network and watcher containers. Docker readiness tests verify target-database checks after `pg_isready`, and aggregate watcher tests still cover partial-result recovery actions. GrepAI Compose render coverage also asserts container-local watcher `HOME`/XDG paths and the optional POSIX UID/GID user block, preventing regression to host-path config lookup or root-owned generated artifacts.

F-04 service tests build a temporary lifecycle settings file and verify that
`providers.lifecycle_service` can run CGC and aggregate watcher dry-run/status
paths without going through the CLI `main(argv)` route.

### Conventions

The tests use temporary directories, dry-run/manual override arguments, and monkey-patched lifecycle functions, so they do not require CodeGraphContext, FalkorDB, GrepAI, or a configured coordinator. Docker-mode tests mock `docker_command()` where needed; dry-run CGC command-shape tests require only Docker executable resolution. They focus on command shape, argument defaults, small lifecycle decisions, and aggregation behavior, not live server startup.

### Invariants And Boundaries

The visualizer is a first-class long-running lifecycle command. It must not be hidden behind `cgc run`, because `run` is the bounded native-query escape hatch. Daemon/server policy must apply to `cgc visualize` and watcher management, but not to bounded `cgc run` queries. The installed provider lifecycle script should work without a repeated `--coordination-root` when invoked from its normal location. Settings-backed GrepAI must stay Docker-owned and must not regress to a host `_bin/grepai`, a PATH lookup, host-path watcher `HOME`, root-owned watcher artifacts, or an externally installed Ollama requirement. Direct non-Docker GrepAI calls must fail as unsupported. Docker command shape, target database readiness, full start dry-run shape, auto-port rendering, project migration shape, and partial aggregation must remain explicit unit-test contracts.

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
| Service tests verify the typed lifecycle service can dispatch CGC, GrepAI, and watcher operations from settings-owned config. | L112-L164; L267-L285; L344-L361 | [test_provider_lifecycle.py](agents-remember-md/mcp/tests/test_provider_lifecycle.py) |
| Render tests assert that captured command output is streamed without wrapper text, successful `cgc run --json` still emits native output, `run --lifecycle-json -- ...` preserves an explicit metadata path, and Compose `auto` ports render as empty published ports. | L21-L97 | [test_provider_lifecycle.py](agents-remember-md/mcp/tests/test_provider_lifecycle.py) |
| Parser tests assert that `visualize` accepts named options after the subcommand and still allows common lifecycle options before the subcommand. | L93-L129 | [test_provider_lifecycle.py](agents-remember-md/mcp/tests/test_provider_lifecycle.py) |
| Default-root parser tests assert that CGC and aggregate watcher commands infer the installed runtime root when `--coordination-root` is omitted. | L140-L155 | [test_provider_lifecycle.py](agents-remember-md/mcp/tests/test_provider_lifecycle.py) |
| Process namespace tests assert that ephemeral daemon actions raise clear errors, namespace status reports `durableForDaemons: false`, `cgc visualize` rejects non-dry-run server launch from that namespace, and bounded `cgc run` queries remain allowed when provider execution is mocked. | L157-L181; L183-L211; L270-L316 | [test_provider_lifecycle.py](agents-remember-md/mcp/tests/test_provider_lifecycle.py) |
| Handler tests assert that `cgc_visualize` dry-run emits an explicit Dockerized long-running server command and that `cgc_run` rejects `visualize`. | L213-L268 | [test_provider_lifecycle.py](agents-remember-md/mcp/tests/test_provider_lifecycle.py) |
| Docker-mode GrepAI tests assert that direct non-settings run calls are unsupported, settings-backed bounded queries use `docker exec ar-grepai-watcher grepai ...` without host `_bin`, and start dry-run builds the full migration/network/Postgres/Ollama/watcher stack with container workspace settings. | L221-L334 | [test_provider_lifecycle.py](agents-remember-md/mcp/tests/test_provider_lifecycle.py) |
| Compose render and CGC start-all tests assert `auto` ports do not leak into rendered YAML, the GrepAI watcher gets container-local config env plus a POSIX user block when available, and CGC project migration includes unmanaged network and watcher removal. | L353-L445 | [test_provider_lifecycle.py](agents-remember-md/mcp/tests/test_provider_lifecycle.py) |
| GrepAI lifecycle tests assert that PostgreSQL readiness proceeds from `pg_isready` to a target database query and aggregate watcher results include partial state plus recovery actions. | L580-L700 | [test_provider_lifecycle.py](agents-remember-md/mcp/tests/test_provider_lifecycle.py) |

## Cross-Repo References

No sibling repository evidence is needed for these tests.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-27T00:41+02:00: Updated after GrepAI Compose render tests started
  guarding watcher container env paths and POSIX UID/GID execution.
- 2026-05-27T00:25+02:00: Updated after provider lifecycle tests added
  Compose `auto` port rendering and project migration coverage.
- 2026-05-26T13:58+02:00: Updated after CGC lifecycle tests asserted Docker-network visualizer commands and guarded the generated runner patch script shape.
- 2026-05-26T12:51+02:00: Updated after CGC dry-run visualizer tests switched from host `cgc` commands to Docker runner commands.
- 2026-05-25T21:14+02:00: Updated after tests switched imports to provider-first lifecycle packages and the split `process_status` helper module.
- 2026-05-25T19:16+02:00: Updated after tests imported `agents_remember.providers.lifecycle` directly and the `provider_lifecycle.py` compatibility module was removed.
- 2026-05-25T18:07+02:00: Updated after native GrepAI fallback tests were removed and direct non-settings GrepAI calls became unsupported.
- 2026-05-25T17:40+02:00: Updated after Docker-mode GrepAI tests asserted settings-backed `docker exec` bounded runs and complete start dry-run stack generation.
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
