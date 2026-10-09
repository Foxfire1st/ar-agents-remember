# mcp/tests/test_tool_log_budgets.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

The MIK-R108 rule-3 budget proofs: byte-budget admission, pressure-bounded eviction inventory, failed-removal reclamation, census coherence, and 31-day sweep continuation.

## Code Commentary

### Logic

- Budget tests pin the 256 MiB / 64 MiB / 8 MiB bounds, oldest-first whole-day eviction, dropped-and-counted writes, and that pre-existing non-owned bytes and failed whole-day removals never permit writer-owned overshoot.
- Inventory tests pin bounded listings under pressure (no per-day whole-folder re-list), the 60-second census rule and finished-day accounting.
- Sweep tests pin at-most-31-days per call with same-day continuation.

### Invariants And Boundaries

- Budgets are shown at two load sizes (D3); the stated listing margin is the admitted overshoot bound.
- Misbudgeted writes are dropped and counted; the call still succeeds.

## Evidence

- Pressure eviction bounds its folder listings against one census. [1]
- A 31-day sweep continues on the next same-day call. [2]
