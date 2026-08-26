# mcp/src/agents_remember/worktrees/activation

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/src/agents_remember/worktrees/activation` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-08-26T08:55+02:00 |
| lastVerifiedCommitHash |  `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`|
| lastVerifiedCommitDate |  2026-08-26T08:10:26+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[worktrees overview](../overview.md)

## Purpose

This focused route owns atomic-series implementation selection for one exact code/external-memory
source pair. It separates durable work existence from current exposure, binds selection to
reconciliation-before-admission, and owns exact cancellation/terminal vacancy without placing
lifecycle or commit evidence in the selector.

## Hot Path Summary

`atomic_series_activation.py` derives normalized source identity, strictly observes one
fingerprint-addressed record, archives corrupt authority, and publishes replace-in-place
`reconciling|active` state. `atomic_series_activation_transaction.py` connects selection to the
root-level resumable sync transaction: select reconciling, reconcile exact sources, then expose
active. `atomic_series_activation_release.py` owns exact durable vacancy, and the terminal bridge
ensures cleanup releases the selected contract before deleting its naming authority while
preserving a newer selection.

## Operating Model

1. A manager/worker dispatch or atomic start/attach selects the canonical series contract.
2. Selection records `reconciling`, logically pausing the former master but preserving its task,
   process, worktree, contract, branch, and journal.
3. The root sync transaction reconciles the exact current source pair and retains conflicts for
   contract-addressed continue/cancel.
4. Only an exact-current pair advances to `active`; moved-again, incomplete, failed, or skipped
   memory remains reconciling.
5. Explicit cancellation or exact terminal cleanup publishes durable `vacant`; another selected
   master is never cleared.

## Invariants And Boundaries

- Task authoring never reads or waits on this route.
- Multiple live series are normal; selection controls exposure, not existence.
- Queue projection observes the selector but owns no transition or recovery.
- Contract presence, queue order, and old-path scanning never elect a master.
- Malformed regular bytes are archived; nonregular entries are quarantined without following them.
- The old flat `worktrees/atomic_series_activation*.py` paths have no compatibility forwarders.

## File-Level Onboarding Map

| Source File | Onboarding File | Status | Reason |
| --- | --- | --- | --- |
| `activation/__init__.py` | [`__init__.py.md`](__init__.py.md) | covered | Canonical activation package boundary |
| `activation/atomic_series_activation.py` | [`atomic_series_activation.py.md`](atomic_series_activation.py.md) | covered | Selector store and strict observation |
| `activation/atomic_series_activation_release.py` | [`atomic_series_activation_release.py.md`](atomic_series_activation_release.py.md) | covered | Exact durable vacancy |
| `activation/atomic_series_activation_terminal.py` | [`atomic_series_activation_terminal.py.md`](atomic_series_activation_terminal.py.md) | covered | Terminal exact-release bridge |
| `activation/atomic_series_activation_transaction.py` | [`atomic_series_activation_transaction.py.md`](atomic_series_activation_transaction.py.md) | covered | Reconciliation-before-exposure transaction |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The package marker names selection and source reconciliation as this route's authority. | "Atomic-series selection and source-reconciliation authority." | mcp/src/agents_remember/worktrees/activation/__init__.py:1-1 |
| The selector strictly owns source-pair observation, publication, quarantine, and waiting reasons. | `observe_atomic_series`; `publish_atomic_series_selection`; `activation_waiting_reason` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:170-187; mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:190-249; mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:298-311 |
| Admission moves from reconciling to active only through exact sync. | `activate_atomic_series_contract` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation_transaction.py:41-79 |

## Needs Verification

- Commit-derived verification metadata awaits governed closeout; route membership and claims are
  reconciled to the frozen candidate, and generated indexes are refreshed in this curator pass.

## Update History

- 2026-08-26T08:55+02:00 — Promoted all five activation package units from provisional to frozen
  covered status after pass 13.

- 2026-08-26T08:20+02:00 — Reconciled all five activation package units and route invariants to
  the frozen candidate; only commit-derived verification remains open.

- 2026-08-26T06:05+02:00 — Created for the structural-limit move of the four activation owners;
  semantic history stays in the moved file cards and no old-path compatibility route exists.
