# mcp/src/agents_remember/serving/ports.py

## Governing Overview

[serving overview](overview.md)

## Purpose

`serving/ports.py` (260731-EFA-L9, R8) is the canonical conversation read and control port
surface. It holds `ActiveConversationPort`, `ConversationLibraryPort`, `ControlSessionLike`,
`TerminalCatalogPort`, and `ControlPlanePort` so conversation modules no longer import
`harness_control_client` or `terminal_catalog` directly; `serving/conversation/ports.py`
re-exports these names for the conversation package.

## Code Commentary

### Logic

`ActiveConversationPort` (cit:(["class ActiveConversationPort"], mcp/src/agents_remember/serving/ports.py:62-62)) and `ConversationLibraryPort`
(cit:(["class ConversationLibraryPort"], mcp/src/agents_remember/serving/ports.py:94-94)) are the two read protocols; `ControlSessionLike`
(cit:(["class ControlSessionLike"], mcp/src/agents_remember/serving/ports.py:122-122)), `TerminalCatalogPort` (cit:(["class TerminalCatalogPort"], mcp/src/agents_remember/serving/ports.py:135-145)), and
`ControlPlanePort` (cit:(["class ControlPlanePort"], mcp/src/agents_remember/serving/ports.py:196-196)) expose the control/terminal seams. The canonical
definitions live here so serving modules can import them without triggering the conversation
package's route composition. `TerminalCatalogPort.list` reads the instance snapshot, while
`list_committed` (cit:([`list_committed`], mcp/src/agents_remember/serving/ports.py:142-142)) explicitly reads the
last committed atomic snapshot for contention-safe sweeper callers; `__all__` (cit:([`__all__`], mcp/src/agents_remember/serving/ports.py:279-285)) curates the surface.

### Invariants And Boundaries

- Exactly two read ports separate active exact-session reads from dormant native library reads;
  lifecycle/control authority is explicitly not a third read store port.
- Conversation modules must consume these ports rather than re-importing the moved
  harness-control/terminal-catalog modules (layering rail + conversation foundation tests).

### Todos

No known follow-up.

## Evidence

### Docs References

No external/domain documentation is configured.

No configured domain documentation was available.

### Repo-Internal References

- The conversation package re-exports the canonical definitions. [1]


### Cross-Repo References

No cross-repository implementation participates.

No meaningful cross-repo references found.

## 260821-CLIVE Retention Port Contract

`TerminalCatalogPort.compact` accepts the exact set of task-registered execution ids. The port keeps
registration proof explicit at the deletion boundary; it does not grant the catalog a task reader
or permit unregistered worker/reviewer/curator rows to be reclaimed.
