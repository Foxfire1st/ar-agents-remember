# mcp/src/agents_remember/worktrees/activation/atomic_series_activation_release.py

## Governing Overview

[activation overview](overview.md)

## Purpose

This file owns the only durable vacancy transitions for atomic-series activation, and it owns them per
series contract. Each canonical series contract has its own activation record, so release separates
strict explicit cancellation release from terminal cleanup release without either call path being able
to clear a different contract's record.

**`release_atomic_series_selection` has a third caller since 260831-LOCR-L37.** The stop-only pause
(`worktrees/modules/pause.py::pause_result`) releases the master's selection through this exact
function, which is what keeps the pause from introducing a second scheduling or vacancy authority. The
pause is therefore a consumer of the strict explicit-release path described below, not a variant of
it, and this function's own refusals are unchanged. Since the 260831-LOCR-L38 already-vacant stop the
pause answers exactly one of them itself: `atomic-series-activation-selection-missing` is reported as
the pause's `atomic-series-already-vacant` success, after re-observing the record and confirming it is
genuinely `vacant`. The other statuses — an unreadable record and a record naming another
master/contract — are still inherited and translated into the caller's own terms, because neither
proves the master is inactive. Explicit sync cancellation is untouched and still requires an existing
exact selection, which is why this function keeps refusing the absent case.

**Which of those two statuses a foreign record produces depends on that record's own state.** An
*active* record naming another master never reaches this file's exact-owner guard: the observation's
`_load_selected_contract` refuses it first (`atomic-series-activation-master-mismatch`, which the
observation reports as `unreadable`), so a caller sees
`atomic-series-activation-release-unreadable`. Only a record that is itself `vacant` — which
`_observation_from_record` returns without loading the selected contract at all — reaches
`_record_selects_contract` and this file's
`atomic-series-activation-selected-contract-mismatch`. Both are refusals and neither releases
anything; the distinction matters because only the second shape can be confused with an
already-vacant master.

## Code Commentary

### Logic

`release_atomic_series_selection` derives this contract's exact activation path from
`activation_path(contract.coordination_root, contract)`, reads beneath the selector store lock,
rejects unreadable authority, and refuses a record that is absent with
`atomic-series-activation-selection-missing`: explicit sync cancellation must address an existing
exact selection rather than silently succeeding. It then proves the record selects this contract's
master and canonical contract path (`_record_selects_contract`); a record selecting any other
master/contract is refused as `atomic-series-activation-selected-contract-mismatch` and left
untouched. An exact non-vacant record is replaced with a revision-incremented vacant record. Replaying
an already-vacant exact record is idempotent.

`release_terminal_atomic_series_selection_if_exact` uses the same identity proof but deliberately
preserves unreadable, absent, or different selection state instead of raising. `_release_record`
retains the last selected master/contract in the durable vacant record so later exact cancellation
replay and audit do not require a surviving task contract.

### Conventions

All writes use the selector owner and per-path exclusive access declared by the activation module.
Release time defaults to a second-granularity UTC timestamp and may be injected by forcing tests.

### Invariants And Boundaries

- Explicit cancellation must prove an existing exact owner for this contract or fail closed; a
  missing selection is refused, never treated as already-released.
- Release addresses only the released contract: another contract's record, including one selecting a
  different master, is never read as this contract's state and is never cleared. That record must be
  `vacant` to reach this file's exact-owner guard at all; an active one is refused earlier by the
  observation, so the guard is not a second implementation of the observation's own identity check.
- Terminal cleanup never clears a different contract's selection.
- Vacancy is a durable selector transition, not task completion or queue mutation.
- Release carries no commit or lifecycle evidence.

### Todos

Exact release claims and citations are reconciled to the frozen source; verification remains empty
while the file is uncommitted.

## Evidence

### Docs References

No Domain Documentation source is configured for this memory root.

### Repo-Internal References

- The selector authority supplies the per-contract activation path, strict observation, and canonical master reference. [1]
- Explicit cancellation refuses an absent exact selection and a record that selects another contract. [2]
- Exact-owner proof and the revision-incremented vacant replacement retain the last selected master/contract. [3]
- The terminal bridge translates exact, absent, unreadable, and different-selection outcomes. [4]
- Tests prove exact release addresses only the released contract and that another contract's record is never adopted. [5]
- The stop-only pause is the third caller of the strict explicit release, and it adds no authority of its own. [6]
- The pause's boundary proof shows that releasing one master leaves the other master's record byte-identical, which is this file's per-contract isolation observed from the caller's side. [7]
- The two foreign-record shapes, proved apart through the public route: the **vacant** foreign record reaches this file's exact-owner guard and is refused as a contract mismatch, while an **active** one is refused by the observation's earlier guard and reports as unreadable. [8]
- The pause's structural guard proves the stop's static import closure cannot reach a publication module, so the third caller releases through this strict path only. [9]

### Cross-Repo References

No cross-repository source is configured for this memory root.
