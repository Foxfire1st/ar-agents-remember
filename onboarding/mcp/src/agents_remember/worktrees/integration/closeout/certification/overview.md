# Selected Closeout Certification

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/src/agents_remember/worktrees/integration/closeout/certification/` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-09-06T21:58:28+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489` |
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[Closeout integration overview](../overview.md)

## What This Area Is

The production bridge between closeout lifecycle ownership and repository-neutral certification. It freezes real admission, retains exact original evidence in the existing store, selects it through the operation journal and executes the permitted suffix. Door/task authority, immutable storage and the journal remain separate owners.

## Hot Path Summary

Read `observation.py` and `admission.py` for actual candidate admission, `selection.py` for full graph readback/CAS, and `execution.py` for gate starts and continuation handoff. `recovery.py` owns change classification and complete prior-red context; `retained_output.py` recognizes only physically proven code output from the selected generation.

## Operating Model

1. Lifecycle coordination classifies generation reuse or a new admission. New admission validates the configured profile, performs strict staged preparation and freezes actual owner input.
2. Initial selection publishes/reopens original authority, admission and recovery records. The existing store/coordinator atomically binds the initial state before claimed-door publication and worker launch.
3. Execution reopens explicit original references and current authority. Complete lower green gates may be reused; red catalogs require an explicit corrective successor. Interrupted uncertified terminal replacement retains its original history.
4. The admitted recovery decision selects the code suffix. Real returned terminals are selected through currentness checks and journal CAS, with complete publication generations protected from pruning.
5. Gate-5 reuse requires current canonical memory input. Finalization-only reuse checks memory again immediately before handoff. The default application bundle installs `PreparedCloseoutContinuation`; selected certificates and physical readback remain required.

## Local Invariants And Traps

- There is no latest-object search, missing-selection recovery by refreezing, or regenerated original provenance.
- Shape-valid wire records alone do not establish actual source, task, current-memory or publication authority.
- Selected results retain red evidence; a missing certificate is not proof of an interruption or success.
- Route-review movement, cancellation, owner/CAS loss or changed authority refuses before selection or handoff.
- Same-generation retained output normalizes only a fully proven code commit. Memory/ledger output cannot enter through that exception.
- Source review and fixture success do not constitute complete production closeout or certified delivery.

## File-Level Onboarding Map

| Source File | Onboarding | Role |
| --- | --- | --- |
| `__init__.py` | [__init__.py.md](__init__.py.md) | Documentation-only namespace |
| `observation.py` | [observation.py.md](observation.py.md) | Actual task/Git/mutation/generated authority inputs |
| `admission.py` | [admission.py.md](admission.py.md) | Strict preparation and original initial selection |
| `recovery.py` | [recovery.py.md](recovery.py.md) | Owner-derived input changes and prior-red admission |
| `selection.py` | [selection.py.md](selection.py.md) | Explicit graph readback and journal CAS |
| `execution.py` | [execution.py.md](execution.py.md) | Selected suffix and current-memory/finalization handoff |
| `retained_output.py` | [retained_output.py.md](retained_output.py.md) | Narrow physically proven code-output comparison |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Admission freezes actual preparation and current owner input; selection binds the exact originals. | `prepare_closeout_certification`; `initial_certification_state` | mcp/src/agents_remember/worktrees/integration/closeout/certification/admission.py:75-142; mcp/src/agents_remember/worktrees/integration/closeout/certification/admission.py:217-283 |
| Currentness rechecks the profile, owner semantics and route review. | `validate_selected_currentness` | mcp/src/agents_remember/worktrees/integration/closeout/certification/admission.py:286-325 |
| Recovery derives actual input changes and requires complete prior-red correction. | `derive_certificate_input_changes`; `build_prior_red_context` | mcp/src/agents_remember/worktrees/integration/closeout/certification/recovery.py:50-79; mcp/src/agents_remember/worktrees/integration/closeout/certification/recovery.py:82-124 |
| Journal selection reopens the complete original graph before its live-owner CAS. | `require_selected_certification`; `select_certification_state` | mcp/src/agents_remember/worktrees/integration/closeout/certification/selection.py:105-109; mcp/src/agents_remember/worktrees/integration/closeout/certification/selection.py:445-463 |
| Execution admits only the selected suffix and current memory/finalization boundary. | `execute_selected_closeout` | mcp/src/agents_remember/worktrees/integration/closeout/certification/execution.py:279-332 |
| Retained output permits only the selected physically proven code commit. | `require_retained_output_currentness` | mcp/src/agents_remember/worktrees/integration/closeout/certification/retained_output.py:24-108 |
| The ordinary service construction installs the prepared closeout continuation. | `build_default_worktree_services` | mcp/src/agents_remember/application/worktree_services.py:199-206 |

## Docs And Cross-Repo References

The configured Domain Documentation registry has no entries. The adjacent closeout, lifecycle and quality owners supply the same-repository authority boundaries; this package defines no external protocol.


## Integrated IAS Recovery Contract

Execution first resumes an already claimed prepared publication, before attempting original-head admission. Otherwise `_refresh_selected_recovery` reobserves canonical memory inputs before choosing reusable certificates. Selection still binds the exact candidate, profile, plan and prior-red disposition. Retained code-output reuse separately proves both original prestates and the current physical commit; helper extraction does not weaken those comparisons.

## Update History

- 2026-09-06T21:58:28+00:00 — Reconciled this route against the source delta from `245057ab16e19afdaabd5c188c9576b22e0c0870` to `d36109038b3f2b500c138f9dc1ea9c9f9a247489`. Updated current ownership and policy claims; prior verification commit/date and history remain unchanged. Source inspection only; no test, review or acceptance claim.


- 2026-09-06T14:58:25+00:00 — Created the nearest route after full source review at `c69d5171187fa1957025e393270db9f5a864ab14`. Reused the parent route's separation of door/task, coherence and journal ownership while distinguishing implemented selected admission/execution from the unbound production continuation. Source verification is not gate or acceptance evidence.
