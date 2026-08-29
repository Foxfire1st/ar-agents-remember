# mcp/tests/test_closeout_ledger_evidence_order.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_closeout_ledger_evidence_order.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-29T19:31+02:00 |
| lastVerifiedCommitHash | `60e429d17e9fcbca3ab1c02563afcaa5761b8c5a` |
| lastVerifiedCommitDate | 2026-08-29T20:33:10+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Forces ledger creation and resume to use the accepted explicit ledger message and the exact mutation-evidence order around Git.

## Code Commentary

### Logic

The shared fixture writes the canonical settings shape, creates real code and external-memory repositories, starts the public closeout generation, and advances its durable recovery tuple through the existing memory result. The created-ledger test then drives the real ledger route and observes the exact mutation sequence: two `mutation-intent` publications (before and after expected-tree binding), Git commit creation, and `commit-proven` evidence. It proves the pre-state HEAD is the memory-content commit, the expected tree is the ledger commit tree, and the observed HEAD/tree are the exact ledger result. The resumed-output test first creates that real result, then re-enters the external closeout route with the durable tuple; it requires one verified-existing ledger progress event and forbids memory refresh or ledger rewrite. Together the tests distinguish created, existing, and resumed authority without inferring a commit subject or replaying Git.

### Invariants And Boundaries

- Mutation intent is durable before staging or Git commit.
- Expected output is bound before the commit and proof follows the exact commit.
- Resume consumes proven output without refresh or rewrite.
- Even when resume bypasses refresh, the production call receives the typed
  `ExternalCloseoutEvidence` boundary rather than a shape-compatible dictionary.
- Memory then ledger is a sequential two-commit path, not an atomic transaction.
- The canonical repository settings fixture participates in the real admission path; tests do not bypass configured authority.

## Docs References

See task `260821-CLIVE-L1` L1-R3, L1-R4, and L1-R6.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The fixture supplies canonical settings and a real journaled external-memory operation. | `_journaled_ledger_fixture` | mcp/tests/test_closeout_ledger_evidence_order.py:30-70 |
| Created ledger output publishes both intent states, exact tree binding, Git commit, and observed proof in order. | `test_created_ledger_output_publishes_intent_bind_commit_and_proof` | mcp/tests/test_closeout_ledger_evidence_order.py:73-130 |
| Resume consumes the exact recovery tuple through one verified-existing event without refresh or rewrite, while still constructing the typed external evidence input. | `test_resumed_external_output_uses_exact_recovery_tuple_without_refresh` | mcp/tests/test_closeout_ledger_evidence_order.py:308-362 |

## Cross-Repo References

The temporary external-memory repository is the ledger Git authority under test.

## 260821-CLIVE-L2 Current Regression Contract

The current forcing seams include `test_created_ledger_output_publishes_intent_bind_commit_and_proof`, `test_ledger_intent_is_exact_before_real_write_or_stage`, `test_resumed_external_output_uses_exact_recovery_tuple_without_refresh`. The L2 additions force immutable normalized input, exact generation retention, evidence-derived cancellation/recovery, and pre-authority refusal of invalid calls. A failed first call remains task-addressably recoverable without amending accepted intent.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| The current test source exercises `test_created_ledger_output_publishes_intent_bind_commit_and_proof`, `test_ledger_intent_is_exact_before_real_write_or_stage`, `test_resumed_external_output_uses_exact_recovery_tuple_without_refresh`. | `test_created_ledger_output_publishes_intent_bind_commit_and_proof`; `test_ledger_intent_is_exact_before_real_write_or_stage`; `test_resumed_external_output_uses_exact_recovery_tuple_without_refresh` | mcp/tests/test_closeout_ledger_evidence_order.py:82-112; mcp/tests/test_closeout_ledger_evidence_order.py:186-254; mcp/tests/test_closeout_ledger_evidence_order.py:308-359 |

## Update History

- 2026-08-29T19:31+02:00 — Generation-12 repair: replaced the legacy dictionary fixture with the
  production `ExternalCloseoutEvidence` type while preserving the resumed no-refresh assertion.
  Verification remains closeout-owned.

- 2026-08-26T10:44:52+02:00 — No content impact: reviewed the ledger-recovery package relocation and corrected porcelain-status expectation; intent, tree, commit, and proof ordering are unchanged.
- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this test card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1 candidate-11: rebound the canonical settings fixture, real created/existing/resumed ledger routes, and exact intent/tree/commit ordering against accepted tree `4241908c`; first verification stamp remains governed-closeout-owned.
