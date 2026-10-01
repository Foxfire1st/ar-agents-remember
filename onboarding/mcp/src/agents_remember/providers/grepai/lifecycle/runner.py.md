# mcp/src/agents_remember/providers/grepai/lifecycle/runner.py

## Governing Overview

[Provider Lifecycle Modules Overview](overview.md)

## Purpose

`runner.py` owns the Docker runner image and watcher container for
GrepAI.

## Code Commentary

### 260731-EFA-L2 Watcher-Start And Stack Objects

- **`GrepaiWatcherStart(layout, runner, network, image)`** — everything a watcher start has in hand
  before compose brings it up, resolved once by `grepai_watcher_start_prerequisites(args, *,
  runner, network_name)` (which now returns `(start, refusal_or_None)` instead of a four-tuple) and
  reported verbatim in every watcher-start result. The refusal payload is still emitted when the
  network or the image build is not ok.
- **`GrepaiStackResults(backend=None, embedder=None, watcher=None)`** — the lifecycle result of each
  container in the stack. `grepai_docker_state(layout, stack, *, action, runner)` takes it, and
  still writes them to the state file's `backend`/`embedder`/`watcher` keys unchanged.

### Logic

The module builds the pinned GrepAI runner image from the upstream Linux release
asset (adding `--no-cache` and bypassing the skip-if-tag-exists shortcut for a
from-scratch rebuild when `no_cache` is set), records runner image locks,
reports watcher container status, runs
`grepai watch` in the managed runner container with runtime and log mounts,
stops the watcher container, and validates workspace status through
`docker exec`. Watcher startup receives the backend and embedder host ports
chosen earlier in the same GrepAI start flow so its Compose override matches
the already-started dependency services, and it shares the GrepAI project
migration helper for standalone watcher startup.
Watcher status includes a normalized Docker container state summary so MCP
provider status can report watcher state and uptime, plus an `initialScan`
probe: `grepai_watcher_initial_scan` reads the watcher's container log since
its start (`docker logs --since`) and `grepai_scan_state_from_log` classifies
the watcher's own markers — `Initial scan complete` → `complete`, progress
markers (`Indexing [`, `Initial scan`, `Embedding`) → `in-progress`, otherwise
`unknown` — the same marker mechanism as the CGC probe, feeding GrepAI's
`indexed`/`indexing` states in current-state mapping.

### Invariants And Boundaries

- Bounded GrepAI commands run through the managed watcher container; no host
  GrepAI binary is required.
- Watcher containers must use container-visible runtime and log mounts.
- Runner image build/status must stay separate from Postgres and Ollama
  container lifecycle.
- Watcher `up` should render dependency port mappings from the current start
  result when those services were just started.
- Watcher status should expose enough Docker state for current provider status
  without requiring callers to inspect containers themselves.
- Functions that thread the runtime layout (`grepai_watcher_inspect`,
  `grepai_watcher_workspace_status`, `grepai_watcher_start_prerequisites`,
  `grepai_watcher_create_start_result`, `grepai_docker_state`) type `layout` as
  the concrete `GrepaiRuntimeLayout` (re-exported from `core`), not bare `Any`.
- The runner image build path resolves the GrepAI Dockerfile via
  `provider_asset_path`; there is no standalone helper that returns the
  Dockerfile text.

## Evidence

### Repo-Internal References

- Runner settings and workspace paths are derived in GrepAI core. [1]
- GrepAI action dispatch uses this module for start, stop, refresh, and bounded run readiness. [2]
- GrepAI project migration lives with backend startup and is reused here. [3]
