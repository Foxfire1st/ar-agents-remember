# mcp/tests/test_provider_limit_hold.py

## Governing Overview

[mcp overview](../overview.md)

## Purpose

The one send check and a drain that waits for the reset.

## Code Commentary

A message to a limited recipient is held with the reason and the reset time on every send path, and the drain pauses before it reads the host, so waiting costs no bridge process. The one exception is the single host read for a recipient the publication shows ended.

**L184 — INV-1ZKP4R.** The one limit check is held here, where its reason and reset are decided. The obligation this leaf records for this place is stated in the invariant named here; the card's earlier account of this file stands, and this paragraph adds what the change made true.
