# mcp/src/agents_remember/cli/paseo_explainer_host.py

## Governing Overview

[Route overview](../../../overview.md)

The host’s initializing view already counts as live and in turn. A prior turn still distinguishes a closed seat from one that never began.

## Purpose

The explainer seat’s adapter to the Paseo host: create or adopt without a first turn, send, resume, archive, inspect seat state, and cancel the exact turn.

## Code Commentary

- This is the half that may call the bridge; the seat service in `canvas` never does, and it reaches the host only through the ports bound at the bottom of this module.
- `_launch_env` supplies the agent marker, workspace marker and binding JSON and refuses `explainer-launch-incomplete` if a supplied launch value is empty. It also carries the browser module when this installation can find one — a user’s `AR_PLAYWRIGHT` first, then the product’s fetched module, then a checkout's `dashboard/node_modules/playwright/index.js`; absence of a browser is left for the render boundary to report.
- Fresh create compares a reported provider and verifies the requested model, effort and features. Adopting an existing seat after a create conflict reads the host's agent record and bypasses the fresh-create check. Create and adoption record the normalized host mode, including a differing or absent value, in `observedChoices.mode` beside the requested `choices.mode`. Normalization takes the first reported value from `lastModeId`, `modeId`, `currentModeId` or `runtimeInfo.modeId`. Resume can send model, effort and mode. If the reply contains an agent record, the applied check verifies the requested model and effort. Resume can fill an absent top-level mode key from the host report and leaves the initial `observedChoices.mode` intact.

- `create_seat` refuses an unlabelled repository, a capability label other than the class's own, and a role setting the runtime cannot honour; `send` reconciles a lost outcome by asking the host whether the message id is present before anything is re-sent, and reports a busy or permission-pending answer as held rather than as denied.
- `cancel` names this one agent and request and leaves the seat unarchived — reporting the request uncertain when the host knows no such seat — while `in_turn` fails closed on absent turn facts yet reads a host-named `closed` seat as not in a turn.

Create supplies the capsule as instructions and uses the shared seat policy for the bound task server. Codex receives the full public roster and the four explainer tools. Claude receives `server_info` and the four explainer tools.

## Evidence



- Fresh create compares reported provider and verifies requested model, effort and features. Adoption reads state without that check. Resume verifies requested model and effort only when the reply includes an agent record. [2]




- A send whose outcome was unknown is reconciled by message id before any resend [5]
- Cancellation names the exact request and never archives or replaces the seat [6]




- The module the product fetched is preferred over a checkout's, so a package installation's module is handed on. [7]



- Launch identity values must be nonempty. The browser module is supplied only when available. [1]




- Creation carries the capsule as instructions and grants each seat its provider's tools on its own server. Codex gets the public roster plus the four explainer additions. Claude gets server_info plus those additions. [4]



- Create and adoption store the normalized host mode separately from the requested choice. A differing or absent report remains observable. [8]


- Resume can fill an absent top-level mode key from the agent report while leaving the initial observedChoices.mode intact. [9]
