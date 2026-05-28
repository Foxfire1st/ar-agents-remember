# mcp/tests/test_models.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/tests/test_models.py`                 |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-28T19:52+02:00                     |
| lastVerifiedCommitHash | `bf3a3c4e310fb11032da885083d026a74a31ee9c` |
| lastVerifiedCommitDate | 2026-05-28T20:06:49+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`test_models.py` verifies the public MCP response model registry.

## Code Commentary

The tests assert that `PUBLIC_TOOL_RESPONSE_MODELS` has exactly the same keys
as `mcp.tools.PUBLIC_TOOLS` and that every registered response model can
generate JSON Schema. This catches public tool additions that forget to declare
a response contract and catches model definitions that are not schema-safe.

## Invariants And Boundaries

- Every public MCP tool requires a declared response model.
- Schema generation is the minimum static sanity check for model importability
  and inspectability.
- Request models are out of scope for this test file.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Public tool metadata lives in `mcp/tools.py`. | [tools.py](agents-remember-md/mcp/src/agents_remember/mcp/tools.py) |
| Response model registry lives in the models package. | [tool_registry.py](agents-remember-md/mcp/src/agents_remember/models/tool_registry.py) |

## Update History

- 2026-05-28T19:52+02:00: Created for public tool response model registry and schema coverage.
