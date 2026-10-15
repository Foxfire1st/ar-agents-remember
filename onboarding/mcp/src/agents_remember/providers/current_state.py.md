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

GrepAI readiness also uses the workspace-status gate: `grepai_workspace_present()` requires a successful `workspaceStatus` exit and stdout without the literal "No workspaces configured" marker. It does not independently verify workspace content or searchability; blank stdout passes this predicate. A missing or nonzero status fails it, downgrading a container-ready GrepAI to `degraded` with `noWorkspace`. When this predicate passes, it maps the watcher's `initialScan` log-marker probe (provided by
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
- GrepAI readiness requires successful workspace status without the literal no-workspaces marker; container liveness alone is insufficient. This gate admits blank stdout and establishes no independent searchability proof.
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

- GrepAI lifecycle settings use the same repository memory-root mapping for roots (`projectId == repoId`) through `_grepai_roots`. [6]

- `provider_status_packet` builds a nonpersisting normalized provider summary; `provider_diagnostics_packet` exposes the current-state object. `refresh_current_provider_state` explicitly persists the payload and returns that object; its path is supplied by the lower writer. [10]


- `ProviderCurrentStateTests` asserts the workspace current-state path and truth shape, disabled aggregation, CGC degradation/restart exclusion, and provider-status recovery integration. Workflow-local instance paths are not asserted by this retained test class.  Anchor: "class ProviderCurrentStateTests(unittest.TestCase):" [11]


### Cross-Repo References

No sibling repository boundary is needed to explain this file.

No meaningful cross-repo references found.

- Current state payloads include version, kind, instance, aggregate state, `ok` (`state == "ready"`), check time, settings file, enabled providers, process namespace, and per-provider state.  Anchor: "def build_current_provider_state("; "def aggregate_state(" [1]
- Current state files are written under `logs/providers/status/<scope>/<instance>/current.json` by `current_state_path`. [2]
- Instance identity uses the shared configured provider scope/id or a deterministic mixed digest through `current_state_instance`. [3]
- GrepAI and CGC status mappers keep provider-specific resources, watcher state, and indexing state separate through `grepai_current_state` and `cgc_current_state`. [4]
- GrepAI target repos are derived from configured repository memory roots and persisted as `targetRepos` in current state.  Anchor: `targetRepos` [5]

- The workspace gate requires workspaceStatus returncode0 and stdout without the literal No workspaces configured marker. Missing/nonzero status fails but blank stdout passes; this predicate does not independently verify content or searchability. [7]

- Container normalization keeps container state, running flag, started-at time, uptime seconds, and health in the current-state payload through `normalize_container_state` and `resource_state`. [8]
- Aggregate state ignores disabled providers and reports ready, degraded, failed, unknown, disabled, or noProviders from current provider facts through `aggregate_state`. [9]
