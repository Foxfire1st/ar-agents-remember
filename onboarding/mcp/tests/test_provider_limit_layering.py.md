# mcp/tests/test_provider_limit_layering.py

## Governing Overview

[mcp overview](../overview.md)

## Purpose

The tick's usage read crosses no layer: it is injected at the composition root.

## Code Commentary

The finding this file guards was a new upward import — the serving lifespan reaching into the cli layer for the bridge's usage read, an edge the base tree did not have. The repair is a port serving declares and calls, bound by the composition root; the cases hold both halves and the absence of new upward imports.

**L184 — INV-4T6KSE.** This case guards the boundary rather than a plugin-only reader: serving declares and calls an injected port, and the composition root binds the real implementation, so no edge runs upward into cli. The obligation this leaf records for this place is stated in the invariant named here; the card's earlier account of this file stands, and this paragraph adds what the change made true.
