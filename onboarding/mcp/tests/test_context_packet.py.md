# test_context_packet.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/tests/test_context_packet.py`         |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-28T19:52+02:00                     |
| lastVerifiedCommitHash | `bf3a3c4e310fb11032da885083d026a74a31ee9c` |
| lastVerifiedCommitDate | 2026-05-28T20:06:49+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`test_context_packet.py` verifies the package context-packet controller and CLI
against configured repository fixtures.

## Code Commentary

### Logic

The tests build temporary code and external-memory repositories, load MCP
settings, and assert that context packets report repo, memory, compact provider
summary, worktree, and drift state. Coverage includes successful
external-memory packets, V2 field placement, provider current-state file path
reporting without embedded raw status, optional drift summaries, unknown repo
rejection before filesystem resolution, non-Git repo error reporting, active
worktree contract reporting without worktree raw status, and CLI JSON output.

### Invariants And Boundaries

The context packet is a read-oriented bootstrap surface. It should report
provider and worktree facts from configured MCP state, but provider raw status
and full worktree manager payloads belong outside `ContextPacketV2`. The V2
contract keeps path rules under `memory.storage.pathRules` and points provider
detail consumers at `provider_diagnostics`.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The context packet controller builds the tested payload. | [context_packet.py](agents-remember-md/mcp/src/agents_remember/controllers/context_packet.py) |
| `ContextPacketV2` defines the compact public response contract. | [context_packet.py](agents-remember-md/mcp/src/agents_remember/models/context_packet.py) |
| MCP config fixtures come from `test_config.py`. | [test_config.py](agents-remember-md/mcp/tests/test_config.py) |

## Update History

- 2026-05-28T19:52+02:00: Updated after context packet tests moved to `ContextPacketV2`, rejected duplicate top-level path rules, and rejected embedded provider/worktree raw status.
- 2026-05-28T12:32+02:00: Updated after context packets began exposing provider current-state files and aggregate current state.
- 2026-05-23T18:05+02:00: Created during direct closeout prep for context-packet test coverage.
