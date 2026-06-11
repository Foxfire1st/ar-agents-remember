# mcp/tests/test_tokens.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_tokens.py`                 |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:30+02:00                     |
| lastVerifiedCommitHash | `c20a3292e667d227a3be0c1fb276f8a701df814f`                                         |
| lastVerifiedCommitDate |2026-05-31T14:17:11+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`test_tokens.py` is the first direct test coverage for the response
token-accounting engine in `models/tokens.py`.

## Code Commentary

The suite exercises both counters and both serializers in isolation:
`ApproximateTokenCounter` (name and `exact=False` flag, deterministic
compact-JSON length, empty-mapping floor of 1), `TiktokenTokenCounter` /
`DEFAULT_TOKEN_COUNTER` (name `tiktoken:o200k_base`, `exact=True`, positive
counts, and `count_response_tokens` delegation), `finalize_payload_tokens`
(stamps all three metadata fields, mutate-and-return identity, fixpoint
convergence under both counters), and `response_payload` /
`dump_with_token_count` (model serialization plus alias equivalence).

The load-bearing assertion is self-consistency: the reported `tokens` value must
equal a fresh `token_counter.count(payload)` over the finalized payload, which
proves the `_finalize_token_count` fixpoint converged after folding the token
metadata fields back into the counted JSON.

## Invariants And Boundaries

- The reported token count must stay self-consistent with a recount of the final
  payload; this guards against fixpoint non-convergence.
- Tests target the counting engine directly and do not exercise MCP dispatch;
  dispatch-level token coverage lives in `test_tools.py`.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Counting engine under test. | [tokens.py](agents-remember/mcp/src/agents_remember/models/tokens.py) |
| `PingResponse` is the representative `ResponseModel` used for the serializer tests. | [core.py](agents-remember/mcp/src/agents_remember/models/core.py) |

## Update History

- 2026-05-31T12:30+02:00 — `PingResponse` fixtures now source `version` from the imported `SERVER_VERSION` (`agents_remember.mcp`) instead of a hardcoded `0.9.6` literal, so they no longer need a per-release bump (1.0.0 review remediation).
- 2026-05-31T01:06+02:00: Updated the `PingResponse` fixtures' `version` to `0.9.6` (MCP 0.9.6); the fixtures stay version-agnostic for the token-count assertions. Verification metadata stays pinned until closeout commits the change.
- 2026-05-30T22:29+02:00: Created for the S6 token-counter wiring — first direct tests of the counting engine and the fixpoint self-consistency guarantee. Verification metadata pending closeout commit.
