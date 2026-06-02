# mcp/src/agents_remember/providers/current_state.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/current_state.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-28T12:32+02:00                     |
| lastVerifiedCommitHash | `dc25f5a63de359926985c925096aad9019968bf4` |
| lastVerifiedCommitDate | 2026-06-02T18:31:01+02:00|
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

`current_state.py` projects provider watcher status into the current runtime
truth that MCP callers should read. It writes the latest provider state to
`logs/providers/status/<scope>/<instance>/current.json` under the coordination
root.

## Code Commentary

### Logic

`build_current_provider_state()` captures the check time, maps raw watcher
status into per-provider state, computes an aggregate state, and returns a
versioned `provider-current-state` payload. `write_current_provider_state()`
persists that payload beside the central provider status logs. Instance path
selection uses a shared provider scope/id when all configured providers match,
or a deterministic mixed digest when the config combines multiple provider
instances.

The provider mappers keep GrepAI and CGC shapes separate. GrepAI state records
PostgreSQL, Ollama, and watcher resources plus `watcherUp` and indexing state.
CGC state records the shared FalkorDB backend plus one watcher resource per
repo. Disabled configured providers are represented explicitly as `disabled`
and do not poison aggregate readiness.

GrepAI readiness is additionally gated on workspace presence.
`grepai_workspace_present()` inspects the watcher's `workspaceStatus` **stdout**
(not just its exit code, because `grepai workspace status` exits 0 even when it
prints "No workspaces configured"). `grepai_current_state()` downgrades a
container-ready GrepAI to `degraded` when no searchable workspace exists, and
`grepai_indexing_state()` reports `noWorkspace` in that case (`unknown` when a
workspace is present but indexing progress is unreported).

### Invariants And Boundaries

- This file reports what is true now; it must not embed last-setup history.
- Disabled providers are current state, not failures.
- Current state is refreshed when the agent asks the MCP for provider status or
  a context packet that includes providers.
- The file does not start, stop, or repair providers; it normalizes status
  facts produced by lifecycle watchers.
- GrepAI is only `ready` when its watcher reports a real, searchable workspace;
  container liveness alone is not readiness. A missing/empty workspace is
  `degraded` with `indexingState: noWorkspace`. Indexing progress for a present
  workspace stays conservative (`unknown`) until the provider exposes a precise
  signal.

### Todos

- Replace GrepAI `unknown` indexing state with real progress when the watcher
  returns an auditable indexing signal.

## Docs References

No external documentation is needed for this local status projection.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation is needed for this provider state projection. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Current state payloads include version, kind, instance, aggregate state, `ok`, check time, settings file, enabled providers, process namespace, and per-provider state. | L16-L34 | [current_state.py](agents-remember-md/mcp/src/agents_remember/providers/current_state.py) |
| Current state files are written under `logs/providers/status/<scope>/<instance>/current.json`. | L37-L58 | [current_state.py](agents-remember-md/mcp/src/agents_remember/providers/current_state.py) |
| Instance identity uses the shared configured provider scope/id or a deterministic mixed digest when providers differ. | L61-L82 | [current_state.py](agents-remember-md/mcp/src/agents_remember/providers/current_state.py) |
| GrepAI and CGC status mappers keep provider-specific resources, watcher state, and indexing state separate. | L85-L174 | [current_state.py](agents-remember-md/mcp/src/agents_remember/providers/current_state.py) |
| GrepAI readiness is gated on workspace presence: `grepai_workspace_present` reads the watcher `workspaceStatus` stdout, `grepai_current_state` downgrades to `degraded`, and `grepai_indexing_state` returns `noWorkspace` when absent. | L131-L160, L256-L283 | [current_state.py](agents-remember-md/mcp/src/agents_remember/providers/current_state.py) |
| Container normalization keeps container state, running flag, started-at time, uptime seconds, and health in the current-state payload. | L196-L226 | [current_state.py](agents-remember-md/mcp/src/agents_remember/providers/current_state.py) |
| Aggregate state ignores disabled providers and reports ready, degraded, failed, unknown, disabled, or noProviders from current provider facts. | L229-L253 | [current_state.py](agents-remember-md/mcp/src/agents_remember/providers/current_state.py) |
| Provider status writes this current-state payload and returns both the file path and current-state object to MCP callers. | L64-L80 | [status.py](agents-remember-md/mcp/src/agents_remember/providers/status.py) |
| Unit tests assert the file path, current truth shape, disabled-provider behavior, workflow-local instance paths, and provider-status integration. | L42-L174 | [test_provider_current_state.py](agents-remember-md/mcp/tests/test_provider_current_state.py) |

## Cross-Repo References

No sibling repository boundary is needed to explain this file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-06-02T16:24+02:00: GrepAI readiness gated on workspace presence — `grepai_workspace_present()` reads the watcher `workspaceStatus` stdout; container-ready GrepAI with no searchable workspace is now `degraded` / `indexingState: noWorkspace`.
- 2026-05-28T12:32+02:00: Created after provider status gained a current-state projection separate from setup history.
