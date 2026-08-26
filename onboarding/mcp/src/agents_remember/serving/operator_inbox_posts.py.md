# mcp/src/agents_remember/serving/operator_inbox_posts.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/operator_inbox_posts.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-25T23:19+02:00 |
| lastVerifiedCommitHash | `c51373425be3e3f488590ad2f444810df89b4ffb`|
| lastVerifiedCommitDate | 2026-08-26T19:22:10+02:00|
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
When a structural caller already supplies a complete document-and-role address with no runtime
coordinates, `_post_address` preserves it verbatim instead of densifying the durable envelope with
the current occupant id. Private delivery correlation remains separate.
`_persist_post` names `store.append` as the durable commit point. Compaction and expectation
publication follow that boundary, so a later exception is post-commit evidence that the structural
dispatch caller must reconcile rather than permission to retire the recipient.

### Conventions

Task topology and catalog are injected collaborators. A returned entry id is plane correlation and
never required for ordinary agent replies.

### Invariants And Boundaries

- Persistence precedes any delivery attempt.
- Post-time and delivery-time resolution both honor occupant replacement.
- Decision items require a current sprint owner.
- One post contains the complete ask/response boundary.
- A complete structural address is not rewritten into a dead-session-id address at post time.
- Append is the durable commit point; failures from later maintenance or delivery do not prove the
  brief absent.

### Todos

None.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Post-time owner rebinding preserves a complete canonical structural address. | `_post_address` | mcp/src/agents_remember/serving/operator_inbox_posts.py:110-149 |
| Append is the durable commit point before compaction and expectation publication. | `_persist_post` | mcp/src/agents_remember/serving/operator_inbox_posts.py:232-248 |
| The shared post path derives, stamps, persists, and delivers the row. | `post_operator_inbox_entry` | mcp/src/agents_remember/serving/operator_inbox_posts.py:268-366 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## Update History

- 2026-08-25T23:19+02:00 — Contract-wide citation curation: re-read the current anchored claim(s), retained the supported wording, and cleared verification metadata for closeout-owned restamping.

- 2026-08-25T22:27+02:00 — 260821-ARSPAWN-L2 final curation: recorded append as the explicit
  durable commit point and prohibited treating post-commit maintenance failure as proof of absence.
  Verification remains closeout-owned.

- 2026-08-25T20:31+02:00 — ARSPAWN-L2 quality pass: extracted canonical-address recognition so
  `_post_address` remains below the complexity limit; behavior is unchanged and citations were
  regenerated against the same candidate. Verification remains closeout-owned.

- 2026-08-25T19:51+02:00 — 260821-ARSPAWN-L2: complete structural destinations remain
  document-and-role-only through persistence; current occupant ids stay out of the durable envelope.
  Verification remains closeout-owned.

- 2026-08-11T19:58+02:00 — Aligned the current serving card for `operator_inbox_posts.py` with seat ownership, delivery, lifecycle, and terminal boundaries represented by this source.
- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
