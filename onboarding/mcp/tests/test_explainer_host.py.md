# mcp/tests/test_explainer_host.py

## Governing Overview

[Route overview](overview.md)

## Purpose

Tests the explainer seat’s host launch, capsule, settings-selected launch values, provider-specific tool preapproval, seat state and cancellation.

## Code Commentary

- A created seat carries the capsule as its instructions, takes no first prompt, and is left idle.
- Its state is read from the host's own turn fields, so live, closed, archived and never-ran come from `turnActive` and `lastTurn` rather than from a request.
- The create-payload fixture asserts the exact Codex public roster plus `render`, `define_category`, `remove_category` and `grade`, and the exact Claude grant of `server_info` plus those four. The fixture observes the create payload through a fake bridge and checks both grants against the seat's own task server.
- A host map with extra arguments and an unreadable daemon configuration still permits creating and sending to the explainer seat.
- The cases refuse a host-reported model mismatch and a seat without the explainer label. A different or absent host-reported permission mode is recorded alongside the launch request's mode. The suite it belongs to exercises the four explainer-owned tools - `render`, `define_category`, `remove_category` and `grade` - and the workspace it writes into, not a read-back tool; removal archives the chat and deletes the workspace.


The cancel case sends the exact seat ID and request ID through the bridge, observes a stopped turn and closed pending permission decision, clears the recorded pending marker, and keeps the seat mode. This test uses a scripted bridge reply, so it is not proof of cancellation against a live host.

- `test_the_launch_environment_carries_the_module_the_product_fetched` holds `_launch_env` to the module the product fetched into its data folder, so a seat launched after the first explanation is handed the same module the fetch placed rather than looking for a checkout's.

## Evidence







- The launch environment carries the module the product fetched. [7]



- The case checks that the capsule is the seat's instructions and no first prompt is sent. [1]


- Seat state comes from the host's own turn fields. [4]


- The settings-selected model, effort and mode reach the create payload, and provenance keeps the reported mode. [5]


- The cancellation fixture checks the exact seat and request, a stopped turn, no open decision and the retained mode. [6]



- The policy case asserts the exact Codex public roster and Claude server_info, each with the four tools on the bound explainer server. [8]

- A host map with extra arguments and an unreadable daemon configuration still permits creating and sending to the seat. [9]

- The explainer records a differing observed mode separately from the request. [10]
- The explainer records the absence of an observed mode while retaining the requested mode. [11]
