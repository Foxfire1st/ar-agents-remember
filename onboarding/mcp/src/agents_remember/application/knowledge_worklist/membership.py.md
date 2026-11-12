# mcp/src/agents_remember/application/knowledge_worklist/membership.py

## Governing Overview

[knowledge worklist overview](overview.md)

## Purpose

This module detects live invariants that newly require a no-family judgment and registers the `unassigned_invariant` worklist kind. Its subject is `membership:<invariant ID>`; its revision fact identifies the candidate revision the leaf's `membership` row must answer.

## Code Commentary

### Logic

`membership_items` builds the candidate and base membership sets, then examines candidate invariants in sorted ID order. It skips retired invariants and every invariant currently listed by a family. It emits an item only for a new invariant or an invariant listed in a base family but no longer listed in the candidate. Each item binds its deterministic identity and facts to the candidate revision.

### Invariants And Boundaries

- A live old orphan unlisted on both sides produces no leaf item: migration owns that inherited stock.
- Restoring family membership removes the item; this detector does not create a membership row or choose families for the Curator.
- The registered satisfying row is the current leaf's `membership` row at the candidate revision, with disposition `no_family`.
- This source account describes the implemented item kind, not execution of L53's deferred inherited-condition repair. The packet's nine inherited records remain separately assigned to L54.

## Evidence

### Repo-Internal References

- Registration binds membership subjects, revision facts and the leaf's current no_family row. [1]
- Detection includes only new or newly unlisted live invariants and excludes old orphans and currently listed or retired invariants. [2]
