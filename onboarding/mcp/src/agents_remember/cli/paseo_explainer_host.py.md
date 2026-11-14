# mcp/src/agents_remember/cli/paseo_explainer_host.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

The explainer seat’s adapter to the Paseo host: create or adopt without a first turn, send, resume, archive, inspect seat state, and cancel the exact turn.

## Code Commentary

- This is the half that may call the bridge; the seat service in `canvas` never does, and it reaches the host only through the ports bound at the bottom of this module.
- `_launch_env` supplies the agent marker, workspace marker and binding JSON and refuses `explainer-launch-incomplete` if a supplied launch value is empty. It also carries the browser module when this installation can find one — a user’s `AR_PLAYWRIGHT` first, then the product’s fetched module, then a checkout's `dashboard/node_modules/playwright/index.js`; absence of a browser is left for the render boundary to report.
- A seat is never trusted on its word: `_require_applied` refuses `explainer-seat-config-unapplied` when the host's own statement of the launched or resumed seat differs from the chosen provider, model, effort, mode or feature values.

- `create_seat` refuses an unlabelled repository, a capability label other than the class's own, and a role setting the runtime cannot honour; `send` reconciles a lost outcome by asking the host whether the message id is present before anything is re-sent, and reports a busy or permission-pending answer as held rather than as denied.
- `cancel` names this one agent and request and leaves the seat unarchived — reporting the request uncertain when the host knows no such seat — while `in_turn` fails closed on absent turn facts yet reads a host-named `closed` seat as not in a turn.

## Evidence

- A seat the host launched on other values than the settings chose is refused [2]


- A send whose outcome was unknown is reconciled by message id before any resend [5]
- Cancellation names the exact request and never archives or replaces the seat [6]




- The module the product fetched is preferred over a checkout's, so a package installation's module is handed on. [7]


- Launch identity values must be nonempty; the browser module is supplied only when available [1]

- The create carries the capsule as instructions; Claude receives preapproval for server_info and the four explainer tools, while Codex receives no toolPolicy. [4]
