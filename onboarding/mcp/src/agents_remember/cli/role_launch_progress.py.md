# mcp/src/agents_remember/cli/role_launch_progress.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

One disposable preparation notice for an in-flight start, owned and reclaimed by the dispatch lock lifetime.

## Code Commentary

The module keeps exactly one `(request_id, phase)` slot: `begin` claims it as `preparing`, `starting` advances the same request, and `finish` clears it in the dispatch owner's finally path. `read` returns the phase only for the exact request id and `None` otherwise. The notice is working state, not a record: the dispatch receipt remains the authority, and no second notice can be created for another request.

## Evidence

- The notice is claimed for one exact request and advanced only in place. [1]
- The notice is reclaimed when the dispatch owner finishes. [2]
- A read returns a phase only for its exact request id. [3]
