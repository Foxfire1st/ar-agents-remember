# mcp/tests/test_conversation_library_cursor.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_conversation_library_cursor.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T16:04+02:00 |
| lastVerifiedCommitHash |  `67cad9bcdc736de70168ea9c153a0f12319a7263`|
| lastVerifiedCommitDate |  2026-07-19T17:19:21+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Contract tests for the 260718-CHATS-L2 library cursor/key authority and the canonical scope
authority: signed-token round-trips, tamper and wrong-purpose rejection, digest semantics, and
the narrow-only scope resolution rules.

## Code Commentary

### Logic

Twelve tests cover: list and read cursor round-trips with tamper and wrong-purpose rejection;
foreign-signature conversation keys; conversation key and resume target round-trips with
garbage rejection; identity-digest stability plus scope/vendor sensitivity; content-derived
positive catalog generations; the harness+scope+sort query digest binding; canonical scope
defaulting to the workspace root, narrowing inside it, and rejecting traversal/symlink/
cross-scope escapes; and the shared page-limit clamp.

### Conventions

Plain pytest functions with `tmp_path` filesystem fixtures; the authorities under test are
constructed directly (no ASGI layer) so the token and scope contracts are probed in isolation.

### Invariants And Boundaries

- A token that verifies under the wrong purpose, prefix, scope, or signature must fail closed.
- Scope resolution must never clamp or guess an escaping cwd into an allowed one.

### Todos

None.

## Docs References

No Domain Documentation source is configured. The repository sources are direct evidence.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The cursor authority under test: mint/verify for cursors, keys, and resume targets plus digests and generations. | L62-L98 | [cursor.py](agents-remember/mcp/src/agents_remember/serving/conversation/library/cursor.py) |
| The canonical scope, query digest, and limit clamp under test. | L30-L97 | [scope.py](agents-remember/mcp/src/agents_remember/serving/conversation/library/scope.py) |

## Cross-Repo References

No neighboring repository participates in this contract suite.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-19T16:04+02:00 — 260718-CHATS-L2 curator: created the cursor/scope contract suite
  sidecar. Verification is blank until closeout commits and stamps the new source.
