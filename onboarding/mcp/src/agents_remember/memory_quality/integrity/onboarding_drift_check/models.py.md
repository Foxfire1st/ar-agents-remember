# mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/models.py

## Governing Overview

[overview.md](../../../../../overview.md)

## Purpose

`models.py` holds `DriftSummaryPacket`, `EntityFingerprint`, `InlineBlock`, recognized sidecar types, inline markers/delimiters and the root placeholder. It imports `DriftStatus` from the canonical `models/drift.py` owner and performs no I/O or classification.

## Code Commentary

### Logic

`DriftSummaryPacket` requires `status` and marks count/sample/report/error/rows and converted measurement fields `NotRequired`. `summary.not_checked`, `run_drift_summary` and `_run_converted_summary` produce the packets; checked measurement, error and notChecked have different available keys. `reportPath` appears only when filing is requested. Consumers must not invent absent optional counts.

`DriftStatus` is declared in `models/drift.py` and reused by the packet and tool/context models. `EntityFingerprint` retains entity/algorithm/fingerprint/evidence paths; `InlineBlock` retains raw text and metadata. Legacy verdict rows/classification sets and blob-set hashing constants are absent.

### Invariants And Boundaries

- Behavior-free: data records, TypedDict and constants only; no I/O, Git or policy.
- `DriftStatus` is imported from `models/drift.py`; do not add another enum here or create a reverse dependency cycle.
- Status-conditional keys stay `NotRequired`; consumers narrow on status and read optional keys defensively.
- Complete rows remain internal opt-in material, not an expanded ordinary transport sample.

## Evidence

### Repo-Internal References


- not_checked, run_drift_summary and _run_converted_summary produce shared typed summary packets. [1]


- The context-packet wire model that reads `DriftStatus` and gained the matching `error` field. [2]

- The tool response model that dropped its third copy of the enum for the same alias. [3]



The converted measurement adds its own optional keys to `DriftSummaryPacket`: `basis`, `memoryRoot`,
`codeRoot`, `sidecarCount`, `states`, `violationCount`, `violationSample`, `reportOnlyCount` and
`unreadableSidecars`. Legacy fields are never invented for a converted card, and vice versa.

- The packet carries the converted measurement fields alongside the legacy ones. [5]
