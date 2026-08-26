# mcp/tests/test_closeout_input_model_invariants.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_closeout_input_model_invariants.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:48+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Pins impossible closeout input, mutation-evidence, and cross-kind lifecycle states at the strict model and public-admission boundaries.

## Code Commentary

### Logic

The suite validates the typed enabled/not-applicable legs directly, proves the normalizer and consumer share exact plan identity, then constructs hostile lifecycle and evidence payloads. Blank or unstripped messages, N/A legs with message authority, incomplete snapshots, a commit on any non-commit-proven state, impossible pre-state/proof combinations, cross-kind authority/results, input/evidence disagreement, and non-closeout journals at closeout admission all fail at the owner that can make the state impossible.
The public-admission regression first proves `LifecycleOperationStore.create` refuses an integrate
record at the closeout address. It then injects those bytes to simulate damaged external state and
proves closeout admission returns a typed `LifecycleOperationReadError` with expected
`operationKind=closeout` and observed `operation-kind-mismatch`, rather than overwriting the file.

### Invariants And Boundaries

- Enabled intent is stripped and nonblank; not-applicable intent has no message.
- The effective plan is immutable between normalization and consumption.
- Evidence state determines which facts must or must not exist.
- `reconciled-unchanged` may retain its bound expected output tree, but it can never name a commit.
- Closeout and integrate authority/results cannot be mixed.
- Public closeout admission accepts only a closeout journal.

## Docs References

See task `260821-CLIVE-L1` L1-R1 through L1-R6.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Typed message-leg and exact-plan invariants are forced. | `test_enabled_message_model_refuses_blank_or_unstripped_text`, `test_normalizer_and_consumer_share_exact_plan_identity` | mcp/tests/test_closeout_input_model_invariants.py:66-68; mcp/tests/test_closeout_input_model_invariants.py:84-104 |
| Mutation evidence refuses incomplete state facts and a commit on reconciled-unchanged evidence. | `test_mutation_evidence_refuses_incomplete_state_facts`, `test_reconciled_unchanged_evidence_cannot_name_a_commit` | mcp/tests/test_closeout_input_model_invariants.py:121-123; mcp/tests/test_closeout_input_model_invariants.py:126-143 |
| Impossible commit proof plus cross-kind and input/evidence contradictions fail closed. | `test_mutation_evidence_refuses_impossible_prestate_and_commit_proof`, `test_operation_model_refuses_cross_kind_authority_and_results`, `test_operation_model_refuses_closeout_input_and_evidence_mismatches`, `test_public_closeout_admission_refuses_a_non_closeout_journal` | mcp/tests/test_closeout_input_model_invariants.py:146-171; mcp/tests/test_closeout_input_model_invariants.py:174-208; mcp/tests/test_closeout_input_model_invariants.py:211-230; mcp/tests/test_closeout_input_model_invariants.py:233-254 |

## Cross-Repo References

The external-memory fixture provides distinct repository identities only to prove repository-bound model facts.

## 260821-CLIVE-L2 Current Regression Contract

The current forcing seams include `test_enabled_message_model_refuses_blank_or_unstripped_text`, `test_not_applicable_leg_has_no_message_authority`, `test_normalizer_and_consumer_share_exact_plan_identity`, `test_mutation_evidence_refuses_incomplete_state_facts`. The L2 additions force immutable normalized input, exact generation retention, evidence-derived cancellation/recovery, and pre-authority refusal of invalid calls. A failed first call remains task-addressably recoverable without amending accepted intent.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| The current test source exercises `test_enabled_message_model_refuses_blank_or_unstripped_text`, `test_not_applicable_leg_has_no_message_authority`, `test_normalizer_and_consumer_share_exact_plan_identity`, `test_mutation_evidence_refuses_incomplete_state_facts`. | `test_enabled_message_model_refuses_blank_or_unstripped_text`; `test_not_applicable_leg_has_no_message_authority`; `test_normalizer_and_consumer_share_exact_plan_identity`; `test_mutation_evidence_refuses_incomplete_state_facts` | mcp/tests/test_closeout_input_model_invariants.py:66-69; mcp/tests/test_closeout_input_model_invariants.py:72-82; mcp/tests/test_closeout_input_model_invariants.py:85-105; mcp/tests/test_closeout_input_model_invariants.py:108-124 |

## Current Contract — 260821 CLIVE Final

This is the current source-backed contract for this test card. It supersedes any earlier
queue-lifecycle, blocker-row, replan/drain, or compatibility-reader wording where present.

Forces strict normalized closeout input, mutation-evidence, and operation-model invariants at the public boundary.

### Current Invariants

- Blank enabled messages, impossible evidence, cross-kind state, and mismatched input are rejected.
- Reconciled-unchanged evidence cannot claim a commit; not-applicable legs own no message.

## Update History

- 2026-08-26T10:44:52+02:00 — Added the cross-kind journal-collision contract: store creation and public closeout admission both fail loud without overwriting unreadable/mismatched authority.

- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: reconciled this test card to current source while preserving prior history and verification provenance.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this test card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-22T11:29+02:00 — 260821-CLIVE-L1 candidate12 rebind: added the
  model-level proof that reconciled-unchanged evidence may retain expected intent but cannot name a
  commit. Bound to reviewed candidate tree `8f03b256fe24aa77262da805f1538ee39ccb4dd6`, full diff SHA
  `ccb36a898b455cd67ca00c378e5ba0f18851be01faf3d26eced3b9af062f429e`, same-reviewer PASS;
  first verification stamp remains governed-closeout-owned.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: created from accepted candidate tree `4241908c`; first verification stamp remains governed-closeout-owned.
