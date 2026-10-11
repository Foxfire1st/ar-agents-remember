# mcp/src/agents_remember/worktrees/modules/integration_gate.py

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Reconcile leaf and master integration admission before any ref moves. Leaf routes rejudge the closeout-cell pair against the current parent-memory tip; series routes run validator/net-staleness/history ownership first, then the admitted landing chain. Preview and apply use the same refusal boundary.

## Code Commentary

The final series route requires the full canonical non-abandoned leaf population; a checkpoint proves only landed leaves. Converted memory is gated, unconverted memory keeps the cutover lock, and removed modes refuse explicitly. A refusal projects knowledge-gate-refused without persisting the contract or recomputed worklist. This module owns admission, not publication, review acceptance or Git recovery.

## Evidence

No external Domain Documentation source is configured for this repository. The following source witnesses establish the contract, not a new execution receipt.

- Integration admission preserves the no-write refusal boundary. [1]
- The exact closeout pair is rejudged against the current parent memory tip. [2]
