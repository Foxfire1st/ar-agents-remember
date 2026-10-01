# mcp/tests/test_models.py

## Governing Overview

[overview.md](../overview.md)

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

## Evidence

### Repo-Internal References

- Public tool metadata lives in the `mcp/tools/` package. [1]
- Response model registry lives in the models package. [2]
