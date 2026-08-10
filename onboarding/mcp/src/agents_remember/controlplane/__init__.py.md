# mcp/src/agents_remember/controlplane/__init__.py

| Field                  | Value                                                 |
| ---------------------- | ----------------------------------------------------- |
| repository             | agents-remember                                       |
| path                   | `mcp/src/agents_remember/controlplane/__init__.py`    |
| doc_type               | `file-level-onboarding`                               |
| lastUpdated            | 2026-08-01T18:30+02:00                                |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb`            |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
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

### 260731-EFA-L5 Durable Store Contract Exports

The facade now also re-exports the `ar-durable-store/1.0` surface from
`controlplane/durable_store.py`: the constants `DURABLE_STORE_CONTRACT` and `SCHEMA_VERSION`; the
error types `DurableStoreError`, `CompactionOwnerError` and `UnsafeLockFilesystemError`; the record
base `DurableRecord`; the ownership value object `StoreOwnership`; and the process-role pair
`declare_process_role` / `declared_process_role`. All are in `__all__`.

What is deliberately **not** exported is the I/O itself — `exclusive_access`, `require_lock_held`,
`append_line`, `rewrite_lines`, `read_log_text`, `thread_mutex_for`, `lock_path_for` and the six
per-store `*_OWNERSHIP` constants stay module-private to the package's own stores, which import
them from `durable_store` directly. The facade exports what a *caller outside the package* legitimately
needs (declare which process I am, catch a contract violation, subclass the record base), not the
primitives that would let an outside caller write one of these logs by hand.

The package docstring now states the contract in one paragraph — single-owner compaction, an
unconditional per-log lock with no store exempt and no flag that turns it off, `schemaVersion` with
an unknown major rejected and an unknown minor accepted, and two deliberate read policies — and
directs anyone changing how these stores touch disk to read `durable_store.py` first.

## Invariants And Boundaries

- Pure export facade — no behavior. The `gate_*` MCP tools live in
  `mcp/tools/gates.py`, and the `operator_inbox_*` MCP tools live in
  `mcp/tools/operator_inbox.py`, not here.
- **The facade exports the contract, not the file I/O.** Adding `exclusive_access` or
  `rewrite_lines` to `__all__` would make it possible to write a control-plane log from outside
  this package without going through the store that owns it, which is exactly the shape the leaf
  removed.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The records this package exports. | "class GateRecord" | mcp/src/agents_remember/controlplane/records.py:45-45 |
| The gate delegation policy this package exports (moved to kernel primitives by L9). | "class GatePolicy:" | mcp/src/agents_remember/kernel/primitives/gate_policy.py:54-54 |
| The store this package exports. | "class GateStore:" | mcp/src/agents_remember/controlplane/store.py:105-105 |
| The enforcement policy this package exports (slice 6b). | "class GateGuard" | mcp/src/agents_remember/controlplane/enforcement.py:42-42 |
| The operator inbox records and store this package now exports. | "class InboxAddress", "class OperatorInboxStore" | mcp/src/agents_remember/controlplane/operator_inbox_records.py:40-40; mcp/src/agents_remember/controlplane/operator_inbox_store.py:53-53 |
| The durable-store contract exports: the package-docstring paragraph stating the contract at L15-L21, the import block at L26-L36, and the matching `__all__` entries at L71-L106. | `__all__` | mcp/src/agents_remember/controlplane/__init__.py:71-106 |
| The module that defines every durable-store symbol re-exported here, and the six per-store ownership constants that are deliberately not re-exported. | "SCHEMA_VERSION = " | mcp/src/agents_remember/controlplane/durable_store.py:45-45 |

## Update History

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B20 curator: replaced the `n/a` table rows with
  exact anchors and source-backed ranges; exact non-fixing check returns zero findings.

- 2026-08-01T18:30+02:00 — 260731-EFA-L5 (durable store integrity). Recorded the new facade
  exports from `durable_store.py` — `DURABLE_STORE_CONTRACT`, `SCHEMA_VERSION`, `DurableRecord`,
  `StoreOwnership`, `DurableStoreError`, `CompactionOwnerError`, `UnsafeLockFilesystemError`,
  `declare_process_role` and `declared_process_role` — and, as the load-bearing half, what is
  deliberately withheld: the locking and rewrite primitives and the six per-store `*_OWNERSHIP`
  constants stay package-internal so no caller outside `controlplane/` can write one of these logs
  without going through the store that owns it. Recorded the new package-docstring paragraph
  stating the contract in one place. Verification metadata pinned until closeout stamps the L5
  commit.
- 2026-07-04T12:32+02:00 — 260703-L4: facade now exports the gate-policy schema,
  evidence-ref model, and kind-generic enforcement resolver. Verification
  metadata pinned until closeout stamps the L4 commit.
- 2026-06-23T13:44+02:00 — Task 10 backend inbox: re-exported the operator inbox record/store symbols and updated the package docstring to describe the external-chat pull channel. Verification metadata pinned until closeout stamps the task-10 code commit.
- 2026-06-18T12:10+02:00 — Task 6 slice 6b: facade now re-exports `apply_gate` (from `records`) and `CloseoutGuard` / `evaluate_closeout_gate` (from the new `enforcement` module). Verification metadata pinned until closeout stamps the 6b code commit.
- 2026-06-18T01:05+02:00 — Created for task 6 slice 6a: the control-plane package facade. Verification metadata pinned until closeout stamps the 6a code commit.
