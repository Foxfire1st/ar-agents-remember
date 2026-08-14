# mcp/tests/test_conversation_library_cursor.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_conversation_library_cursor.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T16:04+02:00 |
| lastVerifiedCommitHash |  `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`|
| lastVerifiedCommitDate |  2026-08-14T14:36:50+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The cursor authority under test: mint/verify for cursors, keys, and resume targets plus digests and generations. | `LibraryCursorAuthority`; `identity_digest`; `catalog_generation`; `mint_list_cursor`; `verify_list_cursor`; `mint_read_cursor`; `verify_read_cursor`; `mint_conversation_key`; `verify_conversation_key`; `mint_resume_target`; `verify_resume_target` | mcp/src/agents_remember/serving/conversation/library/cursor.py:62-297; mcp/src/agents_remember/serving/conversation/library/cursor.py:72-87; mcp/src/agents_remember/serving/conversation/library/cursor.py:89-98; mcp/src/agents_remember/serving/conversation/library/cursor.py:102-115; mcp/src/agents_remember/serving/conversation/library/cursor.py:117-130; mcp/src/agents_remember/serving/conversation/library/cursor.py:132-138; mcp/src/agents_remember/serving/conversation/library/cursor.py:140-146; mcp/src/agents_remember/serving/conversation/library/cursor.py:150-170; mcp/src/agents_remember/serving/conversation/library/cursor.py:172-186; mcp/src/agents_remember/serving/conversation/library/cursor.py:190-211; mcp/src/agents_remember/serving/conversation/library/cursor.py:213-228 |
| The canonical scope, query digest, and limit clamp under test. | `canonical_library_scope`; `query_digest`; `clamp_limit` | mcp/src/agents_remember/serving/conversation/library/scope.py:30-71; mcp/src/agents_remember/serving/conversation/library/scope.py:74-87; mcp/src/agents_remember/serving/conversation/library/scope.py:90-97 |

## Cross-Repo References

No neighboring repository participates in this contract suite.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-02T20:47+02:00 — 260731-EFA-L6 W2-B01 curator: anchored 2 citation rows with exact cursor and scope symbols; scoped citation fixing regenerated the source ranges.

- 2026-07-19T16:04+02:00 — 260718-CHATS-L2 curator: created the cursor/scope contract suite
  sidecar. Verification is blank until closeout commits and stamps the new source.
