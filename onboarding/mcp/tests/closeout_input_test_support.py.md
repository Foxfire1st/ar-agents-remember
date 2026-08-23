# mcp/tests/closeout_input_test_support.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/closeout_input_test_support.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-23T16:08+02:00 |
| lastVerifiedCommitHash | `1d446724d099517f6f52d596b47827ae2391a2a4` |
| lastVerifiedCommitDate | 2026-08-24T00:21:10+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Provides canonical typed closeout admissions, normalized `WorktreeArgs`, and mutation-evidence recording/builders for L1 tests. It replaces repeated fixtures that previously smuggled raw or blank message fields below validation.

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
| Canonical admissions bind accepted input and candidate. | `start_closeout_operation`, `closeout_operation_input` | mcp/tests/closeout_input_test_support.py:64-91; mcp/tests/closeout_input_test_support.py:98-123 |
| Evidence fixtures cover all durable states. | `MutationEvidenceRecorder`, `with_mutation_intent`, `with_commit_proven`, `with_reconciled_unchanged` | mcp/tests/closeout_input_test_support.py:31-61; mcp/tests/closeout_input_test_support.py:150-172; mcp/tests/closeout_input_test_support.py:175-200; mcp/tests/closeout_input_test_support.py:203-215 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## 260821-CLIVE-L2 Current Regression Contract

The current forcing seams include `MutationEvidenceRecorder`. The L2 additions force immutable normalized input, exact generation retention, evidence-derived cancellation/recovery, and pre-authority refusal of invalid calls. A failed first call remains task-addressably recoverable without amending accepted intent.

### Reconciled Source Evidence

| Finding | Citations | Source Path |
| --- | --- | --- |
| The current test source exercises `MutationEvidenceRecorder`. | L31-L61 | `mcp/tests/closeout_input_test_support.py` |

## Update History

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this test card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: created from candidate tree `4241908c`; verification metadata remains blank pending closeout.
