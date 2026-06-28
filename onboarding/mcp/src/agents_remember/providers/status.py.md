# mcp/src/agents_remember/providers/status.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/status.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-28T19:10+02:00|
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1` |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `../../../overview.md`                     |

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

The projection's global `ok` requires both signals to pass: the raw watchers
`ok` (are the containers up) AND the aggregated current-state `ok` (does the
graph/workspace actually hold content). A degraded target — an `empty` graph,
an unreachable backend, a missing workspace — pulls the global flag false even
while every container reports running; `partial` is set when other providers
remain ready so callers can distinguish "one repo degraded" from "everything
down". Separately, the compact summary carries an additive `indexing` list of
busy `"<provider-id>:<repo-id>"` targets: healthy-but-busy targets never
degrade state or `ok`, but agents can relay "ready, indexing in progress" to
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

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Provider response models define summary, diagnostics, watcher, and native provider payload shapes. | [providers.py](agents-remember/mcp/src/agents_remember/models/providers.py) |
| Context packet construction consumes the compact provider summary. | [context_packet.py](agents-remember/mcp/src/agents_remember/controllers/context_packet.py) |
| Provider MCP controllers expose status, diagnostics, watcher, GrepAI, and CGC tools. | [provider_tools.py](agents-remember/mcp/src/agents_remember/controllers/provider_tools.py) |
| Current-state projection and persistence live in the current-state module. | [current_state.py](agents-remember/mcp/src/agents_remember/providers/current_state.py) |
| Restart/rebind recovery wording is shared with runtime-install recovery reporting. | [recovery.py](agents-remember/mcp/src/agents_remember/providers/recovery.py) |
| Provider status appends restart guidance when projected GrepAI state reports `indexingState: noWorkspace`. | [status.py](agents-remember/mcp/src/agents_remember/providers/status.py) |
| Provider current-state tests assert `noWorkspace` stays degraded and that status/diagnostics return the restart recovery action. | [test_provider_current_state.py](agents-remember/mcp/tests/test_provider_current_state.py) |
| `refresh_current_provider_state` calls the regular provider-status projection and returns the current-state payload for dashboard-owned refreshes. | L138-L176 | [status.py](agents-remember/mcp/src/agents_remember/providers/status.py) |

## Update History

- 2026-06-28T19:10+02:00 — Main-carryover reconciliation (PR #95, code 84e95ad): documented `_last_refresh_summary`, which flattens a structured CGC `lastRefresh` object (`{updatedAt, returncode, durationSeconds}`) into a scalar summary string inside `_cgc_watcher_state` (MCP 2.9.x). Grafted onto the series' task-31 `refresh_current_provider_state` content.
- 2026-06-27T23:08+02:00 — Task 31 provider-state honesty: documented `refresh_current_provider_state`, the shared writer-backed seam used by dashboard projection ticks. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-10T06:20+02:00 — Body-quality pass: merged the dual-gate global `ok`, `partial`, `indexing` busy-list, and per-repo CGC recovery mechanics into Code Commentary and Invariants (documentation only).
- 2026-06-09T22:10+02:00 — The projection's global `ok` now requires both the raw watchers ok (containers) and the aggregated current-state ok (graph/workspace content); `partial` is set when other providers remain ready. Recovery actions now include a per-repo CGC restart entry for `empty`/`backend-unreachable` targets, and the compact summary gained the additive `indexing` list of busy `"<provider-id>:<repo-id>"` targets (healthy-but-busy: never degrades state/ok). This closes the 2026-06-09 incident where `context_packet` reported green over a 0-node graph for 3 days.
- 2026-06-08T09:57+02:00: Documented skipped-provider summary behavior: when provider details are skipped, compact summary `items` is empty rather than populated from missing current-state rows.
- 2026-06-04T22:15+02:00 — Documented shared provider restart/rebind recovery guidance for GrepAI `noWorkspace`, including matching compact status and diagnostics recovery actions.
- 2026-05-31T12:30+02:00 — Removed runner-integrity documentation: status projection no longer checks provider runner integrity, dropped the `integrity` diagnostics field, the `runnerIntegrityFailed` state, and the integrity short-circuit invariant (1.0.0 review remediation).
- 2026-05-30T21:33+02:00: Documented that the watcher probe now uses `DEFAULT_DOCKER_CONTROL_SECONDS` instead of the removed `timeout_caps["providerSeconds"]` key (renamed `providerSetupSeconds`). Verified against `825a172`.
- 2026-05-29T18:35+02:00: `_provider_capability`/`_provider_runtime`/`_watcher_state_from_up` return their `Literal` aliases (`ProviderCapability`/`ProviderRuntime`/`WatcherState`); behavior-preserving (commit `0549b28`).
- 2026-05-28T19:52+02:00: Updated after provider status split compact summaries from dedicated diagnostics and began returning Pydantic-modeled packets.
- 2026-05-28T12:32+02:00: Updated after provider status began persisting and returning current provider state snapshots.
- 2026-05-23T22:37+02:00: Created during quality-pass closeout after direct-closeout preview found the changed file lacked sidecar onboarding.
