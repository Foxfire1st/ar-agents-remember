# mcp/src/agents_remember/serving/explainer_routes.py

## Governing Overview

[Route overview](../overview.md)

## Purpose

HTTP request parsing and route handlers for the explainer's bound composition.

## Code Commentary

The explainer's routes parse a request, check it against the binding the seat was launched with, and answer with facts or a named refusal. A request for a seat this process does not hold is refused by name rather than answered from another seat.

## Boundaries

The detail this module owns stops at its own boundary; the route account above says what the surrounding surface promises.

## Evidence

- handle_state answers a request only for the seat this process holds. [1]
