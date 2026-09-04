# `mcp/src/agents_remember/models/lifecycles/operation_wait.py`

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/lifecycles/operation_wait.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T20:19:44+02:00 |
| lastVerifiedCommitHash | `e375f2ebdc87f6843bc76168b646d606fa79caec` |
| lastVerifiedCommitDate | 2026-09-04T20:19:44+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[lifecycles overview](overview.md)

## Purpose

Public vocabulary of the read-only lifecycle status-change wait (CCR-R15): one typed
`LifecycleWaitOutcome` Literal shared by the wait controller, the application controller,
the MCP wire response, and the focused conformance tests so the outcome vocabulary cannot drift
between layers.

## Code Commentary

### Logic

`LifecycleWaitOutcome` distinguishes coherent outcomes (`changed`,
`unchanged`, `successor`) from typed read-only refusals
(`wrong-contract`, `no-operation`, `wrong-generation`,
`wrong-cursor`, `journal-replaced`, `journal-unreadable`, and
`projection-incoherent`). The module exports one constant per outcome
(`OUTCOME_CHANGED`, `OUTCOME_UNCHANGED`, `OUTCOME_SUCCESSOR`,
`OUTCOME_NO_OPERATION`, `OUTCOME_WRONG_GENERATION`,
`OUTCOME_WRONG_CURSOR`, `OUTCOME_JOURNAL_REPLACED`,
`OUTCOME_JOURNAL_UNREADABLE`, `OUTCOME_WRONG_CONTRACT`) so the application
layer never spells raw string literals.

### Conventions

Coherent outcomes return a snapshot plus the next meaningful cursor; every refusal is read-only and
never recommends a mutating action.

### Invariants And Boundaries

- The outcome Literal is the single shared wait vocabulary across layers and tests.
- `projection-incoherent` (CCR-R18) refuses when the record advanced but its public
  projection is incoherent: no snapshot and no mutating recommendation is returned.

### Todos

None.

## Docs References

No configured external Domain Documentation source governs this internal vocabulary.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external source governs this strict wait vocabulary. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The one typed wait-outcome Literal and its constants. | `LifecycleWaitOutcome`; `OUTCOME_CHANGED` | mcp/src/agents_remember/models/lifecycles/operation_wait.py:14-46 |
| The read-only bounded wait loop returning these outcomes. | `wait_for_lifecycle_change` | mcp/src/agents_remember/worktrees/integration/lifecycle/observation/status_wait.py:105-148 |
| The application controller translating outcomes into the public response. | `LifecycleStatusWaitRequest` | mcp/src/agents_remember/application/lifecycle/lifecycle_status_wait.py:66-111 |
| The public wire response carrying the outcome. | `WorktreeStatusWaitResponse.outcome` | mcp/src/agents_remember/models/worktree.py:259-283 |
| The durable cursor the waiters compare. | `meaningfulRevision` | mcp/src/agents_remember/models/lifecycles/operation.py:333 |

## Cross-Repo References

No cross-repository wait vocabulary is defined here.

| Finding | Anchor | Source |
| --- | --- | --- |
| The vocabulary is one repository's lifecycle wait contract. | `LifecycleWaitOutcome` | mcp/src/agents_remember/models/lifecycles/operation_wait.py:14-46 |

## 260831-CCR-L15 Wait Outcome Vocabulary

Created with the lifecycle status-change waiting tool: coherent reads return a snapshot plus the
next meaningful cursor; every other outcome is a typed read-only refusal, and the
`projection-incoherent` member (CCR-R18) covers the record-advanced-but-projection-
incoherent case without recommending mutation.

## Update History

- 2026-09-04T20:19:44+02:00 — 260831-CCR-L15 Gate-5 memory pass for e375f2ebdc87f6843bc76168b646d606fa79caec (lifecycle status-change waiting): created
  this card for the new typed wait-outcome vocabulary module.
