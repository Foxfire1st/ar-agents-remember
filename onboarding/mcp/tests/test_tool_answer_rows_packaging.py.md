# mcp/tests/test_tool_answer_rows_packaging.py

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Derives memory packaging, integrity and coherence answer rows from hermetic service runs.

## Code Commentary

Cases cover refresh and preview, initialization/baseline, carryover plan, validator listing and coherence actions. Retired drift and migration tools have projection-only cases: retained internal services do not restore their public MCP adapters. The forty-path carryover comparison passes a constructed population through the compactor both with a supplied report path and with no report path; it invokes neither apply nor a second plan and asserts no extra per-tool cap. These are assertion/fidelity boundaries, not this Curator’s execution or current-pair verdict.

The initialization/baseline, carryover and integrity row cases author a constant-width, uniquely owned fixture root through `_fixed_width_case_root`, then `_case_xdg` points the embedded XDG roots at it. Fixture cleanup and environment restoration happen at their context boundaries. Bound and actual guard assertions consume the original emitted objects: no response-path rewriting, larger bounds or lost density floors. This fixture choice does not promise that arbitrary ambient paths fit every tool bound.

## Evidence

No Domain Documentation sources are configured; the evidence below is repository implementation or test assertions, not a new execution attestation.



### Current Source-Inspection References

- A constructed forty-path population survives compaction with and without a supplied report path; the retained real carryover case derives plan only. [1]
- Refresh and stale-preview results derive the route row. [2]
- Actual validator results derive integrity answer cases. [3]
- Actual coherence actions derive bounded cases. [4]
- Fixture width is authored and the owned root is cleaned at context exit. [5]
- Embedded XDG roots share that fixture and restore through patch.dict. [6]
