# mcp/src/agents_remember/kernel/worktree_service_binding.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

The one process-wide holder for a process's worktree services: bound directly by the composition, or built once from a supplier on the first operation that actually asks.

## Code Commentary

- It imports nothing internal, so a server startup can name how to build the services without importing the operation package — the naming is light enough to load while the tool surface is being declared.
- `worktree_services` builds from the supplier once, drops the supplier and keeps that instance exactly as if it had been bound at startup; every later caller reaches the same object.
- With neither services nor a supplier it raises `WorktreeServicesUnboundError` naming the composition that must bind them; it never constructs a default.
- `reset_worktree_services` clears both the bound instance and the pending supplier. A subsequent lookup stays unbound until the composition explicitly binds a bundle or supplier; reset cannot rebuild the state the caller just cleared.
- This module is the single definition and `worktrees.services` re-exports these names, preserving object identity for callers that bind through either path.

## Evidence

- Unbound services refuse an operation by name instead of building a default [1]
- The first dependent operation builds the services from the supplier and keeps them [2]
- A supplier can be named at startup without loading the services package [3]
- Binding directly leaves any pending supplier untouched [5]

- One light process holder accepts a supplier without constructing services. The first dependent lookup builds once and keeps the instance; reset clears both current services and supplier, so reset cannot silently reconstruct cleared services. [6]

- A reset clears both the bound services and the pending supplier [4]
