# test_claude_stream_transport.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_claude_stream_transport.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-14T13:59+02:00 |
| lastVerifiedCommitHash | `bc2958ae2d90ab3d34bffde5402d2dc21100e41b` |
| lastVerifiedCommitDate | 2026-07-14T16:16:44+02:00|
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

## 260713-PHA-L6 Evidence Boundary

Transport tests cover strict stream framing only; production compatibility is proven by structured
initialize/system-init tests, not an exact CLI probe.

## Update History
- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: clarified the transport test boundary after removing the
  production version preflight.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: added deterministic Claude transport coverage for the bridge.
