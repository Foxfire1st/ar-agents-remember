# mcp/tests/mcp_memory_bounded_receipts.py

## Governing Overview

[MCP Tests](overview.md)

## Purpose

Converts a completed capture from one native stdio server into regression measurements.

## Code Commentary

The reader matches call starts and replies by process, cycle, position and variant. It requires successful typed task and knowledge reads and the expected cursor use. Each cycle must produce a leaf-candidate quality receipt with a complete worklist, one successful planned write preview, and one successful applied write. Across three cycles, that gives three quality receipts with distinct memory trees, three previews and three applied writes with distinct paths. It checks cap and OOM counters when available. After validation it computes growth from cycle two to cycle three and the peak sampled values.

## Relationships

The driver shares the cursor predicate. The executable test consumes these measurements and checks the recorded writes and limits.

## Evidence

- Each completed pair must match its expected call identity and read outcome. [1]

- Each of the three cycles requires a complete leaf quality receipt, a successful preview and a successful write. Quality memory trees and written paths must be distinct across cycles. [2]

- Only a completed workload produces the measured result. [3]
