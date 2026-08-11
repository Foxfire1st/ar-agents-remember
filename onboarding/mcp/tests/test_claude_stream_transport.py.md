# test_claude_stream_transport.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_claude_stream_transport.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-12T00:08+02:00 |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c` |
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
| governingOverview | `overview.md` |

## Governing Overview
[tests overview](overview.md)

## Purpose
Locks the Claude stream adapter's line transport, transcript rendering, and bounded protocol behavior,
plus the transport's own process-ownership lifecycle across start, stop, and restart.

## Code Commentary
Framing, guarded-write, and shutdown-mode cases assign a fake process onto the transport, which is why
they never exercised `start`. `ClaudeSubprocessTransportLifecycleTests` therefore launches a real local
`sys.executable` child that waits on stdin, and drives start -> completed stop -> start on one object to
pin ownership release, plus the live start -> start refusal.

### Invariants And Boundaries
Protocol and framing cases use deterministic transport seams; the lifecycle cases use a real local
subprocess because an injected fake cannot prove that a completed stop releases ownership. Neither tier
makes a live credentialed request — the lifecycle child is a local interpreter with no credentials — and
they do not authorize pane or timing fallback.

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

- 2026-08-12T00:08+02:00 — No content impact: the guarded-write failure subtest now records the
  exception type name instead of the type object so xdist can serialize diagnostics; transport
  behavior and assertions are unchanged. Verification metadata remains pinned until closeout.

- 2026-07-30T15:05+02:00 — 260727-CHATS-IM-L4: recorded the real-subprocess lifecycle tier that pins
  ownership release across start -> stop -> start and retains the live double-start refusal. Split the
  "deterministic transport seams" invariant, which had become false for the whole suite, and aligned the
  `governingOverview` metadata with the body link.
- 2026-07-17T21:39+02:00 — FEUI-L5: added guarded-write and concurrent serialization proof.
- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: clarified the transport test boundary after removing the
  production version preflight.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: added deterministic Claude transport coverage for the bridge.
