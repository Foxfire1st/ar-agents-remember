# mcp/tests/test_tool_entry_point_sweep_controls.py

## Governing Overview

[MCP test overview](overview.md)

## Purpose

The controls the entry-point sweep depends on: a bad payload must be caught by the choke point, and the census must be able to see a write, a rewrite and a delete.

## Code Commentary

`ChokePointControlTests` requires a tool that never answers to fail by name and close its handler, a payload its model forbids to be refused by the choke point, and a raising entry point to be classified as losing the envelope. It also drives the two shapes a break takes for a caller: a producer key the response model forbids arrives as boundary validation, which the sweep asserts empty by name because the choke point validates before returning; and a handler that returns a raw dict past the choke point arrives as unvalidatable, which is the only route to that arm. An invalid argument lands in its own arm and names the caller's side, which only the refusing model separates from the boundary shape. `EntryPointCensusControlTests` requires the census to notice a write, a rewrite and a delete in a repository, and the coordination boundary to notice an undeclared addition, rewrite and deletion outside every write zone, which is where the repository censuses are blind.

## Invariants And Boundaries

Each arm is proven reachable by a constructed shape rather than assumed, and one arm is asserted empty by name so a break cannot hide in it. The census control exercises the same predicate the hermeticity case asserts.

## Evidence

### Repo-Internal References

- The choke point catches a forbidden payload, and the two failure shapes arrive in their own named arms. [1]

- The census notices a write, a rewrite and a delete inside a repository and at the coordination boundary. [2]
