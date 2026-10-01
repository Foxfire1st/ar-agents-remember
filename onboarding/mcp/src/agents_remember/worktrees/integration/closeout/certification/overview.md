# Selected Closeout Certification

| Field | Value |
| --- | --- |
| sourceRoute | `mcp/src/agents_remember/worktrees/integration/closeout/certification/` |

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

## Evidence

### Repo-Internal References

- Admission freezes actual preparation and current owner input; selection binds the exact originals. [1]
- Currentness rechecks the profile, owner semantics and route review. [2]
- Recovery derives actual input changes and requires complete prior-red correction. [3]
- Journal selection reopens the complete original graph before its live-owner CAS. [4]
- Execution first refuses the prepared path on converted memory (MIK-R09, gap 3) and, since L37, on locked unconverted memory, then admits only the selected suffix and current memory/finalization boundary. [5]
- Retained output permits only the selected physically proven code commit. [6]
- The ordinary service construction installs the prepared closeout continuation. [7]

### Docs And Cross-Repo References

The configured Domain Documentation registry has no entries. The adjacent closeout, lifecycle and quality owners supply the same-repository authority boundaries; this package defines no external protocol.


## 260928-MIK-L09 The Prepared Closeout Fails Closed On Converted Memory

**Route impact (MIK-R09@v2, leaf 260928-MIK-L09, ruling 2026-09-30T14:38:47 gap 3).** This certified (prepared)
closeout binds its memory commit to the exact curator-attested candidate, so it cannot set `closed: true` in the leaf's
history file (MIK-R07 rule 7), which MIK-R09 rule 3 requires of a closeout memory commit. `execute_selected_closeout`
therefore first asks `worktrees/knowledge_gate.prepared_closeout_refusal(contract)`, before recovery, and on
converted memory refuses with `prepared-closeout-knowledge-history-unclosable`, naming why and that the leaf should
close out through the worktree closeout commit; `application/prepared_certification._realize_prepared_memory` carries
the same check. The path has no production caller today. Tested by
`test_the_prepared_closeout_path_fails_closed_on_converted_memory`.

**Since 260928-MIK-L37 (MIK-R09 rule 6)** unconverted memory is no longer always untouched: after that check both
entries ask `worktrees/knowledge_gate.prepared_closeout_lock(contract)`, and in a memory repository that holds
converted memory the prepared closeout of unconverted memory is refused with `unconverted-memory-locked`, naming
the crossing sync. In a repository that holds none it is untouched, as before. Tested by
`test_the_prepared_closeout_refuses_by_the_lock_at_both_entry_points`.

- The cutover lock on the prepared closeout, after the unclosable-history refusal. [9]

- The refusal before recovery. [8]

## Integrated IAS Recovery Contract

Execution first resumes an already claimed prepared publication, before attempting original-head admission. Otherwise `_refresh_selected_recovery` reobserves canonical memory inputs before choosing reusable certificates. Selection still binds the exact candidate, profile, plan and prior-red disposition. Retained code-output reuse separately proves both original prestates and the current physical commit; helper extraction does not weaken those comparisons.
