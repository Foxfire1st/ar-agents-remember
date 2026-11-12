# mcp/tests/test_explainer_surface.py

## Governing Overview

[Route overview](overview.md)

## Purpose

One server bound at launch serving only the explainer's tools: it advertises exactly that surface, dispatches only that surface, and refuses service rather than falling back to the ordinary roster.

## Code Commentary

- A bound server advertises the explainer's own tools and nothing else, while naming an AR tool directly is refused — the half discovery cannot show.
- An invalid, non-JSON or empty binding refuses service as a binding fault; an ordinary server with neither marker nor binding keeps the full roster.
- A lost binding on a launched explainer seat refuses rather than taking the ordinary branch, so absence never chooses the roster.
- A new generation refuses the old server's calls, a marker pointing at another environment refuses, and every bound tool refuses a forged seat while answering the launched one. The suite it belongs to exercises that four-tool surface - `render`, `define_category`, `remove_category` and `grade` - and the workspace it writes into, not a read-back tool; removal archives the chat and deletes the workspace.

## Evidence

- The case `test_a_bound_server_advertises_the_explainers_surface_and_nothing_else` protects a bound server advertising exactly the explainer's surface. 
- The case `test_a_bound_server_refuses_a_tool_outside_its_surface_by_name` protects a direct call to a tool outside the surface being refused by name. 
- The case `test_a_lost_binding_on_a_launched_explainer_seat_refuses_rather_than_taking_the_ordinary_branch` protects a launched seat with no binding refusing instead of taking the ordinary branch. [3]
- The case `test_a_new_generation_refuses_the_old_servers_calls` protects a server launched for an old generation refusing the calls made after a resume. [4]
- The case `test_the_production_surface_wires_the_delivery_sender` protects the launch-built surface handing its bound tools the production delivery sender. 

- Retired at the fifth freeze d59c3493: mcp/tests/test_explainer_surface.py::test_a_bound_server_advertises_the_explainers_surface_and_nothing_else - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 5f8398b32760677c370e3145add73cfa8388357b; mcp/tests/test_explainer_surface.py::test_a_bound_server_refuses_a_tool_outside_its_surface_by_name - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 5f8398b32760677c370e3145add73cfa8388357b; mcp/tests/test_explainer_surface.py::test_the_production_surface_wires_the_delivery_sender - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 5f8398b32760677c370e3145add73cfa8388357b. Retired means the anchor no longer stands, not that the cited subject was deleted.
