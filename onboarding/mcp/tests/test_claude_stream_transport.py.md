# test_claude_stream_transport.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_claude_stream_transport.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-14T13:59+02:00 |
| lastVerifiedCommitHash | `cff3e8f9a64258ea3e7d3007e2153b22c01e273b` |
| lastVerifiedCommitDate | 2026-07-14T14:23:24+02:00|
| governingOverview | `../overview.md` |

## Governing Overview
[tests overview](overview.md)

## Purpose
Locks the Claude stream adapter's line transport, transcript rendering, and bounded protocol behavior.

## Code Commentary
### Invariants And Boundaries
Tests use deterministic transport seams; they prove adapter semantics without making a live credentialed
request. They do not authorize pane or timing fallback.

## Docs References
No relevant external/domain documentation was configured.

## Repo-Internal References
- [harness_control_claude.py](../src/agents_remember/serving/harness_control_claude.py)

## Cross-Repo References
No meaningful cross-repo references.

## Update History
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: added deterministic Claude transport coverage for the bridge.
