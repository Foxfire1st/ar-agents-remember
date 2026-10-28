# mcp/tests/test_explainer_host.py

## Governing Overview

[Route overview](overview.md)

## Purpose

The seat on the host: the capsule is its instructions, its tool policy preapproves exactly the surface its bound server declares, and its model, effort and mode come from the settings role.

## Code Commentary

- A created seat carries the capsule as its instructions, takes no first prompt, and is left idle.
- Its state is read from the host's own turn fields, so live, closed, archived and never-ran come from `turnActive` and `lastTurn` rather than from a request.
- The policy admits exactly the tools the bound server declares — a tool the server admits is callable, and no other.
- A host map carrying extra arguments, or one that cannot be read, refuses the confined step.
- A seat launched on values other than the role's own is refused, and a seat without the explainer label is not this seat at all. The suite it belongs to exercises that four-tool surface - `render`, `define_category`, `remove_category` and `grade` - and the workspace it writes into, not a read-back tool; removal archives the chat and deletes the workspace.


The cancel case sends the exact seat ID and request ID through the bridge, observes a stopped turn and closed pending permission decision, clears the recorded pending marker, and keeps the seat mode. This test uses a scripted bridge reply, so it is not proof of cancellation against a live host.

## Evidence

- The case `test_the_seat_is_created_with_the_capsule_and_no_first_prompt` protects the capsule being the seat's instructions with no first prompt. [1]
- The case `test_the_policy_preapproves_exactly_the_tools_the_server_declares` protects the tool policy matching the server's declared surface and nothing more. 
- The case `test_a_host_map_with_extra_arguments_refuses_the_confined_step` protects a confined step refusing to run where the host map adds arguments. 
- The case `test_the_seat_state_reads_the_hosts_own_agent_view` protects seat state being read from the host's own turn fields. [4]
- The case `test_the_settings_role_owns_the_seats_model_effort_and_mode` protects the role's model, effort and permission mode reaching the create and holding. [5]

- The cancel case sends the exact seat ID and request ID through the bridge, observes a stopped turn and closed pending permission decision, clears the recorded pending marker, and keeps the seat mode. This test uses a scripted bridge reply, so it is not proof of cancellation against a live host. [6]

- Retired at the fifth freeze d59c3493: mcp/tests/test_explainer_host.py::test_the_policy_preapproves_exactly_the_tools_the_server_declares - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 5f8398b32760677c370e3145add73cfa8388357b; mcp/tests/test_explainer_host.py::test_a_host_map_with_extra_arguments_refuses_the_confined_step - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 5f8398b32760677c370e3145add73cfa8388357b. Retired means the anchor no longer stands, not that the cited subject was deleted.
