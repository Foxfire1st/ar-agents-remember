# {S}mcp/tests/test_lifecycle_status_wait_outcomes.py{S}

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | {S}mcp/tests/test_lifecycle_status_wait_outcomes.py{S} |
| doc_type | {S}file-level-onboarding{S} |
| lastUpdated | 2026-09-04T20:19:44+02:00 |
| lastVerifiedCommitHash | {S}e375f2ebdc87f6843bc76168b646d606fa79caec{S} |
| lastVerifiedCommitDate | 2026-09-04T20:19:44+02:00 |
| governingOverview | {S}overview.md{S} |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Typed outcome forcing for the read-only lifecycle status-change wait (CCR-R15/CCR-R18): wrong-cursor refusals before any journal read, absent-journal no-operation, malformed-journal unreadable refusal, noise-field classification versus meaningful-field flags, unchanged timeout without failure, changed with the next cursor after a meaningful advance, journal-replaced and wrong-generation refusals, generation-successor wake with explicit information (and unproven-archive refusal), and application refusals that never recommend mutation.

## Code Commentary

### Logic

The module drives `worktree_status_wait_tool` through fixture contracts and records, asserting the typed `LifecycleWaitOutcome` returned for each refusal and coherent case, and that unreadable-journal application refusals stay typed.

### Invariants And Boundaries

- Standalone per the evidence-lifecycle isolation rule; imports no pre-existing mcp/tests support
  module.
- Asserts public behavior through the typed outcome vocabulary and the store's dual-revision
  contract, never through private operation identity.

## Docs References

No configured external Domain Documentation source governs this test module.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external source governs these tests. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Typed refusals precede journal reads. | `test_wrong_cursor_is_refused_before_any_journal_read` | mcp/tests/test_lifecycle_status_wait_outcomes.py:538-555 |
| Meaningful classification ignores noise fields. | `test_meaningful_classification_ignores_noise_and_flags_meaningful_fields` | mcp/tests/test_lifecycle_status_wait_outcomes.py:585-623 |
| Successor wake with explicit information. | `test_generation_successor_wakes_old_wait_with_explicit_information` | mcp/tests/test_lifecycle_status_wait_outcomes.py:691-728 |
| Refusals never recommend mutation. | `test_application_refusals_never_recommend_mutation` | mcp/tests/test_lifecycle_status_wait_outcomes.py:753-808 |

## 260831-CCR-L15 Status-Wait Test Module

Created with the lifecycle status-change waiting tool (CCR-R15).

## Update History

- 2026-09-04T20:19:44+02:00 — 260831-CCR-L15 Gate-5 memory pass for e375f2ebdc87f6843bc76168b646d606fa79caec (lifecycle status-change waiting): created
  this card for the new status-wait test module.
