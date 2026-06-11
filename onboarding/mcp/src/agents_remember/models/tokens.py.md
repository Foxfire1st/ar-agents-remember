# mcp/src/agents_remember/models/tokens.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/models/tokens.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-30T22:29+02:00                     |
| lastVerifiedCommitHash | `5ccfed5b722ee34158b9533fb7e86e4196cfb569` |
| lastVerifiedCommitDate | 2026-05-30T22:38:37+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`tokens.py` owns token accounting helpers for modeled MCP responses.

## Code Commentary

The module counts tokens over compact, sorted JSON payloads (`_payload_json`
serializes with `ensure_ascii=False`, `separators=(",", ":")`, `sort_keys=True`).
The default counter, `DEFAULT_TOKEN_COUNTER`, is a `TiktokenTokenCounter` on the
`o200k_base` encoding (`exact=True`); an `ApproximateTokenCounter` (compact-JSON
character length divided by four) remains available as a deterministic fallback.

`finalize_payload_tokens()` stamps `tokenizer` and `tokenCountExact` onto an
already-serialized response dict, then resolves `tokens` through
`_finalize_token_count()`, which recounts until the value stops changing —
necessary because writing the count into the payload alters the payload's own
length. `response_payload()` serializes a model and delegates to
`finalize_payload_tokens()`, and `dump_with_token_count()` is its
backward-compatible alias. Both serializers accept any `ResponseModel`, not only
operation-bearing `ToolResponse` envelopes, because the token fields live on the
shared `ResponseModel` base and the dispatch path stamps tokens onto
operation-less responses such as `ping`.

## Invariants And Boundaries

- Token counts are response-overhead metadata, not session/task logging.
- The MCP dispatch path applies these counts at the single choke point
  `_tool_payload()` (`mcp/tools/base.py`), which calls `finalize_payload_tokens()`
  on every public tool response.
- Use the canonical JSON form here when writing token-budget tests.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Shared response envelopes define the token metadata fields on the `ResponseModel` base. | [base.py](agents-remember/mcp/src/agents_remember/models/base.py) |
| `_tool_payload` finalizes token metadata on every public tool response via this module. | [tools/base.py](agents-remember/mcp/src/agents_remember/mcp/tools/base.py) |
| Direct tests for the counters, serializers, and the fixpoint self-consistency guarantee. | [test_tokens.py](agents-remember/mcp/tests/test_tokens.py) |

## Update History

- 2026-05-30T22:29+02:00: S6 wiring completed — `_tool_payload` now calls the new `finalize_payload_tokens()` so every MCP response carries a real `tokens`/`tokenizer`/`tokenCountExact` instead of the Pydantic defaults; `response_payload`/`dump_with_token_count` were widened to accept any `ResponseModel`. Removed the pre-S6 "placeholder defaults" note and repaired the stale `mcp/tools.py` reference to `mcp/tools/base.py`. Verification metadata stays pinned until closeout commits the source change.
- 2026-05-28T19:52+02:00: Created for the token-accounting model helpers planned for S6 wiring.
