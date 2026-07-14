# mcp/tests/test_pi_rpc_process.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_pi_rpc_process.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-14T12:17+02:00 |
| lastVerifiedCommitHash | `d5f8edf0ccab21f1cf71723615e394eba40fcebc` |
| lastVerifiedCommitDate | 2026-07-14T12:29:36+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview
[mcp/tests overview](../overview.md)

## Purpose
Exercises the actual async Pi RPC subprocess transport at its process boundary.

## Code Commentary
Deterministic child scripts prove correlated responses plus event streaming and clean stop,
malformed stdout propagation, and EOF during a request as possible-send ambiguity.

## Invariants And Boundaries
- Tests the real subprocess seam without installing Pi or mutating global tools.
- Transport failures remain typed and are not silently reclassified or retried.

## Repo-Internal References
| Finding | Source Path |
| --- | --- |
| Transport under test. | [pi_rpc_process.py](../src/agents_remember/serving/pi_rpc_process.py) |
| Strict frame decoder. | [pi_rpc_protocol.py](../src/agents_remember/serving/pi_rpc_protocol.py) |

## Cross-Repo References
No meaningful cross-repo references found.

## Update History
- 2026-07-14T12:17+02:00 — 260713-PHA-L4 curator: created onboarding for subprocess correlation,
  malformed stdout, EOF ambiguity, and clean-stop tests.
