# mcp/src/agents_remember/controlplane/__init__.py

| Field                  | Value                                                 |
| ---------------------- | ----------------------------------------------------- |
| repository             | agents-remember                                       |
| path                   | `mcp/src/agents_remember/controlplane/__init__.py`    |
| doc_type               | `file-level-onboarding`                               |
| lastUpdated            | 2026-07-04T12:32+02:00                                |
| lastVerifiedCommitHash | `e358c4ac520d94ae2e597ae3cbe186e07a4d1063`            |
| lastVerifiedCommitDate | 2026-07-07T05:26:14+02:00|
| governingOverview      | `overview.md`                                         |

## Purpose

Package export surface for control-plane records: gate records/store/enforcement
and the external-chat operator inbox records/store.

## Code Commentary

Re-exports `GATE_RECORD_SCHEMA`, `DECISION_STATES`, the `GateKind` / `GateState`
/ `DecidedVia` Literals, `GateEvidenceRef`, `GateRecord`, `create_gate`,
`decide_gate`, and (slice 6b) `apply_gate` from `records`; `GateStore` from
`store`; the L4 `DecisionRole`, `GatePolicy`, `GatePolicyRule`,
`DEFAULT_GATE_POLICY`, `make_gate_policy`, and `named_gate_policy` from
`gate_policy`; and (slice 6b/L4) `GateGuard`, `CloseoutGuard`,
`evaluate_gate`, and `evaluate_closeout_gate` from `enforcement`.

Task 10 adds the operator inbox exports: `OPERATOR_INBOX_RECORD_SCHEMA`,
`OperatorInboxEntry`, `OperatorInboxState`, `OperatorInboxVia`,
`create_operator_inbox_entry`, `consume_operator_inbox_entry`, and
`OperatorInboxStore`. The module docstring now names this as the pull-based
counterpart for non-AR-hosted chats, while `__all__` keeps the facade explicit.

## Invariants And Boundaries

- Pure export facade — no behavior. The `gate_*` MCP tools live in
  `mcp/tools/gates.py`, and the `operator_inbox_*` MCP tools live in
  `mcp/tools/operator_inbox.py`, not here.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The records this package exports. | [records.py](agents-remember/mcp/src/agents_remember/controlplane/records.py) |
| The gate delegation policy this package exports. | [gate_policy.py](agents-remember/mcp/src/agents_remember/controlplane/gate_policy.py) |
| The store this package exports. | [store.py](agents-remember/mcp/src/agents_remember/controlplane/store.py) |
| The enforcement policy this package exports (slice 6b). | [enforcement.py](agents-remember/mcp/src/agents_remember/controlplane/enforcement.py) |
| The operator inbox records and store this package now exports. | [operator_inbox_records.py](agents-remember/mcp/src/agents_remember/controlplane/operator_inbox_records.py) and [operator_inbox_store.py](agents-remember/mcp/src/agents_remember/controlplane/operator_inbox_store.py) |

## Update History

- 2026-07-04T12:32+02:00 — 260703-L4: facade now exports the gate-policy schema,
  evidence-ref model, and kind-generic enforcement resolver. Verification
  metadata pinned until closeout stamps the L4 commit.
- 2026-06-23T13:44+02:00 — Task 10 backend inbox: re-exported the operator inbox record/store symbols and updated the package docstring to describe the external-chat pull channel. Verification metadata pinned until closeout stamps the task-10 code commit.
- 2026-06-18T12:10+02:00 — Task 6 slice 6b: facade now re-exports `apply_gate` (from `records`) and `CloseoutGuard` / `evaluate_closeout_gate` (from the new `enforcement` module). Verification metadata pinned until closeout stamps the 6b code commit.
- 2026-06-18T01:05+02:00 — Created for task 6 slice 6a: the control-plane package facade. Verification metadata pinned until closeout stamps the 6a code commit.
