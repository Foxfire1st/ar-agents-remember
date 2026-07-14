# test_harness_control_claude.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_harness_control_claude.py` |
| doc_type | file-level-onboarding |
| lastUpdated | 2026-07-14T12:45:11+02:00 |
| lastVerifiedCommitHash | `bc2958ae2d90ab3d34bffde5402d2dc21100e41b` |
| lastVerifiedCommitDate | 2026-07-14T16:16:44+02:00|
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

## 260713-PHA-L6 Evidence Boundary

Focused regressions prove Claude accepts a compatible newer reported version when the structured
contract is complete and rejects a missing required capability; they do not pin production CLI text.

## Update History
- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: recorded structured Claude negotiation and incompatible
  contract coverage.
- 2026-07-14T12:45:11+02:00 — 260713-PHA-L2 source-tip reconciliation: refreshed verification
  metadata to accepted candidate `acb308c50072d8cde0015c4828e39d12480872ed`.
- 2026-07-14T12:30+02:00 — 260713-PHA-L2 curator: created sidecar.
