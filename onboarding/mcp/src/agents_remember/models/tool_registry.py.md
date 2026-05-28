# mcp/src/agents_remember/models/tool_registry.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/models/tool_registry.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-28T19:52+02:00                     |
| lastVerifiedCommitHash | `bf3a3c4e310fb11032da885083d026a74a31ee9c` |
| lastVerifiedCommitDate | 2026-05-28T20:06:49+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`tool_registry.py` maps public MCP tool names to their response model classes.

## Code Commentary

`PUBLIC_TOOL_RESPONSE_MODELS` is the enforcement registry consumed by
`mcp.tools._tool_payload()`. It currently covers all public core, runtime,
memory, skill install, provider, worktree, and benchmark tools.

## Invariants And Boundaries

- The registry keys must equal `mcp.tools.PUBLIC_TOOLS`.
- Adding or removing a public tool requires updating this registry and the
  schema coverage tests.
- The registry is response-only; it does not own request validation.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Payload builders validate through this registry. | [tools.py](agents-remember-md/mcp/src/agents_remember/mcp/tools.py) |
| Tests assert exact coverage between `PUBLIC_TOOLS` and this registry. | [test_models.py](agents-remember-md/mcp/tests/test_models.py) |

## Update History

- 2026-05-28T19:52+02:00: Created for the public tool response model coverage registry.
