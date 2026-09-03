# mcp/tests/closeout_input_test_support.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/closeout_input_test_support.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `685f83c4405570ca8356e7481e0e2a9a16945757` |
| lastVerifiedCommitDate | 2026-09-02T11:38:00+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Provides canonical typed closeout admissions, normalized `WorktreeArgs`, and mutation-evidence recording/builders for L1 tests. It replaces repeated fixtures that previously smuggled raw or blank message fields below validation.


CCR-R22@v1 (L22, commit `685f83c44055`) makes `closeout_worktree_args` default
`certification_profile` to `Path("mcp/certification-profile-v1.json")`, so closeout fixtures
carry the repository-owned profile reference exactly like the real application path.

## Code Commentary

### Logic

The helpers construct production `EffectiveCloseoutInput` and accepted admission values rather than parallel test-only models. `MutationEvidenceRecorder` captures progress transitions, while builders create intent, reconciled-unchanged, and commit-proven states with the same snapshot vocabulary as the operation store.

### Invariants And Boundaries

- Test setup must cross the same normalized-input boundary as production.
- Evidence helpers record expected calls; they do not weaken production authority checks.
- Queue fixtures remain separate from admission fixtures.

## Docs References

See task `260821-CLIVE-L1` L1-R1 through L1-R6.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Canonical admissions bind accepted input and candidate. | `start_closeout_operation`, `closeout_operation_input` | mcp/tests/closeout_input_test_support.py:90-136; mcp/tests/closeout_input_test_support.py:342-367 |
| Evidence fixtures cover all durable states. | `MutationEvidenceRecorder`, `with_mutation_intent`, `with_commit_proven`, `with_reconciled_unchanged` | mcp/tests/closeout_input_test_support.py:50-84; mcp/tests/closeout_input_test_support.py:395-417; mcp/tests/closeout_input_test_support.py:420-451; mcp/tests/closeout_input_test_support.py:454-466 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## 260821-CLIVE-L2 Current Regression Contract

The current forcing seams include `MutationEvidenceRecorder`. The L2 additions force immutable normalized input, exact generation retention, evidence-derived cancellation/recovery, and pre-authority refusal of invalid calls. A failed first call remains task-addressably recoverable without amending accepted intent.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| The current test source exercises `MutationEvidenceRecorder`. | `MutationEvidenceRecorder` | mcp/tests/closeout_input_test_support.py:50-80 |

## Current Contract — 260821 CLIVE Final

This is the current source-backed contract for this test card. It supersedes any earlier
queue-lifecycle, blocker-row, replan/drain, or compatibility-reader wording where present.

Builds explicit normalized closeout inputs and journal mutations for behavioral fixtures, including waiting-door publication, finalization, mutation intent, reconciled-unchanged evidence, and commit proof.

### Current Invariants

- Enabled legs receive explicit nonblank messages; disabled legs remain typed not-applicable.
- Fixture mutations preserve one operation generation and never synthesize fallback input.

## Update History
- 2026-09-03T12:30+02:00 -- 260831-CCR memory curation pass for 685f83c44055 (CCR-R22@v1/L22): recorded the certification_profile default in closeout_worktree_args.


- 2026-08-26T10:44:52+02:00 — No behavior change: exposed `ensure_fixture_waiting_door` as the shared fixture seam and updated package imports; closeout input construction and waiting-door authority are unchanged.

- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: reconciled this test card to current source while preserving prior history and verification provenance.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this test card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: created from candidate tree `4241908c`; verification metadata remains blank pending closeout.
