# skills/l-01-agent-lifecycles/roles

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | skills/l-01-agent-lifecycles/roles |
| doc_type | route-local-overview |
| lastUpdated | 2026-07-12T14:20:00+02:00 |
| lastVerifiedCommitHash | `cff3e8f9a64258ea3e7d3007e2153b22c01e273b`|
| lastVerifiedCommitDate | 2026-07-14T14:23:24+02:00|

## Purpose

Role-specific dispatch guidance shares the exact session-id handoff, ready proof, delivered-plus-harness-log-confirmed completion, launch-phase sessionCommands, and post-ready promptKeywords timing.

## Hot Path Summary

Role-specific dispatch guidance shares the exact session-id handoff, ready proof, delivered-plus-harness-log-confirmed completion, launch-phase sessionCommands, and post-ready promptKeywords timing.

### 260713-PHA-L5 Route Contract Review

Hosted role dispatch now relies on exact adapter readiness and correlated delivery evidence. The
durable inbox remains the message root, explicit recipient consume remains acknowledgement, and
pane/log classifiers are diagnostics-only. The packaged role briefs and source lifecycle guidance
must stay aligned with this contract.

## Update History

- 2026-07-14T13:59+02:00 — 260713-PHA-L5: reviewed route impact for the accepted hosted cutover.
- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator: established governing route coverage for the final candidate.
