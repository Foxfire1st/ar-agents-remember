# hosted_interactions.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/hosted_interactions.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-14T13:59+02:00 |
| lastVerifiedCommitHash | `cff3e8f9a64258ea3e7d3007e2153b22c01e273b` |
| lastVerifiedCommitDate | 2026-07-14T14:23:24+02:00|
| governingOverview | `overview.md` |

## Governing Overview
[serving overview](overview.md)

## Purpose
Synchronizes adapter-owned pending questions and terminal completion evidence with durable gates
and durable inbox rows.

## Code Commentary
### Logic
Pending interactions create `agent-question` gates containing exact session/interaction identity,
prompt, choices, and raw detail. A decided gate responds through the same adapter interaction id;
disappearance expires only the matching open gate. Transcript terminal results update adapter
completion evidence on the matching inbox row.
### Invariants And Boundaries
Completion never calls `consume`; acceptance and completion mutate delivery metadata only. Explicit
recipient consumption remains the sole inbox acknowledgement. Adapter failures leave durable state
truthful and retryable.

## Docs References
No relevant external/domain documentation was configured; gate, inbox, and interaction tests are authoritative.

## Repo-Internal References
- [operator_inbox_store.py](../controlplane/operator_inbox_store.py) persists delivery evidence.
- [GateResponder.tsx](../../../../../../dashboard/src/panels/GateResponder.tsx) renders interaction context.
- [harness_control_client.py](harness_control_client.py) sends interaction responses.

## Cross-Repo References
No meaningful cross-repo references.

## Update History
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: documented durable interaction gates and completion-without-consumption.
