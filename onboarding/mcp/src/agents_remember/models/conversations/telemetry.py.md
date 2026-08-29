# mcp/src/agents_remember/models/conversations/telemetry.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/models/conversations/telemetry.py` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-29T17:23+02:00                                               |
| lastVerifiedCommitHash | `60e429d17e9fcbca3ab1c02563afcaa5761b8c5a`                                        |
| lastVerifiedCommitDate | 2026-08-29T20:33:10+02:00|
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

- 2026-08-29T17:23+02:00 — No content impact: reviewed `MetricEvidence` after its Python 3.13 lexical type-parameter migration and confirmed that metric value, evidence, scope, and provenance behavior remain as documented. Verification remains closeout-owned.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
