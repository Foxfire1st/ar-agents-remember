# mcp/tests/test_models.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/tests/test_models.py`                 |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-06T12:28+02:00                     |
| lastVerifiedCommitHash | `11f28a2035f06f8bc33f11b0617b41cda1122c1f` |
| lastVerifiedCommitDate | 2026-06-06T13:01:33+02:00|
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
| Public tool metadata lives in the `mcp/tools/` package. | [base.py](agents-remember-md/mcp/src/agents_remember/mcp/tools/base.py) |
| Response model registry lives in the models package. | [tool_registry.py](agents-remember-md/mcp/src/agents_remember/models/tool_registry.py) |

## Update History

- 2026-06-06T12:28+02:00: Corrected the public-tool metadata reference after the former `mcp/tools.py` module became the `mcp/tools/` package; source behavior unchanged.
- 2026-05-28T19:52+02:00: Created for public tool response model registry and schema coverage.
