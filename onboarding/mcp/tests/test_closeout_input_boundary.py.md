# mcp/tests/test_closeout_input_boundary.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_closeout_input_boundary.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-22T10:39+02:00 |
| lastVerifiedCommitHash |  `eb7ea60ab9919f009fef58f81afe5861aa1709da`|
| lastVerifiedCommitDate |  2026-08-22T11:44:33+02:00|
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
| Public input matrix and no-effect boundary are forced. | `test_enabled_message_observations_refuse_with_exact_correction`, `test_invalid_apply_after_selection_changes_no_authority_or_git_fact` | mcp/tests/test_closeout_input_boundary.py:54-96; mcp/tests/test_closeout_input_boundary.py:247-279 |
| Preview/apply/fingerprint/worker parity and immutable duplicate intent are forced. | `test_preview_apply_and_duplicate_fingerprints_share_one_normalized_input`, `test_valid_duplicate_keeps_one_generation_and_invalid_duplicate_cannot_observe_it` | mcp/tests/test_closeout_input_boundary.py:166-246; mcp/tests/test_closeout_input_boundary.py:446-491 |
| Retry refuses candidate or contract drift after proven output; crash cuts repair derived projection. | `test_public_retry_uses_accepted_plan_after_each_proven_output_cut`, `test_atomic_proof_publication_and_restart_repair_each_recovery_projection` | mcp/tests/test_closeout_input_boundary.py:512-560; mcp/tests/test_closeout_input_boundary.py:602-658 |

## Cross-Repo References

External-memory fixtures use real scratch repositories to distinguish memory content and ledger commits.

## Update History

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: created from candidate tree `4241908c`; verification metadata awaits the landed commit.
