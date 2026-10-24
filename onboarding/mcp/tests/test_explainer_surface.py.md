# mcp/tests/test_explainer_surface.py

## Governing Overview

[Route overview](overview.md)

## Purpose

One server bound at launch serving only the explainer's tools: it advertises exactly that surface, dispatches only that surface, and refuses service rather than falling back to the ordinary roster.

## Code Commentary

- A bound server advertises the explainer's own tools and nothing else, while naming an AR tool directly is refused — the half discovery cannot show.
- An invalid, non-JSON or empty binding refuses service as a binding fault; an ordinary server with neither marker nor binding keeps the full roster.
- A lost binding on a launched explainer seat refuses rather than taking the ordinary branch, so absence never chooses the roster.
- A new generation refuses the old server's calls, a marker pointing at another environment refuses, and every bound tool refuses a forged seat while answering the launched one.

## Evidence

- The case `test_a_bound_server_advertises_the_explainers_surface_and_nothing_else` protects a bound server advertising exactly the explainer's surface. [1]
- The case `test_a_bound_server_refuses_a_tool_outside_its_surface_by_name` protects a direct call to a tool outside the surface being refused by name. [2]
- The case `test_a_lost_binding_on_a_launched_explainer_seat_refuses_rather_than_taking_the_ordinary_branch` protects a launched seat with no binding refusing instead of taking the ordinary branch. [3]
- The case `test_a_new_generation_refuses_the_old_servers_calls` protects a server launched for an old generation refusing the calls made after a resume. [4]
- The case `test_the_production_surface_wires_the_delivery_sender` protects the launch-built surface handing its bound tools the production delivery sender. [5]
