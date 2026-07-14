# harness_control_client.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/harness_control_client.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-14T13:59+02:00 |
| lastVerifiedCommitHash | `cff3e8f9a64258ea3e7d3007e2153b22c01e273b` |
| lastVerifiedCommitDate | 2026-07-14T14:23:24+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving overview](overview.md)

## Purpose

Synchronous exact-session client for the Unix control socket owned by a hosted harness runner.
It is the serving boundary for snapshots, correlated prompt submission, reconciliation,
interaction responses, transcript reads, and graceful or forced stop.

## Code Commentary

### Logic

Every request carries protocol version and catalog identity. Responses are schema-checked,
request-correlated, and converted into typed adapter snapshots, receipts, reconciliation results,
or transcript entries. Socket, timeout, malformed JSON, identity, and message-size failures become
`HarnessControlError`; this client never falls back to terminal input.

### Invariants And Boundaries

The catalog row's exact session identity and endpoint are authoritative. Acceptance is delivery
evidence, not inbox consumption. Vendor raw detail is retained additively while the caller owns
durable projection and gate policy.

## Docs References

No relevant external/domain documentation was configured; the local control protocol and tests are
the source of truth.

## Repo-Internal References

- [harness_control_models.py](harness_control_models.py) defines the wire value objects.
- [inbox_delivery.py](inbox_delivery.py) records receipts under durable inbox rows.
- [hosted_interactions.py](hosted_interactions.py) uses interaction and transcript operations.

## Cross-Repo References

No meaningful cross-repo references.

## Update History

- 2026-07-14T13:59+02:00 — 260713-PHA-L5: documented identity-bound protocol requests,
  correlated acceptance/reconciliation, interaction responses, and no raw-terminal fallback.
