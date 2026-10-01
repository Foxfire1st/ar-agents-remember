# mcp/src/agents_remember/models/conversations/telemetry.py

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

`RuntimeFixtureEvidence` records a runtime observation with its runtime version, capture time,
production seam, and declared `allowlist-v1` redaction policy. Its `enables_capabilities` field is
literally false: a recording, version pin, or fixture count cannot enable a runtime capability.
Each observation retains an explicit reason and distinguishes `observed`, `partial`, `unavailable`,
and `not-exercised`; unavailable operations must not be rewritten as successful observations.
The model validates these evidence fields, not whether arbitrary captured text was actually redacted.

cit:([`RuntimeFixtureObservation`], mcp/src/agents_remember/models/conversations/telemetry.py:80-84)
cit:([`RuntimeFixtureEvidence`], mcp/src/agents_remember/models/conversations/telemetry.py:87-97)

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/agents_remember/models/conversations/telemetry.py`.

## Evidence

### Repo-Internal References

The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module.
