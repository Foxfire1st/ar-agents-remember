# mcp/tests/mcp_memory_bounded_receipts.py

## Governing Overview

[MCP Tests](overview.md)

## Purpose

Converts a completed capture from one native stdio server into regression measurements.

## Code Commentary

The reader matches call starts and replies by process, cycle, position and variant. It requires successful typed task and knowledge reads and the expected cursor use. Each cycle requires a leaf-candidate quality receipt with a complete worklist, one planned write and one applied write. The full report and recorded reply agree on the write state and exact paths. Each preview names its planned weakness and the owning leaf history. Each apply names its created weakness and that history. The first apply also lists `.gitignore`. The three quality trees and three applied weakness paths are distinct. The reader checks cap and OOM counters when available, then computes growth from cycle two to cycle three and the peak sampled values.

## Relationships

The driver shares the cursor predicate. The executable test consumes these measurements and checks the recorded writes and limits.

## Evidence

- Each completed pair must match its expected call identity and read outcome. [1]

- Each cycle requires a complete leaf quality receipt and one successful preview and apply. Each write report agrees with its reply and names its revision-one weakness and owning leaf history. The first apply also lists `.gitignore`. The three quality trees and three applied weakness paths are distinct. [2]

- Only a completed workload produces the measured result. [3]
