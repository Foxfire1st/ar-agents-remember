# test_terminal_ws.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_terminal_ws.py`                  |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-07T22:45:00+02:00               |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`       |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview      | `overview.md`                                 |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

`test_terminal_ws.py` covers the Mode B2 WebSocket bridge and the daemon terminal-open HTTP route:
client-frame parsing, socketpair-backed PTY attachment, catalog lifecycle, role/leaf behavior, and
the complete native model/effort launch-selection contract (no real PTY or vendor harness).

## Code Commentary

### FEUI-L9R Reviewed Candidate Delta

The harness endpoint regression still pins detected availability for Claude, Codex, and Pi, and now
also requires that every pre-session row omit `control`. This makes the test prove the narrow
discovery boundary rather than inventing adapter process state before any session is opened.

### 260707-HFX2-L17 HTTP Pair Attach Regressions

HTTP tests send explicit role, assert role-required behavior for untyped hand-opened sessions,
exercise same-pair `409` only with live host evidence, and verify current/previous seat-role fields
in successful attach responses.

### Logic

### Pre-session discovery and post-open control projection

The final serving tests require `GET /api/harnesses` to remain narrow discovery
(`id`/`name`/`detected`, no `control`) while terminal-open and live catalog responses retain their
separate post-open control evidence. Bridge-era control modules are tested separately by
`test_harness_control.py`; this route suite pins the HTTP/catalog boundary.

### 260714-ACPUI-L4 launch-selection and reopen coverage

The HTTP route accepts model and effort only as a complete pair for an AR native harness and carries
that pair once into `RunnerConfig`. Partial selection, a plain terminal selection, and a non-native
harness selection all fail before `host.ensure`. Reopening an already-live session with the same
pair returns the actual retained model/effort and control endpoint; a changed pair returns `409
launch-selection-conflict` with that same actual row and no second process. Once the host probe says
the original process is dead, the route opens a fresh generation with the new pair and a new control
endpoint. Direct concurrent race fencing is covered in `test_terminal_opener.py`; this file pins the
public HTTP projection of the same shared opener behavior.

L16 review follow-up adds MalformedSettingsScratchTerminalTests: a broken settings.json + kind=terminal open reaches the opener with harnesses=None (builtin fallback), proving the registry load is scoped to harness-resolving requests (L16R-1).

`ApplyTerminalInputTests` drive `_apply_terminal_input` against a `_RecordingHost`: a
`stdin` frame writes the decoded bytes, a `resize` frame forwards `(cols, rows)`, and
non-int dimensions / unknown types / malformed JSON / non-object JSON are all ignored
(no write, no resize). `TerminalWebSocketTests` build the app with
`create_app(..., terminal_host=cast(TerminalHost, fake))` where the fake is a
`_FakeTerminalHost` backed by `socket.socketpair()` — each websocket attachment gets its own
master/peer pair so tests can model multiple browser tabs attached to one durable tmux name. The
test-side helpers drive a peer (`feed`/`feed_to`/`feed_all` = child output, `read_child_input` =
delivered stdin, `end` = child exit). The cases assert: an unknown session is refused with close
code `4404`; PTY output arrives as a **binary** frame (raw VT bytes preserved); a client
`stdin` frame reaches the child; a `resize` is forwarded and ordered before a following
`stdin` (read-back proves order); child exit emits the `_TERMINAL_EXIT_FRAME` text frame
then disconnects; two websocket clients can attach to the same catalog row and closing one leaves the
other usable; and app teardown calls `host.shutdown()`. Slice 6e-2a adds `test_post_open_*` (the fake host gains
`open`; `POST /api/terminal/{id}` `{kind:"terminal"}` records `host.open` with the workspace-root cwd +
a shell argv; an unknown kind ⇒ 400; HFX-L4 invalid `leafKey` refs return `leaf-ref-not-found` before
host ensure or catalog upsert) and `ResolveTerminalLaunchTests` (the pure `resolve_terminal_launch`).
Slice 6e-2b adds the harness path: `GET /api/harnesses` lists the supported set with detection
(monkeypatching `shutil.which`), a `{kind:"harness"}` POST spawns the registry argv at the
workspace root, and an uninstalled / unknown harness ⇒ 400 — plus harness cases in
`ResolveTerminalLaunchTests` (a `_which` fake injected directly). Slice 6f: the `_FakeTerminalHost`/
`_FakeSession` gain a `cwd` + `open(..., suspend_unsafe=...)`, the opener cases assert the
`suspend_unsafe` flag flows (`True` for a harness, `False` for a shell), and a new
`TerminalImageEndpointTests` covers `POST /api/terminal/{session}/image`: a valid image saves under
`<cwd>/.dashboard-pastes/` and returns its path; a hostile filename (`../../etc/passwd.png`) still
yields a uuid basename confined under the cwd; non-image extension, non-image content for an image
extension (magic-byte sniff), empty body, oversize (post-read and via `Content-Length`), and an unknown
session are each rejected with the right status. Task 22 extends the fake host with tmux
probe/terminate state, per-connection `attach`/`close_session` clients, and a temp `TerminalCatalog`
injected into `create_app`; the route tests now
assert opener rows persist label/lifecycle/tmux/status through `host.ensure`, `GET
/api/terminal/sessions` lists and refreshes catalog rows, WebSocket attach creates a catalog-backed
client only when the tmux probe says the session exists, the first WebSocket after POST open can read
from the detached session, stale catalog rows become `exited`, explicit terminate kills the tmux name
and marks the row `terminated`, browser disconnect closes the local host attachment while leaving the
catalog row `running`, and image upload can use a catalog cwd after dashboard restart.
Slice L5 adds the leaf-registry cases over the same fake host + temp `TerminalCatalog`: the opener with a
`leafKey` claims + persists `leaf_key` on the catalog row and echoes `leafKey` in the body, a null/absent
leaf opener still succeeds (back-compatible), the opener and `POST /api/terminal/{session}/attach-leaf`
both return `409 leaf-taken` when a *different* running session of the **same role** already owns the leaf,
the same session re-claiming its own leaf is allowed (self-reclaim, no 409), and `attach-leaf` returns
`200 attached` for a known running session while a `404` covers an unknown / terminated session; HFX-L4
adds invalid-ref coverage proving `/attach-leaf` returns `400` without mutating the row. The L5
fix pass adds the **per-(leaf, role)** cases: `test_terminal_shares_a_leaf_with_its_chat_but_two_chats_conflict`
opens a `harness` chat + a `terminal` on one leaf (both `200` — they share the leaf), then proves a
**second chat** and a **second terminal** each `409` (reporting the existing owner `chat-1` / `term-1`);
`test_attach_leaf_terminal_does_not_conflict_with_existing_chat` proves the attach path is role-scoped too —
a terminal can `attach-leaf` to a leaf already held by a running chat (`200`, the row persists the leaf).
**HFX2-L11** adds three cases: `test_websocket_attaches_landed_catalog_session_for_inspection` proves a
`status:"landed"` row can still be attached and read over the WebSocket for inspection (landing keeps the
tmux pane alive; only the background liveness sweep skips it), and the row's status stays `"landed"`
afterward (attach never reanimates it to `"running"`). `test_landed_cleanup_closes_only_landed_rows_and_reports_skips`
covers `POST /api/terminal/landed-cleanup`: given a landed, a running, and an exited row plus one unknown
id, it asserts the endpoint rechecks live catalog status per id rather than trusting the caller's list —
only the landed row is terminated (`host.terminated == ["ar-landed"]`, `retired_reason` set to
`"landed group cleanup"`) while running/exited/unknown ids are reported as skipped with a
`status:<status>` / `unknown-session` reason each, and the response totals (`closed`/`skipped`,
`closedSessions`/`skippedSessions`) match exactly. `test_attach_leaf_404_for_landed_session` asserts
`POST /api/terminal/{id}/attach-leaf` returns `404` for a landed session (a landed row cannot be
re-claimed onto a new leaf assignment).

### Conventions

Inserts `mcp/src` on `sys.path` (suite idiom). Since L2 `resolve_terminal_launch` is imported from
`agents_remember.serving.terminal_opener` (it moved out of `serving.app` into the shared opener), and
the `_FakeTerminalHost` `ensure`/`open` signatures gained the optional `env` param so they stay
compatible with the opener's env-seeding call. `cast(TerminalHost, fake)` bridges the duck
-typed fakes to the typed `create_app`/`_apply_terminal_input` signatures without subclassing.
The fake's peer sockets carry a 2s timeout so `read_child_input` never hangs the suite.
`_config(tmp)` mirrors `test_serving.py` (a `McpRuntimeConfig` over a temp root; the projector
primes empty). Real PTY/tmux behavior is covered separately by `test_terminal.py` (6d-1).

### Invariants And Boundaries

- Model and effort are an all-or-nothing launch pair for native harness sessions; invalid selection
  is rejected before any host or catalog spawn mutation.
- The route and role-based MCP tool compose the same opener. This suite covers the HTTP projection;
  direct transaction races and role provenance are covered in `test_terminal_opener.py`.
- Live reopen responses report the process's actual command, pair, and control endpoint. Changed
  selection conflicts rather than rewriting provenance; dead replacement creates a fresh generation.
- WebSocket stdin remains raw terminal input and is not the daemon's reliable control-submit API.
- Existing leaf/role, terminal liveness, image, and landed-inspection behavior remains additive.

### Todos

None known for this leaf.

## Docs References

No Domain Documentation category is configured for this repository, so no live documentation
source was available for this test-file curation pass.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured Domain Documentation source was available to cite. | — | — |

## Repo-Internal References

This route suite remains broad, but L4's new authority is narrow: complete-pair carriage and truthful
live/dead reopen projection over the shared opener.

| Finding | Anchor | Source |
| --- | --- | --- |
| A complete native model/effort pair reaches the encoded runner exactly once and is returned as resolved launch truth. | "test_post_open_harness_carries_complete_model_effort_pair_once"; "/api/terminal/h-selected" | mcp/tests/test_terminal_ws_websocket_2.py:274-274; mcp/tests/test_terminal_ws_websocket_2.py:277-277 |
| Same-pair live reopen preserves the original endpoint; changed-pair reopen conflicts with actual truth; dead replacement uses the new pair and a fresh endpoint. | "test_post_open_reopen_preserves_live_truth_conflicts_then_replaces_dead"; "launch-selection-conflict" | mcp/tests/test_terminal_ws_websocket_2.py:297-297; mcp/tests/test_terminal_ws_websocket_2.py:321-321 |
| Partial, plain-terminal, and non-native selections all fail before host ensure. | "test_post_open_rejects_partial_or_non_harness_selection_before_spawn"; "launch-selection-invalid" | mcp/tests/test_terminal_ws_websocket_2.py:335-335; mcp/tests/test_terminal_ws_websocket_2.py:358-358 |
| WebSocket and catalog cases continue to cover raw PTY framing, parallel attachments, liveness, leaf/role claims, and landed inspection. | "class ApplyTerminalInputTests(unittest.TestCase):"; "class TerminalWebSocketTests(unittest.TestCase):"; "def feed_all(self" | mcp/tests/test_terminal_ws.py:368-368; mcp/tests/test_terminal_ws.py:395-395; mcp/tests/test_terminal_ws.py:427-427 |
| `TerminalOpenRequest` carries optional model/effort, and the HTTP route validates them into one resolved launch before calling the shared opener. | "class TerminalOpenRequest(BaseModel):"; "def _open_terminal_response(" | mcp/src/agents_remember/serving/_app_common.py:268-268; mcp/src/agents_remember/serving/_app_terminal_routes.py:225-225 |
| A launch conflict returns 409 with the retained session's actual model, effort, control state, and endpoint. | "def _terminal_entry_payload(entry: TerminalCatalogEntry) -> dict[str"; "def _open_terminal_response(" | mcp/src/agents_remember/serving/_app_terminal_routes.py:207-207; mcp/src/agents_remember/serving/_app_terminal_routes.py:225-225 |
| Direct opener regressions provide the complementary same/different/dead/concurrent transaction and role-path authority. | `OpenTerminalSessionTests`; "spawnedByLifecycle"; "seatRole"; "ar-owner-1"; `reviewer_entry`; `first_worker`; `KnobApplicationTests`; "attempted metadata rewrite"; `pair_conflict`; "other-workspace"; "resolved launch requested 'codex'"; `second_runner`; `open_after_blocker` | mcp/tests/test_terminal_opener.py:217-479; mcp/tests/test_terminal_opener.py:482-772 |

## Cross-Repo References

No sibling repository is required for this local daemon/open/WebSocket suite.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

### 260713-PHA-L5 Reviewed Hosted Cutover Impact

Reviewed this file against the accepted hosted-session cutover and PASS verdict. Its relevant
contract now follows exact adapter evidence for readiness, delivery, liveness, or interactions;
legacy/custom sessions are unsupported, pane/log classifiers are diagnostics-only, and durable
inbox acceptance remains distinct from explicit consumption where applicable.

## 260731-EFA-L2 Delta — launch args ride the resolved argv

`test_launch_args_ride_the_resolved_argv` pins that caller-supplied launch arguments travel on the
**resolved** argv rather than being appended somewhere later, so what the seat runs is what
`resolve_terminal_launch` decided.

Note on shape: the terminal fixtures now build `TerminalSessionSpec` / `TerminalSessionBinding`,
`TerminalLaunchRequest` / `SpawnKnobs`, `ServingCollaborators` and `ProjectionCadence` objects
instead of long keyword lists. The assertions are unchanged.

## L23 Web Route Fixture Admission

Terminal websocket fixtures now seed canonical current lineage for both the
generic repository and the operations-integration example. This keeps websocket
behavior under test while respecting structural task admission.

## Update History

- 2026-08-18T09:05+02:00 — Renamed the atomic 'barrier' concept to 'blocker' throughout (terminology unification; no behavioral change). Verification remains closeout-owned.

- 2026-08-12T20:10+02:00 — L23 curator: documented current-lineage setup for terminal web fixtures; verification remains closeout-owned.

- 2026-08-11T19:58+02:00 — Aligned the regression card for `test_terminal_ws.py` with the source's current task-document, seat-routing, inbox, or lifecycle assertions.
- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: this test module was split in place into a family under 1,200 lines (L7-R5); the card remains the family entry point and the name set was reconciled item for item. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-04T14:24:05+02:00 — 260731-EFA-L6 S18-B08 curator: regenerated launch-pair/reopen/pre-spawn test anchors and retained the generated WebSocket/direct-opener body extents so behavior-bearing evidence remains cited through the whole-claim audit.

- 2026-07-31T15:32+02:00 — 260731-EFA-L2 curator: recorded the arms this leaf added; the rest of this card was re-read against the file and remains true. Call sites in this module now build parameter objects (see the route overview) — what the suite proves is unchanged. Verification metadata pinned until closeout stamps the code commit.

- 2026-07-18T12:43+02:00 — FEUI-L9R: replaced the stale pre-session control assertion with exact
  field-absence coverage; verification metadata remains pinned pending candidate closeout.
- 2026-07-16T06:15+02:00 — 260714-ACPUI-L4 curator: documented the complete native launch-pair
  request, pre-spawn partial/non-native refusal, same-pair live reopen, changed-pair 409 with actual
  truth, fresh dead replacement, and the HTTP boundary from direct concurrent/role opener coverage;
  added the governing overview and required reference sections. Body verified against the
  uncommitted L4 candidate; verification metadata remains pinned to the latest committed source
  revision until closeout.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: reviewed hosted cutover impact and refreshed the body.
- 2026-07-14T12:00+02:00 — 260713-PHA-L1 closeout remediation: documented additive harness-control
  projection coverage and its boundary with the standalone bridge conformance suite.

- 2026-07-10T15:07+02:00 — 260707-HFX2-L17: updated HTTP attach coverage for explicit role claims,
  live pair conflicts, and role-aware response fields.

- 2026-07-09T14:05+02:00 — HFX2-L11 (landed chat archive): added coverage for
  `POST /api/terminal/landed-cleanup` — asserts the endpoint rechecks live catalog `status` per
  session (not client-supplied group membership) and closes ONLY rows still `status:"landed"`,
  skipping running/exited/unknown rows with a reported reason, returning accurate `closed`/`skipped`
  counts and session-id lists; also confirms `test_websocket_attaches_landed_catalog_session_for_inspection`
  still passes (landed WS attach re-probes tmux/turn-state on demand, unaffected by the round-2
  background-sweep exclusion fix in `terminal_liveness.py`). Verification metadata pinned until
  closeout stamps the 260707-HFX2-L11 commit.
- 2026-07-07T20:50+02:00 — 260707-HFX-L4: app fixtures now write representative task docs and cover
  invalid `leafKey` rejection for `POST /api/terminal/{session}` and `/attach-leaf`, proving no host ensure
  or catalog mutation happens before resolver success. Verification metadata pinned until closeout stamps
  the 260707-HFX-L4 commit.
- 2026-07-07T12:40+02:00 — L16 adversarial-review follow-up: malformed-settings scratch-terminal regression test (L16R-1). Verification metadata pinned until closeout stamps the L16 commit.

- 2026-07-04T11:10+02:00 — L2 (agent-facing dispatch): `resolve_terminal_launch` is now imported from
  `serving.terminal_opener` (the opener extraction moved it out of `serving.app`), and the
  `_FakeTerminalHost` `ensure`/`open` fakes gained the optional `env` param to match the opener's
  env-seeding call. Import/signature alignment only — the WebSocket/opener assertions are unchanged; the
  new opener + paste + spawn coverage lives in the dedicated L2 test files. Verification metadata pinned
  until closeout stamps the L2 commit.
- 2026-06-30T00:00:00+02:00 — L5 follow-up: added per-(leaf, role) route coverage —
  `test_terminal_shares_a_leaf_with_its_chat_but_two_chats_conflict` (a chat + a terminal share one leaf,
  but a second chat and a second terminal each `409` against the existing same-role owner) and
  `test_attach_leaf_terminal_does_not_conflict_with_existing_chat` (a terminal can `attach-leaf` to a leaf
  already held by a chat). Verification metadata pinned until closeout stamps the L5 commit.
- 2026-06-30T00:00:00+02:00 — L5 (Sidebar chat): added leaf-registry route coverage — the opener claims + persists
  `leaf_key` and echoes `leafKey`, a null-leaf opener still works, the opener and
  `POST /api/terminal/{session}/attach-leaf` both `409 leaf-taken` against a different running owner while
  self-reclaim is allowed, and `attach-leaf` returns `200 attached` / `404` for unknown or terminated
  sessions. Verification metadata pinned until closeout stamps the L5 commit.
- 2026-06-27T02:28+02:00 — Task 22 follow-up: `_FakeTerminalHost` now models `ensure` separately from
  `open`; opener tests assert no starter PTY client is opened or closed, and a new first-WebSocket test
  proves POST open leaves a detached session available for attach. Verification metadata pinned until
  closeout stamps the task-22 follow-up code commit.
- 2026-06-27T01:25+02:00 — Task 22 follow-up: `_FakeTerminalHost` now models multiple
  per-WebSocket socketpair clients with `attach`/`close_session`; tests seed catalog rows before
  websocket attach, assert catalog-backed attach uses `host.attach`, and cover two simultaneous
  websockets where closing one client does not close the other. Verification metadata pinned until
  closeout stamps the task-22 follow-up code commit.
- 2026-06-27T00:45+02:00 — Task 22 follow-up: added coverage that a browser WebSocket disconnect closes
  the local terminal client but keeps the catalog row running, which forces the next refresh to reattach
  through tmux instead of reusing a stale PTY.
- 2026-06-26T23:05+02:00 — Task 22: fake sessions/host now carry tmux name, command, lifecycle,
  suspend flag, probe names, and terminate calls; tests inject a temp `TerminalCatalog` and cover
  persisted opener metadata, session listing, tmux-probed WebSocket rehydrate, stale-row exit marking,
  explicit terminate, and image upload using catalog cwd after restart. Verification metadata pinned
  until closeout stamps the task-22 code commit.
- 2026-06-19T20:30 — Task 6 slice 6f: added `TerminalImageEndpointTests` for `POST /api/terminal/{session}/image` (save-under-cwd + returned path, hostile-filename confinement to a uuid name, non-image-type / magic-byte-mismatch / empty / oversize-post-read / oversize-via-Content-Length / unknown-session rejections); gave `_FakeTerminalHost`/`_FakeSession` a `cwd` + `suspend_unsafe` open param; and asserted the opener passes `suspend_unsafe` (True harness / False shell). Verification metadata pinned until closeout stamps the 6f code commit.
- 2026-06-18T21:27+02:00 — Task 6 slice 6e-2b: added the harness endpoint cases (`GET /api/harnesses` detection via `patch("shutil.which")`; `{kind:"harness"}` POST → registry argv at the workspace root; uninstalled/unknown ⇒ 400) + harness cases in `ResolveTerminalLaunchTests` + a `_which` fake. Verification metadata pinned until closeout stamps the 6e-2b code commit.
- 2026-06-18T17:40+02:00 — Task 6 slice 6e-2a: added `test_post_open_*` (the `POST /api/terminal/{id}` opener calls `host.open` with the workspace-root cwd + a shell argv; unknown kind ⇒ 400) + `ResolveTerminalLaunchTests`, and gave the fake host an `open` method. Verification metadata pinned until closeout stamps the 6e-2a code commit.
- 2026-06-18T16:10+02:00 — Created for task 6 slice 6d-2: covers `_apply_terminal_input` (frame parsing) and the `/api/terminal/{session}` WebSocket bridge end-to-end via TestClient + a socketpair fake host (binary output, stdin delivery, resize ordering, 4404 refusal, exit frame, host shutdown). Verification metadata pinned to the 6d-1 base until closeout stamps the 6d-2 code commit.
