# tools.md

## Governing Overview

[overview](../../../../../../../../overview.md)

## Current source contract evidence

- Current source declarations support the qualified naming or fixture account; no executed test or acceptance is inferred. [7]

## Purpose

The packaged coordinator tools example separates shared coordinator commands from each
repository memory layer's checks and workflow instructions. It is a template, not provider
execution authority or the actual advertised MCP roster.

## Code Commentary

Repository-specific commands belong in memory `system/tools.md`; resolve the selected
repository through `context_packet` before choosing its task, worktree, memory or validation paths. Source/package-owned
legacy lifecycle and Docker mechanics are distinct from coordinator-local scripts and
shared authoritative settings. Discovery evidence never replaces verified source/intent.

The current context_packet example is context_packet(repo_id="<repoId>"), without include_providers. Pre-retirement provider dependency/setup and enabled-provider prose remains legacy specimen material, not current provider execution authority. These are legacy specimen descriptions, not current calls:
the two retired providers never count as enabled, normal setup
starts nothing, and former provider search/status/watcher tools are absent. Runtime
installation retains scaffold/copy and old-watcher-stop behavior; explicit deletion is
separately requested through providers-remove. Do not revive provider workflows or alter
managed configuration because an old command shape appears in this template.

## Current evidence


- The coordinator-level tools example: global commands, the runtime_install and context_packet MCP entry points, the managed provider lifecycle, and the containment checks that keep provider output as discovery evidence. [6]


## Evidence

### Docs References

No external documentation is needed.

No relevant external documentation found.

### Repo-Internal References


- The coordinator tools example places repository-specific checks, commands, branch workflow and code quality tools in the selected memory layer's system/tools.md, not here. [1]


- The provider command block shows only the `runtime_install` and `context_packet(repo_id="<repoId>")` MCP call shapes; the CGC `run -- ...` and `visualize --port <port>` shapes appear in the lifecycle notes. [2]

- The provider notes say GrepAI lifecycle commands expand `grepai-memory` workspace roots, ensure Docker network/PostgreSQL/Ollama health, bind-mount and index the live memory roots in place, write provider-owned workspace config/state, and use the Docker runner container instead of host binaries; CGC lifecycle commands expand the configured `roots` array, ensure FalkorDB Docker, start/stop every configured root unless `--repo-id` narrows it, pass post-`--` arguments to native CGC for bounded queries, and expose the visualizer as a separate long-running lifecycle command. [3]

- The process namespace note says long-running daemon actions such as watcher start/stop/shutdown, CGC start/stop/visualize, and GrepAI watcher start/stop/refresh must run from a durable host namespace; lifecycle status reports `processNamespace` diagnostics, and daemon actions refuse to run from `--die-with-parent` sandboxes. [4]

- The containment notes say a CGC provider should not be used in managed mode if indexing writes `.cgcignore`, `.codegraphcontext`, reports, databases, or logs into the indexed source repository, and a GrepAI provider should not be used if indexing creates `.grepai/` inside source repositories or durable memory roots. [5]

- The notes tell agents to resolve the target repository through `context_packet` before choosing task, worktree, memory or validation paths. [8]

### Cross-Repo References

No sibling repository evidence is needed.

No meaningful cross-repo references found.
