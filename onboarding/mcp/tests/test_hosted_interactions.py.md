# test_hosted_interactions.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_hosted_interactions.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-14T17:18:47+02:00 |
| lastVerifiedCommitHash | `8fc3ecb0cb22da53ba639ad37dee37ce0e8d7c9b` |
| lastVerifiedCommitDate | 2026-07-14T17:24:18+02:00|
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

## Update History
- 2026-07-14T17:18:47+02:00 — 260713-PHA-L6 curator: added Codex completion-correlation projection and
  explicit pending/unconsumed plus no-replacement terminal-state coverage.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: added durable interaction and non-consumption regression coverage.
