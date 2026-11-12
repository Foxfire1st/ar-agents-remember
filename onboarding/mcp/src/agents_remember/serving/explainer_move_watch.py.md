# mcp/src/agents_remember/serving/explainer_move_watch.py

## Governing Overview

[Route overview](../overview.md)

## Purpose

Comparing explainer bindings on page opens and turn ends, publishing in-process notices.

## Code Commentary

Explainer bindings are compared at page open and at turn end, and a move is published as an in-process notice to the subscribers that asked for that exact repository, master and leaf. The watch opens no connection and takes no model turn.

## Boundaries

The detail this module owns stops at its own boundary; the route account above says what the surrounding surface promises.

## Evidence

- MoveNoticeWatch publishes a move to the subscribers keyed by the exact scope. [1]
