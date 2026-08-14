# mcp/tests/test_serving_app_routes.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_serving_app_routes.py`     |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T15:32+02:00                     |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Behavioural coverage for the dashboard route arms **that only fire when something is
wrong**. `serving/app.py`'s happy paths are covered by `test_serving.py` and
`test_terminal_ws.py`; what was untested is the half of each handler that decides what the
cockpit sees when the world does not cooperate — a request landing before the first
projection tick, a task document that is not there (or is somewhere it must never be read
from), a seat whose tmux pane died between the catalog write and the request, a harness
whose control socket is gone, a rename of an already-retired session, and the
gate-decision arm reached only for a workspace-level cancel.

## Layering, And Why Each Test Sits Where It Does

- **Boot race** — `TestClient` is used **deliberately without its context manager**, so the
  app's lifespan (and therefore `Projector.prime`) never runs. That is exactly the
  pre-first-tick window the three `503 projection not ready` guards exist for, reproduced
  over real HTTP. Do not "fix" this by wrapping it in `with`.
- **Routes** — driven through the real FastAPI app with a real `TerminalCatalog` and real
  task documents. The only double is `_CatalogOnlyHost`, a `TerminalHost` duck-type standing
  in for tmux: which panes exist, and killing them. Its `on_terminate` hook is the seam that
  interleaves another process's catalog write with a retire, which is the only way the
  "`mark_retired` returned nothing" arm is reachable.
- **Helpers below the wire** — `_gate_decision_response` is called directly for the
  gate-id-only decision, because assembling that shape through the app would say nothing the
  route tests in `test_serving.py` do not already say.
- **Protocol harness** — `HarnessSubmissionTests` drives `_harness_submit_response` against
  a **real control bridge** in a worker thread (as the sync route is), so the bridge's
  asyncio server keeps servicing the socket; the adapter at the far edge is the only double.
  Acceptance is what decides `delivered`.

## What Each Class Owns

| Class | Route / arm |
| --- | --- |
| `BeforeTheFirstProjectionTests` | Every read/write needing a projection refuses honestly during the boot window. |
| `TaskDocumentEndpointTests` | `/api/task-document`: the on-demand reader body, and what it refuses to read. |
| `OperatorInboxDismissTests` | Dismissing a row that is already gone is a **404**, not a silent success. |
| `GateDecisionHelperTests` | A decision addressed by gate id alone (the workspace-level `cancel` path). Whether a decision names anything to decide is answered once in `evaluate_action` (400 `missing-target`, asserted over HTTP in `test_serving.ActionGateTests`); what remains here is the recorder's own arm. |
| `LandedCleanupRaceTests` | A landed row that disappears mid-cleanup is reported **skipped**, never counted as closed. |
| `AttachLeafRoleTests` | A hand-opened harness seat must say what role it is before it may claim a leaf. |
| `PasteRouteTests` | `POST /api/terminal/{session}/paste`: who may be pasted into, and how a harness answers. |
| `HarnessSubmissionTests` | The submit mapping against a real bridge: acceptance decides `delivered`. |
| `TerminateRouteTests` | `POST …/terminate`: nothing to kill, and a bridge that will not stop. |
| `RenameRouteTests` | `POST …/rename`: identity text only, and only for a live row. |

Seat fixtures cover both shapes the catalog really holds: a plain shell seat as the
dashboard's own opener writes it, and a harness seat with no spawn role (the hand-opened
shape, optionally protocol-backed). `_write_task_documents` writes a real master + leaf pair.

## Invariants And Boundaries

- No PTY is ever attached; none of these routes need one.
- The `503 projection not ready` guards are proven over real HTTP, not by calling a handler.
- A failure arm must produce the *specific* status and body a cockpit acts on (404 vs. 503
  vs. a skipped count), not merely "an error".

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The routes and handlers under test. |"async def stream_events"|mcp/src/agents_remember/serving/_app_common.py:115-115|
| The happy paths these arms sit beside. | `AppTests`, `TerminalWebSocketTests` | mcp/tests/test_serving.py:480-554; mcp/tests/test_terminal_ws.py:422-449 |
| The same app's background loops and lifespan wiring. | `AgentNotifierLoopTests` | mcp/tests/test_serving_app_background_loops.py:220-272 |
| Helper-level arms of the same module. | `ImageSniffTests` | mcp/tests/test_serving_helper_behaviour.py:100-139 |

## L23 Attach Route Fixture

Structural attach-route tests now seed a current master/leaf contract chain so
their existing HTTP and seat-binding assertions pass through the new admission
gate for the intended reason.

## Update History
- 2026-08-12T20:10+02:00 — L23 curator: documented current-lineage setup for structural attach routes; verification remains closeout-owned.

- 2026-08-11T19:58+02:00 — Aligned the regression card for `test_serving_app_routes.py` with the source's current task-document, seat-routing, inbox, or lifecycle assertions.
- 2026-08-08T23:15+02:00 — 260713-TES-L1 completion round 3 (curator): body refreshed for the supervisor -> agent-notifier rename (citation ranges and/or rename wording); verification metadata pinned until closeout stamps the 260713-TES-L1 commit.


- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B20 curator: replaced the `n/a` table rows with
  exact anchors and fixer-generated ranges; exact non-fixing check returns zero findings.

- 2026-07-31T15:32+02:00 — 260731-EFA-L2 curator: created onboarding for the new
  dashboard route-failure suite. Verification metadata is pinned to the leaf's reformat
  commit until closeout stamps the code commit.
