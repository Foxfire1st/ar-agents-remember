# mcp/src/agents_remember/serving/conversation/ports.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/ports.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-18T10:55+02:00 |
| lastVerifiedCommitHash |  `7bf564a663bb61f12844dee39538dd09a1633cdb`|
| lastVerifiedCommitDate |  2026-08-10T12:28:42+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No Domain Documentation source is configured for this repository-owned port boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The conversation facade imports its library protocol from the canonical serving port owner. Current source: `ConversationLibraryPort` (mcp/src/agents_remember/serving/ports.py:94-119).


| Finding | Anchor | Source |
| --- | --- | --- |
| Normalized cursor, identity, page, event, status, capability, and resume types are defined centrally. |"class ConversationEventEnvelope"|mcp/src/agents_remember/models/conversations/stream_events.py:88-88|


## Cross-Repo References

No meaningful cross-repo boundary exists for these local protocols.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260731-EFA-L9 Change

The module is now a thin re-export of `serving/ports.py` (R8 backwards-edge removal): the port
protocols moved to the canonical serving port surface, and `__all__` here mirrors those five
names. Conversation modules must not import `harness_control_client` or `terminal_catalog`
directly; they consume these ports.

## Update History

- 2026-08-08T14:38+02:00 — 260731-EFA-L9 curator: rewrote for the canonical-port re-export;
  body updated from the two-port-only description. Verification metadata pinned until closeout
  stamps the L9 code commit.
- 2026-07-18T10:55+02:00 — 260715-FEUI-L9 curator: created the exact two-port boundary sidecar.
  Verification is blank until closeout commits and stamps the new source.
