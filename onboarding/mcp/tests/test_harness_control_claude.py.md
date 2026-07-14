# test_harness_control_claude.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_harness_control_claude.py` |
| doc_type | file-level-onboarding |
| lastUpdated | 2026-07-14T12:45:11+02:00 |
| lastVerifiedCommitHash | `21049f92238f35e8307c9ed489f4340544c1d147` |
| lastVerifiedCommitDate | 2026-07-14T12:49:29+02:00|
| governingOverview | `../overview.md` |

## Governing Overview
[tests overview](../overview.md)

## Purpose
Fake-transport conformance coverage for pinned Claude startup, correlation, interactions, limits, shutdown, and terminal normalization.

## Code Commentary
Deterministic fixtures cover the mixed `success`/`is_error=true` API-429 frame and assert failed outcome with safe metadata only.

## Invariants And Boundaries
No credentials or model output; tests cover the unregistered adapter only.

## Repo-Internal References
| Finding | Citations | Source Path |
| --- | --- | --- |
| Adapter under test. | `L1-L25` | [harness_control_claude.py](../src/agents_remember/serving/harness_control_claude.py) |

## Update History
- 2026-07-14T12:45:11+02:00 — 260713-PHA-L2 source-tip reconciliation: refreshed verification
  metadata to accepted candidate `acb308c50072d8cde0015c4828e39d12480872ed`.
- 2026-07-14T12:30+02:00 — 260713-PHA-L2 curator: created sidecar.
