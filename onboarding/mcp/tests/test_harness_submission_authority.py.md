# mcp/tests/test_harness_submission_authority.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_harness_submission_authority.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-17T21:39+02:00 |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb` |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Provides the focused concurrency and lifecycle proof for `HarnessSubmissionAuthority`, including
the pop-back linearization point that end-to-end FEUI-L5 required.

## Code Commentary

### Logic

The suite races withdrawal against dispatch, keeps status/withdraw responsive during slow adapter
work, and proves completion-before-receipt dominance for prompts and setters. It exercises full-ref
dedupe under id reuse, strict timeline ordering, payload/source conflicts, bounded duplicate tables,
certified preflight busy versus impossible safe retry after a possible first byte, epoch mismatch,
raw-free disclosure, and invalid operation references. These tests are the regression pins for the
architectural gap surfaced when Alt+Up first put queue, adapter, and UI behavior under one end-to-end
interaction. The shared `_authority(...)` fixture builds the system under test from two parameter
objects — `BridgeSnapshotPort(clock, snapshot, set_snapshot, publish)` for the bridge seam and
`SubmissionLimits(timeline, ledger, dispatch_grace_seconds)` for the bounds — with `bridge_epoch`
still a direct keyword.

### Invariants And Boundaries

- Concurrency tests synchronize at authority/adapter seams rather than relying on sleeps alone.
- A successful withdraw proves the operation never claimed adapter dispatch; losing the race keeps
  truthful non-withdrawable state.
- Early exact terminal evidence may dominate unknown, but stale/partial/id-only completion cannot.
- Bounds never evict live, active, or unknown rows.

## Docs References

No Domain Documentation source is configured for this repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live domain-documentation source was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Slow-adapter responsiveness and dispatch/withdraw races. | `test_dispatch_claim_wins_atomic_withdrawal_race` | mcp/tests/test_harness_submission_authority.py:307-321 |
| Early completion, full-ref reuse, ordering, conflicts, bounds, epoch, and privacy. | `test_completion_before_receipt_is_buffered_and_releases_exact_head` | mcp/tests/test_harness_submission_authority.py:351-379 |
| The system under test defines the sole timeline and lifecycle lock. | `HarnessSubmissionAuthority` | mcp/src/agents_remember/serving/harness_submission_authority.py:116-1023 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| This is a repository-local authority suite. | — | — |

## 260718-CHATS-L5I Current Delta

Submission-authority tests now pin the bounded dispatch-acceptance grace: a delayed healthy echo becomes an honest queued receipt and only later authoritative lifecycle evidence settles it.

This entry supersedes conflicting earlier coverage notes while retaining their history; source verification metadata is deliberately unchanged until the code commit.

## Update History

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-04T18:16+02:00 — 260731-EFA-L6 S18-B16 curator: repaired 3 citation rows: the concurrency/race tests at test_harness_submission_authority.py L230-L350, the early-completion/invalid-ref tests at L351-L687, and the authority class under test at harness_submission_authority.py L116-L150. Scoped fixer + non-fixing recheck green under the frozen snapshot; verification metadata unchanged.

- 2026-07-31T16:50+02:00 — 260731-EFA-L2 curator: corrected both self-file line ranges in
  Repo-Internal References and recorded the fixture's new shape. The leaf rewired the `_authority`
  helper to construct `HarnessSubmissionAuthority` from a `BridgeSnapshotPort` and a
  `SubmissionLimits` parameter object instead of six loose keywords, and collapsed five wrapped
  `authority.withdraw`/`authority.status` calls onto single lines; together those shifted this
  file's contents by up to six lines in either direction. Verified against the current source,
  the slow-adapter and dispatch/withdraw race block now spans L222-L339 (was cited L214-L292) and
  the early-completion through invalid-operation-reference block spans L341-L674 (was cited
  L293-L636). No test method was added, removed or renamed and no assertion changed, so the
  Purpose, Logic and all four invariants stand as written.
- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: refreshed the regression-coverage record for the current backend/shared behavior and preserved the pre-commit verification stamp.

- 2026-07-17T21:39+02:00 — Created for 260715-FEUI-L5; captured authoritative pop-back races,
  completion-before-receipt, exact-ref id reuse, ordering, idempotency/conflict, retry safety,
  retention, epoch, and privacy proofs. Verification metadata remains pinned to the leaf base.
