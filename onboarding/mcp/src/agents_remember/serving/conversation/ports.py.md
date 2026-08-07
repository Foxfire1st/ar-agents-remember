# mcp/src/agents_remember/serving/conversation/ports.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/ports.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-18T10:55+02:00 |
| lastVerifiedCommitHash |  `b252c42cca200933d5c9c36e26de47a526a569ce`|
| lastVerifiedCommitDate |  2026-08-07T23:58:52+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Structured conversation contract overview](overview.md)

## Purpose

Defines the only two structured-conversation read boundaries: one for an already-running exact AR
session and one for dormant native catalog/history access for a specific harness.

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

| Finding | Anchor | Source |
| --- | --- | --- |
| Normalized cursor, identity, page, event, status, capability, and resume types are defined centrally. |"class ConversationEventEnvelope"|mcp/src/agents_remember/serving/conversation/_models_status.py:232-232|
| The topology regression requires exactly these two ports and forbids a control port. | `test_exactly_two_conversation_ports_exist` | mcp/tests/test_conversation_foundation.py:22-29 |

## Cross-Repo References

No meaningful cross-repo boundary exists for these local protocols.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-18T10:55+02:00 — 260715-FEUI-L9 curator: created the exact two-port boundary sidecar.
  Verification is blank until closeout commits and stamps the new source.
