# mcp/tests/test_explainer_host.py

## Governing Overview

[Route overview](overview.md)

## Purpose

Tests the explainer seat’s host launch, capsule, settings-selected launch values, provider-specific tool preapproval, seat state and cancellation.

## Code Commentary

- A created seat carries the capsule as its instructions, takes no first prompt, and is left idle.
- Its state is read from the host's own turn fields, so live, closed, archived and never-ran come from `turnActive` and `lastTurn` rather than from a request.
- Claude is granted `server_info` and exactly `render`, `define_category`, `remove_category` and `grade`; Codex receives no `toolPolicy`. These assertions do not establish confinement of either harness.
- A host map with extra arguments and an unreadable daemon configuration still permits creating and sending to the explainer seat.
- A seat launched on values other than the role's own is refused, and a seat without the explainer label is not this seat at all. The suite it belongs to exercises that four-tool surface - `render`, `define_category`, `remove_category` and `grade` - and the workspace it writes into, not a read-back tool; removal archives the chat and deletes the workspace.


The cancel case sends the exact seat ID and request ID through the bridge, observes a stopped turn and closed pending permission decision, clears the recorded pending marker, and keeps the seat mode. This test uses a scripted bridge reply, so it is not proof of cancellation against a live host.

- `test_the_launch_environment_carries_the_module_the_product_fetched` holds `_launch_env` to the module the product fetched into its data folder, so a seat launched after the first explanation is handed the same module the fetch placed rather than looking for a checkout's.

## Evidence







- The launch environment carries the module the product fetched. [7]


- The case `test_the_seat_is_created_with_the_capsule_and_no_first_prompt` protects the capsule being the seat's instructions with no first prompt. [1]
- The case `test_the_seat_state_reads_the_hosts_own_agent_view` protects seat state being read from the host's own turn fields. [4]
- The case `test_the_settings_role_owns_the_seats_model_effort_and_mode` protects the role's model, effort and permission mode reaching the create and holding. [5]
- The cancel case sends the exact seat ID and request ID through the bridge, observes a stopped turn and closed pending permission decision, clears the recorded pending marker, and keeps the seat mode. This test uses a scripted bridge reply, so it is not proof of cancellation against a live host. [6]

- The policy case grants Claude server_info and the four explainer tools, and omits toolPolicy for Codex. [8]
- A host map with extra arguments and an unreadable daemon configuration still permits creating and sending to the seat. [9]
