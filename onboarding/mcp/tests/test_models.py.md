# mcp/tests/test_models.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_models.py`                 |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-06T12:28+02:00                     |
| lastVerifiedCommitHash | `1580f92715ff93c988f9a15439ad9bec60ef4c5d` |
| lastVerifiedCommitDate | 2026-08-13T00:18:59+02:00|
| governingOverview      | `../overview.md`                              |

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

| Finding | Anchor | Source |
| --- | --- | --- |
| Public tool metadata lives in the `mcp/tools/` package. | "def _tool_payload" | mcp/src/agents_remember/mcp/tools/base.py:72-72 |
| Response model registry lives in the models package. | `INTERNAL_COMPAT_TOOL_NAMES` | mcp/src/agents_remember/models/tool_registry.py:113-134 |

## Update History
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B21 curator: replaced the `n/a` rows with exact
  anchors and fixer-generated ranges; exact non-fixing check returns zero findings.

- 2026-06-06T12:28+02:00: Corrected the public-tool metadata reference after the former `mcp/tools.py` module became the `mcp/tools/` package; source behavior unchanged.
- 2026-05-28T19:52+02:00: Created for public tool response model registry and schema coverage.
