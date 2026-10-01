# mcp/tests/test_checkout_coordination_isolation.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Checkout-local coordination isolation at configuration and store boundaries.

## Code Commentary

### Logic

Loaded source identifies the linked checkout regardless of cwd. Its effective configuration uses the dummy coordination root, disables live providers and services, and writes an incident-shaped inbox only there. Escape writes refuse before parent or lock creation; the admitted report path remains writable.

Since `260918-TSIP-L3` the suite also holds **two pins on the execution-mode boundary, and they assert today's behaviour on purpose** (`T30`/`T28`): `declare_execution_mode` is one assignment with no caller identity, PID or parent check, environment proof, signature or operation record, so the boundary checks only *was any mode declared* — `checkout_cli_location` and `require_durable_write_target` both test `is not None`. The first pin is a two-arm case: **arm A** is the plane's real refusal of an undeclared primary checkout and of a write outside any checkout, and **arm B** is that one `declare_execution_mode("mcp")` lifts both and makes `load_config` read the **live** authority settings (`direct_execution_enabled` true) rather than the synthetic non-authority config. Arm A is the positive control — without it a case that passes after the declaration could be passing because the refusal never fired. The second pin drives `declare_lifecycle_operation_process()`, whose docstring reserves the mode to a plane-owned operation record while the function itself is a bare declaration with **zero callers** in `mcp/src` or `mcp/tests`, and shows `durable_store.declared_process_role()` reporting it as a declared writer of every store `mcp` owns. Both are **pins, not endorsements**: authentication is deliberately not implemented (registered as `D-L3-1` in `notes/defect-index.md`), so a future leaf that authenticates the declaration will red these cases and should read the register before repairing them.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

The rewrite guard also rejects manually constructed live targets. Primary undeclared access fails closed, while explicit temporary test mode retains legitimate temporary writes. The two mode pins above are the deliberate exception to this file's usual posture: they assert a **declared-but-unenforced** boundary as it is, so that making it enforced is a visible test change rather than a silent one.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- Linked checkout is derived from loaded source not cwd. [1]
- Checkout config ignores live authority and uses only dummy root. [2]
- Incident shaped inbox write lands only in leaf dummy root. [3]
- Store guard refuses escape before creating lock or parent. [4]
- Enclosure report write is allowed without opening coordination escape. [5]
- Rewrite guard refuses a manually constructed live target. [6]
- Primary checkout undeclared config access fails closed. [7]
- Explicit test mode preserves temporary store writes. [8]
- Any mode declaration lifts the primary refusal and the write confinement, with the refusal itself as the positive control. [9]
- The reserved lifecycle-operation mode is declarable by any caller, and reports as a writer of every store `mcp` owns. [10]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
