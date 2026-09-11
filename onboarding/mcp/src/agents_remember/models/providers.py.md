# mcp/src/agents_remember/models/providers.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/models/providers.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-31T20:30+02:00     |
| lastVerifiedCommitHash | `205c0b664e7dbf6efd07c2c811d0d8295aa07c91` |
| lastVerifiedCommitDate | 2026-08-31T20:38:14+02:00|
| governingOverview      | `overview.md`                              |

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Provider status projection builds these models before returning MCP payloads. | `ProviderStatusProjection` | mcp/src/agents_remember/providers/status.py:38-50 |
| Provider application entry point functions expose provider status, diagnostics, watcher, GrepAI, and CGC operations. | `provider_status_tool`; `provider_diagnostics_tool`; `provider_watchers_tool`; `grepai_search_tool`; `cgc_symbol_search_tool` | mcp/src/agents_remember/application/provider_tools.py:32-37; mcp/src/agents_remember/application/provider_tools.py:40-45; mcp/src/agents_remember/application/provider_tools.py:48-87; mcp/src/agents_remember/application/provider_tools.py:273-303; mcp/src/agents_remember/application/provider_tools.py:343-356 |

## Update History

- 2026-08-31T20:30+02:00 — No content impact: corrected the source-file verification citation
  from the retired `mcp/tests/code_quality/` location to the current
  `mcp/test_support/agents_remember_test_support/code_quality/wire_contract.py` owner. Provider
  models and wire behavior are unchanged.

- 2026-08-08T22:10+02:00 — 260713-TES-L1 completion round 2 (curator): No content impact: the supervisor -> agent-notifier rename does not change the behavior this sidecar documents; reviewed current against the changed source. Verification metadata pinned until closeout stamps the 260713-TES-L1 commit.
- 2026-08-02T16:56+02:00 — 260731-EFA-L6 curator W1-B06: anchored 2 citation claims
  (Repo-Internal reference rows); scoped result 0 findings.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-06-10T05:30+02:00 — `ProviderDiagnosticsResponse` and `ProviderWatchersResponse` gain documented optional `reportPath` fields for the S4 response-budget compaction (2.5.1).
- 2026-06-09T22:10+02:00 — `ProviderSummary` gained the additive `indexing: list[str]` field (busy `"<provider-id>:<repo-id>"` targets with an initial scan in progress; empty when idle, default-factory so older payloads still validate). Released in 2.5.0.
- 2026-06-08T09:57+02:00: Made compact provider `ok` fields optional-null defaults so skipped provider summaries survive public payload serialization and re-validation.
- 2026-05-31T12:30+02:00 — Dropped `integrity` block from diagnostics commentary; `runnerIntegrityFailed` state and `ProviderDiagnosticsResponse.integrity` field removed (1.0.0 review remediation).
- 2026-05-28T19:52+02:00: Created for compact provider summaries and the dedicated diagnostics response contract.
