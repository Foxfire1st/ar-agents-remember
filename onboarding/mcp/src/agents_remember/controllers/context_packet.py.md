# mcp/src/agents_remember/controllers/context_packet.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/controllers/context_packet.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-24T02:47+02:00                     |
| lastVerifiedCommitHash | `b25d52f2b445554bb64115db2f27fd156954bcf3` |
| lastVerifiedCommitDate | 2026-05-24T02:36:33+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`context_packet.py` builds the versioned startup packet that agents use to
learn repository, coordination, memory, worktree, provider, and optional drift
state from MCP settings.

## Code Commentary

### Logic

`build_context_packet()` resolves the allowed repo id, builds coordination
context, collects Git facts, composes provider and worktree status, and adds a
drift packet only when requested. Drift summaries now come from
`memory_quality.integrity.onboarding_drift_check.summary`.

### Invariants And Boundaries

- Repo ids must be allowed by MCP settings.
- Context packets may report drift but should not mutate onboarding or start
  providers.
- Provider status and drift details are bounded by request limits.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Server/tool payloads call this controller for `context_packet`. | [tools.py](agents-remember-md/mcp/src/agents_remember/mcp/tools.py); [server.py](agents-remember-md/mcp/src/agents_remember/mcp/server.py) |
| Drift summaries are owned by the memory quality integrity subdomain. | [summary.py](agents-remember-md/mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/summary.py) |

## Update History

- 2026-05-24T02:47+02:00: Created after context packets imported drift summary from the new memory quality package.
