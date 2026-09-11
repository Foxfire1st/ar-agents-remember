# mcp/tests/test_pi_rpc_process.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_pi_rpc_process.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:46+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489` |
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Actual Pi subprocess transport correlation and cancellation.

## Code Commentary

### Logic

A deterministic child replies to a correlated request, streams an event and exposes stderr before clean stop. EOF during an outstanding request is ambiguous with its original correlation ID. Cancellation discards a late response so the next request/reader can complete normally.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

The process boundary is real but the child is a fixture, not an installed Pi model session. Ambiguous receipt must not be reclassified as never sent.

### Todos

No file-local implementation change is requested by this reconciliation.

## Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain evidence applies to the file-local claims above. | N/A | N/A |

## Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

| Finding | Anchor | Source |
| --- | --- | --- |
| Correlates response streams event and stops cleanly. | `test_correlates_response_streams_event_and_stops_cleanly` | mcp/tests/test_pi_rpc_process.py:32-64 |
| Eof during correlated request is ambiguous. | `test_eof_during_correlated_request_is_ambiguous` | mcp/tests/test_pi_rpc_process.py:66-80 |
| Cancelled request ignores late response and next reader survives. | `test_cancelled_request_ignores_late_response_and_next_reader_survives` | mcp/tests/test_pi_rpc_process.py:82-110 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:46+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


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
