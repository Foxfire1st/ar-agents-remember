# mcp/src/agents_remember/controllers/context_packet.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/controllers/context_packet.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-08T09:57+02:00                     |
| lastVerifiedCommitHash | `d92bc99c82eaa3e8d89ee9352075def2c66c1235` |
| lastVerifiedCommitDate | 2026-06-08T10:09:59+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`context_packet.py` builds the modeled `ContextPacketV2` startup packet that
agents use to learn repository, coordination, memory, worktree, provider, and
optional drift facts.

## Code Commentary

`build_context_packet()` resolves the allowed repo ID, builds coordination
context, reads Git facts, projects paths and memory state into explicit
Pydantic nested models, obtains read-only worktree status, obtains compact
provider summary status, and adds a drift summary only when requested. The
controller validates the serialized provider summary through
`ProviderSummary.model_validate(...)` before inserting it into the packet, then
returns the JSON-compatible model dump of `ContextPacketV2`.

Provider summary still performs the underlying provider status/current-state
read so runtime state remains current, but the context packet only receives
compact readiness, runtime, identity, watcher, target-repo, and recovery-action
facts. Detailed provider internals are intentionally moved to the
`provider_diagnostics` tool.

## Invariants And Boundaries

- Repo IDs must be allowed by MCP settings.
- `ContextPacketError` (the authority-gate failure raised when the request
  violates MCP authority settings) subclasses `AuthorityError` from
  `agents_remember.errors`, not bare `ValueError`.
- Context packet version is now `contextPacketVersion: 2`.
- Do not embed `rawStatus`, duplicated top-level `pathRules`, or full provider
  current-state payloads in this controller.
- Construct nested model objects explicitly, or validate raw service payloads
  at narrow adapter boundaries with `NestedModel.model_validate(...)`.
- Keep the provider-summary validation boundary in this controller; skipped
  provider fields that are omitted from JSON must be modeled as optional in the
  provider response model, not bypassed by removing validation here.
- Context packet construction may read provider status and write current-state
  snapshots through the provider status path; it must not start providers or
  mutate onboarding.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| `ContextPacketV2` and nested summary models define the response shape. | [context_packet.py](agents-remember-md/mcp/src/agents_remember/models/context_packet.py) |
| Provider summary projection keeps context compact and points details at diagnostics. | [status.py](agents-remember-md/mcp/src/agents_remember/providers/status.py) |
| Worktree status projection supplies the read-only worktree summary. | [status.py](agents-remember-md/mcp/src/agents_remember/worktrees/status.py) |
| Public payload builder validates this controller output through the model registry. | [core.py](agents-remember-md/mcp/src/agents_remember/mcp/tools/core.py) |

## Update History

- 2026-06-08T09:57+02:00: Restored the provider-summary model-validation boundary after skipped provider summaries moved the omitted nullable `ok` contract into the provider response model.
- 2026-06-06T12:28+02:00: Corrected the context-packet payload-builder reference after the former `mcp/tools.py` module became the `mcp/tools/` package; source behavior unchanged.
- 2026-05-31T12:50+02:00 — `ContextPacketError` re-typed to subclass `AuthorityError` (imported from `agents_remember.errors`) instead of `ValueError`; noted the new base in Invariants And Boundaries (1.0.0 review remediation).
- 2026-05-28T19:52+02:00: Updated after context packets moved to explicit `ContextPacketV2` model construction and compact provider summaries.
- 2026-05-24T02:47+02:00: Created after context packets imported drift summary from the new memory quality package.
