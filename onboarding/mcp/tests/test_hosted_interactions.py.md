# test_hosted_interactions.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_hosted_interactions.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-14T17:18:47+02:00 |
| lastVerifiedCommitHash | `842b487b854503d95c9c2d9dce1841198ba93c7d` |
| lastVerifiedCommitDate | 2026-07-24T17:08:25+02:00|
| governingOverview | `overview.md` |

## Governing Overview
[tests overview](overview.md)

## Purpose
Proves pending adapter interactions become durable gates, responses use the exact interaction id,
disappearance expires the matching open gate, and protocol-owned null-requestId/vendor-correlation
completion projects onto the same accepted row while inbox consumption remains pending. The exact
2.1.207, 0.144.3, and 0.80.6 values are fixture/smoke evidence only; production behavior is based
on consumed structured fields.

## Code Commentary
### Invariants And Boundaries
These tests pin the acceptance-versus-consumption boundary and prevent diagnostic pane state from
becoming an action trigger. Missing, non-text, unmatched, and ambiguous correlation evidence fails
loudly. Completion records adapter metadata without consuming the row, and terminal state is
`idle` / `immediate` without a queued replacement; `settling` / `queued` requires an actual one.
R9 remains limited to optional `adapterDeliveryState` and `adapterDeliveryDetail`; R10 remains
queued and unimplemented.

## Docs References
No relevant external/domain documentation was configured.

## Repo-Internal References
- [hosted_interactions.py](../src/agents_remember/serving/hosted_interactions.py)
- [test_operator_inbox.py](test_operator_inbox.py)

## Cross-Repo References
No meaningful cross-repo references.

## 260718-CHATS-L5I Current Delta

Hosted-interaction tests now cover serialized multi-question answers and failure reopening with adapter-decision evidence, preventing a failed delivery from silently consuming an operator decision.

This entry supersedes conflicting earlier coverage notes while retaining their history; source verification metadata is deliberately unchanged until the code commit.

## Update History

- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: refreshed the regression-coverage record for the current backend/shared behavior and preserved the pre-commit verification stamp.
- 2026-07-14T17:18:47+02:00 — 260713-PHA-L6 curator: added Codex completion-correlation projection and
  explicit pending/unconsumed plus no-replacement terminal-state coverage.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: added durable interaction and non-consumption regression coverage.
