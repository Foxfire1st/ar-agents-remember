# tools.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/system/defaults/examples/coordinator/tools.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-02T01:15+02:00                     |
| lastVerifiedCommitHash |                                            `53b17f574a53ae400f8abb9fda264fa9fa3e8dff`|
| lastVerifiedCommitDate |                                            2026-06-02T16:24:22+02:00|
| governingOverview      | `../../../../../../../../overview.md`                              |

## Governing Overview

[overview.md](../../../../../../../../overview.md)

## Purpose

This example documents the coordinator-level tools surface, including the shared provider setup entrypoint and expected lifecycle command shapes for configured context providers.

## Code Commentary

### Logic

The file says coordinator tools are commands useful across many repositories.
Repo-specific checks, branch workflow, and code quality tools belong in
memory-layer `system/tools.md`. When MCP `contextProviders` are enabled,
runtime installation is exposed through the `runtime_install` MCP tool and
lower-level provider diagnostics use explicit generated settings with
`--from-settings`. GrepAI search is documented through the `grepai_search` MCP tool
tool rather than a host binary, global command, or path filter. CGC commands
expand configured roots into per-repo runtime
instances under `providers/runners/codegraphcontext`, ensure the shared FalkorDB
Docker backend is healthy, start or stop one watcher per configured code repo,
run bounded native relationship queries through `cgc ... run -- <native cgc
args>`, and launch the long-running visualizer through `cgc ... visualize --port
<port>`. The provider notes distinguish long-running daemon/server actions from
bounded query actions: watcher starts/stops, CGC start/stop/visualize, and
GrepAI watcher start/stop/refresh must run from a durable host process
namespace, while lifecycle status reports `processNamespace` diagnostics.
Benchmark/worktree setup remains settings-gated and may use package-local
provider setup for CGC seed export/import with path rewrite before fallback
refresh.

### Conventions

Global commands stay here; repository-specific command details and code quality
tools stay in the selected memory layer. Setup flows should use the MCP
`runtime_install` tool for installation; direct `provider-lifecycle.py` calls
are lower-level provider diagnostics and operations. GrepAI lifecycle commands
read the `grepai-memory` settings, expand workspace roots into explicit
projects, ensure the shared Docker network plus PostgreSQL/pgvector and Ollama
containers are healthy, watch the live memory roots in place (read-write
bind-mounted into the watcher), and write GrepAI workspace config under
`providers/runners/grepai/home/.grepai/workspace.yaml`. The GrepAI
binary lives in the Docker runner container, not under `providers/_bin`.
CGC/FalkorDB runtime env
keys are process env only; for CGC v0.4.10 they should not be written into
`<instanceRoot>/.codegraphcontext/.env`. Use `start` or `start-all` to start
every configured watcher and `stop`, `stop-all`, or `shutdown-all` to stop every
configured watcher; single-repo CGC operations add `--repo-id`. Use `cgc
visualize --port <port>` for the visualizer server instead of hiding it behind
`cgc run`. Use `watchers status`/provider status to inspect `processNamespace`
before starting daemons from automation or sandbox-like harnesses.

### Invariants And Boundaries

Agents should resolve the target repository with `c-08-ar-coordination-context-resolver` skill before choosing task, worktree, memory, validation paths, or context provider roots. Provider output is discovery evidence only, and source/onboarding proof remains required. Managed mode should fail containment/health checks if CGC writes `.cgcignore`, `.codegraphcontext`, reports, databases, or logs inside indexed source code repositories. GrepAI indexes the live memory roots in place, so its `.grepai/` working dir is expected inside each memory root and is kept out of git via the root's `.gitignore` (it must still not land in indexed source code repositories). Daemon/server lifecycle actions must be launched from a durable host process namespace; bounded retrieval commands like `cgc run` remain usable from sandboxed harnesses.

### Todos

None.

## Docs References

No external documentation is needed.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The coordinator tools example separates global commands from repository-specific checks, branch workflow, and code quality tools. | `# Coordinator Tools Example` | mcp/src/agents_remember/package_data/runtime/system/defaults/examples/coordinator/tools.md:1-91 |
| The provider command section records MCP runtime install, `grepai_search`, aggregate provider status/watcher flows, and CGC bounded `run -- ...` plus long-running `visualize --port 8000` command shapes. | "Expected provider setup and lifecycle command shapes" | mcp/src/agents_remember/package_data/runtime/system/defaults/examples/coordinator/tools.md:22-22 |
| The provider notes say GrepAI lifecycle commands expand `grepai-memory` workspace roots, ensure Docker network/PostgreSQL/Ollama health, bind-mount and index the live memory roots in place, write provider-owned workspace config/state, and use the Docker runner container instead of host binaries; CGC lifecycle commands expand the configured `roots` array, ensure FalkorDB Docker, start/stop every configured root unless `--repo-id` narrows it, pass post-`--` arguments to native CGC for bounded queries, and expose the visualizer as a separate long-running lifecycle command. | "The GrepAI lifecycle command reads" | mcp/src/agents_remember/package_data/runtime/system/defaults/examples/coordinator/tools.md:42-42 |
| The process namespace note says long-running daemon actions such as watcher start/stop/shutdown, CGC start/stop/visualize, and GrepAI watcher start/stop/refresh must run from a durable host namespace, while lifecycle status reports `processNamespace` diagnostics and refuses `--die-with-parent` sandboxes. | `processNamespace` | mcp/src/agents_remember/package_data/runtime/system/defaults/examples/coordinator/tools.md:69-75 |
| The containment notes say a CGC provider should not be used in managed mode if indexing writes `.cgcignore`, `.codegraphcontext`, reports, databases, or logs into the indexed source repository, and a GrepAI provider should not be used if indexing creates `.grepai/` inside source repositories or durable memory roots. | "A CGC provider should not be used" | mcp/src/agents_remember/package_data/runtime/system/defaults/examples/coordinator/tools.md:77-78 |

## Cross-Repo References

No sibling repository evidence is needed.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-08-02T20:42:26+02:00 — W2-B07 curator: repaired 4 repository-reference citations (4/4 anchored and sourced; scoped citation check clean).

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 4 self-file line citations that all ran
  past the end of the 91-line `coordinator/tools.md`, and corrected two claims the source no longer
  supports. Verified ranges by reading the file: the global-vs-repo-specific split is L1-L7 plus the
  `## Notes` closer at L87-L91 (was `L121-L125`); the GrepAI/CGC lifecycle notes are L42-L67 (was
  `L70-L109`); the process-namespace note is L69-L75 (was `L111-L117`); the containment note is
  L77-L81 (was `L119-L127`). Rewrote the lifecycle row to drop "aggregate `watchers` commands start
  or stop every enabled provider watcher" — the file's only `watchers` mention is the
  durable-namespace list at L69-L70 and it makes no such claim; kept the aggregate behaviour the
  file does state (`cgc start` without `--repo-id` starts every configured root, L57-L59). Rewrote
  the containment row: L80-L81 says a GrepAI provider creating `.grepai/` inside source repositories
  **or durable memory roots** should not be used in managed mode, so the previous "`.grepai/`
  working dir is expected and git-ignored [in memory roots]" reading was false against that
  paragraph.

- 2026-06-02T01:15+02:00: Updated GrepAI guidance for watch-live: roots are indexed in place (read-write bind-mounted) instead of mirrored under `index-roots/`, and `.grepai/` is now git-ignored per memory root rather than rejected from memory roots.
- 2026-05-25T18:07+02:00: Updated GrepAI tool guidance after managed mode became Docker-only and stopped using `providers/_bin`.
- 2026-05-24T18:10+02:00: Moved onboarding to mirror the packaged runtime source route under `mcp/src/agents_remember/package_data/runtime/` after F-10 packaged runtime asset discovery.
- 2026-05-23T21:25+02:00: Clarified that repo-specific code quality tools belong in the selected memory layer's `system/tools.md`.
- 2026-05-23T04:43+02:00: Updated coordinator tool onboarding for `runtime_install` MCP tool and the `providers/runners` provider layout.
- 2026-05-21T17:16+02:00: Updated examples after daemon/server lifecycle actions began requiring durable host process namespaces and status began reporting `processNamespace`.
- 2026-05-21T15:42+02:00: Updated examples after normal provider lifecycle commands began inferring the coordinator root from the installed script path.
- 2026-05-21T12:40+02:00: Updated CGC command doctrine to show `cgc visualize --port <port>` as the explicit long-running visualizer command, separate from bounded `cgc run` queries.
- 2026-05-21T12:35+02:00: Updated GrepAI lifecycle command notes for provider-owned mirror roots under the former `providers/grepai/index-roots/` runner path.
- 2026-05-21T11:50+02:00: Updated GrepAI command doctrine for backend status/start, runtime-owned binary usage, workspace-mode PostgreSQL config, and `.grepai/` containment checks.
- 2026-05-21T04:53+02:00: Added shared `provider-setup.py` setup commands and documented CGC seed export/import with path rewrite for benchmark and worktree preparation.
- 2026-05-21T03:05+02:00: Corrected GrepAI search to query-first JSON compact output and documented lifecycle-managed `cgc run` relationship queries.
- 2026-05-21T02:33+02:00: Added aggregate `watchers` command documentation for starting, checking, and stopping every enabled provider watcher through one coordinator-level command.
- 2026-05-21T02:33+02:00: Updated CGC command examples for the earlier direct lifecycle CLI settings model.
- 2026-05-21T01:47+02:00: Updated provider command documentation for FalkorDB Docker lifecycle management, all-root watcher start/stop commands, and source-containment checks.
- 2026-05-20T19:11+02:00: Documented provider command shapes for GrepAI and CodeGraphContext, including CGC process-env-only keys and containment checks.
- 2026-05-13T13:38: Created onboarding for the coordinator tools example.
