# mcp/src/agents_remember/controlplane/__init__.py

## Governing Overview

[Control-plane overview](overview.md)

## Purpose

Package export surface for control-plane records: gate records/store/enforcement
and the external-chat operator inbox records/store.

## Code Commentary

### Logic

Re-exports `GATE_RECORD_SCHEMA`, `DECISION_STATES`, the `GateKind` / `GateState`
/ `DecidedVia` Literals, `GateEvidenceRef`, `GateRecord`, `create_gate`,
`decide_gate`, and (slice 6b) `apply_gate` from `records`; `GateStore` from
`store`; `GatePolicy`, `GatePolicyRule`, and `DEFAULT_GATE_POLICY` from
`kernel.primitives.gate_policy`; and (slice 6b/L4) `GateGuard`, `CloseoutGuard`,
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
`append_line`, `rewrite_lines`, `read_log_text` and the six per-store `*_OWNERSHIP` constants remain direct durable-store imports. The mechanical `thread_mutex_for` and `lock_path_for` functions now belong to `kernel.file_lock`; they are neither defined by `durable_store` nor exported by this facade. The facade exports what a *caller outside the package* legitimately
needs (declare which process I am, catch a contract violation, subclass the record base), not the
primitives that would let an outside caller write one of these logs by hand.

The package docstring now states the contract in one paragraph — single-owner compaction, an
unconditional per-log lock with no store exempt and no flag that turns it off, `schemaVersion` with
an unknown major rejected and an unknown minor accepted, and two deliberate read policies — and
directs anyone changing how these stores touch disk to read `durable_store.py` first.

### Conventions

Keep the import list and `__all__` explicit; package exports remain distinct from internal I/O ownership.

### Invariants And Boundaries

- Pure export facade — no behavior. The `gate_*` MCP tools live in
  `mcp/tools/gates.py`, and the `operator_inbox_*` MCP tools live in
  `mcp/tools/operator_inbox.py`, not here.
- **The facade exports the contract, not the file I/O.** Adding `exclusive_access` or
  `rewrite_lines` to `__all__` would make it possible to write a control-plane log from outside
  this package without going through the store that owns it, which is exactly the shape the leaf
  removed.

### Todos

None identified in this bounded export review.

## Evidence

### Docs References

No external Domain Documentation source is configured.

No configured domain documentation source.

### Repo-Internal References

- The records this package exports. [1]
- The gate delegation policy this package exports (moved to kernel primitives by L9). [2]
- The store this package exports. [3]
- The enforcement policy this package exports (slice 6b). [4]
- The operator inbox records and store this package now exports. [5]
- The durable-store contract exports: the package-docstring paragraph stating the contract at L15-L21, the import block at L26-L36, and the matching `__all__` entries at L73-L108. [6]
- The module that defines every durable-store symbol re-exported here, and the six per-store ownership constants that are deliberately not re-exported. [7]


### Cross-Repo References

No cross-repository implementation dependency is exported here.

No cross-repository evidence is required.
