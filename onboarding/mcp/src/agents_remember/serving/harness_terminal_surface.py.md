# mcp/src/agents_remember/serving/harness_terminal_surface.py

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Renders the normalized transcript and input surface for a hosted harness while routing terminal and
automated messages into the bridge's shared ordered queue.

## Code Commentary

The surface owns `UncommittedDraft`: only draft update and draft submit operations touch it. A
durable delivery is a separate whole message and cannot inject into, submit, or discard draft text.
Immediate/queued acceptance clears only the submitted draft revision; ambiguous acceptance retains
the draft for reconciliation. Pane content remains a readable projection, not authority.

## Invariants And Boundaries

- Human draft custody belongs to the surface, not the adapter or durable delivery path.
- Transcript rendering is derived from normalized bridge state.
- No native vendor full-screen TUI is driven concurrently with the bridge.

## Evidence

### Repo-Internal References

- Draft and transcript models. [1]
- Shared queue owner. [2]
