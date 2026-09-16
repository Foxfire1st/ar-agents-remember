# mcp/src/agents_remember/worktrees/activation/atomic_series_activation_release.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/activation/atomic_series_activation_release.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T13:18+02:00 |
| lastVerifiedCommitHash |  `806649b91bdce18f7b915bfbbf6727967f4e7a88`|
| lastVerifiedCommitDate |  2026-09-16T12:23:53+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The selector authority supplies the per-contract activation path, strict observation, and canonical master reference. | "def activation_path("; `observe_atomic_series_path`; `series_master_ref` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:137-142; mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:290-335; mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:418-431 |
| Explicit cancellation refuses an absent exact selection and a record that selects another contract. | `release_atomic_series_selection`; `atomic-series-activation-selection-missing`; `atomic-series-activation-selected-contract-mismatch` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation_release.py:23-53; mcp/src/agents_remember/worktrees/activation/atomic_series_activation_release.py:43-47; mcp/src/agents_remember/worktrees/activation/atomic_series_activation_release.py:48-52 |
| Exact-owner proof and the revision-incremented vacant replacement retain the last selected master/contract. | `_record_selects_contract`; `_release_record` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation_release.py:79-88; mcp/src/agents_remember/worktrees/activation/atomic_series_activation_release.py:91-118 |
| The terminal bridge translates exact, absent, unreadable, and different-selection outcomes. | `with_terminal_atomic_series_release` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation_terminal.py:17-65 |
| Tests prove exact release addresses only the released contract and that another contract's record is never adopted. | "def test_release_addresses_only_the_released_contract(self) -> None:"; "def test_another_contracts_record_can_never_be_adopted(self) -> None:" | mcp/tests/test_atomic_series_activation.py:152-173; mcp/tests/test_atomic_series_activation.py:174-209 |
| The stop-only pause is the third caller of the strict explicit release, and it adds no authority of its own. | `pause_result`; `_already_stopped_result` | mcp/src/agents_remember/worktrees/modules/pause.py:80-128; mcp/src/agents_remember/worktrees/modules/pause.py:131-150 |
| The pause's boundary proof shows that releasing one master leaves the other master's record byte-identical, which is this file's per-contract isolation observed from the caller's side. | `test_pausing_one_master_leaves_the_other_masters_record_byte_identical` | mcp/tests/test_pause_stop_only_end_to_end.py:362-404 |
| The two foreign-record shapes, proved apart through the public route: the **vacant** foreign record reaches this file's exact-owner guard and is refused as a contract mismatch, while an **active** one is refused by the observation's earlier guard and reports as unreadable. | `test_a_record_naming_another_master_is_refused_not_released`; `test_a_record_this_contract_does_not_own_is_refused_not_released` | mcp/tests/test_pause_stop_only_end_to_end.py:473-526; mcp/tests/test_pause_stop_only_end_to_end.py:406-443 |
| The pause's structural guard proves the stop's static import closure cannot reach a publication module, so the third caller releases through this strict path only. | `PUBLICATION_MODULES` | mcp/tests/test_pause_is_not_publication.py:37-52 |

## Cross-Repo References

No cross-repository source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History
- 2026-09-15T13:18+02:00 — 260831-LOCR-L38 verification envelope (uncommitted change set on
  `ar/260831-locr-l38`, base `67b21aeb`): this file is byte-identical to HEAD; the leaf proved
  behaviour rather than changing it. Recorded the guard order the leaf's second new case exists to
  reach, because it is what makes the two foreign-record refusals distinguishable: an *active* record
  naming another master is refused by the observation's `_load_selected_contract` and reports as
  `atomic-series-activation-release-unreadable`, so only a **vacant** foreign record reaches this
  file's `_record_selects_contract` and its `atomic-series-activation-selected-contract-mismatch` —
  and only that shape can be confused with an already-vacant master. Added the reference row for both
  shapes as proved through the public route, repointed the per-contract isolation case to its current
  range (`test_pause_stop_only_end_to_end.py:362-404`, re-derived after the module grew to ten cases),
  and corrected `_already_stopped_result` to `pause.py:131-150`. Verification metadata remains
  closeout-owned; no verification stamp advanced and no acceptance claim.
- 2026-09-13T20:42+02:00 — 260831-LOCR-L38 (uncommitted change set on
  `ar/260831_lifecycle-owned-completion-relay`): corrected the third-caller paragraph. The pause no
  longer translates all three release refusals into its own terms — it now answers
  `atomic-series-activation-selection-missing` itself as the `atomic-series-already-vacant` success,
  after re-observing the record and confirming it is `vacant`. This file's behaviour is unchanged:
  `release_atomic_series_selection` still refuses the absent case, because explicit sync cancellation
  requires an existing exact selection, and the unreadable/foreign-records refusals are still inherited
  by the pause. Re-cited `pause_result` to `pause.py:80-128` (the module grew from 148 to 209 lines),
  added the `_already_stopped_result` anchor, and re-derived the per-contract isolation case to
  `test_pause_stop_only_end_to_end.py:329-371`. Verification metadata remains closeout-owned; no
  acceptance claim and no verification stamp advanced.
- 2026-09-13T19:02+02:00 — 260831-LOCR-L37: recorded the third caller of this file's strict explicit
  release — the stop-only pause (`worktrees/modules/pause.py`), which delegates to
  `release_atomic_series_selection` rather than introducing a second scheduling or vacancy authority,
  inherits all three refusals unchanged, and is observed from the caller's side by the per-contract
  isolation case in the pause boundary suite. Added the two reference rows. Verification metadata
  remains closeout-owned; no acceptance claim.
- 2026-09-13T14:19:25+02:00 — Per-contract release: rewrote Purpose/Logic/Invariants so release derives its own contract's activation path, refuses a missing exact selection with `atomic-series-activation-selection-missing`, and never clears another contract's record; rebound every citation to the frozen source. Verification metadata remains closeout-owned; no acceptance claim.
- 2026-09-13T09:43+00:00 -- 260831-LOCR-L34 curator citation review: every claim this card carries was re-read against its cited range in the code worktree; anchors were rebound to the exact literal bytes at the cited location, ranges stale by a line shift were repaired, and claims the generated projection left unsupported were re-cited or re-worded. No verification stamp advanced.
- 2026-09-08T18:54:49+02:00 — CCR-L38 CQ01 preparation rebound selector release citations to the current source-pair, observation, selection, and cancellation definitions; release ownership is unchanged and no acceptance claim is made.
- 2026-09-08T16:45:00+02:00 — CCR-L38 final preparation repair: repointed frozen-source citations after the final contract diagnostic; no behavioral prose change, no verification or acceptance claim.
- 2026-09-06T22:41:21+00:00: Generated citation repair: `AtomicSeriesActivationTests` repointed to mcp/tests/test_atomic_series_activation.py:96-137. No content impact: mechanical anchor-range projection bound to citation source snapshot 250eac92295fa399589ccf1c9726bfb4cd28a1a0b20dca126769403fba09b52d; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-08-26T08:20+02:00 — Final frozen reconciliation of exact cancellation/terminal vacancy;
  verification awaits the real code commit.

- 2026-08-26T06:05+02:00 — Moved with exact release ownership into
  `worktrees/activation/`; no forwarding or compatibility module remains.

- 2026-08-26T02:55+02:00 — Drafted exact-release ownership for the pre-Dagger frozen partition;
  final ranges and verification remain open.
