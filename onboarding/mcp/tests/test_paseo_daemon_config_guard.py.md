# mcp/tests/test_paseo_daemon_config_guard.py

## Governing Overview

[mcp overview](../overview.md)

## Purpose

The live provider-map guard is real, reads the daemon's own envelope, and closes.

## Code Commentary

Three things hold together: the bridge dispatches the daemon-config command, the serving adapter reads providers where the running daemon reports them rather than from the file's agent section, and a failed read refuses instead of passing as no live arguments. The serving module reaches none of that itself — the read is the composition root's port, so serving adds no import at or above its own rank.

**L184 — INV-0TCWT9, NEW-R192-RULE19-PORT.** The guard's two routes are asserted in this case. The guard case holds the refusal path of the injected read, so the boundary's behaviour is asserted where the port is exercised. The obligation this leaf records for this place is stated in the invariant named here; the card's earlier account of this file stands, and this paragraph adds what the change made true.
