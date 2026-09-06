# mcp/tests/test_dispatch_brief.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | mcp/tests/test_dispatch_brief.py |
| doc_type | file-level-onboarding |
| lastUpdated | 2026-09-06T21:46+00:00 |
| lastVerifiedCommitHash | `f2b7c648f540efb9d64ceea22e11e651cb5cc914`|
| lastVerifiedCommitDate | 2026-08-31T15:32:32+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Durable initial dispatch-brief delivery and exact-target retry.

## Code Commentary

### Logic

Ready delivery creates one inbox-rooted landed row and meets the briefed-by expectation through the adapter. Rejected or not-ready delivery preserves one pending row. Ambiguous retry reconciles retained adapter truth without another submit; an exact missing agent target never redirects to a matching lifecycle.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

No raw paste fallback is allowed. A durable row ID is not embedded as prompt content, and unresolved acceptance must remain unconfirmed.

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
| Ready dispatch is inbox rooted lands and starts expectation clocks. | `test_ready_dispatch_is_inbox_rooted_lands_and_starts_expectation_clocks` | mcp/tests/test_dispatch_brief.py:148-173 |
| Rejected adapter receipt keeps same row pending. | `test_rejected_adapter_receipt_keeps_same_row_pending` | mcp/tests/test_dispatch_brief.py:176-184 |
| Ambiguous redelivery reconciles without resubmitting. | `test_ambiguous_redelivery_reconciles_without_resubmitting` | mcp/tests/test_dispatch_brief.py:187-233 |
| Not ready queues one durable dispatch row for plane retry. | `test_not_ready_queues_one_durable_dispatch_row_for_plane_retry` | mcp/tests/test_dispatch_brief.py:236-260 |
| Exact agent target never falls back to matching lifecycle. | `test_exact_agent_target_never_falls_back_to_matching_lifecycle` | mcp/tests/test_dispatch_brief.py:263-287 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:46+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-08-30T22:33:39+02:00 — 260821-ARSPAWN-L5 recorded the single bounded
  spawn-to-bridge readiness window and preserved no-resubmission semantics.

- 2026-08-11T19:58+02:00 — Reconciled `test_dispatch_brief.py` with its current structural task/seat, tool-vocabulary, or quality-boundary regression contract and removed stale exact-id/leaf implications where present.
- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-05T03:47+02:00 — 260731-EFA-L6 curator: replaced the placeholder body with the actual
  suite: inbox-rooted dispatch with expectation clocks, receipt/reconciliation handling, refusal
  and no-fallback pins, and canonical/packaged skill sync equality. Recorded that imports now come
  from `serving.dispatch_brief` after the tool-layer move. Verification metadata pinned until
  closeout stamps the code commit.
- 2026-07-31T15:32+02:00 — 260731-EFA-L2 curator: recorded the arms this leaf added; the rest of this card was re-read against the file and remains true. Call sites in this module now build parameter objects (see the route overview) — what the suite proves is unchanged. Verification metadata pinned until closeout stamps the code commit.

- 2026-07-14T13:59+02:00 — 260713-PHA-L5: reviewed hosted cutover impact and refreshed the body.

- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator refresh: final candidate onboarding; exact-session dispatch and serialized-writer/lock-free-reader concurrency recorded.
