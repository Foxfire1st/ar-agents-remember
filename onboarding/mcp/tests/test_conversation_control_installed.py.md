# mcp/tests/test_conversation_control_installed.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_conversation_control_installed.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-21T11:00+02:00 |
| lastVerifiedCommitHash |  `68b3205526dae210cd902eef39d93c4f4352c2d4`|
| lastVerifiedCommitDate |  2026-07-21T01:12:04+02:00|
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

`_LiveHost` (L84), `_ControlledEntry` (L90), and `_LiveHarness` (L98) build the live seam against the
installed harnesses. `CodexInstalledControlApiTests` (L196): typed submit → live turn id →
`POST /conversation/interrupt` 202 accepted → native `turn/completed status=interrupted` →
`interrupt-status` 200 `interrupted` with advanced revision; withdrawal recovery with the exact body;
typed attachment submit as `localImage`; telemetry usage with `runtimeVersion: 0.144.5` and the
fixture id on the wire. `PiInstalledControlApiTests` (L364): guarded abort accepted → settlement
polls to `interrupted`; stale expected identity after settlement → 422 rejected.
`ClaudeInstalledHonestyTests` (L432): the control gate stays `unverified` at the installed-vs-locked
version mismatch (a plain `TestCase`, no live harness needed).

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
pi 0.80.7; without the opt-in flag the live classes skip with exact reasons.

### Invariants And Boundaries

- Live proof crosses the registered production routes over a real wire, never scenario fixtures.
- Interrupt acknowledgement and settlement are both proven live (codex `interrupted`, pi polled
  `interrupted` + stale-identity 422).
- Claude honesty holds at the version mismatch (control gate stays `unverified`).
- A settled live codex turn projects exactly once on the re-read conversation page (L5 F1): the
  installed regression asserts post-settlement page uniqueness (2/2 turns), which no prior installed
  suite did, and fails `2 != 1` on stashed `projector.py`.

### Todos

None.

## Docs References

No Domain Documentation source is configured; the installed contract is repository-owned.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The suite drives the registered routes against the live installed adapters.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The seventeen registered routes proven live. | L57-L570 | [control/api.py](agents-remember/mcp/src/agents_remember/serving/conversation/control/api.py) |
| The interrupt ledger whose live settlement this proves. | L87-L449 | [control/operations.py](agents-remember/mcp/src/agents_remember/serving/conversation/control/operations.py) |
| The control capability gate whose Claude version-mismatch honesty this pins. | L301-L342 | [control/capabilities.py](agents-remember/mcp/src/agents_remember/serving/conversation/control/capabilities.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

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
