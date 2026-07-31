# mcp/src/agents_remember/providers/grepai/lifecycle/embedder.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/grepai/lifecycle/embedder.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T00:00+02:00     |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d` |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview      | `overview.md`                              |

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

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Embedder settings and container endpoint are derived in GrepAI core. | [core.py](agents-remember/mcp/src/agents_remember/providers/grepai/lifecycle/core.py) |
| GrepAI install/start composes backend, embedder, and runner lifecycle steps. | [actions.py](agents-remember/mcp/src/agents_remember/providers/grepai/lifecycle/actions.py) |
| GrepAI project migration lives with backend startup and is reused here. | [backend.py](agents-remember/mcp/src/agents_remember/providers/grepai/lifecycle/backend.py) |
| `isolated.py` populates `seedFromContainer` in worktree embedder settings. | [isolated.py](agents-remember/mcp/src/agents_remember/providers/grepai/isolated.py) |
| Unit tests cover the tar-pipe command shape, no-source guard, successful-seed-skips-pull, and failed-seed-falls-back-to-pull paths. | [test_ollama_model_seed.py](agents-remember/mcp/tests/test_ollama_model_seed.py) |

## Update History

- 2026-07-31T00:00+02:00 — 260731-EFA-L2 (gate honesty, `PLR0913` armed with no exemptions):
  `grepai_embedder_start_context` now returns `GrepaiEmbedderContext` instead of a tuple. Emitted
  payloads are unchanged. Verification metadata pinned until closeout stamps the L2 commit.
- 2026-06-25T09:55+02:00 — `auto` host-port selection now uses the centralized GrepAI Ollama preferred host port (`61434`) instead of preferring host `11434`; existing mappings and explicit configured ports still win.
- 2026-06-10T07:30+02:00 — No content impact: import path updated to `providers/context_common.py` (shared helpers moved out of the facade package, GitHub #58); documented behavior unchanged.
- 2026-06-10T05:30+02:00 — Leaf import replaces the `providers.context` aggregator import (circular-import fix; see core.py 2026-06-10 entry).
- 2026-06-01T00:00+02:00 — `docker_ensure_ollama_model` now seeds the model from the workspace Ollama via `_seed_ollama_model_from_source` (local tar pipe) before falling back to `ollama pull`; `seedFromContainer` key drives the seed path; updated Logic, added two new Invariants, added Repo-Internal References section.
- 2026-05-31T12:50+02:00 — Re-typed the `layout` params of `grepai_embedder_health`, `grepai_embedder_remove_mismatched_container`, `grepai_embedder_inspect`, and `grepai_embedder_create_start_result`, plus the `grepai_embedder_start_context` return tuple, from `Any` to the `GrepaiRuntimeLayout` dataclass (re-exported via the `core` star-import); behavior-preserving, recorded the layout typing in Invariants And Boundaries (1.0.0 review remediation).
- 2026-05-29T18:35+02:00: `grepai_embedder_dry_run_result` `commands` -> `list[dict[str, Any]]`; behavior-preserving (commit `0549b28`).
- 2026-05-28T12:32+02:00: Updated after GrepAI embedder status began including normalized container-state summaries.
- 2026-05-27T00:25+02:00: Updated after Ollama startup began reusing existing
  Compose port mappings and shared GrepAI project migration.
- 2026-05-25T19:09+02:00: Moved into the provider-specific subpackage and dropped the filename prefix while preserving behavior.
- 2026-05-25T19:01+02:00: Created from GrepAI Ollama embedder lifecycle extracted out of provider lifecycle.
