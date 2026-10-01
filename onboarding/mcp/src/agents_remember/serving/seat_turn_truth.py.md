# mcp/src/agents_remember/serving/seat_turn_truth.py

## Governing Overview

[serving/ overview](overview.md)

## Purpose

The catalog write surface for seat-turn truth (260713-TES-L2): module-level free functions
over `TerminalCatalog`'s public atomic `get`+`upsert` seams that persist the lifted terminal
outcome, the terminal-evidence cursors, the interrupt-request provenance stamp, and the
state-signal/non-reaction/compound-idle dedupe markers. The frozen `TerminalCatalogEntry` and
the catalog classes carry a strict surface budget, so this module exists instead of growing new
catalog methods.

## Code Commentary

### Logic

The `with_*` copiers cit:([`with_turn_evidence`], mcp/src/agents_remember/serving/seat_turn_truth.py:23-78) are pure `dataclasses.replace` copies: `with_turn_evidence`
sets the seat state plus one terminal observation, preserving `turn_state_changed_at` when the
state did not actually transition; `with_state_signal_emitted`/`with_non_reaction_emitted`
stamp one evidence/row episode; `with_compound_idle_emitted` stamps one compound-idle episode
signature; `with_interrupt_request` stamps developer provenance; `with_terminal_cursors`
advances only the supplied cursors.

The `record_*` helpers cit:([`record_turn_projection`, `record_compound_idle_emitted`], mcp/src/agents_remember/serving/seat_turn_truth.py:73-88; mcp/src/agents_remember/serving/seat_turn_truth.py:155-166) are the locked-style write points: read the current row via
`catalog.get`, apply the copier, and `catalog.upsert` only when the row actually changed;
unknown session ids return `None`/no-op; re-recording the same compound signature is a no-op
(the already-emitted guard). `record_terminal_cursors` is called by the liveness
sweep ONLY after a successful terminal-evidence read — a failed read never advances the
cursors (the F2 no-loss fix).

### Conventions

One write path for the relay and liveness projection: no caller mutates catalog fields
directly; every terminal-truth mutation rides `get`+`upsert` through this module.

### Invariants And Boundaries

- The turn-state timestamp is preserved when the state is unchanged (a no-op observation must
  not mint a boundary transition).
- Signal markers are idempotent: re-recording the same evidence id is a no-op; the
  compound-idle marker is signature-keyed (`compound_idle_emitted_for`), so re-recording the
  same episode signature is a no-op and a NEW episode (signature change) overwrites the marker
  — that is the re-arm (260713-TES-L3).
- When a marker is written is the caller's contract, not this module's: since 260831-LOCR-L10 the
  state-signal marker is stamped from inside the posting primitive's post-persistence callback, so
  the row is already durable and delivery has not been attempted. Nothing in this write surface
  changed for that — `record_state_signal_emitted` still reads through `catalog.get` and upserts
  only a changed row.
- Cursors advance only on success; the snapshot pointer and terminal cursors are independent
  positions.
- The module never posts inbox rows, never classifies, and never decides delivery — it only
  persists catalog truth.

### Todos

None for this module.

## Evidence

### Docs References

No Domain Documentation entries are configured in the resolved `system/sources.md`; the
write semantics are same-repository runtime behavior proven by source and tests.

- No external/domain document defines these catalog writes; the atomic seam contract is the source of truth. [1]

### Repo-Internal References

The module consumes `TerminalCatalog`/`TerminalCatalogEntry`/`CatalogTurnEvidence` and is
called by the liveness sweep and the interrupt route and the state-signal actions.

- The frozen catalog row, evidence stamp, and public get/upsert seams it writes through. [2]
- The liveness sweep's read-before-projection ordering that calls `record_terminal_cursors`. [3]
- The interrupt route stamping developer provenance after an accepted interrupt. [4]
- The state-signal and non-reaction action markers. The state-signal marker is written from the emitter's post-persistence callback — after the row is durable and on the sweep fold, before any delivery attempt — while the non-reaction marker stays a post-return write. [5]
- The compound-idle action-time marker write (ask + marker share the fresh signature). [6]


### Cross-Repo References

No meaningful cross-repo references found.

No cross-repo boundary owns or consumes these catalog writes.
