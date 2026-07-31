# mcp/tests/test_conversation_active_api.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_conversation_active_api.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-27T14:20+02:00 |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`|
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
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

`_FakeAdapter`/`_NativePageAdapter` (L107-L248) emit native frames exactly as the production
mappers do and let the real submission authority own dispatch/provenance; `_Harness` (L258-L360)
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
production authority exists in the active modules. `PiProductionRouteTests` (L948-L1035) drives
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
| The three registered production routes under test. | L121-L249 | [api.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/api.py) |
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

## 260727-CHATS-IM-L2 Selected-Child Route Regression Delta

The production-route suite now posts an exact child id and bridge epoch to the selected-child
history route, verifies the projector receives only that id, and proves the returned local outcome
does not replace or fail the parent page. Existing page/event authorization and epoch behavior
remain intact.

## Update History

- 2026-07-31T17:48+02:00 — 260731-EFA-L2 curator: re-derived the stale `PiProductionRouteTests`
  self-citation — the class is L948-L1035 (was L785-L866) after the selected-child and L5I
  bootstrap/recovery cases grew `ProductionRouteTests`. Its one test is still
  `test_pi_native_hydration_tools_and_capabilities`. Still stale and left for the next citation
  pass (verified, not repaired here): `ProductionRouteTests` runs L379-L946 (cited L362-L781) and
  the fake adapters are L111-L257 (cited L107-L248).

- 2026-07-31T16:50+02:00 — 260731-EFA-L2 curator, code-quality hardening sweep.
  No content impact: the whole diff is the new `ControlSubmission` import plus the
  `submit_control_prompt` call inside `ProductionRouteTests` folding its
  `source`/`request_id`/`expected_bridge_epoch`
  arguments into that parameter object. The same cockpit source, request id, and bridge epoch
  still reach the real submission authority, no test was added, removed, or renamed, and no
  assertion moved — so the three-route page/events composition, the provenance-lane exactness,
  the epoch-mismatch 409, the cursor and SSE refusals, and the no-PTY source scan all hold as
  written.

- 2026-07-27T14:20+02:00 — 260727-CHATS-IM-L2 curator: updated the active route count to three
  and documented exact selected-child POST/parent-continuity coverage. Verification metadata
  remains pinned while uncommitted.

- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: refreshed the regression-coverage record for the current backend/shared behavior and preserved the pre-commit verification stamp.

- 2026-07-19T17:35+02:00 — 260718-CHATS-L1 curator: created the sidecar for the production-route
  suite — real-socket composition proof of identity, ordering, idempotence, epoch-flip gap,
  provenance, parity, and no-PTY authority (15 tests). Verification is blank because the new
  source file is uncommitted; closeout owns its first source stamp.
