# mcp/src/agents_remember/models/base.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/models/base.py`   |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-28T19:52+02:00                     |
| lastVerifiedCommitHash | `bf3a3c4e310fb11032da885083d026a74a31ee9c` |
| lastVerifiedCommitDate | 2026-05-28T20:06:49+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`base.py` defines the shared Pydantic primitives for modeled MCP responses.

## Code Commentary

`StrictResponseModel` forbids unknown fields for owned public contracts.
`FlexibleResponseModel` intentionally allows unknown fields for native/detail
payloads that must preserve provider or service output. `ResponseModel` and
`ToolResponse` add the shared `ok`, `tokens`, `tokenizer`, and
`tokenCountExact` fields plus JSON-compatible `to_payload()` serialization.

## Invariants And Boundaries

- Default to strict response models for public contracts.
- Use flexible envelopes only for intentionally raw/detail payloads.
- Token fields are part of the contract even before S6 calculates them from
  final serialized output.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Token serialization helpers consume `ToolResponse` instances. | [tokens.py](agents-remember/mcp/src/agents_remember/models/tokens.py) |
| Public tool payloads validate through concrete subclasses. | [tool_registry.py](agents-remember/mcp/src/agents_remember/models/tool_registry.py) |

## Update History

- 2026-05-28T19:52+02:00: Created for the shared Pydantic response primitives added during the response-contract work.
