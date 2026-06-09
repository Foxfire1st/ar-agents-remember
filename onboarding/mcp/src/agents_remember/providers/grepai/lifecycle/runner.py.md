# mcp/src/agents_remember/providers/grepai/lifecycle/runner.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/grepai/lifecycle/runner.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-10T05:30+02:00     |
| lastVerifiedCommitHash | `592274a52cec61d97521771c630272c72240ed01` |
| lastVerifiedCommitDate | 2026-06-10T01:38:42+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[Provider Lifecycle Modules Overview](overview.md)

## Purpose

`runner.py` owns the Docker runner image and watcher container for
GrepAI.

## Code Commentary

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

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Runner settings and workspace paths are derived in GrepAI core. | [core.py](agents-remember-md/mcp/src/agents_remember/providers/grepai/lifecycle/core.py) |
| GrepAI action dispatch uses this module for start, stop, refresh, and bounded run readiness. | [actions.py](agents-remember-md/mcp/src/agents_remember/providers/grepai/lifecycle/actions.py) |
| GrepAI project migration lives with backend startup and is reused here. | [backend.py](agents-remember-md/mcp/src/agents_remember/providers/grepai/lifecycle/backend.py) |

## Update History

- 2026-06-10T05:30+02:00 — Watcher status gains `initialScan`: `grepai_watcher_initial_scan` reads the watcher's own container-log scan markers since container start (`Indexing [` progress, `Initial scan complete`) via `grepai_scan_state_from_log` — the same mechanism as the CGC probe, giving GrepAI real indexed/indexing states instead of permanent unknown.
- 2026-06-02T01:15+02:00 — `grepai_docker_state` roots payload no longer emits `sourcePath` after `GrepaiMemoryRoot.source_path` was removed (roots are watched live in place).
- 2026-05-31T12:50+02:00 — Removed the unused `grepai_runner_dockerfile` helper and its `provider_asset_text` import (build path uses `provider_asset_path`); re-typed the `layout` param from `Any` to `GrepaiRuntimeLayout` across `grepai_watcher_inspect`/`grepai_watcher_workspace_status`/`grepai_watcher_start_prerequisites`/`grepai_watcher_create_start_result`/`grepai_docker_state`; added matching Invariants And Boundaries notes (1.0.0 review remediation).
- 2026-05-30T21:33+02:00: Documented the `no_cache` build path for the GrepAI runner/watcher image (`--no-cache` + skip-shortcut bypass for a from-scratch rebuild). Verified against `8927f03`.
- 2026-05-29T18:35+02:00: `grepai_watcher_dry_run_start_result` `commands` -> `list[dict[str, Any]]`; behavior-preserving (commit `0549b28`).
- 2026-05-28T12:32+02:00: Updated after GrepAI watcher status began including normalized container-state summaries.
- 2026-05-27T00:25+02:00: Updated after watcher startup began rendering
  dependency ports from the current start flow and sharing GrepAI project
  migration.
- 2026-05-25T19:09+02:00: Moved into the provider-specific subpackage and dropped the filename prefix while preserving behavior.
- 2026-05-25T19:01+02:00: Created from GrepAI runner image and watcher lifecycle extracted out of provider lifecycle.
