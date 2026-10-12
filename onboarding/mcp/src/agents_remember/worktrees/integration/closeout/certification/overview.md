# Selected Closeout Certification

| Field | Value |
| --- | --- |
| sourceRoute | `mcp/src/agents_remember/worktrees/integration/closeout/certification/` |

## Governing Overview

[Closeout integration overview](../overview.md)

## What This Area Is

This area bridges closeout lifecycle authority and repository-neutral certification. Its admission helpers freeze actual owner inputs, retain original evidence in the certificate store and bind explicit references into an operation's certification selection. Its execution entry consumes that selection to run the permitted suffix and hand off to memory certification or finalization. Door/task authority, immutable storage and the operation journal remain separate owners.

## Hot Path Summary

Read `observation.py` and `admission.py` for candidate observation and strict preparation, `selection.py` for complete selected-graph readback and journal compare-and-swap, and `execution.py` for gate starts and continuation handoff. `recovery.py` classifies owner-produced input changes and validates complete prior-red context. `retained_output.py` recognizes only physically proven code output from the selected generation.

## Construction And Execution

Admission distinguishes an existing queued or running generation from a new admission. Existing generations undergo selected-currentness validation. New admission validates the configured profile before staging or invoking a hook, performs strict staged preparation, observes task/Git/mutation/generated-input authorities, and compiles admission and recovery records.

Initial-state construction publishes and reopens the original authority, admission and recovery records. It retains explicit predecessor and input-terminal references and checks the resulting selected graph. The selection helper reads back that graph before updating the live operation journal through compare-and-swap.

Execution checks the prepared-closeout knowledge refusal and then the cutover lock before attempting publication recovery. It resumes an already claimed prepared publication before validating the current selected admission. Otherwise it reobserves canonical memory inputs when a selected or inherited Gate-5 certificate could be reused, then updates the recovery decision before choosing the suffix.

The selected recovery plan controls code-gate execution. Returned terminals are selected through current-owner checks and journal compare-and-swap; selected and historical publication generations are exposed to the executor as protected generations. The selected graph continues to bind the exact candidate, profile, plan and prior-red disposition.

Gate-5 reuse requires current canonical memory input. Finalization-only reuse compares memory input again immediately before handoff. The default service bundle installs `PreparedCloseoutContinuation`, which uses the installed memory producer and selected original certificates for memory certification and prepared finalization.

## Invariants And Boundaries

- Selection follows explicit original references. It does not search for a latest object, refreeze a missing selection or regenerate original provenance.
- Shape-valid records alone do not establish source, task, current-memory or publication authority. Observation checks actual owners; selection recompiles admission, recovery and terminal evidence.
- Red catalogs require an explicit corrective successor. A missing certificate proves neither interruption nor success. Replacing an uncertified terminal requires an explicitly interrupted original publication and retains that terminal in history; stale Gate-5 recovery also retains the previous terminal.
- Route-review movement, cancellation, worker-owner loss, journal compare-and-swap loss or changed selected authority refuses at the corresponding currentness, selection or handoff boundary.
- Retained code output must prove both original prestates and the current physical commit. Only the original code HEAD and its single owned lineage edge may be normalized to that proven commit; every other candidate and authority field must still match. Memory or ledger output cannot use this exception.
- The prepared path cannot set `closed: true` in the leaf history while binding its memory commit to the exact curator-attested candidate. On converted memory it therefore refuses with `prepared-closeout-knowledge-history-unclosable` and directs the leaf to the worktree closeout commit. An unreadable conversion probe also refuses. The execution entry and prepared-memory realization both perform this check before their later work.
- After that refusal check, both entries apply the unconverted-memory cutover lock. An external memory repository holding converted memory refuses with `unconverted-memory-locked` and names the crossing sync; a repository holding none is not locked. An unanswered lock probe refuses rather than being treated as unlocked.
- Source inspection and fixture assertions do not establish completed production closeout or certified delivery.

## Wiring And Evidence Limits

The current production source has no caller of the selected-closeout execution entry. The default service construction does install its continuation; that construction alone does not demonstrate execution of the entry or completed delivery.

The existing test sources contain assertions for converted-memory refusal and for the cutover lock at both entries. These describe the protected behavior, not a test-execution result or lifecycle acceptance status.

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

- Admission freezes actual preparation and current owner input; initial selection binds the exact originals. [1]
- Currentness rechecks the profile, owner semantics and route review. [2]
- Recovery derives actual input changes and requires complete prior-red correction. [3]
- Journal selection reopens the complete original graph before its live-owner compare-and-swap. [4]
- Execution checks the knowledge refusal and lock before publication recovery, then admits only the selected suffix and current memory/finalization boundary. [5]
- Retained output permits only the selected physically proven code commit. [6]
- The ordinary service construction installs the prepared closeout continuation. [7]
- The unclosable-history refusal precedes publication recovery. [8]
- The prepared execution entry applies the cutover lock after the unclosable-history refusal. [9]
- Task, Git, mutation and generated-input observations supply distinct actual authority records. [10]
- Selected readback binds originals, predecessor history, recovery decisions and terminal publication evidence; terminal replacement preserves history. [11]
- Current worker authority, canonical memory observation, suffix execution and publication protection are checked at their execution boundaries. [12]
- Retained output validates both original prestates and the physical commit before authority normalization. [13]
- Converted-memory refusal and the subsequent unconverted-memory lock are distinct checks; unreadable probes are not permission to proceed. [14]
- Prepared-memory realization repeats both knowledge checks before metadata work and requires curator refresh if that work moves memory. [15]
- The installed continuation observes the production memory owner and requires the selected original fifth certificate for finalization. [16]
- Existing test sources assert converted-memory refusal and the lock at both entries; no execution result is claimed. [17]
