# mcp/src/agents_remember/models/providers.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/models/providers.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-28T19:52+02:00                     |
| lastVerifiedCommitHash | `bf3a3c4e310fb11032da885083d026a74a31ee9c` |
| lastVerifiedCommitDate | 2026-05-28T20:06:49+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`providers.py` defines provider response models for compact readiness,
dedicated diagnostics, watcher lifecycle, GrepAI, and CodeGraphContext tools.

## Code Commentary

`ProviderSummary` and `ContextProviderItem` are the compact context-facing
shape: identity, runtime, capability, aggregate state, watcher state, and
target repo readiness. `ProviderDiagnosticsResponse` is the detail surface that
can include current-state files, integrity blocks, process namespace, raw
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

- 2026-05-28T19:52+02:00: Created for compact provider summaries and the dedicated diagnostics response contract.
