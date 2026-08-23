# mcp/tests/test_closeout_candidate_publication_guard.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_closeout_candidate_publication_guard.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-23T16:08+02:00 |
| lastVerifiedCommitHash | `1d446724d099517f6f52d596b47827ae2391a2a4` |
| lastVerifiedCommitDate | 2026-08-24T00:21:10+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Forces the last reversible closeout boundary to reload and revalidate the task contract inside publication authority before candidate claim or Git mutation.

## Code Commentary

### Logic

The focused regression admits a valid closeout, then changes the contract at the publication seam. It expects the callback to reject the stale contract identity before the candidate is committed. This proves the long preflight cannot hand a previously loaded contract object to mutation after authority is acquired.

### Invariants And Boundaries

- Candidate review is necessary but does not replace under-authority contract reload.
- Publication rechecks contract identity, closeout authority, workbench state, and the accepted tree.
- Refusal occurs before queue claim, approval consumption, mutation intent, or Git.

## Docs References

See task `260821-CLIVE-L1` L1-R5 and L1-R6.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| A contract changed at publication is refused before candidate commit. | `test_closeout_candidate_publication_rechecks_the_contract` | mcp/tests/test_closeout_candidate_publication_guard.py:16-65 |
| The production callback reloads and revalidates under authority. | `publication` in `closeout_result` | mcp/src/agents_remember/worktrees/modules/closeout.py:722-752; mcp/src/agents_remember/worktrees/modules/closeout.py:1002-1091 |

## Cross-Repo References

No cross-repository authority is created by this test; its temporary Git checkout models the code leg only.

## 260821-CLIVE-L2 Current Regression Contract

The current forcing seams include `test_closeout_candidate_publication_rechecks_the_contract`. The L2 additions force immutable normalized input, exact generation retention, evidence-derived cancellation/recovery, and pre-authority refusal of invalid calls. A failed first call remains task-addressably recoverable without amending accepted intent.

### Reconciled Source Evidence

| Finding | Citations | Source Path |
| --- | --- | --- |
| The current test source exercises `test_closeout_candidate_publication_rechecks_the_contract`. | L16-L65 | `mcp/tests/test_closeout_candidate_publication_guard.py` |

## Update History

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this test card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-22T11:29+02:00 — No content impact: candidate12 changes only the
  `closeout_changed_paths` test double to the production-faithful `all`/`working`/`committed`
  mapping shape; the candidate-publication contract and assertions documented here are unchanged.
  Reviewed against candidate tree `8f03b256fe24aa77262da805f1538ee39ccb4dd6`, full diff SHA
  `ccb36a898b455cd67ca00c378e5ba0f18851be01faf3d26eced3b9af062f429e`, same-reviewer PASS;
  first verification stamp remains governed-closeout-owned.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: created from accepted candidate tree `4241908c`; first verification stamp remains governed-closeout-owned.
