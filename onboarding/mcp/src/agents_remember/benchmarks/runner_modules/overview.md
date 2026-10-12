# mcp/src/agents_remember/benchmarks/runner_modules Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| sourceRoute            | `mcp/src/agents_remember/benchmarks/runner_modules` |

## Governing Overview

[overview.md](../../../../overview.md)

## Purpose

The `runner_modules` package contains the focused implementation modules behind the public `benchmarks/runner.py` facade. It separates benchmark manifest handling, workspace preparation, local MCP registration, Codex execution, JSONL analysis, service payloads, and CLI wiring so their owners are independently navigable. The facade re-exports these modules and retains a repository-preparation wrapper for its caller hooks.

## Hot Path Summary

- `models.py`, `constants.py`, and `manifest.py` define case data, supported provider identifiers, manifest path validation, case loading, and prompt/variant selection.
- `filesystem.py`, `commands.py`, and `workspace.py` prepare the source-only and with-memory workspaces: copy runtime assets, remove old paths, render instructions, prepare pinned Git checkouts and the memory repository, then write registration and invoke provider setup.
- `mcp_registration.py` writes benchmark-local MCP settings and Codex configuration. Its runtime configuration helper constructs benchmark-scoped provider paths under `providers/runners` and `logs/providers`, with MCP transcripts under `logs/mcp`. Its lifecycle-settings helper takes no workspace argument and delegates to the shared generator, which emits `contextProviders.enabled=false` and an empty provider map. The setup call therefore does not establish the former promise that every benchmark builds provider indexes.
- `execution.py` resolves Codex from PATH, validates sandbox selection, constructs the command, records run metadata, schedules prompt/variant/repetition tasks, and writes summaries. It reads the workspace's Codex MCP configuration into command overrides so the run can use that workspace's configured server.
- `analysis.py` extracts JSONL event counts, command counts, turn token usage, final answers and errors, combines them with run metadata, and renders summaries. `services.py` returns prepare/run payloads; `cli.py` calls those services and exposes list, prepare, run and analyze commands. `roots.py` selects an explicit benchmark root or the packaged benchmark cases.

## Construction

Five frozen value objects describe the runner's preparation and execution flow: `BenchmarkWorkspace`, `BenchmarkTask`, `BenchmarkRun`, `BenchmarkPreparation`, and `BenchmarkRunOutcome`. Both service request types project their preparation fields into `BenchmarkPreparation`, including `allowed_provider_ids`. Prepare passes that object to case preparation; run passes it through execution's preparation step unless preparation is skipped.

Case preparation filters requested provider identifiers before constructing the workspace object used for registration and provider setup. Registration persists the filtered identifiers with benchmark scope and instance identity. Provider setup skips an empty selection; otherwise it receives a temporary document from the disabled, empty lifecycle-settings generator. The request wires no seed source, retains its explicit CGC refresh option, and removes the temporary document in a `finally` block.

The prepare service sweeps persisted registrations before preparing selected cases. The run service sweeps them before executing selected cases. CLI requests do not supply an authority set, so they reach the filtering and sweep functions with `allowed_provider_ids=None`.

Runner runtime-configuration imports come from `kernel/primitives/runtime_config.py`. Git preparation delegates to `kernel/git_command.py`; `commands.py` owns dry-run reporting and failure reporting rather than subprocess construction.

## Invariants and Boundaries

Manifest provider selection is not launch authority. An explicit authority set retains only matching identifiers and reports skipped identifiers. With no authority set, filtering returns no providers unless `AR_BENCHMARK_ALLOW_UNFILTERED_PROVIDERS=1` is explicitly set. This filtering boundary does not override the shared lifecycle generator's disabled provider settings.

The registration sweep narrows provider maps in matching persisted benchmark settings and reports each changed file. It leaves them untouched when the authority set is `None` and makes no change when their identifiers already fit the supplied set. Both services invoke the sweep independently of their preparation/execution dry-run behavior.

Benchmark Git preparation uses the shared runner, which strips `GIT_DIR`, `GIT_WORK_TREE`, `GIT_INDEX_FILE`, `GIT_OBJECT_DIRECTORY`, `GIT_ALTERNATE_OBJECT_DIRECTORIES`, `GIT_COMMON_DIR`, `GIT_NAMESPACE`, and `GIT_PREFIX`. It captures stdout/stderr and supplies `DEVNULL` as stdin when no input is provided, keeping these Git subprocesses off the parent's protocol streams. A nonzero preparation command raises with at most the last 2,000 characters of its selected output. Clone and fetch use the bulk remote timeout; repository reuse is checked through the metadata timeout. Repository preparation checks out the pinned commit, resets it, and cleans untracked files in the benchmark checkout.

Local MCP registration requires the source repository directory name to match the repository identifier and the memory repository to be at `coordinationRoot/memory-repos/ar-<repoId>`.

The retained GrepAI clone and CGC seed resolvers skip a benchmark-scoped target before starting a source backend. These are conditional protections in the retained seed implementation; they do not establish a current index-build promise for this runner's disabled lifecycle settings.

Benchmark cases can clone external repositories, but the implementation owners described here are local to `agents-remember`.

## Authority Bounds

The retained service implementations and CLI callers establish the local call flow described here. The inherited reference numbered 2 targets runtime skill installation, which does not call benchmark services; it cannot substantiate the former MCP benchmark-caller claim. Current MCP exposure is not established by that reference.

Lifecycle, landing and acceptance authority are outside this source account. Their current status is a named uncertainty: this inspection supplies no test execution, native-host execution, whole-build result, landing result or memory acceptance.

## Evidence

- The facade re-exports runner modules and retains its repository-preparation wrapper. [1]
- The inherited targets implement runtime skill installation, not benchmark service calls. [2]
- Retained seed options and resolver predicates preserve the benchmark-scoped no-seeding boundary. [3]
- Case models, manifest validation, selection, shared preparation and workspace construction. [4]
- Benchmark registration, registration sweep and disabled lifecycle-settings construction. [5]
- Git preparation delegates to the shared environment, argv and subprocess owner. [6]
- Codex execution, analysis, service payloads and direct CLI callers. [7]
