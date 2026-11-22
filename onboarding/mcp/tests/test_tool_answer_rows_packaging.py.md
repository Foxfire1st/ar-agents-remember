# mcp/tests/test_tool_answer_rows_packaging.py

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Derives memory packaging, integrity and coherence answer rows from hermetic service runs.

## Code Commentary

Cases cover refresh and preview, initialization/baseline, carryover plan, validator listing and coherence actions. The retired drift adapter retains internal projection cases, while the legacy migration cases and compactor are deleted; no retired public MCP adapter is restored. The forty-path carryover comparison passes a constructed population through the compactor both with a supplied report path and with no report path; it invokes neither apply nor a second plan and asserts no extra per-tool cap. These are assertion/fidelity boundaries, not this Curator’s execution or current-pair verdict.

The initialization, carryover, integrity and coherence row cases use the shared fixed_width_row_case_root helper with its literal /tmp parent and temporary XDG variables. The coherence fixture requests an actual 160-byte root. The assertions use the emitted responses, including the existing bounds and density floors.

## Evidence
- Packaging imports the surviving fixture owner directly; this replaces only the removed test-module provider edge. [7]


- The fixture builder composes a review world and its owned topology. The coherence case exercises real actions over forty constructed candidates and measures the emitted answers. [8]



No Domain Documentation sources are configured; the evidence below is repository implementation or test assertions, not a new execution attestation.



### Current Source-Inspection References



- A constructed forty-path population survives compaction with and without a supplied report path. The real carryover row derives its result from a plan. [1]


- Refresh and stale-preview results derive the route row. [2]


- Actual validator results derive the reported and refused integrity answer cases. [3]


- The coherence case requests a real 160-byte root from the shared helper and tests emitted responses against its 850-token bound and density floor. [4]
- The shared helper controls fixture width and removes the temporary root on exit. [5]
- The shared helper directs XDG configuration, data and cache into the fixture and restores the environment on exit. [6]
- Initialization, carryover, integrity and coherence use the shared helper’s uniquely owned /tmp roots. The emitted responses stay subject to the existing row bounds and density floors. [9]
