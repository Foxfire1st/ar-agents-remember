# Native retirement proofs

[Tests route overview](overview.md)

## Contract

Fake-host operation and MCP-entry tests exercise original-starter retirement, explicit interruption of an active turn, unknown IDs, duplicate current receipts, current-plus-history ambiguity, and unauthorized repeats. A successful retirement records the original caller/reason, archives without a child turn, and makes both ID- and role-addressed messages refuse archived delivery.

The record-write fault test distinguishes a host already archived from a receipt not yet naming retirement and proves an identical authorized retry converges. The tests do not establish restoration of the removed hosted-seat path, or a real-host replacement journey.

## Evidence

- The original starter archives its agent without a child turn and records retirement provenance. [1]
- Current plus historical receipt duplication refuses through the entry point without effects. [2]
- A failed final receipt write reports the split and an identical retry converges. [3]
