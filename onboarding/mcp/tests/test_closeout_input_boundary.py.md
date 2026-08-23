# mcp/tests/test_closeout_input_boundary.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_closeout_input_boundary.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-23T16:08+02:00 |
| lastVerifiedCommitHash | `1d446724d099517f6f52d596b47827ae2391a2a4` |
| lastVerifiedCommitDate | 2026-08-24T00:21:10+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Forces the worktree closeout input contract across omitted, empty, whitespace, enabled/not-applicable, internal/external, preview/apply, duplicate, candidate-drift, and crash-cut cases.

## Code Commentary

### Logic

The tests assert typed `invalidFields`, `resolvedPlan`, and `correctedCall` responses and spy on lifecycle authority and Git so refusals prove zero effect. They compare preview, durable fingerprint, accepted input, and worker args to establish one normalized value. Candidate-tree, same-tree/different-HEAD, and post-proof contract-drift cases prove stable provenance. Restart cases prove mutation evidence repairs the derived recovery projection rather than trusting cells. Low-level model impossibilities and ledger evidence ordering now live in their focused cards rather than expanding this route boundary.

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
| Preview/apply/fingerprint/worker parity and immutable duplicate intent are forced. | `test_preview_apply_and_duplicate_fingerprints_share_one_normalized_input`, `test_valid_duplicate_keeps_one_generation_and_invalid_duplicate_cannot_observe_it` | mcp/tests/test_closeout_input_boundary.py:166-245; mcp/tests/test_closeout_input_boundary.py:447-490 |
| Retry refuses candidate or contract drift after proven output; crash cuts repair derived projection. | `test_public_retry_uses_accepted_plan_after_each_proven_output_cut`, `test_atomic_proof_publication_and_restart_repair_each_recovery_projection` | mcp/tests/test_closeout_input_boundary.py:513-559; mcp/tests/test_closeout_input_boundary.py:603-657 |

## Cross-Repo References

External-memory fixtures use real scratch repositories to distinguish memory content and ledger commits.

## 260821-CLIVE-L2 Current Regression Contract

The current forcing seams include `test_enabled_message_observations_refuse_with_exact_correction`, `test_plan_uses_lifecycle_possible_writes_and_typed_not_applicable`, `test_preview_apply_and_duplicate_fingerprints_share_one_normalized_input`, `test_invalid_apply_after_selection_changes_no_authority_or_git_fact`. The L2 additions force immutable normalized input, exact generation retention, evidence-derived cancellation/recovery, and pre-authority refusal of invalid calls. A failed first call remains task-addressably recoverable without amending accepted intent.

### Reconciled Source Evidence

| Finding | Citations | Source Path |
| --- | --- | --- |
| The current test source exercises `test_enabled_message_observations_refuse_with_exact_correction`, `test_plan_uses_lifecycle_possible_writes_and_typed_not_applicable`, `test_preview_apply_and_duplicate_fingerprints_share_one_normalized_input`, `test_invalid_apply_after_selection_changes_no_authority_or_git_fact`. | L54-L94; L97-L163; L166-L245; L248-L277 | `mcp/tests/test_closeout_input_boundary.py` |

## Update History

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this test card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: created from candidate tree `4241908c`; verification metadata awaits the landed commit.
