# test_claude_stream_transport.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_claude_stream_transport.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-17T21:39+02:00 |
| lastVerifiedCommitHash | `f8196d98982f834d68152d307ff8025ea69440d5` |
| lastVerifiedCommitDate | 2026-07-17T22:08:10+02:00|
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

## 260715-FEUI-L5 Submission Authority Delta

The transport suite now proves a rejected final guard writes zero bytes and concurrent
prompt/response/setter frames preserve shared-lock order. These cases pin the server-side
withdrawal linearization seam for Claude.

## Update History

- 2026-07-17T21:39+02:00 — FEUI-L5: added guarded-write and concurrent serialization proof.
- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: clarified the transport test boundary after removing the
  production version preflight.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: added deterministic Claude transport coverage for the bridge.
