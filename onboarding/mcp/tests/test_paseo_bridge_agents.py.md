# mcp/tests/test_paseo_bridge_agents.py

## Governing Overview

[Route overview](overview.md)

## Purpose and current source account

The Node client seam distinguishes created/existing/refused identities, explicit workspace placement and task workspace reuse, first-message ordering, exact get/archive and data-size handling. serviceTier is native feature data and unsupported values refuse before create. A refused `fast_mode` names that offending feature and may perform feature discovery, but sends no public create, daemon create or first message. Returned agents retain `modeId` and `featureValues`, and provider rows retain modes/default-mode/fetched-at fields. A stub client exercises the protocol; these are not live provider success claims.

## First-message send shape

`AgentCommandScriptTests` asserts the options the first-message send actually passes: `{messageId}` alone, with no `activeTurnBehavior`. A newly created agent runs no turn, and the only behaviours the client route offers can end one, so the script asks for none; the same message id goes with the call on every run. The expectation is the script stub's record, not a live host call.

## Workspace test support

The controlled host accepts workspace descriptors keyed by the exact idempotency key and exposes `current()` before refresh. Selected keys can disappear from the live refresh listing while their completed creation replay remains available. This fixture supports the separate reopened-workspace cases through the real Node bridge; it is not a live host or provider execution witness. Existing live-task, folder-only and placement refusal assertions remain.

## Evidence

- Keyed completed creation replay, pre-refresh current identity and selectively hidden live listing support the real-bridge archive tests. [3]

- The scoped current source carries the module/document behavior described above. [1]

- Feature discovery may precede refusal, but refused features send no agent create or message. [2]
