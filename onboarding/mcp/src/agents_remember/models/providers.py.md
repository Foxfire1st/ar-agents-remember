# mcp/src/agents_remember/models/providers.py

## Governing Overview

[overview.md](overview.md)

## Purpose

Retain provider state/response DTOs for legacy and internal backend consumers, not MCP tools.

## Code Commentary

Strict identities, target-repo states, watcher discriminators and ProviderSummary remain,
as do flexible provider-native responses. Nullable ok/watcher/refresh fields preserve unknown
state rather than coercing it into success; list fields default empty and watcher kinds
remain typed. ProviderSummary no longer has diagnosticsTool. Legacy status diagnostics and
watcher response shapes, metrics/indexState and reportPath fields still exist in this model
module, but removed MCP registrars/adapters do not make those operations callable. The current
context packet asks for a skipped projection, not provider readiness or restart permission.
No promise of current provider_diagnostics compaction is inferred from a retained DTO.

## Current model evidence

- Current source section contains excerpt `class ContextProviderItem(StrictResponseModel):`; DTO/control ownership is not execution acceptance. [3]

- Current source section contains excerpt `TOOL_RESPONSE_MODELS: dict[str, type[ResponseEnvelope]] = {`; DTO/control ownership is not execution acceptance. [4]

- Current source section contains excerpt `providers=ProviderSummary.model_validate(`; DTO/control ownership is not execution acceptance. [5]

## Historical superseded account (non-operative)

Prior removed-tool/current-roster claims below are preserved provenance, not current
registration, runtime capability or execution evidence.



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
