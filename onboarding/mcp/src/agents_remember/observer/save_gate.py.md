# mcp/src/agents_remember/observer/save_gate.py

## Governing Overview

[overview.md](overview.md)

## Purpose

`save_gate.py` is the pure decision vocabulary of the **save gate** — the choice
forced when leaving a *fleeting* lifecycle (design §1.2/§1.5): **save** promotes
it to persistent so the work is not lost, **discard** ends it `abandoned`. It has
no I/O or threading, so the slice-3 projection reducer can reuse the scope rule.

## Code Commentary

`SaveDecision = Literal["save","discard"]` with `SAVE_DECISIONS = get_args(...)`;
`coerce_save_decision(value)` validates a raw tool-boundary string into a
`SaveDecision` or raises `LifecycleError`. `SaveGateRequired(LifecycleError)` is
raised when a switch/attach would abandon unsaved fleeting work and no decision
was supplied — it carries the active id and tells the caller to pass `on_unsaved`.
`compute_scope(repo_id, *, cross_repo=False)` returns the scope tag recorded on
`lifecycle.promoted`: the `repo_id` for single-repo work, `CROSS_REPO_SCOPE`
(`1_cross-repo`) for multi-repo enclosures, or `UNSCOPED_SCOPE` (`0_unscoped`)
when there is no managed-repo binding; the numeric prefixes sort above the
per-repo folders in the dashboard hangar (slice 4).

## Invariants And Boundaries

- Pure vocabulary: imports only `LifecycleError` from `lifecycle_state.py`; no
  I/O, no threading, no import from the ambient module — kept reusable by the
  projection reducer.
- The gate is **foundational, not interactive**: 2c records the decision from an
  explicit input and *blocks* (`SaveGateRequired`) when none is given; slice 06
  docks interactive resolution, a durable gate record, and enforcement onto this
  seam. There is deliberately no auto-save default.

## Evidence

### Repo-Internal References

- The ambient methods that raise/consume this vocabulary (`switch`/`attach`/`promote`). [1]
- The typed-error family base (`LifecycleError` → `AgentsRememberError`). [2]
- The design separates fleeting and persistent sessions with a save gate and TTL. [3]
