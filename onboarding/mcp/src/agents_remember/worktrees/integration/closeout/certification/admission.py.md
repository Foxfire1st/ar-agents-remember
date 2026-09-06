# mcp/src/agents_remember/worktrees/integration/closeout/certification/admission.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/closeout/certification/admission.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T14:58:25+00:00 |
| lastVerifiedCommitHash | `c69d5171187fa1957025e393270db9f5a864ab14` |
| lastVerifiedCommitDate | 2026-09-06T16:32:29+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Selected closeout certification overview](overview.md)

## Purpose

Freezes real closeout candidate authority and constructs the exact certification selection before a journal owner may execute it.

## Code Commentary

### Logic

`prepare_closeout_certification` revalidates an existing queued/running selection without staging or rerunning preparation. For a new admission, it validates the configured repository profile before the strict staged-code preparation, freezes certification records against the contract's code base, observes actual owner inputs, and compiles lifecycle admission and recovery from any explicit predecessor.

Prior red terminals require the supplied corrective dispositions and exact prior certificate prefix. `initial_certification_state` publishes and reopens immutable lifecycle/recovery objects, retains a semantically matching original authority record with its original provenance, and constructs typed predecessor, input-terminal and recovery references. Only certificates admitted for reuse enter the initial selected prefix. The complete proposed graph is read back before this function returns it to the store's atomic initial-selection composition.

`validate_selected_currentness` reloads the configured profile, reobserves candidate and owner semantics, admits only the separately proven retained-code-output adjustment, and rechecks the current route review. It does not refresh a selected run or replace its provenance.

### Conventions

Lifecycle coordination decides whether a request resumes the current generation or creates a successor. This module returns a frozen admission or selected state; the existing store/coordinator owns durable create/replacement, predecessor archival, claimed-door publication and worker launch.

### Invariants And Boundaries

- A missing or malformed profile refuses before staging or hooks.
- Selected references are explicit; a missing selection is not reconstructed from recent store objects.
- Reusing an existing semantic authority address reopens the original record; unequal semantic content refuses as a collision.
- Route-review removal or drift refuses current use even when task intent is unchanged.
- Initial object publication alone does not authorize a gate start or complete closeout.

### Todos

None recorded.

## Docs References

The configured Domain Documentation registry has no entries. The source below establishes this repository-owned boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| The resolved registry supplies no applicable external Domain Documentation source for this card. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| New admission uses actual profile, staged preparation, owner observations and prior selection. | `prepare_closeout_certification` | mcp/src/agents_remember/worktrees/integration/closeout/certification/admission.py:75-142 |
| Only exact selected red evidence and supplied corrective decisions enter prior-red admission. | `_prior_red_context` | mcp/src/agents_remember/worktrees/integration/closeout/certification/admission.py:164-188 |
| An existing semantic authority address retains its original stored record. | `_retain_original_authorities` | mcp/src/agents_remember/worktrees/integration/closeout/certification/admission.py:191-201 |
| Initial state binds original objects and is fully read back before it reaches journal selection. | `initial_certification_state`; `select_initial_certification` | mcp/src/agents_remember/worktrees/integration/closeout/certification/admission.py:217-283; mcp/src/agents_remember/worktrees/integration/closeout/certification/admission.py:204-214 |
| Currentness rechecks profile, candidate/owner semantics, retained output and route review. | `validate_selected_currentness` | mcp/src/agents_remember/worktrees/integration/closeout/certification/admission.py:286-325 |

## Cross-Repo References

No cross-repository implementation or external protocol is owned here.


| Finding | Anchor | Source |
| --- | --- | --- |
| No separately configured cross-repository source is used for this card. | — | — |
## Update History

- 2026-09-06T14:58:25+00:00 — Created after full source review at `c69d5171187fa1957025e393270db9f5a864ab14`. Records current implementation and remaining composition boundaries; source verification is not gate execution, delivery or acceptance.
