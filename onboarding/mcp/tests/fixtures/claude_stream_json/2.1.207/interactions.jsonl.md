# interactions.jsonl

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/fixtures/claude_stream_json/2.1.207/interactions.jsonl` |
| doc_type | file-level-onboarding |
| lastUpdated | 2026-08-14T14:49:13+02:00 |
| lastVerifiedCommitHash | `409891a4bea54f3b6c3a125611afe54c41cca661` |
| lastVerifiedCommitDate | 2026-07-14T10:43:35+02:00 |
| governingOverview | `../../../overview.md` |

## Governing Overview
[tests overview](../../../overview.md)

## Purpose
Pinned permission and AskUserQuestion control-request frames.

## Code Commentary
Exercises correlated durable interaction routing without credentials or model content.

## Invariants And Boundaries
Fixtures are bounded protocol evidence and do not authorize automatic responses.

## Repo-Internal References
| Finding | Anchor | Source |
| --- | --- | --- |

## Update History
- 2026-08-14T14:49:13+02:00 — No content impact: repaired the incomplete verification pair for
  release carryover by adding the actual date of existing source commit
  `409891a4bea54f3b6c3a125611afe54c41cca661`. Fixture meaning, claims, and routing are unchanged.

- 2026-08-04T12:19:51+02:00 — 260731-EFA-L6 S18-B01 curator: reconciled the bounded worker ledger; source-clear citations were repaired, split, rewritten, or deleted as applicable, then the exact scoped fixer/check passed.
- 2026-08-02T01:42+02:00 — No content impact: corrected Source Path link depth. The link(s) in this document carried one `../` too many and had never resolved from this card's directory — not code moving out from under a citation, the path as written. Enumerating every depth in both trees leaves exactly one that resolves and it is exactly one level shallower, so there was nothing to judge (`memory_quality/style/citations`, `citation_link_depth_wrong`). No claim, range or target document changed. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-14T12:30+02:00 — 260713-PHA-L2 curator: created sidecar.
