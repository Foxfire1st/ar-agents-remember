# test_hosted_interactions.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_hosted_interactions.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-14T13:59+02:00 |
| lastVerifiedCommitHash | `cff3e8f9a64258ea3e7d3007e2153b22c01e273b` |
| lastVerifiedCommitDate | 2026-07-14T14:23:24+02:00|
| governingOverview | `overview.md` |

## Governing Overview
[tests overview](overview.md)

## Purpose
Proves pending adapter interactions become durable gates, responses use the exact interaction id,
disappearance expires the matching open gate, and completion leaves inbox consumption pending.

## Code Commentary
### Invariants And Boundaries
These tests pin the acceptance-versus-consumption boundary and prevent diagnostic pane state from
becoming an action trigger.

## Docs References
No relevant external/domain documentation was configured.

## Repo-Internal References
- [hosted_interactions.py](../src/agents_remember/serving/hosted_interactions.py)
- [test_operator_inbox.py](test_operator_inbox.py)

## Cross-Repo References
No meaningful cross-repo references.

## Update History
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: added durable interaction and non-consumption regression coverage.
