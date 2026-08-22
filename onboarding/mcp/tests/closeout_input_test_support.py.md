# mcp/tests/closeout_input_test_support.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/closeout_input_test_support.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-22T10:39+02:00 |
| lastVerifiedCommitHash |  `eb7ea60ab9919f009fef58f81afe5861aa1709da`|
| lastVerifiedCommitDate |  2026-08-22T11:44:33+02:00|
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
| Canonical admissions bind accepted input and candidate. | `start_closeout_operation`, `closeout_operation_input` | mcp/tests/closeout_input_test_support.py:63-89; mcp/tests/closeout_input_test_support.py:96-121 |
| Evidence fixtures cover all durable states. | `MutationEvidenceRecorder`, `with_mutation_intent`, `with_commit_proven`, `with_reconciled_unchanged` | mcp/tests/closeout_input_test_support.py:30-60; mcp/tests/closeout_input_test_support.py:148-213 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## Update History

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: created from candidate tree `4241908c`; verification metadata remains blank pending closeout.
