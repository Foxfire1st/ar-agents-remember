# mcp/src/agents_remember/models/context_packet.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/models/context_packet.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-28T19:52+02:00                     |
| lastVerifiedCommitHash | `bf3a3c4e310fb11032da885083d026a74a31ee9c` |
| lastVerifiedCommitDate | 2026-05-28T20:06:49+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`context_packet.py` defines `ContextPacketV2`, the compact startup/bootstrap
response contract for `context_packet`.

## Code Commentary

The model separates repository Git facts, resolved paths, memory/storage facts,
worktree summary, provider summary, and drift summary into explicit nested
objects. `ContextPacketV2` fixes `contextPacketVersion` to `2` and carries a
diagnostics hint pointing agents at `provider_diagnostics` for raw provider
details.

## Invariants And Boundaries

- `memory.storage.pathRules` is the only path-rule location in the context
  packet contract.
- `rawStatus`, provider current-state internals, and duplicated raw provider
  payloads do not belong in `ContextPacketV2`.
- Nested model objects should be built explicitly or validated at narrow raw
  adapter boundaries.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The context controller constructs `ContextPacketV2` from resolver, Git, provider, worktree, and drift facts. | [context_packet.py](agents-remember-md/mcp/src/agents_remember/controllers/context_packet.py) |
| Provider readiness in the packet uses compact provider summary models. | [providers.py](agents-remember-md/mcp/src/agents_remember/models/providers.py) |

## Update History

- 2026-05-28T19:52+02:00: Created after context packets moved to the compact V2 Pydantic contract.
