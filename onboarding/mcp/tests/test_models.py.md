# mcp/tests/test_models.py

## Governing Overview

[overview.md](../overview.md)

## Purpose

### STOP-delta current source contract

Existing whole-result model validation remains, with explicit absence pins for fields omitted by shaped answers. No synthetic field is injected to make a compact projection satisfy a whole-result predicate.

These are current source/assertion-carrier meanings. The qualified attempt14 CODE verdict is inherited, not a Curator test run, native freeze-currentness certification or independent MEMORY acceptance. Earlier contrary accounts are historical only; unaffected contracts and typed provenance remain.

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

- Existing whole-result model validation remains, with explicit absence pins for fields omitted by shaped answers. No synthetic field is injected to make a compact projection satisfy a whole-result predicate. [3]
