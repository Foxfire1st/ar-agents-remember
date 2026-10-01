# mcp/src/agents_remember/providers/current_state.py

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

`current_state.py` projects provider watcher status into the current runtime
truth that MCP callers should read. It writes the latest provider state to
`logs/providers/status/<scope>/<instance>/current.json` under the coordination
root.

## Code Commentary

### Logic

`build_current_provider_state()` captures the check time (or accepts an injected
`checked_at` from the dashboard projector), maps raw watcher status into per-provider
state, computes an aggregate state, and returns a versioned `provider-current-state`
payload. `write_current_provider_state()`
persists that payload beside the central provider status logs. Instance path
selection uses a shared provider scope/id when all configured providers match,
or a deterministic mixed digest when the config combines multiple provider
instances.

The provider mappers keep GrepAI and CGC shapes separate. GrepAI state records
PostgreSQL, Ollama, and watcher resources plus `watcherUp`, indexing state, and
configured repo targets. `grepai_target_repos(config)` derives those targets from
the MCP repository memory roots (`repoId` + memory-root `path`) and
`grepai_current_state()` persists them as `targetRepos` when present. The
readiness/indexing values are still provider-level until GrepAI exposes per-root
health, but the repo coverage itself is explicit and stable. `targetRepos` means
the aggregate GrepAI instance has addressable repo/project targets; it does not
mean the current-state payload has split GrepAI into separate processes. CGC state records
the shared FalkorDB backend plus one watcher resource per repo. Disabled
configured providers are represented explicitly as `disabled` and do not poison
aggregate readiness.

GrepAI readiness is additionally gated on workspace presence.
`grepai_workspace_present()` inspects the watcher's `workspaceStatus` **stdout**
(not just its exit code, because `grepai workspace status` exits 0 even when it
prints "No workspaces configured"). `grepai_current_state()` downgrades a
container-ready GrepAI to `degraded` when no searchable workspace exists, and
`grepai_indexing_state()` reports `noWorkspace` in that case. With a workspace
present, it maps the watcher's `initialScan` log-marker probe (provided by
`grepai/lifecycle/runner.py`) to `indexing` (scan in progress) or `indexed`
(scan complete), falling back to `unknown` only when markers are absent —
parity with the CGC graph probe.

Crash-looping containers are not live: `resource_state()` returns `failed` for
`containerState == "restarting"` (Docker reports Running=true between
restarts), and both the CGC `watcherUp` and GrepAI `watcher_up` derivations
exclude restarting containers.

### Invariants And Boundaries

- This file reports what is true now; it must not embed last-setup history.
- Disabled providers are current state, not failures.
- Current state is refreshed when the agent asks the MCP for provider status or
  a context packet that includes providers, and the dashboard projector can now
  refresh it on cadence with the same timestamp used for projection.
- The file does not start, stop, or repair providers; it normalizes status
  facts produced by lifecycle watchers.
- GrepAI repo coverage is derived from configured repository memory roots and
  persisted as `targetRepos`; consumers should not rediscover that mapping from
  provider names or workspace strings.
- `targetRepos` is coverage/addressing evidence for topology and query routing,
  not per-root health evidence. Keep GrepAI readiness provider-level until the
  provider exposes root-level health.
- GrepAI is only `ready` when its watcher reports a real, searchable workspace;
  container liveness alone is not readiness. A missing/empty workspace is
  `degraded` with `indexingState: noWorkspace`.
- A `restarting` (crash-looping) container must never count as a ready
  watcher — observed during the 2.5.0 rollout, when a crash loop surfaced as
  `running: true` → `ready`.
- `indexing` is healthy-but-busy at every level: it must not degrade
  state/ok; it feeds the compact summary busy list instead.

### Todos

No open file-local todos (the former "replace GrepAI unknown indexing state"
todo is resolved by the `initialScan` marker probe).

## Evidence

### Docs References

No external documentation is needed for this local status projection.

No relevant external documentation is needed for this provider state projection.

### Repo-Internal References

- Current state payloads include version, kind, instance, aggregate state, `ok` (`state == "ready"`), check time, settings file, enabled providers, process namespace, and per-provider state. [1]
- Current state files are written under `logs/providers/status/<scope>/<instance>/current.json` by `current_state_path`. [2]
- Instance identity uses the shared configured provider scope/id or a deterministic mixed digest through `current_state_instance`. [3]
- GrepAI and CGC status mappers keep provider-specific resources, watcher state, and indexing state separate through `grepai_current_state` and `cgc_current_state`. [4]
- GrepAI target repos are derived from configured repository memory roots and persisted as `targetRepos` in current state. [5]
- GrepAI lifecycle settings use the same repository memory-root mapping for roots (`projectId == repoId`) through `_grepai_roots`. [6]
- GrepAI readiness is gated on workspace presence: `grepai_workspace_present` reads the watcher `workspaceStatus` stdout, `grepai_current_state` downgrades to `degraded`, and `grepai_indexing_state` returns `noWorkspace` when absent. [7]
- Container normalization keeps container state, running flag, started-at time, uptime seconds, and health in the current-state payload through `normalize_container_state` and `resource_state`. [8]
- Aggregate state ignores disabled providers and reports ready, degraded, failed, unknown, disabled, or noProviders from current provider facts through `aggregate_state`. [9]
- Provider status writes this current-state payload and returns both the file path and current-state object to MCP callers through `provider_status_packet` and `refresh_current_provider_state`. [10]
- Unit tests assert the file path, current truth shape, disabled-provider behavior, workflow-local instance paths, and provider-status integration in `ProviderCurrentStateTests`. [11]

### Cross-Repo References

No sibling repository boundary is needed to explain this file.

No meaningful cross-repo references found.
