# mcp/tests/test_conversation_control_api.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_conversation_control_api.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T15:45+02:00 |
| lastVerifiedCommitHash |  `0be0099744bf1287805acf0b95072127b70f7104`|
| lastVerifiedCommitDate |  2026-07-20T15:34:11+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Production-route tests for the conversation control API (R7). Every test drives the real composition
on one loop — bridge + IPC server on a real user-private socket, a real catalog row, the L0
`register_conversation_routes` composition, and HTTP over a real uvicorn wire — with the structural
fake adapter as the only double at the harness edge.

## Code Commentary

### Logic

`ControlApiTests` (L26) exercises the seventeen registered routes over the real wire: the O4
typed-error mapping per route family, remote-peer 403, epoch guards, multipart attachment staging,
read-only policy 405s on PATCH/PUT/DELETE, the queue-truth privacy + withdrawal flow end-to-end, and
`test_no_paste_pty_or_native_queue_substitution_in_control_modules` (L354), the source scan proving
no PTY Esc / paste / native-queue substitution anywhere in the control modules.

### Conventions

This is the only L3 suite that crosses a real HTTP wire; the routes resolve their service through the
unmodified `conversation_control_service` path (the harness seeds the `NOW`-anchored instance into the
memo, so the wire is time-consistent without touching this file). The source scan is a
topology/absence assertion, intentional for a leaf that establishes what does NOT exist.

### Invariants And Boundaries

- Every routine refusal lands on its precise HTTP status over the real wire — no raw 500.
- Non-loopback peers fail 403; every wire verifies the expected bridge epoch.
- Policy/telemetry/queue/pending are GET-only; policy mutation verbs return 405.
- No paste/PTY/native-queue substitution exists in the control modules (source-scanned).

### Todos

None.

## Docs References

No Domain Documentation source is configured; the route contract is repository-owned.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The suite drives the registered routes and their O4 mapping over the real wire and shared topology.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The seventeen registered routes and the O4 typed-error mapping under test. | L57-L570 | [control/api.py](agents-remember/mcp/src/agents_remember/serving/conversation/control/api.py) |
| The shared fake-topology harness (real bridge/IPC/authority/L0 composition). | L408-L520 | [_control_plane.py](agents-remember/mcp/tests/_control_plane.py) |
| The foundation pin that independently asserts the exact seventeen routes. | L54-L82 | [test_conversation_foundation.py](agents-remember/mcp/tests/test_conversation_foundation.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-20T15:45+02:00 — 260718-CHATS-L3 curator: created the sidecar for the production-route
  suite — the seventeen routes over a real uvicorn wire, O4 mapping, remote-peer 403, epoch guards,
  multipart staging, policy 405s, the queue-truth privacy/withdrawal flow, and the no-paste/no-
  substitution source scan. Verification is blank because the new source file is uncommitted;
  closeout owns its first source stamp.
