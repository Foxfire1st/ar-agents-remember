# mcp/src/agents_remember/serving/retire.py

## Governing Overview

[serving/ overview](overview.md)

## Purpose

`retire.py` owns the single-seat retirement primitive: it optionally stops the
control session, terminates the terminal host session, and persists a
`SeatClosure` through the terminal catalog.

## Code Commentary

### Logic

`retire_entry` accepts a `SeatClosure` rather than separate provenance
keywords. When a control endpoint exists it first calls
`stop_control_session`. A `HarnessControlError` is recorded in
`control_raw["retireControlStopError"]` and the entry is upserted so an
orphaned terminal can still be reaped. The function then calls
`host.terminate` and `catalog.mark_retired` with the closure's four fields.

### Conventions

`TerminalHost` is imported only under `TYPE_CHECKING` (a lazy/type-only import) to avoid a runtime
import cycle — callers pass a real `TerminalHost` instance at call time.

### Invariants And Boundaries

- Transcripts are never touched here — retiring is a catalog-and-tmux operation only; this module
  has no knowledge of transcript storage.
- A graceful control-stop failure is retained on the catalog entry before
  terminal termination continues.
- Exceptions other than the explicitly handled `HarnessControlError` are
  not swallowed by this module.

### Todos

No known follow-up in this file.

## Evidence

### Docs References

No relevant external documentation found after checking the repo Domain Documentation for
seat-retirement-specific behavior; this file is same-repository runtime plumbing implementing a
developer-ruled cleanup automation, not an external standard.

No relevant external/domain document is needed; the module's implementation is the source of truth.

### Repo-Internal References

- The closure record carries timestamp, reason, edge, and acting session. [1]
- Retirement handles graceful control-stop failure, terminal termination, and catalog marking. [2]
- The control-session stop failure type is handled explicitly. [3]
- Retirement invokes the control-session stop path when configured. [4]

### Cross-Repo References

No meaningful cross-repo references found.

No cross-repo boundary owns or consumes this local retire-mechanics module.
