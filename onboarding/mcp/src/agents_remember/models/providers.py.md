# mcp/src/agents_remember/models/providers.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/models/providers.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:30+02:00                     |
| lastVerifiedCommitHash | `c20a3292e667d227a3be0c1fb276f8a701df814f` |
| lastVerifiedCommitDate | 2026-05-31T14:17:11+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`providers.py` defines provider response models for compact readiness,
dedicated diagnostics, watcher lifecycle, GrepAI, and CodeGraphContext tools.

## Code Commentary

`ProviderSummary` and `ContextProviderItem` are the compact context-facing
shape: identity, runtime, capability, aggregate state, watcher state, and
target repo readiness. `ProviderDiagnosticsResponse` is the detail surface that
can include current-state files, process namespace, raw
status, and per-provider diagnostics. Provider-native GrepAI and CGC tools use
flexible response envelopes because their service payloads can expose
provider-specific fields.

## Invariants And Boundaries

- Context provider summaries should remain small enough for startup packets.
- Raw lifecycle status belongs in `ProviderDiagnosticsResponse`, not
  `ContextPacketV2`.
- `GrepAIWatcherState` and `CGCWatcherState` make watcher state typed and
  distinguish workspace-level memory search from per-repo code graph watchers.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Provider status projection builds these models before returning MCP payloads. | [status.py](agents-remember-md/mcp/src/agents_remember/providers/status.py) |
| Provider controller functions expose provider status, diagnostics, watcher, GrepAI, and CGC operations. | [provider_tools.py](agents-remember-md/mcp/src/agents_remember/controllers/provider_tools.py) |

## Update History

- 2026-05-31T12:30+02:00 — Dropped `integrity` block from diagnostics commentary; `runnerIntegrityFailed` state and `ProviderDiagnosticsResponse.integrity` field removed (1.0.0 review remediation).
- 2026-05-28T19:52+02:00: Created for compact provider summaries and the dedicated diagnostics response contract.
