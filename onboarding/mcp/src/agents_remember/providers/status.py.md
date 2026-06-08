# mcp/src/agents_remember/providers/status.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/status.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-08T09:57+02:00|
| lastVerifiedCommitHash | `d92bc99c82eaa3e8d89ee9352075def2c66c1235` |
| lastVerifiedCommitDate | 2026-06-08T10:09:59+02:00|
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

When status is read, lifecycle settings are generated from trusted MCP
settings, watcher status is invoked, and the current provider state file is
written under the coordinator log/status root. The watcher probe runs as a
bounded docker-control command timed by `DEFAULT_DOCKER_CONTROL_SECONDS`; it no
longer reads the removed `timeout_caps["providerSeconds"]` key (renamed to
`providerSetupSeconds`, which caps only provider setup, not status probing).
Context packet callers receive the current-state file path and summary facts,
not the full raw status tree.

`_provider_recovery_actions()` preserves raw lifecycle recovery actions and adds
shared restart guidance when the current projected GrepAI state has
`indexingState == "noWorkspace"`. The same action list is returned from compact
provider status and provider diagnostics so the model sees the same
non-destructive next step from either surface.

## Invariants And Boundaries

- `context_packet` uses `provider_summary_packet()`, not diagnostics/raw status.
- `provider_diagnostics` is the detail surface for raw provider state.
- A skipped provider projection reports aggregate skipped state only; it does
  not emit per-provider summary rows with unknown or omitted `ok` fields.
- Temporary lifecycle settings come from MCP settings and are deleted after the
  status read.
- Provider status is read-only from the MCP caller perspective; setup history
  belongs in provider setup summary logs.
- `noWorkspace` remains a degraded state; status adds restart/rebind guidance
  rather than treating missing workspaces as acceptable readiness.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Provider response models define summary, diagnostics, watcher, and native provider payload shapes. | [providers.py](agents-remember-md/mcp/src/agents_remember/models/providers.py) |
| Context packet construction consumes the compact provider summary. | [context_packet.py](agents-remember-md/mcp/src/agents_remember/controllers/context_packet.py) |
| Provider MCP controllers expose status, diagnostics, watcher, GrepAI, and CGC tools. | [provider_tools.py](agents-remember-md/mcp/src/agents_remember/controllers/provider_tools.py) |
| Current-state projection and persistence live in the current-state module. | [current_state.py](agents-remember-md/mcp/src/agents_remember/providers/current_state.py) |
| Restart/rebind recovery wording is shared with runtime-install recovery reporting. | [recovery.py](agents-remember-md/mcp/src/agents_remember/providers/recovery.py) |
| Provider status appends restart guidance when projected GrepAI state reports `indexingState: noWorkspace`. | [status.py](agents-remember-md/mcp/src/agents_remember/providers/status.py) |
| Provider current-state tests assert `noWorkspace` stays degraded and that status/diagnostics return the restart recovery action. | [test_provider_current_state.py](agents-remember-md/mcp/tests/test_provider_current_state.py) |

## Update History

- 2026-06-08T09:57+02:00: Documented skipped-provider summary behavior: when provider details are skipped, compact summary `items` is empty rather than populated from missing current-state rows.
- 2026-06-04T22:15+02:00 — Documented shared provider restart/rebind recovery guidance for GrepAI `noWorkspace`, including matching compact status and diagnostics recovery actions.
- 2026-05-31T12:30+02:00 — Removed runner-integrity documentation: status projection no longer checks provider runner integrity, dropped the `integrity` diagnostics field, the `runnerIntegrityFailed` state, and the integrity short-circuit invariant (1.0.0 review remediation).
- 2026-05-30T21:33+02:00: Documented that the watcher probe now uses `DEFAULT_DOCKER_CONTROL_SECONDS` instead of the removed `timeout_caps["providerSeconds"]` key (renamed `providerSetupSeconds`). Verified against `825a172`.
- 2026-05-29T18:35+02:00: `_provider_capability`/`_provider_runtime`/`_watcher_state_from_up` return their `Literal` aliases (`ProviderCapability`/`ProviderRuntime`/`WatcherState`); behavior-preserving (commit `0549b28`).
- 2026-05-28T19:52+02:00: Updated after provider status split compact summaries from dedicated diagnostics and began returning Pydantic-modeled packets.
- 2026-05-28T12:32+02:00: Updated after provider status began persisting and returning current provider state snapshots.
- 2026-05-23T22:37+02:00: Created during quality-pass closeout after direct-closeout preview found the changed file lacked sidecar onboarding.
