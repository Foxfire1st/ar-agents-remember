# mcp/tests/test_closeout_recovery_projection_invariants.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_closeout_recovery_projection_invariants.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T10:05+02:00|
| lastVerifiedCommitHash | `f93ac631ca161e5880db3a937728cb256686b13b` |
| lastVerifiedCommitDate | 2026-09-04T09:56:23+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Forces recovery commits to remain an exact derived projection of authoritative mutation proof and rejects structurally impossible proof/finalization payloads.

## Code Commentary

### Logic

The tests construct external closeout records at successive crash cuts. Memory proof cannot precede accepted code output; reported cells cannot contradict proof or durable output; an existing verified output cannot be replaced; and the store requires the complete exact projection. Separate model and worker-progress cases reject malformed commit proof and non-string finalization identity before transition logic can treat them as facts.

### Invariants And Boundaries

- Recovery cells never authorize or replace lifecycle evidence.
- Commit-proven evidence is repository- and leg-specific.
- Projection advances monotonically in code→memory→ledger order.
- Finalization identity is the exact canonical string hash.

## Docs References

See task `260821-CLIVE-L1` L1-R4 and L1-R6.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Ordering and contradiction cases force proof-owned projection. | `test_memory_proof_cannot_precede_accepted_code_output`, `test_store_requires_the_exact_projection_of_valid_commit_proof` | mcp/tests/test_closeout_recovery_projection_invariants.py:82-144 |
| Impossible proof and finalization payloads fail at model/public boundaries. | `test_structurally_impossible_proof_is_refused_by_the_model`, `test_worker_progress_refuses_non_string_finalization_identity` | mcp/tests/test_closeout_recovery_projection_invariants.py:168-197 |

## Cross-Repo References

The external runtime fixture creates separate code and memory identities so cross-leg projection cannot pass accidentally.

## CCR-R18@v1 Revision-1 Create Gate

260831-CCR-L18 updated the store-discipline forcing: a fresh lifecycle generation must begin at record revision 1, so a mid-lifecycle snapshot (a later journal revision) can never be replayed through `create()` — the revision gate refuses it before any projection check or write (`must begin at record revision 1`). The exact-projection guard still refuses a revision-1 candidate whose code evidence claims commit proof while its durable snapshot carries no recovery output, keeping durable output the exact projection of admitted commit proof.

## Update History

- 2026-09-04T10:05+02:00 — 260831-CCR-L18 Gate-5 memory pass: recorded the revision-1 creation gate and retained exact-projection guard forcing. Verified at code commit f93ac631ca161e5880db3a937728cb256686b13b.

- 2026-08-24T00:51+02:00 — No content impact: 260821-CLIVE-L2 the test only repoints operation runtime and store imports to their moved lifecycle packages. Verified at code commit `1d446724`.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: created from accepted candidate tree `4241908c`; first verification stamp remains governed-closeout-owned.
