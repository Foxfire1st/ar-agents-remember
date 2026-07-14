# test_harness_control_runner.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_harness_control_runner.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-14T13:59+02:00 |
| lastVerifiedCommitHash | `cff3e8f9a64258ea3e7d3007e2153b22c01e273b` |
| lastVerifiedCommitDate | 2026-07-14T14:23:24+02:00|
| governingOverview | `overview.md` |

## Governing Overview
[tests overview](overview.md)

## Purpose
Verifies runner payload decoding, adapter factory composition, Codex app-server argv translation,
session-command correlation, transcript rendering, and shutdown behavior.

## Code Commentary
### Invariants And Boundaries
The tests preserve ordinary terminal passthrough and ensure hosted runner behavior remains bridge-owned.

## Docs References
No relevant external/domain documentation was configured.

## Repo-Internal References
- [harness_control_runner.py](../src/agents_remember/serving/harness_control_runner.py)

## Cross-Repo References
No meaningful cross-repo references.

## Update History
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: added runner and factory conformance coverage.
