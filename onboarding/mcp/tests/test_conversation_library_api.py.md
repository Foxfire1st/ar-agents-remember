# mcp/tests/test_conversation_library_api.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_conversation_library_api.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T16:04+02:00 |
| lastVerifiedCommitHash |  `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`|
| lastVerifiedCommitDate |  2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

ASGI contract suite for the native conversation-library list, read, open, status, and reconcile routes.

## Code Commentary

### Logic

The suite pins typed success/refusal status mapping, authorization and composition boundaries, request-id reconciliation, and open launch context. Launch context carries optional canonical `taskDocumentRef` plus seat role and reaches the service without a leaf-key field.

### Conventions

Test-only evidence uses deterministic fakes/fixtures and exercises the public or owning internal seam directly.

### Invariants And Boundaries

Routine refusals remain typed; open outcomes stay total over declared statuses; exact opened proof is required before publishing focusable session identity.

## Docs References

No Domain Documentation source is configured for this repository-local regression contract.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Current suite declaration anchoring this card. | `LibraryApiTests` | mcp/tests/test_conversation_library_api.py:312-312 |

## Cross-Repo References

No cross-repository implementation source governs this test module.

## Update History

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
