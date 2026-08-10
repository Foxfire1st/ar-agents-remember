# mcp/tests/test_pi_rpc_process.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_pi_rpc_process.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-16T01:21+02:00 |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb` |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Exercises the actual async Pi RPC subprocess transport at its process boundary, including
cancellation-safe correlation and bounded reclamation when vendor responses arrive late or never.

## Code Commentary

### Logic

Deterministic child scripts prove correlated responses plus event streaming and clean stop,
malformed stdout propagation, and EOF during a request as possible-send ambiguity.

The L3 cases cancel a request after it is written and prove that its eventual response is ignored
without killing the reader or contaminating the next request. A second case runs the no-response
path at 8 and 64 cancellations, then completes a fresh request. This proves that request
cancellation removes the pending future and does not create an unbounded late-response tombstone
store.

### Conventions

Tests use `unittest.IsolatedAsyncioTestCase` and self-contained Python child scripts. The
cancellation reclamation case checks two input sizes so boundedness is observable.

### Invariants And Boundaries

- Tests the real subprocess seam without installing Pi or mutating global tools.
- Transport failures remain typed and are not silently reclassified or retried.
- A cancelled request's late correlated response is stale and cannot satisfy the next reader.
- Cancelled requests whose responses never arrive leave no retained tombstones; the transport must
  remain usable after both tested volumes.

### Todos

None known for this leaf.

## Docs References

No Domain Documentation category is configured for this repository, so no live documentation
source was available for this test-file curation pass.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured Domain Documentation source was available to cite. | — | — |

## Repo-Internal References

The subprocess tests and transport implementation directly prove cancellation reclamation and
late-response behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| A cancelled request's eventual response is ignored and a separately correlated next request still completes. | `test_cancelled_request_ignores_late_response_and_next_reader_survives` | mcp/tests/test_pi_rpc_process.py:90-118 |
| Two-size coverage proves that 8 and 64 cancelled requests with no response require no retained tombstone store. | `test_cancelled_requests_without_responses_need_no_retained_tombstones` | mcp/tests/test_pi_rpc_process.py:120-151 |
| The transport removes a cancelled pending future, and response dispatch drops an id that has no live future instead of retaining it. | "if request_id in self._pending:"; "async def _dispatch(self" | mcp/src/agents_remember/serving/pi_rpc_process.py:90-112; mcp/src/agents_remember/serving/pi_rpc_process.py:221-238 |
| Strict frame decoding remains the protocol boundary used by the subprocess transport. | `PiRpcJsonlDecoder`; `_decode_frame` | mcp/src/agents_remember/serving/pi_rpc_protocol.py:59-103; mcp/src/agents_remember/serving/pi_rpc_protocol.py:383-394 |

## Cross-Repo References

No sibling repository is required to prove this process boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-03T04:00:52+02:00 — 260731-EFA-L6 W3-B06 curator: curated 8 citation findings for cancellation tests, pending-request dispatch, and strict frame decoding.

- 2026-07-31T16:35+02:00 — No content impact: the only change to `mcp/tests/test_pi_rpc_process.py`
  since the L2 base commit is the whole-tree `ruff format` pass in `00e8379`, which re-wrapped 1
  line(s) and normalised string quoting to double quotes. Checked by parsing both revisions and
  comparing the abstract syntax trees (identical) and the comment tokens (identical), so no
  symbol, signature, default, decorator, control-flow branch, docstring, or assertion this card
  describes has moved, and every claim this card makes about its own source still holds.

- 2026-07-16T01:21+02:00 — 260714-ACPUI-L3 curator: documented cancelled-request reclamation,
  stale late-response disposal, and two-size proof that no-response cancellations require no
  retained tombstones; normalized required sidecar sections and corrected the governing overview
  backlink. Verification metadata remains pinned until closeout stamps the L3 code commit.
- 2026-07-14T12:17+02:00 — 260713-PHA-L4 curator: created onboarding for subprocess correlation,
  malformed stdout, EOF ambiguity, and clean-stop tests.
