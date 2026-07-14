# test_hosted_control_conformance.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_hosted_control_conformance.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-14T13:59+02:00 |
| lastVerifiedCommitHash | `cff3e8f9a64258ea3e7d3007e2153b22c01e273b` |
| lastVerifiedCommitDate | 2026-07-14T14:23:24+02:00|
| governingOverview | `overview.md` |

## Governing Overview
[tests overview](overview.md)

## Purpose
Runs one deterministic bridge scenario across Claude, Codex, and Pi covering ready handshake,
identity, immediate/queued delivery, blocked interaction, completion, ambiguous transport,
restart recovery, incompatibility, and shutdown.

## Code Commentary
### Invariants And Boundaries
The matrix tests the shared protocol contract, not vendor-specific pane or log heuristics. It proves
R13 inbox-rooted delivery and R14 explicit consumption separation through durable evidence assertions.

## Docs References
No relevant external/domain documentation was configured.

## Repo-Internal References
- [harness_control_bridge.py](../src/agents_remember/serving/harness_control_bridge.py)
- [inbox_delivery.py](../src/agents_remember/serving/inbox_delivery.py)

## Cross-Repo References
No meaningful cross-repo references.

## Update History
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: added cross-adapter protocol conformance matrix.
