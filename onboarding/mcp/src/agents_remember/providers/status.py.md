# mcp/src/agents_remember/providers/status.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/status.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:30+02:00|
| lastVerifiedCommitHash | `c20a3292e667d227a3be0c1fb276f8a701df814f` |
| lastVerifiedCommitDate | 2026-05-31T14:17:11+02:00|
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

`status.py` reads provider watcher state and projects it into either compact
provider summaries or detailed provider diagnostics.

## Code Commentary

`provider_status_packet()` wraps a compact `ProviderSummary` in the public
`ProviderStatusResponse`. `provider_summary_packet()` returns just the compact
summary for `ContextPacketV2`. `provider_diagnostics_packet()` returns the
dedicated diagnostics contract with current-state, process-namespace,
recovery-action, raw-status, and per-provider raw status detail.

When status is read, lifecycle settings are generated from trusted MCP
settings, watcher status is invoked, and the current provider state file is
written under the coordinator log/status root. The watcher probe runs as a
bounded docker-control command timed by `DEFAULT_DOCKER_CONTROL_SECONDS`; it no
longer reads the removed `timeout_caps["providerSeconds"]` key (renamed to
`providerSetupSeconds`, which caps only provider setup, not status probing). Context packet callers receive
the current-state file path and summary facts, not the full raw status tree.

## Invariants And Boundaries

- `context_packet` uses `provider_summary_packet()`, not diagnostics/raw status.
- `provider_diagnostics` is the detail surface for raw provider state.
- Temporary lifecycle settings come from MCP settings and are deleted after the
  status read.
- Provider status is read-only from the MCP caller perspective; setup history
  belongs in provider setup summary logs.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Provider response models define summary, diagnostics, watcher, and native provider payload shapes. | [providers.py](agents-remember-md/mcp/src/agents_remember/models/providers.py) |
| Context packet construction consumes the compact provider summary. | [context_packet.py](agents-remember-md/mcp/src/agents_remember/controllers/context_packet.py) |
| Provider MCP controllers expose status, diagnostics, watcher, GrepAI, and CGC tools. | [provider_tools.py](agents-remember-md/mcp/src/agents_remember/controllers/provider_tools.py) |
| Current-state projection and persistence live in the current-state module. | [current_state.py](agents-remember-md/mcp/src/agents_remember/providers/current_state.py) |

## Update History

- 2026-05-31T12:30+02:00 — Removed runner-integrity documentation: status projection no longer checks provider runner integrity, dropped the `integrity` diagnostics field, the `runnerIntegrityFailed` state, and the integrity short-circuit invariant (1.0.0 review remediation).
- 2026-05-30T21:33+02:00: Documented that the watcher probe now uses `DEFAULT_DOCKER_CONTROL_SECONDS` instead of the removed `timeout_caps["providerSeconds"]` key (renamed `providerSetupSeconds`). Verified against `825a172`.
- 2026-05-29T18:35+02:00: `_provider_capability`/`_provider_runtime`/`_watcher_state_from_up` return their `Literal` aliases (`ProviderCapability`/`ProviderRuntime`/`WatcherState`); behavior-preserving (commit `0549b28`).
- 2026-05-28T19:52+02:00: Updated after provider status split compact summaries from dedicated diagnostics and began returning Pydantic-modeled packets.
- 2026-05-28T12:32+02:00: Updated after provider status began persisting and returning current provider state snapshots.
- 2026-05-23T22:37+02:00: Created during quality-pass closeout after direct-closeout preview found the changed file lacked sidecar onboarding.
