# settings.md

## Purpose

This file is the human-facing coordinator settings example for `ar-coordination/system/settings.md`, including the human-readable doctrine for optional context providers.

## Code Commentary

### Logic

The example describes the coordinator as workspace-wide routing and workflow state. It lists global instructions, shared tools, workspace source registries, task/worktree roots, notes, selected memory repos, and operator conventions as coordinator-owned surfaces. The context provider section frames providers as local discovery accelerators, maps semantic discovery to GrepAI, relationship discovery to CodeGraphContext, and intent retrieval back to onboarding plus bounded source confirmation. Machine-readable provider authority belongs to the MCP settings file outside the coordinator root, not to this human-facing coordinator example.

The provider install guidance says installs should be coordination-owned:
pinned requirements under `providers/requirements/`, patches under
`providers/patches/`, and Docker image locks beside those pins. `providers/_bin`
and `providers/_venvs` are explicitly not managed provider contracts. Providers
that need native binaries, databases, or daemonized infrastructure should prefer
Docker-wrapped providers/backends and must not require host-level PostgreSQL,
FalkorDB, Ollama, OS services, launch agents, package-manager services, Python
virtual environments, or global user daemons for normal managed mode.

The GrepAI guidance says one `grepai-memory` provider can declare multiple memory roots in workspace mode, covering the configured external memory repos with explicit `{ projectId, path }` entries; the former repo-internal `ar-memory/` roots were removed from the product and are no longer an indexing target. Managed lifecycle tooling indexes those live roots in place and git-ignores GrepAI's per-root `.grepai/` working directory so generated GrepAI artifacts stay out of memory commits. GrepAI config, state, cache, home files, and provider state live under `providers/runners/grepai/`; operator logs live under `logs/providers/grepai/`; all memory roots share one lifecycle-owned Docker network, PostgreSQL/pgvector container with durable state under `providers/data/grepai/postgres/`, and Ollama container for embeddings. GrepAI itself runs from the Docker runner container, so managed mode must not install GrepAI or Ollama into host user space. A `.grepai/` directory inside any indexed memory root is runtime artifact output rather than durable memory.

The CodeGraphContext guidance says one `codegraphcontext-code` provider can
declare multiple code repository roots. Lifecycle tooling expands those roots
into one watcher/runtime instance per configured code repo under
`providers/runners/codegraphcontext/<repo-id>/`, runs CodeGraphContext itself
from a lifecycle-owned Docker runner image/container as the host user when
supported, and shares one lifecycle-owned FalkorDB Docker DBMS on the shared CGC
Docker network with durable state under
`providers/data/codegraphcontext/falkordb/`. Reinstall/update may delete and
recreate package-owned provider defaults plus runner scaffolding while
preserving `providers/data` and central logs under `logs/`; `_bin` and `_venvs` are not
preserved as managed provider paths. MCP install generates lifecycle settings
from MCP authority rather than coordinator-local JSON authority. Deleting
FalkorDB data, graph namespaces, repository indexes, or GrepAI PostgreSQL data
requires an explicit destructive lifecycle action.

### Conventions

Repo-specific rules belong in the selected memory layer rather than this coordinator settings file. Provider settings should stay declarative in MCP settings, while start/stop/status/refresh/install behavior belongs in MCP/package-owned lifecycle tooling. Concrete GrepAI and CGC root entries should name existing memory or code repository directories; placeholder examples should not be applied as live settings.

### Invariants And Boundaries

`c-08-ar-coordination-context-resolver` skill remains the route from coordinator context into the target repository's active memory settings, tools, sources, onboarding, and ledger paths. Context providers must not replace source proof, verified onboarding, drift checks, branch validity, or memory promotion rules. Disposable GrepAI runtime artifacts must stay under `providers/runners/grepai/` or per-root git-ignored `.grepai/` working directories, disposable CGC runtime artifacts must stay under `providers/runners/codegraphcontext/<repo-id>/.codegraphcontext/`, durable database state must stay under `providers/data/`, CGC command execution must stay Docker-owned, and process-only env keys must not be persisted into `.env` when CGC v0.4.10 rejects them as invalid config.

### Todos

None.

### Docs References

No external documentation is needed.

## Evidence

### Repo-Internal References

- The example states that coordinator settings are workspace-wide and do not replace per-repository memory settings. [1]
- The routing section tells agents to invoke "c-08-ar-coordination-context-resolver" and treat repository-specific memory guidance as more specific. [2]
- The provider section defines semantic, relationship, and intent retrieval substrates and keeps provider authority in MCP settings. [3]
- The provider lifecycle section routes behavior through MCP/package-owned tooling, removes `_bin` and `_venvs` from the managed contract, and prefers Docker-wrapped providers/backends over host services. [4]
- The GrepAI notes define workspace roots, live-root indexing, `.grepai/` containment, runner/config/log/data locations, and Docker-owned execution. [5]
- The CGC notes define configured code roots, per-repository runners, Docker-owned execution, shared FalkorDB state, environment separation, and explicit database deletion. [6]

### Cross-Repo References

No sibling repository evidence is needed.
