# mcp/tests/test_conversation_active_api.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_conversation_active_api.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T17:35+02:00 |
| lastVerifiedCommitHash | `842b487b854503d95c9c2d9dce1841198ba93c7d`|
| lastVerifiedCommitDate | 2026-07-24T17:08:25+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Production-route tests for the active conversation API (260718-CHATS-L1, R6): every test drives
the REAL composition — a per-session `HarnessControlBridge` + `HarnessControlServer` on a real
user-private Unix socket (the L0E seam), a real `TerminalCatalog` row, the L0
`register_conversation_routes` composition, and HTTP over a real loopback uvicorn server (true
TCP, true SSE wire). The only double is the harness adapter at the far edge; no PTY, no runner
log, no fixture authority.

## Code Commentary

### Logic

`_FakeAdapter`/`_NativePageAdapter` (L105-L247) emit native frames exactly as the production
mappers do and let the real submission authority own dispatch/provenance; `_Harness` (L256-L361)
wires the bridge, IPC server, catalog row, and composed app per test. `ProductionRouteTests`
(L362-L781): a remote peer fails closed typed 403 over a real wire (XFF); the page serves
native identity, items, canonical status, and capabilities; user-item provenance resolves
through the REAL authority (cockpit/terminal/durable lanes exact); epoch mismatch maps to 409
with expected/actual fields; unknown session 404 / unsupported 409; `before` paging walks back
with minted cursors; tampered and foreign cursors fail typed; the events route requires a
cursor and rejects dual-resume conflict (`400 cursor-conflict`); generation mismatch resets
typed; resume replays in order with cursor ids (and earlier replays are marked `resume-replay`);
an epoch flip mid-stream emits exactly one gap + close read off the live wire (the runner
generation restarts on the same socket); orchestration parity proves the seat projection comes
from the same canonical classification; and a source scan proves no PTY/runner-log/fixture
production authority exists in the active modules. `PiProductionRouteTests` (L783-L865) drives
pi native hydration, tool convergence, and capabilities through the same real seam.

### Conventions

SSE is served over a real uvicorn loopback server because `httpx.ASGITransport` buffers entire
responses and can never deliver an event stream (worker round-2 issue 2); blocking IPC client
reads are offloaded with `asyncio.to_thread` on the same loop. The suite was re-run 4× for
stability by the worker.

### Invariants And Boundaries

- The composition under test is the production one — no test-only routers, services, or
  authorization shortcuts.
- Every pre-stream error is asserted typed; established-stream failure is asserted as one gap +
  close on the wire.
- The no-PTY/runner-log/fixture source scan keeps production authority honest by construction.

### Todos

None.

## Docs References

The resolved `Domain Documentation` registry has no entries; the composition/seam contracts are
repository-owned and cited below.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available for this suite. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The two registered production routes under test. | L121-L186 | [api.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/api.py) |
| The L0 root composition the suite installs verbatim. | L7-L32 | [router.py](agents-remember/mcp/src/agents_remember/serving/conversation/router.py) |
| The bridge/IPC server seam (L0E) the suite runs on a real socket. | L103-L149 | [harness_control_runner.py](agents-remember/mcp/src/agents_remember/serving/harness_control_runner.py) |
| The cursor mint helpers used to forge/tamper cursors in the refusal tests. | L197-L262 | [cursor.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/cursor.py) |

## Cross-Repo References

No cross-repository implementation participates in this suite.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260718-CHATS-L5I Current Delta

This suite now covers the active page/event bootstrap and recovery wire, including fresh cursor continuity, epoch-safe direct interaction behavior, and honest refusal paths when a projection cannot resume.

This entry supersedes conflicting earlier coverage notes while retaining their history; source verification metadata is deliberately unchanged until the code commit.

## Update History

- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: refreshed the regression-coverage record for the current backend/shared behavior and preserved the pre-commit verification stamp.

- 2026-07-19T17:35+02:00 — 260718-CHATS-L1 curator: created the sidecar for the production-route
  suite — real-socket composition proof of identity, ordering, idempotence, epoch-flip gap,
  provenance, parity, and no-PTY authority (15 tests). Verification is blank because the new
  source file is uncommitted; closeout owns its first source stamp.
