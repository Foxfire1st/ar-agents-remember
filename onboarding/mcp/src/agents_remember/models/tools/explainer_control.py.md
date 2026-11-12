# mcp/src/agents_remember/models/tools/explainer_control.py

## Governing Overview

[Route overview](../overview.md)

## Purpose

The strict response model for `explainer_control`: one answer shape for three actions, carrying the state reached and the record the action read or wrote.

## Code Commentary

- The answer names the state reached — updated, current, retired, claimed or refused — together with the master-to-Architect ownership record, the architect id the call was accepted from or refused against, and the per-action record.
- `update` and `retire` carry the seat service's own record unchanged, and a refusal carries its reason so the answer says how to take the master over.
- An admitted state whose action is not one of the three valid actions is rejected by the model, while a refusal may carry the unknown action that was refused.
- The withdrawn id list stops at 200 entries, claim counts are non-negative integers without a declared upper bound, and the architect id is bounded at 128 characters.

## Evidence

- An admitted answer must name one of the three admitted actions [1]
- One answer carries the state, the seat record and the architect id together [2]
- A refusal may name an action the surface does not admit [3]
- What a claim did with held reports is its own bounded record [4]
- The seat record is the id, the act and when it was written [5]

- ExplainerControlRecord is master-to-Architect authority; the claim list has a 200-entry bound while integer claim counts have only nonnegative constraints. [6]
