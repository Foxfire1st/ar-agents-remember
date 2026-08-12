# mcp/tests/test_conversation_control_installed.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_conversation_control_installed.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated            | 2026-08-12T08:41+02:00 |
| lastVerifiedCommitHash |  `df36127113619f4e85522eb615cc20c7eb637405`|
| lastVerifiedCommitDate | 2026-08-12T08:57:17+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Installed-runtime production proof for the L3 control API (R7). Opt-in
(`AR_RUN_CONTROL_INSTALLED=1`, version-locked): a real installed harness → real adapter → control
bridge → IPC server → real catalog row → the L0 composition → a real uvicorn wire into the L3 control
routes. Proves live interrupt acknowledgement AND settlement, source-aware queue truth, withdrawal
recovery, typed attachment submit, and evidence-bound telemetry through the registered production
routes — never through scenario fixtures.

## Code Commentary

### Logic

cit:([`_LiveHost`], mcp/tests/test_conversation_control_installed.py:90-94), cit:([`_ControlledEntry`], mcp/tests/test_conversation_control_installed.py:97-103), and cit:([`_LiveHarness`], mcp/tests/test_conversation_control_installed.py:97-192) build the live seam against the
installed harnesses. cit:([`CodexInstalledControlApiTests`], mcp/tests/test_conversation_control_installed.py:195-484): typed submit → live turn id →
`POST /conversation/interrupt` 202 accepted → native `turn/completed status=interrupted` →
`interrupt-status` 200 `interrupted` with advanced revision; withdrawal recovery with the exact body;
typed attachment submit as `localImage`; telemetry usage with `runtimeVersion: 0.144.5` and the
fixture id on the wire. Those last three stages live in
`_assert_withdrawal_recovers_the_exact_body`, `_assert_typed_attachment_submit_is_accepted`, and
`_assert_telemetry_carries_exact_usage` — ordered helper stages of
`test_live_interrupt_settlement_queue_recovery_assets_and_telemetry`, sharing its one live harness
and turn sequence, not standalone tests. cit:([`PiInstalledControlApiTests`], mcp/tests/test_conversation_control_installed.py:487-557): guarded abort
accepted → settlement polls to `interrupted`; stale expected identity after settlement → 422
rejected. cit:([`ClaudeInstalledHonestyTests`], mcp/tests/test_conversation_control_installed.py:593-614): the control gate stays `unverified` at the
installed-vs-locked version mismatch (a plain `TestCase`, no live harness needed).

### 260718-CHATS-L5 F1 — installed twin-suppression regression (real codex wire)

`CodexInstalledControlApiTests::test_settled_live_turn_projects_once_on_the_conversation_page` is the
reviewer-required real-wire proof of the projector's F1 disjoint-id-namespace fix (opt-in
`AR_RUN_CONTROL_INSTALLED=1`, isolated `CODEX_HOME`, persisted thread). It opens the conversation
page, drives two real codex 0.144.5 turns to settlement, re-reads
`GET /api/terminal/{id}/conversation`, and asserts each settled turn's user message projects EXACTLY
once (2/2 turns). Before/after is faithful on the wire: **1 passed** (~21–23 s) with the fix;
**`AssertionError: 2 != 1`** on stashed `projector.py`, dumping both twins — the live UUID item
(`operator`/`cockpit-composer`/`exact`) and the `item-1` `unknown-input`/`native-history` twin
sharing one `turnId`+`requestId`. No prior (P) suite asserted post-settlement page uniqueness (the
scripted B-tier bridges reuse one id namespace across channels, so the twin cannot appear there);
this is the installed companion to the always-run F1 tests in `test_conversation_active_service.py`.

### Conventions

The installed suite does not use the fake `ControlHarness` (it drives the real routes unseeded, so it
also exercises the production memo's create-on-miss branch). Version-locked to live codex 0.144.5 and
pi 0.80.7; without the opt-in flag the live classes skip with exact reasons. Both live classes also
carry `@pytest.mark.ar_run_control_installed` above their `skipUnless`, so the environment-gated
suite can be selected or deselected by marker under `--strict-markers`; the marker is a selector
only and the `AR_RUN_CONTROL_INSTALLED=1` skip guard remains the thing that decides whether a live
runtime is touched. `ClaudeInstalledHonestyTests` is unmarked — it needs no installed runtime.
The shared `_version_of` probe skips when the executable is absent or the explicit opt-in is off.
Once an executable is selected for an opted-in run, process-start or subprocess failure is a real
test failure rather than an unavailable-evidence skip.

### Invariants And Boundaries

- Live proof crosses the registered production routes over a real wire, never scenario fixtures.
- Interrupt acknowledgement and settlement are both proven live (codex `interrupted`, pi polled
  `interrupted` + stale-identity 422).
- Claude honesty holds at the version mismatch (control gate stays `unverified`).
- A missing installed harness skips before live evidence is claimed; a selected but unrunnable
  executable fails the opted-in proof.
- A settled live codex turn projects exactly once on the re-read conversation page (L5 F1): the
  installed regression asserts post-settlement page uniqueness (2/2 turns), which no prior installed
  suite did, and fails `2 != 1` on stashed `projector.py`.

### Todos

None.

## Docs References

No Domain Documentation source is configured; the installed contract is repository-owned.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The suite drives the registered routes against the live installed adapters.

| Finding | Anchor | Source |
| --- | --- | --- |
| The seventeen registered routes proven live. | "async def conversation_interrupt(" | mcp/src/agents_remember/serving/conversation/control/api.py:170-170 |
| The interrupt ledger whose live settlement this proves. | "class InterruptRecord:" | mcp/src/agents_remember/serving/conversation/control/operations.py:79-79 |
| The control capability gate whose Claude version-mismatch honesty this pins. | "def control_capabilities_for(" | mcp/src/agents_remember/serving/conversation/control/capabilities.py:320-320 |
| The installed-version probe skips only absent or unselected harnesses and runs the selected executable strictly. | `_version_of` | mcp/tests/test_conversation_control_installed.py:79-88 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-12T08:41+02:00 — 260731-EFA-L20 removed the broad process-error skip: opted-in installed tests still skip a missing executable, but a selected executable that cannot run now fails instead of being reported as unavailable evidence.
- 2026-08-11T22:28+02:00 — 260731-EFA-L19 final curator pass: recorded the exact skip boundary for
  an installed harness whose version process cannot start or complete. No live evidence or fixture
  authority is inferred from that skip; verification metadata remains pinned until closeout.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: this test module was split in place into a family under 1,200 lines (L7-R5); the card remains the family entry point and the name set was reconciled item for item. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-02T17:00+02:00 — 260731-EFA-L6 curator W1-B03: repaired 3 citation rows and 3 historical prose citations with exact anchors and current source paths; scoped citation recheck recorded separately. Verification metadata remains pinned until closeout.

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 2 cross-file line citations that the same
  hardening sweep moved on the other side of the link. `control/api.py` L57-L570 became L131-L631 —
  the seventeen decorated handlers from `@router.post("/conversation/interrupt")` cit:(["async def conversation_interrupt("], mcp/src/agents_remember/serving/conversation/control/api.py:170-170) through the
  end of `conversation_telemetry` cit:(["async def conversation_telemetry("], mcp/src/agents_remember/serving/conversation/control/api.py:741-741), counted on the file and excluding the multipart helpers
  below them. `control/operations.py` L87-L449 became L95-L511, the acknowledge-plus-settle
  machinery this suite proves live: `interrupt`/`interrupt_status` through `_drive_interrupt`,
  `_observe_settlement`, and the per-harness terminal readers ending at `_pi_stop_reason` cit:(["async def _pi_stop_reason("], mcp/src/agents_remember/serving/conversation/control/operations.py:490-490) —
  the old range stopped inside the claude branch and never reached the pi settlement this sidecar
  says it proves.
- 2026-07-31T16:50+02:00 — 260731-EFA-L2 curator, code-quality hardening sweep. Three changes hit
  this suite. `test_live_interrupt_settlement_queue_recovery_assets_and_telemetry` was split for
  the tightened complexity gate: withdrawal recovery, typed attachment submit, and telemetry now
  live in `_assert_withdrawal_recovers_the_exact_body`,
  `_assert_typed_attachment_submit_is_accepted`, and `_assert_telemetry_carries_exact_usage`,
  ordered stages over the same live harness. `@pytest.mark.ar_run_control_installed` was added
  above the `skipUnless` on `CodexInstalledControlApiTests` and `PiInstalledControlApiTests`.
  Rewrote the Logic paragraph to name the three helpers and the Conventions paragraph to record
  the marker alongside the unchanged env-var skip guard, and corrected every class/helper line
  citation for the lines the split, the marker, and the `ruff format` reflow moved: `_LiveHost`
  L83, `_ControlledEntry` L89, `_LiveHarness` L97, `CodexInstalledControlApiTests` L200,
  `PiInstalledControlApiTests` L492, `ClaudeInstalledHonestyTests` L560. No route, assertion, or
  version lock changed.
- 2026-07-21T11:00+02:00 — 260718-CHATS-L5 curator: recorded the reviewer-required F1 installed
  regression `test_settled_live_turn_projects_once_on_the_conversation_page` — opens the page, drives
  two real codex turns to settlement, re-reads the conversation, and asserts each settled turn
  projects exactly once (2/2); before/after faithful on the real wire (1 passed vs stashed
  `AssertionError: 2 != 1` dumping both disjoint-namespace twins). Verification metadata stays pinned
  until L5 closeout stamps the candidate commit.
- 2026-07-20T15:45+02:00 — 260718-CHATS-L3 curator: created the sidecar for the opt-in installed-
  runtime proof — live codex/pi interrupt ack+settlement, queue truth, withdrawal recovery, typed
  attachment submit, and telemetry through the registered routes, plus the Claude version-honesty gate.
  Verification is blank because the new source file is uncommitted; closeout owns its first source
  stamp.
