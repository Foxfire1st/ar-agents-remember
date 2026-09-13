# mcp/src/agents_remember/worktrees/activation/atomic_series_activation_release.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/activation/atomic_series_activation_release.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-13T11:43+02:00 |
| lastVerifiedCommitHash |  `e0820b04a499cbfb2079c78485346c50917a238a`|
| lastVerifiedCommitDate |  2026-09-13T18:02:04+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[activation overview](overview.md)

## Purpose

This file owns the only durable vacancy transitions for atomic-series activation, and it owns them per
series contract. Each canonical series contract has its own activation record, so release separates
strict explicit cancellation release from terminal cleanup release without either call path being able
to clear a different contract's record.

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
  different master, is never read as this contract's state and is never cleared.
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

## Cross-Repo References

No cross-repository source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History
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
