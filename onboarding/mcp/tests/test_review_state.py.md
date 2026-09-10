# test_review_state.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_review_state.py`         |
| doc_type               | `file-level-onboarding`                 |
| lastUpdated            | 2026-09-08T22:13:55+02:00                                     |
| lastVerifiedCommitHash |                                            `6f3e3fde75a1ca0202c9b07557cf86a7893e8532`|
| lastVerifiedCommitDate |                                            2026-09-10T07:24:09+02:00|
| governingOverview      | `overview.md`                            |

## Governing Overview

[tests/overview.md](overview.md)

## Purpose

Focused R27/R28 tests for the persisted fixed-list review state, ordinary three-round cap, and
direct recorded developer-permission transition.

## Code Commentary

### Logic

The fixture builds a minimal `TaskDocument` without `reviewState`, proving that missing state is
accepted as zero. The missing-state and explicit-zero tests then start round one and make the
pending bit observable; replaying a pending begin is idempotent.

The baseline test seals two findings on a blocking result, then verifies successor rounds advance
to rounds two and three while retaining the baseline and shrinking remaining IDs to an empty list.
The successor-refusal test rejects new IDs, duplicate IDs, and passing results with unresolved IDs.
The final R27 test rejects recording without `begin_task_review` and rejects a result without a
valid verdict. The cap tests refuse a fourth ordinary round with an actionable count, accept one
direct recorded developer approval only at exhaustion, accumulate a second allowance without
resetting the sealed issue list, and leave exhausted state unchanged for malformed permission
payloads.

### Conventions

This is implementation preparation evidence. The R27 worker report records the original state
checks and identity tests; the L41 report records the cap and direct-permission checks, plus the
32-test focused run and static checks. This card does not elevate those results to independent
review or acceptance. The tests exercise recorded permission fields only; they do not authenticate
the purported developer.

### Invariants And Boundaries

- Tests preserve the small state model: missing/zero state, pending admission, sealed baseline and
  monotonic remaining IDs.
- They preserve the ordinary three-round ceiling, cumulative explicit allowances, and pending
  replay idempotence.
- They do not prove authentication, human authorship, or integration review.

## Docs References

No external Domain Documentation source governs these repository-owned tests.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external source applies. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Missing/zero state starts round one and pending replay is idempotent. | `test_missing_state_starts_round_one_and_replay_is_pending_idempotent`; `test_explicit_zero_state_starts_round_one` | mcp/tests/test_review_state.py:30-54 |
| Baseline sealing and successor rounds only shrink remaining IDs. | `test_baseline_seals_findings_and_successors_only_shrink_remaining` | mcp/tests/test_review_state.py:49-80 |
| Successors reject new, duplicate, reintroduced and unresolved passing IDs. | `test_successor_rejects_new_duplicate_reintroduced_and_unresolved_passing_ids` | mcp/tests/test_review_state.py:83-104 |
| Recording requires begin and a valid verdict. | `test_record_requires_begin_and_verdict` | mcp/tests/test_review_state.py:115-120 |
| Ordinary exhaustion refuses a fourth round with count and limit. | `test_default_three_round_limit_refuses_fourth_with_actionable_count` | mcp/tests/test_review_state.py:139-147 |
| A direct developer permission adds cumulative rounds only after exhaustion and preserves findings. | `test_one_explicit_extra_round_preserves_count_and_issue_list_then_refuses_fifth` | mcp/tests/test_review_state.py:149-190 |
| Malformed permission payloads leave exhausted state unchanged. | `test_invalid_developer_exception_leaves_exhausted_state_unchanged` | mcp/tests/test_review_state.py:192-209 |

## Source File Binding

The current L41 source bytes are SHA-256
`b007e8ec8440b0aca8f7897f86108c982ec33e9c03e7517240993282874f5212`
(`7707` bytes, `209` lines). The source is an uncommitted preparation candidate, so
verification metadata remains blank until a genuine commit-owned refresh.

## Update History

- 2026-09-09T14:10+02:00 — CCR-L42 curator intake created/reconfirmed this one-to-one card against the current uncommitted source bytes (SHA-256 `b007e8ec8440b0aca8f7897f86108c982ec33e9c03e7517240993282874f5212`, `7707` bytes, `209` lines). Verification remains closeout-owned; no test, review, acceptance, or future commit is asserted.

- 2026-09-08T22:56:00+02:00 — CCR-R27/R28 bounded memory curation: corrected 2 report-listed citation anchor/range entries against the paired frozen source; existing verification metadata and historical bindings remain unchanged.

- 2026-09-08T22:13:55+02:00 — CCR-R28 L41 memory curation: refreshed this card to the exact L41
  source and documented the ordinary cap, exhaustion-only direct permission, cumulative allowance,
  pending replay preservation, and malformed-payload refusal cases.

- 2026-09-08T22:01:43+02:00 — CCR-R27 domain-foundation preparation: created the focused review-state test card from
  the exact L40 source. Composition manifest SHA-256: `05d471d6ba42bbcfd76aed54ed592a3478eaa051a21459f45370bf15878b7bb0`; worker execution evidence
  remains preparation-only.
