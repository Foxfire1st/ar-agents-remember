# mcp/src/agents_remember/providers/status.py

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

`status.py` reads provider watcher state and projects it into either compact
provider summaries or detailed provider diagnostics, including recovery guidance
for known degraded states such as GrepAI `noWorkspace`.

## Code Commentary

`provider_status_packet()` wraps a compact `ProviderSummary` in the public
`ProviderStatusResponse`. `provider_summary_packet()` returns just the compact
summary for `ContextPacketV2`. `provider_diagnostics_packet()` returns the
dedicated diagnostics contract with current-state, process-namespace,
recovery-action, raw-status, and per-provider raw status detail.
When provider details are intentionally skipped, compact summary item
construction returns an empty `items` list instead of synthesizing provider rows
from absent current-state detail.

`provider_status_packet()` also attaches the daemon-sampled containment
metrics (containment R4, 260707-HFX-L1): it reads
`ProviderMetricsStore(config.coordination_root).read_current()` and, when a
snapshot exists, rides it on the packet as `metrics`. The read is deliberately
unconditional — leftover container stacks from a dead session are exactly what
must stay observable, so the metrics ride the packet even when providers are
disabled — and read-only; the field is simply absent until the serving
daemon's first sample lands. Beside `metrics`, the packet carries `indexState`
(260707-HFX-L2): the newest index-lifecycle rows (last 10, via
`store.read_recent_index_states`) — seed catch-up outcomes, `staleIndex`
blocks, watcher readiness — because index staleness is a reportable STATE: an
operator sees behind-ness from status instead of reading setup logs. Absent
when no index rows exist yet.

The projection's global `ok` requires both signals to pass: the raw watchers
`ok` (are the containers up) AND the aggregated current-state `ok` (does the
graph/workspace actually hold content). A degraded target — an `empty` graph,
an unreachable backend, a missing workspace — pulls the global flag false even
while every container reports running; `partial` is set when other providers
remain ready so callers can distinguish "one repo degraded" from "everything
down". Separately, the compact summary carries an additive `indexing` list of
busy `"<provider-id>:<repo-id>"` targets: healthy-but-busy targets never
degrade state or `ok`, but agents can relay "ready" to
developers instead of guessing why fresh symbols are missing.

`_cgc_watcher_state()` projects each CGC watcher row, and its `lastRefresh` now
passes through `_last_refresh_summary()`: a structured refresh record
(`{updatedAt, returncode, durationSeconds}`) is flattened into a single scalar
string (`"<updatedAt> returncode=<n> durationSeconds=<s>"`), a plain string is
passed through unchanged, and an empty record collapses to `None`. This keeps the
watcher payload's `lastRefresh` a stable scalar even after the backend began
emitting a structured object.

When status is read, lifecycle settings are generated from trusted MCP
settings, watcher status is invoked, and the current provider state file is
written under the coordinator log/status root. The watcher probe runs as a
bounded docker-control command timed by `DEFAULT_DOCKER_CONTROL_SECONDS`; it no
longer reads the removed `timeout_caps["providerSeconds"]` key (renamed to
`providerSetupSeconds`, which caps only provider setup, not status probing).
Context packet callers receive the current-state file path and summary facts,
not the full raw status tree.

`refresh_current_provider_state(config, *, checked_at=None)` is the dashboard-facing
refresh seam: it runs the same provider projection as status with `include_providers=True`
and returns the persisted current-state payload. It exists so dashboard projection ticks
can refresh provider truth without pretending the reducer or frontend owns provider status
semantics.

`_provider_recovery_actions()` preserves raw lifecycle recovery actions and adds
shared restart guidance when the current projected GrepAI state has
`indexingState == "noWorkspace"`. It also emits a per-repo CGC restart entry
for each target whose state is `empty` or `backend-unreachable`, naming the
affected repo so the suggested action is scoped rather than a blanket restart.
The same action list is returned from compact provider status and provider
diagnostics so the model sees the same non-destructive next step from either
surface.

## Invariants And Boundaries

- `context_packet` uses `provider_summary_packet()`, not diagnostics/raw status.
- `provider_diagnostics` is the detail surface for raw provider state.
- A skipped provider projection reports aggregate skipped state only; it does
  not emit per-provider summary rows with unknown or omitted `ok` fields.
- Temporary lifecycle settings come from MCP settings and are deleted after the
  status read.
- Provider status is read-only from the MCP caller perspective; setup history
  belongs in provider setup summary logs.
- Dashboard refreshes go through the same current-state writer as MCP status, so
  the persisted provider contract has one owner.
- `noWorkspace` remains a degraded state; status adds restart/rebind guidance
  rather than treating missing workspaces as acceptable readiness.
- Container liveness alone must never produce global `ok: true`; content-level
  current-state aggregation gates it too. Running containers over a 0-node
  graph reported green for three days before this rule existed (2026-06-09
  incident).
- `indexing` is informational, never degrading: a busy target stays `ok` and
  appears in the busy list, so "wait" and "intervene" remain distinguishable
  signals.
- The `metrics` block is daemon-sampled and read-only from the status path; it
  must stay attached even when providers are disabled so leftover container
  stacks remain observable (containment R4).
- Index staleness is a reportable state (260707-HFX-L2): the `indexState`
  rows surface behind-ness on the status packet; they never gate or degrade
  the projection's `ok`.

## Evidence

### Repo-Internal References

- Provider response models define summary, diagnostics, watcher, and native provider payload shapes. [1]
- Context packet construction consumes the compact provider summary. [2]
- Provider MCP application entry points expose status, diagnostics, watcher, GrepAI, and CGC tools. [3]
- Current-state projection and persistence live in the current-state module. [4]
- Restart/rebind recovery wording is shared with runtime-install recovery reporting. [5]
- The containment metrics store whose rolling current snapshot rides the status packet (containment R4). [6]
- Provider status appends restart guidance when projected GrepAI state reports `indexingState: noWorkspace`. [7]

| `refresh_current_provider_state` calls the regular provider-status projection and returns the current-state payload for dashboard-owned refreshes. | `refresh_current_provider_state` | mcp/src/agents_remember/providers/status.py:157-167 |
