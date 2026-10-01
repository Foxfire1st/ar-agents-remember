# mcp/src/agents_remember/providers/grepai/lifecycle/embedder.py

## Governing Overview

[Provider Lifecycle Modules Overview](overview.md)

## Purpose

`embedder.py` owns the managed GrepAI Ollama Docker embedder.

## Code Commentary

### 260731-EFA-L2 Embedder Context

`grepai_embedder_start_context(args)` returns the frozen
**`GrepaiEmbedderContext(settings_path, provider_settings, layout, embedder, network_name)`**
instead of a tuple — which settings file the invocation read, the provider entry it found, the
runtime layout, the resolved embedder settings, and the docker network the Ollama container joins.
Every embedder command needs all of it, so it is resolved once and consumed whole. Host reconciliation is reported through `BackendStartReconciliation`. Emitted payloads,
the model pull and the readiness probe are unchanged.

### Logic

The module starts or reuses an `ollama/ollama` container, keeps model data under
provider-managed data roots, reuses any already-running Compose-managed host
port mapping, starts Ollama through the package Compose project, waits for
`ollama list`, detects whether the configured model is present, and ensures the
model is loaded. It shares the GrepAI project migration helper so standalone
embedder startup can clean pre-Compose containers and networks before Compose
owns them. Status includes a normalized Docker container state summary so MCP
provider status can report embedder state and uptime. For new `auto` host-port
allocations it prefers `GREPAI_OLLAMA_DEFAULT_PORT` (`61434`) while keeping the
container-side Ollama HTTP port at `11434`.

`docker_ensure_ollama_model` now seeds the model from the workspace Ollama
before falling back to `ollama pull`. `_seed_ollama_model_from_source` reads
the `seedFromContainer` key from embedder settings (populated for worktree
embedders; absent for the workspace embedder itself). When present, it streams
the model store from the source container to the target via a shell tar pipe:
`docker exec <source> tar -C /root/.ollama -cf - models | docker exec -i
<target> tar -C /root/.ollama -xf -`. If the seed succeeds and `ollama list`
confirms the model is present, `ollama pull` is skipped entirely. If the seed
fails or no `seedFromContainer` is configured, the existing `ollama pull`
fallback runs. The failed seed result is attached to the response as
`seedAttempt` so failures remain diagnosable.

### Invariants And Boundaries

- GrepAI must not require a host Ollama installation.
- The embedder container must be reachable from the GrepAI runner through the
  managed Compose network.
- Model readiness is part of lifecycle health, not an optional follow-up.
- Existing Compose-managed embedder port mappings are reused on repeated starts
  rather than reallocated from host socket availability.
- The preferred host port avoids developer-owned host Ollama services; the
  container port remains the Ollama service port used inside the Docker network.
- Embedder status should expose enough Docker state for current provider status
  without requiring callers to inspect containers themselves.
- `_seed_ollama_model_from_source` returns `None` (not a failed result dict)
  when no `seedFromContainer` is configured or the source equals the target, so
  callers skip the seed path entirely for the workspace embedder.
- The tar-pipe copies the `/root/.ollama/models` subtree container-to-container
  without touching the host filesystem; network bandwidth is not consumed.
- Layout-consuming helpers (`grepai_embedder_health`,
  `grepai_embedder_start_context` return value,
  `grepai_embedder_remove_mismatched_container`, `grepai_embedder_inspect`, and
  `grepai_embedder_create_start_result`) are typed against the
  `GrepaiRuntimeLayout` dataclass (re-exported via the `core` star-import), not
  an opaque `Any`.

## Evidence

### Repo-Internal References

- Embedder settings and container endpoint are derived in GrepAI core. [1]
- `grepai_install_workspace` is the GrepAI install/start entry. [2]
- `grepai_backend_start` is the GrepAI backend startup entry. [3]
- The embedder lifecycle is the compose-owned startup path that consumes the migrated settings. [4]
- `isolated.py` populates `seedFromContainer` in worktree embedder settings. [5]
