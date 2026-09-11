# mcp/src/agents_remember/tasks/route_review.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/tasks/route_review.py` |
| doc_type               | `file-level-onboarding`                 |
| lastUpdated            | 2026-09-08T22:13:55+02:00                                     |
| lastVerifiedCommitHash |                                            `6f3e3fde75a1ca0202c9b07557cf86a7893e8532`|
| lastVerifiedCommitDate |                                            2026-09-10T07:24:09+02:00|
| governingOverview      | `overview.md`                            |

## Governing Overview

[tasks/overview.md](overview.md)

## Purpose

Persisted route-review models shared by task documents and worktree review gates. The module also
owns the small fixed-list `ReviewState` record that makes review progress explicit without
introducing a second review-history store.

## Code Commentary

### Logic

`RouteReviewUnit` records one reviewed route and its evidence reference. `RouteReviewChildIntent`
and `RouteReviewScope` bind ordered atomic-master children to their canonical task intents.
`ReviewFinding` is the immutable finding definition used by the review state transition layer.

`ReviewState` carries a monotonic round number, a pending bit, a sealed baseline finding list, and
the remaining finding IDs. It also persists one nonblank `developerApproval` answer with its
positive cumulative `additionalRounds` allowance when the ordinary limit is exhausted. Its
validator requires unique baseline and remaining IDs, makes a zero-round state empty, requires
remaining IDs to belong to the sealed baseline, and requires the recorded permission and allowance
to appear together. Missing `TaskDocument.reviewState` is interpreted by the document and
transition owners as zero state.

`RouteReviewRecord` remains the candidate-bound persisted evidence record. Its coherence validator
keeps route verdicts consistent, requires aggregate intent when a scope is present, and treats
evidence digests, the dependency declaration, and record digest as an all-or-nothing group.

### Invariants And Boundaries

- Review state has no caller-selected purpose, identity, or authentication field; transition
  admission is owned by `worktrees/review_history.py`.
- The ordinary three-round limit is enforced by the transition service; this model carries only the
  bounded recorded developer permission and cumulative allowance used after exhaustion. It does
  not authenticate the answer or introduce a second authority.
- Route-review content addressing remains all-or-nothing, and atomic-master scope remains
  integration-owned.

### Todos

None.

## Docs References

No external Domain Documentation source governs these repository-owned models.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external source applies. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Route and child-intent model shapes. | `RouteReviewUnit`; `RouteReviewChildIntent`; `RouteReviewScope` | mcp/src/agents_remember/tasks/route_review.py:36-73 |
| Fixed-list finding, round-cap permission fields, and review-state validation. | `ReviewFinding`; `ReviewState` | mcp/src/agents_remember/tasks/route_review.py:76-137 |
| Candidate-bound route record coherence and content-addressing checks. | `RouteReviewRecord` | mcp/src/agents_remember/tasks/route_review.py:140-197 |

## Source File Binding

The current L41 source bytes are SHA-256
`b117340a17d8b38e60373e7878a609a48b615b1d5a7e75f330b4241a147afeb2`
(`8050` bytes, `209` lines). The source is an uncommitted preparation candidate, so
verification metadata remains blank until a genuine commit-owned refresh.

## Update History

- 2026-09-09T14:10+02:00 — CCR-L42 curator intake created/reconfirmed this one-to-one card against the current uncommitted source bytes (SHA-256 `b117340a17d8b38e60373e7878a609a48b615b1d5a7e75f330b4241a147afeb2`, `8050` bytes, `209` lines). Verification remains closeout-owned; no test, review, acceptance, or future commit is asserted.


- 2026-09-08T22:13:55+02:00 — CCR-R28 L41 memory curation: refreshed this card to the exact L41
  source and recorded the ordinary three-round boundary plus the paired developer-approval and
  cumulative-additional-round fields. The transition service owns the direct recorded-permission
  behavior; no authentication or second authority is implied.

- 2026-09-08T22:01:43+02:00 — CCR-R27 domain-foundation preparation: created the persisted route-review model card,
  including the small fixed-list ReviewState semantics, from the exact L40 source. Composition
  manifest SHA-256: `05d471d6ba42bbcfd76aed54ed592a3478eaa051a21459f45370bf15878b7bb0`; worker evidence only, with no independent review or
  acceptance claim.
