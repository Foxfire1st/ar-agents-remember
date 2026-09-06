# mcp/tests/test_conversation_library_cursor.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_conversation_library_cursor.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:46+00:00 |
| lastVerifiedCommitHash |  `7bf564a663bb61f12844dee39538dd09a1633cdb`|
| lastVerifiedCommitDate |  2026-08-10T12:28:42+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Conversation-library cursor purpose and canonical scope authority.

## Code Commentary

### Logic

List and read tokens round-trip their exact purpose, scope and continuation position. Tampered tokens and wrong-purpose reuse refuse. Canonical scope rejects traversal, symlink escape and cross-scope widening.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

A signed continuation is not permission to widen its bound project scope. Retained tests exercise repository-owned token contracts rather than an external conversation provider.

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
| List cursor round trip and tamper rejection. | `test_list_cursor_round_trip_and_tamper_rejection` | mcp/tests/test_conversation_library_cursor.py:32-45 |
| Read cursor round trip and wrong purpose rejection. | `test_read_cursor_round_trip_and_wrong_purpose_rejection` | mcp/tests/test_conversation_library_cursor.py:48-61 |
| Canonical scope rejects traversal symlink and cross scope. | `test_canonical_scope_rejects_traversal_symlink_and_cross_scope` | mcp/tests/test_conversation_library_cursor.py:64-82 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:46+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-02T20:47+02:00 — 260731-EFA-L6 W2-B01 curator: anchored 2 citation rows with exact cursor and scope symbols; scoped citation fixing regenerated the source ranges.

- 2026-07-19T16:04+02:00 — 260718-CHATS-L2 curator: created the cursor/scope contract suite
  sidecar. Verification is blank until closeout commits and stamps the new source.
