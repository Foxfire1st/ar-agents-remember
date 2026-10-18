# mcp/tests/test_tool_answer_rows_packaging.py

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Derives memory packaging, integrity and coherence answer rows from hermetic service runs.

## Code Commentary

Cases cover refresh and preview, initialization/baseline, carryover plan, validator listing and coherence actions. The retired drift adapter retains internal projection cases, while the legacy migration cases and compactor are deleted; no retired public MCP adapter is restored. The forty-path carryover comparison passes a constructed population through the compactor both with a supplied report path and with no report path; it invokes neither apply nor a second plan and asserts no extra per-tool cap. These are assertion/fidelity boundaries, not this Curator’s execution or current-pair verdict.

The initialization/baseline, carryover and integrity row cases author a constant-width, uniquely owned fixture root through `_fixed_width_case_root` under `tempfile.gettempdir()`, then `_case_xdg` points the embedded XDG roots at it. Fixture cleanup and environment restoration happen at their context boundaries. Bound and actual guard assertions consume the original emitted objects: no response-path rewriting, larger bounds or lost density floors. The coherence case separately uses `mkdtemp` under `gettempdir()` for a uniquely owned real fixture, authoring a minimum 160-byte encoded root width from the actual parent, stem and random suffix. It applies matching XDG roots and removes that root in `finally`. The original emitted answers, 850 bound and density-floor assertion remain unchanged: no output padding, path normalization, parent clipping or broadened ceiling makes the fixture pass. These source assertions do not claim a fresh execution or universal arbitrary-root bound.

## Evidence

- Packaging imports the surviving fixture owner directly; this replaces only the removed test-module provider edge. [7]
- The actual fixture builder composes its review world and owned topology; packaging's coherence case exercises real service actions over forty constructed candidates without changing guard assertions. [8]

No Domain Documentation sources are configured; the evidence below is repository implementation or test assertions, not a new execution attestation.



### Current Source-Inspection References


- A constructed forty-path population survives compaction with and without a supplied report path; the retained real carryover case derives plan only. [1]

- Refresh and stale-preview results derive the route row. [2]
- Actual validator results derive integrity answer cases. [3]

- Real coherence responses use a uniquely owned fixture whose actual encoded root has a 160-byte minimum; XDG and finally cleanup remain, with unchanged emitted responses, 850 bound and density floor. [4]


- Fixture width is authored and the owned root is cleaned at context exit. [5]

- Embedded XDG roots share that fixture and restore through patch.dict. [6]*** End Patch
