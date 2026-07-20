# mcp/tests/test_conversation_control_installed.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_conversation_control_installed.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T15:45+02:00 |
| lastVerifiedCommitHash |  `0be0099744bf1287805acf0b95072127b70f7104`|
| lastVerifiedCommitDate |  2026-07-20T15:34:11+02:00|
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

### Conventions

The installed suite does not use the fake `ControlHarness` (it drives the real routes unseeded, so it
also exercises the production memo's create-on-miss branch). Version-locked to live codex 0.144.5 and
pi 0.80.7; without the opt-in flag the live classes skip with exact reasons.

### Invariants And Boundaries

- Live proof crosses the registered production routes over a real wire, never scenario fixtures.
- Interrupt acknowledgement and settlement are both proven live (codex `interrupted`, pi polled
  `interrupted` + stale-identity 422).
- Claude honesty holds at the version mismatch (control gate stays `unverified`).

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

- 2026-07-20T15:45+02:00 — 260718-CHATS-L3 curator: created the sidecar for the opt-in installed-
  runtime proof — live codex/pi interrupt ack+settlement, queue truth, withdrawal recovery, typed
  attachment submit, and telemetry through the registered routes, plus the Claude version-honesty gate.
  Verification is blank because the new source file is uncommitted; closeout owns its first source
  stamp.
