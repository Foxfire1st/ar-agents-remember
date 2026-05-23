# test_context_packet.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/tests/test_context_packet.py`         |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-23T18:05+02:00                     |
| lastVerifiedCommitHash | `3417d47f1e76d37e9ba6e803c7b28afa4758da9c` |
| lastVerifiedCommitDate | 2026-05-23T23:06:47+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`test_context_packet.py` verifies the package context-packet controller and CLI
against configured repository fixtures.

## Code Commentary

### Logic

The tests build temporary code and external-memory repositories, load MCP
settings, and assert that context packets report repo, memory, provider,
worktree, and drift state. Coverage includes successful external-memory
packets, optional drift summaries, unknown repo rejection before filesystem
resolution, non-Git repo error reporting, active worktree contract reporting,
and CLI JSON output.

### Invariants And Boundaries

The context packet is a read-oriented status surface. It should report provider
and worktree facts from configured MCP state without accepting arbitrary repo
ids or silently treating unavailable Git facts as trusted context.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The context packet controller builds the tested payload. | [context_packet.py](agents-remember-md/mcp/src/agents_remember/controllers/context_packet.py) |
| MCP config fixtures come from `test_config.py`. | [test_config.py](agents-remember-md/mcp/tests/test_config.py) |

## Update History

- 2026-05-23T18:05+02:00: Created during direct closeout prep for context-packet test coverage.
