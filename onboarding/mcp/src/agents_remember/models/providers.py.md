# mcp/src/agents_remember/models/providers.py

## Governing Overview

[overview.md](overview.md)

## Purpose

`providers.py` defines provider response models for compact readiness,
dedicated diagnostics, watcher lifecycle, GrepAI, and CodeGraphContext tools.

## Code Commentary

`ProviderSummary` and `ContextProviderItem` are the compact context-facing
shape: identity, runtime, capability, aggregate state, watcher state, and
target repo readiness. Their nullable `ok` fields default to `None` because
skipped or unknown provider checks may omit those fields after public payloads
are serialized with `exclude_none=True` and later re-validated.
`ProviderDiagnosticsResponse` is the detail surface for per-provider
diagnostics; since 2.5.1 its `rawStatus`/`currentState` bodies are filed to a
temp report and the documented `reportPath` field (also on
`ProviderWatchersResponse` and `RuntimeInstallResponse`) points at the full
detail while `currentStateFile` keeps pointing at the on-disk state.
Provider-native GrepAI and CGC tools use flexible response envelopes because
their service payloads can expose provider-specific fields.

## Invariants And Boundaries

- Context provider summaries should remain small enough for startup packets.
- Raw lifecycle status belongs in `ProviderDiagnosticsResponse`, not
  `ContextPacketV2`.
- Nullable provider `ok` fields that may be absent from public JSON must declare
  `= None`; `bool | None` without a default is required-nullable and fails a
  later validation pass after `exclude_none=True` drops the key.
- `GrepAIWatcherState` and `CGCWatcherState` make watcher state typed and
  distinguish workspace-level memory search from per-repo code graph watchers.

## Evidence

### Repo-Internal References

- Provider status projection builds these models before returning MCP payloads. [1]
- Provider application entry point functions expose provider status, diagnostics, watcher, GrepAI, and CGC operations. [2]
