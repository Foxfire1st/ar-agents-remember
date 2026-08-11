# mcp/src/agents_remember/serving/operator_inbox_posts.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/operator_inbox_posts.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-11T09:50+02:00 |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c` |
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

Creates, persists, optionally delivers, and reports one whole operator-inbox post. Owner-addressed
traffic is re-resolved through the current structural seat before persistence.

## Code Commentary

### Logic

The post path derives task-document/role ownership from the sender and topology, rebinds only proven
owner addresses, stamps stable subject/routing plus private correlations, appends before delivery,
then records adapter outcome. Arbitrary peer addresses are not hijacked by owner derivation.
Dispatch briefs remain exact-pinned.

### Conventions

Task topology and catalog are injected collaborators. A returned entry id is plane correlation and
never required for ordinary agent replies.

### Invariants And Boundaries

- Persistence precedes any delivery attempt.
- Post-time and delivery-time resolution both honor occupant replacement.
- Decision items require a current sprint owner.
- One post contains the complete ask/response boundary.

### Todos

None.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Post-time owner rebinding is limited to qualified owner addresses. | `_post_address` | mcp/src/agents_remember/serving/operator_inbox_posts.py:110-148 |
| Persistence occurs before optional delivery. | `_persist_post` | mcp/src/agents_remember/serving/operator_inbox_posts.py:218-228 |
| The shared post path derives, stamps, persists, and delivers the row. | `post_operator_inbox_entry` | mcp/src/agents_remember/serving/operator_inbox_posts.py:254-335 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## Update History

- 2026-08-11T19:58+02:00 — Aligned the current serving card for `operator_inbox_posts.py` with seat ownership, delivery, lifecycle, and terminal boundaries represented by this source.
- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
