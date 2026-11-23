# mcp/src/agents_remember/serving/explainer_routes.py

## Governing Overview

[Route overview](overview.md)

## Purpose

HTTP request parsing and route handlers for the explainer's bound composition.

## Code Commentary

The explainer's routes parse a request, check it against the binding the seat was launched with, and answer with facts or a named refusal. A request for a seat this process does not hold is refused by name rather than answered from another seat.

The Build handler forwards the parsed history with the composed message to the seat builder. A blank planned request therefore selects the requirement-and-planned-effects wording.

## Boundaries

The detail this module owns stops at its own boundary; the route account above says what the surrounding surface promises.

## Evidence

- handle_state answers a request only for the seat this process holds. [1]

- The Build handler forwards the validated history to the builder. When the composed message is blank and history is planned, the builder sends the requirement-and-planned-effects request. [2]
