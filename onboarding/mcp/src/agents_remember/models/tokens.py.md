# mcp/src/agents_remember/models/tokens.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/models/tokens.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-28T19:52+02:00                     |
| lastVerifiedCommitHash | `bf3a3c4e310fb11032da885083d026a74a31ee9c` |
| lastVerifiedCommitDate | 2026-05-28T20:06:49+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`tokens.py` owns token accounting helpers for modeled MCP responses.

## Code Commentary

The module counts tokens over compact, sorted JSON payloads. The default
counter uses `tiktoken` with the `o200k_base` encoding; an approximate JSON
character counter remains available as a deterministic fallback. `response_payload()`
serializes a `ToolResponse`, fills `tokens`, `tokenizer`, and
`tokenCountExact`, and iterates until the count includes the token metadata
fields themselves.

## Invariants And Boundaries

- Token counts are response-overhead metadata, not session/task logging.
- S6 wires this helper into the final MCP payload path; before that, models
  carry placeholder token fields through normal Pydantic defaults.
- Use the canonical JSON form here when writing token-budget tests.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Shared response envelopes define the token metadata fields. | [base.py](agents-remember-md/mcp/src/agents_remember/models/base.py) |
| Public tool payloads currently validate through models before S6 token calculation is wired. | [tools.py](agents-remember-md/mcp/src/agents_remember/mcp/tools.py) |

## Update History

- 2026-05-28T19:52+02:00: Created for the token-accounting model helpers planned for S6 wiring.
