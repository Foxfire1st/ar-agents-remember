# mcp/src/agents_remember/serving/conversation/ports.py

## Governing Overview

[Structured conversation contract overview](overview.md)

## Purpose

Defines the structured-conversation read and control boundaries: one for an already-running exact
AR session, one for dormant native catalog/history access for a specific harness, and — since
260731-EFA-L9 — the control/terminal seams (`ControlPlanePort`, `TerminalCatalogPort`,
`ControlSessionLike`). The canonical definitions now live in `serving/ports.py`; this module is a
re-export so conversation modules can import them without triggering the conversation package's
route composition.

## Code Commentary

### Logic

`ActiveConversationPort` identifies an exact session, pages its native-hydrated items, subscribes
after an active-event cursor, and returns status/capabilities. `ConversationLibraryPort` lists one
authorized project scope, reads a native conversation with library-only cursors, and resolves a
server-private exact resume target.

### Conventions

The ports use async reads/streams and normalized models. They declare behavior without selecting a
vendor adapter or persistence implementation.

### Invariants And Boundaries

- Exactly two `*Port` protocols exist.
- Active and dormant library cursors are distinct.
- Control/lifecycle authority stays elsewhere; there is no `NativeControlPort`.
- A native resume target is server-private and not an authorization grant.

### Todos

Concrete per-harness implementations belong to later active/library leaves.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository-owned port boundary.

No configured domain documentation was available.

### Repo-Internal References

The conversation facade imports its library protocol from the canonical serving port owner. Current source: `ConversationLibraryPort` (mcp/src/agents_remember/serving/ports.py:94-119).


- Normalized cursor, identity, page, event, status, capability, and resume types are defined centrally. [1]


### Cross-Repo References

No meaningful cross-repo boundary exists for these local protocols.

No meaningful cross-repo references found.

## 260731-EFA-L9 Change

The module is now a thin re-export of `serving/ports.py` (R8 backwards-edge removal): the port
protocols moved to the canonical serving port surface, and `__all__` here mirrors those five
names. Conversation modules must not import `harness_control_client` or `terminal_catalog`
directly; they consume these ports.
