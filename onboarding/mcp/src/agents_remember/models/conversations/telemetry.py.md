# mcp/src/agents_remember/models/conversations/telemetry.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/models/conversations/telemetry.py` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-07T22:45:00+02:00                                            |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                                        |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[models conversations overview](overview.md)

## Purpose

260731-EFA-L7 split module moved verbatim by 260731-EFA-L9 from
`serving/conversation/_models_telemetry.py` to `models/conversations/telemetry.py`; owns the
telemetry, runtime-fixture evidence, and fingerprint behaviours named by its top-level symbols.

## Code Commentary

- `MetricScope`
- `MetricEvidence`
- `ContextMetricValue`
- `UsageMetricValue`
- `CostMetricValue`
- `RateLimitMetricValue`
- `CompactionMetricValue`
- `ConversationTelemetry`
- `RuntimeFixtureObservation`
- `RuntimeFixtureEvidence`
- `operation_fingerprint`

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/agents_remember/models/conversations/telemetry.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module. | — | — |

## Update History

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
