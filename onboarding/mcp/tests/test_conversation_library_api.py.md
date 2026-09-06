# mcp/tests/test_conversation_library_api.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_conversation_library_api.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:46+00:00 |
| lastVerifiedCommitHash |  `d9a1eb82849baea6c0b86735e772a932f4bbdc7c`|
| lastVerifiedCommitDate |  2026-08-12T00:45:15+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Conversation-library list and idempotent open contracts over ASGI.

## Code Commentary

### Logic

The real route composition validates wire scope and returns a signed conversation key, identity digest and capabilities. Escaped scopes refuse with 403 and an unknown harness with 404. A created open result binds the proven vendor/bridge identity; exact replay reuses it without reopening, while changed input conflicts.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Native ports, opener, proof and retirement are doubled. These three retained tests do not establish the historical read/status/reconcile matrix or an installed-runtime integration.

### Todos

No file-local implementation change is requested by this reconciliation.

## Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain evidence applies to the file-local claims above. | N/A | N/A |

## Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

| Finding | Anchor | Source |
| --- | --- | --- |
| List route returns wire page and authorizes scope. | `test_list_route_returns_wire_page_and_authorizes_scope` | mcp/tests/test_conversation_library_api.py:356-369 |
| List route rejects scope escapes and unknown harness. | `test_list_route_rejects_scope_escapes_and_unknown_harness` | mcp/tests/test_conversation_library_api.py:371-380 |
| Open created replays and focuses only proven identity. | `test_open_created_replays_and_focuses_only_proven_identity` | mcp/tests/test_conversation_library_api.py:459-503 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:46+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-08-11T19:58+02:00 — Reconciled `test_conversation_library_api.py` with its current structural task/seat, tool-vocabulary, or quality-boundary regression contract and removed stale exact-id/leaf implications where present.
- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-02T20:53:56+02:00 — W2-B04 curator: repaired 6 citation findings; scoped check passed.

- 2026-07-31T16:50+02:00 — 260731-EFA-L2 curator: named the new request seam the card's peer
  claims now depend on. `asgi_request` no longer takes the app and a `client=(host, port)` keyword
  separately; it takes one frozen `AsgiClient` dataclass that binds the app to the peer address the
  connection reports, with loopback as the default, and the non-loopback fail-closed case supplies
  `AsgiClient(self.app, peer=("10.0.0.5", 9000))`. The doubled `ConversationOpenService` is now
  constructed from a `LibraryBinding` parameter object. Rewrote the Conventions paragraph to say
  both; the thirteen async cases and the whole status ladder are unchanged. Verification metadata
  stays pinned until closeout stamps the candidate commit.
- 2026-07-19T16:04+02:00 — 260718-CHATS-L2 curator: created the library ASGI route suite
  sidecar. Verification is blank until closeout commits and stamps the new source.
