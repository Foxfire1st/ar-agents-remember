# test_provider_lifecycle.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/tests/test_provider_lifecycle.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-10T06:20+02:00                     |
| lastVerifiedCommitHash | `6beccd0545a2d5c161059715d5ed7830917eba03` |
| lastVerifiedCommitDate | 2026-06-09T22:39:28+02:00|
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

The tests assert that `cgc visualize` accepts named `--port` and `--context` options after the subcommand, that shared lifecycle options can still appear before the subcommand, that CGC and aggregate watcher commands default their coordinator root to the installed runtime root, that process namespace diagnostics report `durableForDaemons`, and that daemon/server actions reject ephemeral `--die-with-parent` namespaces. Dry-run coverage verifies an explicit Dockerized long-running `cgc visualize --repo <repo> --port <port>` command against the `agents-remember/codegraphcontext:<pin>` runner image on the shared CGC Docker network. The generated runner patch script has a regression guard so replacements are embedded as Python data rather than `json.loads({...})`. The CGC migration-boundary tests require `cgc run -- visualize ...` to fail with guidance to use `cgc visualize`, and also protect that bounded `cgc run` queries are still allowed in an ephemeral process namespace when the command itself is mocked. The `test_run_allows_bounded_query_in_ephemeral_process_namespace` test now also stubs `cgc_query.cgc_backend_status` (saved/restored alongside `cgc_status`) because `cgc run` gates on backend readiness, not the watcher. GrepAI tests protect the Docker-only boundary: direct non-settings GrepAI `run` calls return unsupported instead of trying host binaries, settings-backed bounded GrepAI queries use `docker exec ar-grepai-watcher grepai ...` without host `_bin`, and GrepAI start dry-run includes managed Compose migration, the managed network, Postgres backend, Ollama embedder, runner image/container, container DSN, container project path, and container Ollama endpoint. CGC dry-run coverage also asserts project migration for the backend network and watcher containers. Docker readiness tests verify target-database checks after `pg_isready`, and aggregate watcher tests still cover partial-result recovery actions. Compose render coverage also asserts generated ownership labels, rejects missing `instance.labels`, and checks GrepAI container-local watcher `HOME`/XDG paths plus the optional POSIX UID/GID user block, and that each live memory root is bind-mounted read-write at `/grepai/roots/<project_id>` (the workspace-state `projectPaths` resolve there too). The parallel CGC refresh test also asserts each runner bind-mount target is a driveless POSIX container path rendered as `host:container:ro`.

New `no_cache` image-build cases assert that both the CGC and GrepAI runner
image builds insert the `--no-cache` flag in their dry-run command when
`no_cache=True`, and omit it otherwise.

Persistence-and-readiness coverage (2.5.0) asserts the rendered FalkorDB
volume binds the backend `dataDestination` (`/var/lib/falkordb/data` by
default, configurable) and the watcher entrypoint references
`cgc-watch-guard.py`; it also pins `cgc_graph_content_state` reply-text
classification (File-node count, auto-created empty key, `LOADING` reply,
connection failure — exit codes alone are not trusted) and the scan-marker
`indexing` probe over watcher container logs.

Current-state note: the optional POSIX UID/GID assertion in the GrepAI Compose
render test resolves `os.getuid` and `os.getgid` with `getattr()` and checks
both values are callable before asserting the rendered `user:` line. Windows
test runs therefore skip that POSIX-only assertion while POSIX runs still
protect the host-user YAML block.

F-04 service tests build a temporary lifecycle settings file and verify that
`providers.lifecycle_service` can run CGC and aggregate watcher dry-run/status
paths without going through the CLI `main(argv)` route. Those CGC settings
fixtures use Docker runner fields and generated ownership labels without
`venvRoot`.

### Conventions

The tests use temporary directories, dry-run/manual override arguments, and monkey-patched lifecycle functions, so they do not require CodeGraphContext, FalkorDB, GrepAI, or a configured coordinator. Docker-mode tests mock the `docker_command()` symbol the command builder actually consults — for settings-backed GrepAI runs that is `compose_runtime.docker_command` (the executable is resolved there via `compose_plan`/`run_compose`), not the re-exported `grepai_actions.docker_command`. Dry-run CGC command-shape tests require only Docker executable resolution and compare the executable as `Path(command[0]).stem.lower()` so they tolerate the Windows-resolved `docker.EXE`. The `cgc visualize --repo` expectation uses `to_container_path(repo.resolve())` because that argument is the in-container mount path (drive stripped on Windows), not the host path. They focus on command shape, argument defaults, small lifecycle decisions, and aggregation behavior, not live server startup.

### Invariants And Boundaries

The visualizer is a first-class long-running lifecycle command. It must not be hidden behind `cgc run`, because `run` is the bounded native-query escape hatch. Daemon/server policy must apply to `cgc visualize` and watcher management, but not to bounded `cgc run` queries. The installed provider lifecycle script should work without a repeated `--coordination-root` when invoked from its normal location. Settings-backed GrepAI must stay Docker-owned and must not regress to a host `_bin/grepai`, a PATH lookup, host-path watcher `HOME`, root-owned watcher artifacts, or an externally installed Ollama requirement. Direct non-Docker GrepAI calls must fail as unsupported. Docker command shape, target database readiness, full start dry-run shape, auto-port rendering, required provider ownership labels, project migration shape, and partial aggregation must remain explicit unit-test contracts.

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
| Process namespace tests assert that ephemeral daemon actions raise clear errors, namespace status reports `durableForDaemons: false`, `cgc visualize` rejects non-dry-run server launch from that namespace, and bounded `cgc run` queries remain allowed when provider execution is mocked; the bounded-run test stubs both `cgc_status` and `cgc_backend_status` (saved/restored in `originals`). | L157-L181; L183-L211; L270-L316 | [test_provider_lifecycle.py](agents-remember-md/mcp/tests/test_provider_lifecycle.py) |
| Handler tests assert that `cgc_visualize` dry-run emits an explicit Dockerized long-running server command and that `cgc_run` rejects `visualize`. | L213-L268 | [test_provider_lifecycle.py](agents-remember-md/mcp/tests/test_provider_lifecycle.py) |
| Docker-mode GrepAI tests assert that direct non-settings run calls are unsupported, settings-backed bounded queries use `docker exec ar-grepai-watcher grepai ...` without host `_bin`, and start dry-run builds the full migration/network/Postgres/Ollama/watcher stack with container workspace settings. | L221-L334 | [test_provider_lifecycle.py](agents-remember-md/mcp/tests/test_provider_lifecycle.py) |
| Compose render and CGC start-all tests assert `auto` ports do not leak into rendered YAML, provider ownership labels are required, the GrepAI watcher gets container-local config env plus a POSIX user block when available, and CGC project migration includes unmanaged network and watcher removal. | L387-L533 | [test_provider_lifecycle.py](agents-remember-md/mcp/tests/test_provider_lifecycle.py) |
| The optional POSIX user-block assertion uses `getattr()` plus `callable()` checks before reading `os.getuid` and `os.getgid`, so the test remains valid on Windows hosts. | L428-L434 | [test_provider_lifecycle.py](agents-remember-md/mcp/tests/test_provider_lifecycle.py) |
| GrepAI lifecycle tests assert that PostgreSQL readiness proceeds from `pg_isready` to a target database query and aggregate watcher results include partial state plus recovery actions. | L580-L700 | [test_provider_lifecycle.py](agents-remember-md/mcp/tests/test_provider_lifecycle.py) |

## Cross-Repo References

No sibling repository evidence is needed for these tests.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-06-10T06:20+02:00 — Body-quality pass: merged the 2.5.0 persistence-and-readiness coverage (dataDestination bind, watch-guard entrypoint, reply-text classification, scan-marker probe) into Logic (documentation only).
- 2026-06-09T22:10+02:00 — Compose render test now asserts the FalkorDB volume binds `/var/lib/falkordb/data` and the watcher entrypoint references `cgc-watch-guard.py`; added tests for configurable `dataDestination`, `cgc_graph_content_state` reply-text classification (count / empty-key / LOADING / connection failure), and the scan-marker `indexing` probe.
- 2026-06-06T17:27+02:00 — Updated after the optional POSIX UID/GID assertion switched to `getattr()` plus `callable()` checks so the provider lifecycle tests type-check cleanly on Windows.
- 2026-06-02T01:15+02:00 — Watch-live: the GrepAI workspace-state `projectPaths` assertion is now `/grepai/roots/<project_id>` (was `/grepai/runtime/index-roots/...`), and the Compose render test asserts each live memory root is bind-mounted read-write at `/grepai/roots/<project_id>`.
- 2026-06-01T23:40+02:00 — `test_run_allows_bounded_query_in_ephemeral_process_namespace` now stubs `cgc_query.cgc_backend_status` (saved/restored alongside `cgc_status`) because `cgc run` gates on backend readiness rather than the full provider status. Updated Logic and the process-namespace Repo-Internal References row.
- 2026-05-30T21:51+02:00: Documented the new CGC/GrepAI runner-image `no_cache` build cases (`--no-cache` present in the dry-run command when `no_cache=True`, absent otherwise). Verified against `8927f03`.
- 2026-05-29T08:53+02:00: Updated after Windows-host portability fixes: the
  Docker executable assertions compare `Path(command[0]).stem.lower()` (tolerating
  `docker.EXE`), the GrepAI docker-command mock moved to
  `compose_runtime.docker_command` (the symbol the command builder consults), and
  the `cgc visualize --repo` expectation switched to `to_container_path(...)`.
- 2026-05-29T07:19+02:00: Updated after the parallel CGC refresh test asserted
  driveless POSIX runner bind-mount targets (`host:container:ro`) for
  Windows-host support.
- 2026-05-28T14:21:08+02:00: Updated after provider lifecycle tests began
  asserting generated Compose ownership labels and rejection of unlabeled
  provider settings.
- 2026-05-28T13:40+02:00: Updated after CGC lifecycle service fixtures stopped carrying `venvRoot`.
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
