# harness_control_claude.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/harness_control_claude.py` |
| doc_type | file-level-onboarding |
| lastUpdated | 2026-07-14T12:45:11+02:00 |
| lastVerifiedCommitHash | `21049f92238f35e8307c9ed489f4340544c1d147` |
| lastVerifiedCommitDate | 2026-07-14T12:49:29+02:00|
| governingOverview | `overview.md` |

## Governing Overview
[serving overview](overview.md)

## Purpose
Facade for the unregistered Claude Code 2.1.207 long-lived stream-json adapter over the L1 contract.

## Code Commentary
Validates version, preserves launch identity and options, negotiates structured startup, then delegates
frame reduction, interactions, reconciliation, and shutdown to bounded components.

## Invariants And Boundaries
Exact 2.1.207 only; unsupported versions are explicit. L2 does not register or cut over production.
Acceptance is not completion and disconnect never resends.

## Repo-Internal References
| Finding | Citations | Source Path |
| --- | --- | --- |
| L1 adapter contract. | `L1-L25` | [harness_control_adapter.py](harness_control_adapter.py) |
| Conformance tests. | `L1-L35` | [test_harness_control_claude.py](../../../tests/test_harness_control_claude.py) |

## Update History
- 2026-07-14T12:45:11+02:00 — 260713-PHA-L2 source-tip reconciliation: refreshed verification
  metadata to accepted candidate `acb308c50072d8cde0015c4828e39d12480872ed`.
- 2026-07-14T12:30+02:00 — 260713-PHA-L2 curator: created sidecar.
