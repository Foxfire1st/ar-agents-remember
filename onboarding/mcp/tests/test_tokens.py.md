# mcp/tests/test_tokens.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_tokens.py`                 |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:30+02:00                     |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`                                         |
| lastVerifiedCommitDate |2026-07-31T19:28:50+02:00|
| governingOverview      | `../overview.md`                              |

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

| Finding | Anchor | Source |
| --- | --- | --- |
| Counting engine under test. | `ApproximateTokenCounter`; `finalize_payload_tokens` | mcp/src/agents_remember/models/tokens.py:169-180; mcp/src/agents_remember/models/tokens.py:232-249 |
| `PingResponse` is the representative `ResponseModel` used for the serializer tests. | `PingResponse` | mcp/src/agents_remember/models/core.py:14-17 |

## Update History

- 2026-08-04T18:16+02:00 — 260731-EFA-L6 S18-B16 curator: repaired 2 citation rows: the counting engine (models/tokens.py L170-L275) and the representative `PingResponse` (models/core.py L14-L18). Scoped fixer + non-fixing recheck green under the frozen snapshot; verification metadata unchanged.

- 2026-07-31T16:35+02:00 — No content impact: the only change to `mcp/tests/test_tokens.py` since
  the L2 base commit is the whole-tree `ruff format` pass in `00e8379`, which re-wrapped 3 line(s)
  with no token change whatsoever. Checked by parsing both revisions and comparing the abstract
  syntax trees (identical) and the comment tokens (identical), so no symbol, signature, default,
  decorator, control-flow branch, docstring, or assertion this card describes has moved, and every
  claim this card makes about its own source still holds.

- 2026-05-31T12:30+02:00 — `PingResponse` fixtures now source `version` from the imported `SERVER_VERSION` (`agents_remember.mcp`) instead of a hardcoded `0.9.6` literal, so they no longer need a per-release bump (1.0.0 review remediation).
- 2026-05-31T01:06+02:00: Updated the `PingResponse` fixtures' `version` to `0.9.6` (MCP 0.9.6); the fixtures stay version-agnostic for the token-count assertions. Verification metadata stays pinned until closeout commits the change.
- 2026-05-30T22:29+02:00: Created for the S6 token-counter wiring — first direct tests of the counting engine and the fixpoint self-consistency guarantee. Verification metadata pending closeout commit.
