# tools.md

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

## Evidence

### Docs References

No external documentation is needed.

No relevant external documentation found.

### Repo-Internal References

- The coordinator tools example separates global commands from repository-specific checks, branch workflow, and code quality tools. [1]
- The provider command section records MCP runtime install, `grepai_search`, aggregate provider status/watcher flows, and CGC bounded `run -- ...` plus long-running `visualize --port 8000` command shapes. [2]
- The provider notes say GrepAI lifecycle commands expand `grepai-memory` workspace roots, ensure Docker network/PostgreSQL/Ollama health, bind-mount and index the live memory roots in place, write provider-owned workspace config/state, and use the Docker runner container instead of host binaries; CGC lifecycle commands expand the configured `roots` array, ensure FalkorDB Docker, start/stop every configured root unless `--repo-id` narrows it, pass post-`--` arguments to native CGC for bounded queries, and expose the visualizer as a separate long-running lifecycle command. [3]
- The process namespace note says long-running daemon actions such as watcher start/stop/shutdown, CGC start/stop/visualize, and GrepAI watcher start/stop/refresh must run from a durable host namespace, while lifecycle status reports `processNamespace` diagnostics and refuses `--die-with-parent` sandboxes. [4]
- The containment notes say a CGC provider should not be used in managed mode if indexing writes `.cgcignore`, `.codegraphcontext`, reports, databases, or logs into the indexed source repository, and a GrepAI provider should not be used if indexing creates `.grepai/` inside source repositories or durable memory roots. [5]

### Cross-Repo References

No sibling repository evidence is needed.

No meaningful cross-repo references found.
