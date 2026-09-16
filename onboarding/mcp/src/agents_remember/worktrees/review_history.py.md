# mcp/src/agents_remember/worktrees/review_history.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/worktrees/review_history.py` |
| doc_type               | `file-level-onboarding`                 |
| lastUpdated            | 2026-09-08T22:13:55+02:00                                     |
| lastVerifiedCommitHash |                                            `3b552f5a215648274dc5e6e4d5f0a01c2ee80be2`|
| lastVerifiedCommitDate |                                            2026-09-12T01:54:48+02:00|
| governingOverview      | `../../../overview.md`                   |

## Governing Overview

[worktrees overview](../../../overview.md)

## Purpose

Owns task-document transitions for the fixed-list review protocol: begin a pending round,
publish one result, require the pending bit before reviewer work, and enforce the ordinary
three-round limit with a directly recorded developer permission for cumulative extra rounds.

## Code Commentary

### Logic

`begin_task_review` treats missing or explicit zero `reviewState` as round zero and starts round
one with `pending=True`. Replaying a pending begin is idempotent and does not consume an allowance.
A completed sealed state with no remaining findings refuses a new round. The transition imports
the existing ordinary three-round limit; at exhaustion it requires a nonblank `developerApproval`
and positive `additionalRounds`, records that answer, and accumulates the allowance without
resetting the round or sealed issue list. Before exhaustion, or on a first/zero-state begin, that
permission payload is rejected. The recorded answer is a direct workflow input; this module adds
no authentication or provenance claim.

`record_task_review` requires a pending state and permits only verdict, findings,
`remainingFindingIds`, and `verdictRef`. The first result validates and seals the baseline
findings; a non-empty baseline must remain blocking and remaining IDs are derived from those findings.
Successor rounds may not add findings and may only shrink the prior remaining set and the sealed
baseline. A passing successor must leave no finding unresolved.

`require_pending_review` is the reviewer-work admission guard. It refuses when state is missing or
not pending and otherwise returns the task-owned state unchanged.

### Invariants And Boundaries

- Missing state means zero; no external history store or identity/authentication claim is introduced.
- The transition is monotonic over the sealed finding list: later rounds can only remove remaining IDs.
- The ordinary cap is fixed at the existing settings constant; explicit developer permission adds
  only a positive cumulative allowance and never resets the count or baseline.
- This module owns state transitions, not candidate-tree, evidence, integration authority, or
  reviewer authentication.
- The worker report records implementation checks only; this card does not claim review or acceptance.

### Todos

None.

## Docs References

No external Domain Documentation source governs these task-owned transitions.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external source applies. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Error/status boundary, cap-aware begin semantics, and pending admission. | `ReviewHistoryError`; `begin_task_review`; `require_pending_review` | mcp/src/agents_remember/worktrees/review_history.py:13-105 |
| Publication field validation, developer-permission parsing, and sealed baseline creation. | `_validate_publication_fields`; `_parse_developer_exception`; `_record_baseline` | mcp/src/agents_remember/worktrees/review_history.py:94-107; mcp/src/agents_remember/worktrees/review_history.py:110-147; mcp/src/agents_remember/worktrees/review_history.py:150-172 |
| Successor monotonicity and duplicate/blank-ID refusals. | `_record_successor`; `_require_unique_ids` | mcp/src/agents_remember/worktrees/review_history.py:175-206; mcp/src/agents_remember/worktrees/review_history.py:209-213 |

## Source File Binding

The current L41 source bytes are SHA-256
`a9ef793019ed3e2a66c258d977a493d9f431194b91d2f6c4897acd5821a895b6`
(`9166` bytes, `235` lines). The source is an uncommitted preparation candidate, so
verification metadata remains blank until a genuine commit-owned refresh.

## Update History
- 2026-09-11T22:39:01+00:00: Generated citation repair: `_validate_publication_fields`; `_parse_developer_exception`; `_record_baseline` repointed to mcp/src/agents_remember/worktrees/review_history.py:94-107; mcp/src/agents_remember/worktrees/review_history.py:110-147; mcp/src/agents_remember/worktrees/review_history.py:150-172. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `_record_successor`; `_require_unique_ids` repointed to mcp/src/agents_remember/worktrees/review_history.py:175-206; mcp/src/agents_remember/worktrees/review_history.py:209-213. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-09T14:10+02:00 — CCR-L42 curator intake created/reconfirmed this one-to-one card against the current uncommitted source bytes (SHA-256 `a9ef793019ed3e2a66c258d977a493d9f431194b91d2f6c4897acd5821a895b6`, `9166` bytes, `235` lines). Verification remains closeout-owned; no test, review, acceptance, or future commit is asserted.


- 2026-09-08T22:13:55+02:00 — CCR-R28 L41 memory curation: refreshed this card to the exact
  transition source and recorded the existing three-round cap, actionable exhaustion refusal,
  pending replay behavior, and direct recorded developer-approval allowance. No auth or second
  review-history authority is implied.

- 2026-09-08T22:01:43+02:00 — CCR-R27 domain-foundation preparation: created the review-history transition card from
  the exact L40 source, preserving absence-as-zero, direct-call rejection and monotonic finding
  semantics. Composition manifest SHA-256: `05d471d6ba42bbcfd76aed54ed592a3478eaa051a21459f45370bf15878b7bb0`; implementation evidence only.
