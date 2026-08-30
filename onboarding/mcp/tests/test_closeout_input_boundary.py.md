# mcp/tests/test_closeout_input_boundary.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_closeout_input_boundary.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-30T07:05+02:00 |
| lastVerifiedCommitHash | `346507af24396ab7b491e02511c4af006ccd3dc5` |
| lastVerifiedCommitDate | 2026-08-30T07:51:57+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Forces the worktree closeout input contract across omitted, empty, whitespace, enabled/not-applicable, internal/external, preview/apply, duplicate, candidate-drift, and crash-cut cases.

## Code Commentary

### Logic

The tests assert typed `invalidFields`, `resolvedPlan`, and `correctedCall` responses and spy on lifecycle authority and Git so refusals prove zero effect. They compare preview, durable fingerprint, accepted input, and worker args to establish one normalized value. Candidate-tree, same-tree/different-HEAD, and post-proof contract-drift cases prove stable provenance. Restart cases prove mutation evidence repairs the derived recovery projection rather than trusting cells. Low-level model impossibilities and ledger evidence ordering now live in their focused cards rather than expanding this route boundary.

The normalized-input parity scenario counts only the two valid apply calls as lifecycle-journal
admissions. Its whitespace-only third request must return the typed input refusal before invoking
`start_or_observe_closeout_operation`; reaching that owner would itself violate the no-effect
boundary.

### Invariants And Boundaries

- “Rejects blank strings” is insufficient: plan derivation, explicit enabled intent, typed N/A legs, normalization parity, and effect ordering are all forced.
- Invalid requests neither create nor observe lifecycle operations and do not transition queue state.
- Early crash recovery is evidence-based.

## Docs References

See task `260821-CLIVE-L1` L1-R1 through L1-R6.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Public input matrix and no-effect boundary are forced. | `test_enabled_message_observations_refuse_with_exact_correction`, `test_invalid_apply_after_selection_changes_no_authority_or_git_fact` | mcp/tests/test_closeout_input_boundary.py:54-94; mcp/tests/test_closeout_input_boundary.py:248-277 |
| Preview/apply/fingerprint/worker parity and immutable duplicate intent are forced. | `test_preview_apply_and_duplicate_fingerprints_share_one_normalized_input`, `test_valid_duplicate_keeps_one_generation_and_invalid_duplicate_cannot_observe_it` | mcp/tests/test_closeout_input_boundary.py:168-252; mcp/tests/test_closeout_input_boundary.py:506-551 |
| Retry refuses candidate or contract drift after proven output; crash cuts repair derived projection. | `test_public_retry_uses_accepted_plan_after_each_proven_output_cut`, `test_atomic_proof_publication_and_restart_repair_each_recovery_projection` | mcp/tests/test_closeout_input_boundary.py:576-625; mcp/tests/test_closeout_input_boundary.py:671-738 |

## Cross-Repo References

External-memory fixtures use real scratch repositories to distinguish memory content and ledger commits.

## 260821-CLIVE-L2 Current Regression Contract

The current forcing seams include `test_enabled_message_observations_refuse_with_exact_correction`, `test_plan_uses_lifecycle_possible_writes_and_typed_not_applicable`, `test_preview_apply_and_duplicate_fingerprints_share_one_normalized_input`, `test_invalid_apply_after_selection_changes_no_authority_or_git_fact`. The L2 additions force immutable normalized input, exact generation retention, evidence-derived cancellation/recovery, and pre-authority refusal of invalid calls. A failed first call remains task-addressably recoverable without amending accepted intent.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| The current test source exercises `test_enabled_message_observations_refuse_with_exact_correction`, `test_plan_uses_lifecycle_possible_writes_and_typed_not_applicable`, `test_preview_apply_and_duplicate_fingerprints_share_one_normalized_input`, `test_invalid_apply_after_selection_changes_no_authority_or_git_fact`. | `test_enabled_message_observations_refuse_with_exact_correction`; `test_plan_uses_lifecycle_possible_writes_and_typed_not_applicable`; `test_preview_apply_and_duplicate_fingerprints_share_one_normalized_input`; `test_invalid_apply_after_selection_changes_no_authority_or_git_fact` | mcp/tests/test_closeout_input_boundary.py:50-95; mcp/tests/test_closeout_input_boundary.py:98-164; mcp/tests/test_closeout_input_boundary.py:167-247; mcp/tests/test_closeout_input_boundary.py:250-281 |

## 2026-08-26 Boundary Fidelity Corrections

The test now accepts the authority layer's admitted contract wrapper by comparing its canonical
contract path, rather than requiring object identity with the pre-admission fixture. A launcher
crash is exposed as the typed `lifecycle-worker-launch-failed` refusal and must not leak the
private exception text. Import paths also follow the extracted closeout model/admission packages.

## MCAR-L03 Apply Admission Evidence

The boundary now proves the initial apply acknowledgement reports the exact contract/code pair and
that a stale pair refuses with the named field plus contract-addressed `worktree_sync` arguments
before lifecycle admission.

## Update History

- 2026-08-30T07:05+02:00 — MCAR-L03 A008: aligned the journal-call assertion with mandatory
  blank-input precedence; invalid commit intent now proves zero lifecycle-journal observation.

- 2026-08-30T05:55+02:00 — MCAR-L03 A005: added the shared coherence-refusal projection
  and retained canonical blank-input precedence before exact-pair or lifecycle admission.

- 2026-08-29T21:46+02:00 — MCAR-L03: added initial-apply pair reporting and pre-admission typed
  refusal evidence. Dagger verification remains closeout-owned.

- 2026-08-26T10:44:52+02:00 — Reconciled admitted-contract identity and sanitized worker-launch failure behavior at the public closeout-input boundary.
- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this test card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: created from candidate tree `4241908c`; verification metadata awaits the landed commit.
