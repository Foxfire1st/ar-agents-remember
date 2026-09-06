# test_hosted_interactions.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_hosted_interactions.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:46+00:00 |
| lastVerifiedCommitHash | `f2b7c648f540efb9d64ceea22e11e651cb5cc914` |
| lastVerifiedCommitDate | 2026-08-31T15:32:32+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Durable hosted interactions and bounded delivery retry.

## Code Commentary

### Logic

Pending adapter questions become exact durable gates. A successful response applies the gate. Pre-write failure retains the decision for bounded retry then reopens after exhaustion; post-write uncertainty reopens with failure evidence and does not answer again. Ambiguous null-request-ID vendor correlation leaves inbox rows accepted rather than falsely completed.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Not-sent and unknown delivery have different retry rights. Developer decision attribution is preserved in failure evidence when an interaction is handed back.

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
| Pending interaction round trips through durable gate. | `test_pending_interaction_round_trips_through_durable_gate` | mcp/tests/test_hosted_interactions.py:70-91 |
| Failed respond reopens the gate instead of silently swallowing. | `test_failed_respond_reopens_the_gate_instead_of_silently_swallowing` | mcp/tests/test_hosted_interactions.py:94-128 |
| Pre write failure keeps the decision and retries until the budget runs out. | `test_pre_write_failure_keeps_the_decision_and_retries_until_the_budget_runs_out` | mcp/tests/test_hosted_interactions.py:150-200 |
| Post write failure hands the decision back without re answering. | `test_post_write_failure_hands_the_decision_back_without_re_answering` | mcp/tests/test_hosted_interactions.py:203-226 |
| Null request id completion rejects ambiguous vendor correlation. | `test_null_request_id_completion_rejects_ambiguous_vendor_correlation` | mcp/tests/test_hosted_interactions.py:229-279 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:46+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-08-31T10:13+02:00 — 260821-ARSPAWN-L5 closeout repair: extended direct request-id
  completion proof to initially queued inbox rows while preserving strict null-id correlation.
  Verification remains closeout-owned.

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-07-31T16:50+02:00 — 260731-EFA-L2 curator: records the Purpose-line correction made
  earlier in this task, where the pinned Pi evidence version was changed from `0.80.6` to
  `0.80.7` to match the locked helper — the conversation-library helper's
  `PI_CODING_AGENT_VERSION` constant and its `@earendil-works/pi-coding-agent` package pin are
  both `0.80.7`, and its `protocol.test.ts` asserts that exact string; the version never appears
  in this test file itself, so it is provenance only and the surrounding
  acceptance-versus-consumption claims are untouched. Also records this leaf's source change:
  every `decide_gate` call now passes a `GateVerdict` instead of the four loose
  `decision`/`by`/`via`/`note` keywords, and the three inbox fixtures build their rows through
  `InboxMessage`/`InboxAddress`/`InboxRouting`/`InboxPoster`, so a Conventions section was added
  naming both call shapes. No test case or assertion changed; the rest of the diff is
  `ruff format` reflow of the `mock.patch` and set-comprehension lines.

- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: refreshed the regression-coverage record for the current backend/shared behavior and preserved the pre-commit verification stamp.
- 2026-07-14T17:18:47+02:00 — 260713-PHA-L6 curator: added Codex completion-correlation projection and
  explicit pending/unconsumed plus no-replacement terminal-state coverage.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: added durable interaction and non-consumption regression coverage.
