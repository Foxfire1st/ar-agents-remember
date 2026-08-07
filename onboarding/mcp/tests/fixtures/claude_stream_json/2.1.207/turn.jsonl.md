# turn.jsonl

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/fixtures/claude_stream_json/2.1.207/turn.jsonl` |
| doc_type | file-level-onboarding |
| lastUpdated | 2026-08-04T00:41+02:00 |
| lastVerifiedCommitHash | `b252c42cca200933d5c9c36e26de47a526a569ce` |
| lastVerifiedCommitDate | 2026-08-07T23:58:52+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview
[tests overview](../../../overview.md)

## Purpose
Retained locked-schema specimen for Claude 2.1.207 replay, assistant activity, API retry, and
successful terminal-result frames.

## Code Commentary
The four-frame sequence records replay correlation, assistant output, a non-terminal 529 retry,
and an explicit successful result. It remains schema evidence; the active fake-adapter regression
loads a separate 2.1.210 fixture root.

## Invariants And Boundaries
This exact 2.1.207 path is not a current test-loader target or a production version pin.
`api_retry` is non-terminal in the projector, and completion comes from the final successful
`result` frame.

## Repo-Internal References
No repository test loads this exact path. The projector names the locked 2.1.207 and 2.1.210
fixture cohorts as schema authority, while the active adapter suite is explicitly rooted at
2.1.210.

| Finding | Anchor | Source |
| --- | --- | --- |
| The specimen contains the replayed correlated user frame. | `isReplay` | mcp/tests/fixtures/claude_stream_json/2.1.207/turn.jsonl:1-1 |
| The specimen contains the API retry system frame. | `api_retry` | mcp/tests/fixtures/claude_stream_json/2.1.207/turn.jsonl:3-3 |
| The specimen contains the successful terminal result. | `result` | mcp/tests/fixtures/claude_stream_json/2.1.207/turn.jsonl:4-4 |
| The Claude projector names both locked fixture cohorts as schema authority; that is evidence provenance, not a direct file consumer. | `Schema` | mcp/src/agents_remember/serving/conversation/projectors/claude.py:3-3 |
| The focused loader is fixed to 2.1.210, and the correlated-turn regression obtains `turn.jsonl` through that loader rather than this path. | "FIXTURE_ROOT = Path(__file__).parent / \"fixtures\" / \"claude_stream_json\" / \"2.1.210\""; "def _load_fixture(name: str) -> list[dict[str, object]]:"; `test_correlated_acceptance_retry_activity_and_terminal_result_are_distinct` | mcp/tests/test_harness_control_claude.py:32-32; mcp/tests/test_harness_control_claude.py:41-42; mcp/tests/test_harness_control_claude_stream_1.py:392-433 |

## Update History
- 2026-08-04T03:21:00+02:00 — S18-SR3-B05 curator: retained the factually exact isReplay line-1 binding and regenerated only api_retry/result with the locked scoped fixer; inspected both generated ranges and preserved approved semantics.
- 2026-08-04T03:03:32+02:00 — S18-SR3-B05 worker: preserved the factual line-1 replay binding and returned only the manually authored `api_retry` and `result` ranges to provisional fixer input.
- 2026-08-04T02:35:12+02:00 — S18-B05 curator delta: resolved provisional source-local citation bindings with fixer-generated current-source ranges; no approved semantic claim changes.
- 2026-08-04T00:41:58+02:00 — 260731-EFA-L6 S18-SR1 worker: resolved the B05 report-only version-alignment
  residual. The 2.1.207 turn file has no direct test consumer; it remains locked-schema evidence
  named by the Claude projector, while the active fixture loader is rooted at 2.1.210. Replaced the
  stale consumer row with source-backed provisional bindings; preserved the prior curator entry and did
  not run citation mechanics. Verification metadata remains pinned until closeout stamps the L6
  code commit.
- 2026-08-04T00:22:04+02:00 — 260731-EFA-L6 S18-B05 curator: repaired and normalised mechanical citation findings with current source anchors and fixer-generated ranges; no semantic claim changes. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T01:42+02:00 — No content impact: corrected Source Path link depth. The link(s) in this document carried one `../` too many and had never resolved from this card's directory — not code moving out from under a citation, the path as written. Enumerating every depth in both trees leaves exactly one that resolves and it is exactly one level shallower, so there was nothing to judge (`memory_quality/style/citations`, `citation_link_depth_wrong`). No claim, range or target document changed. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-14T12:30+02:00 — 260713-PHA-L2 curator: created sidecar.
