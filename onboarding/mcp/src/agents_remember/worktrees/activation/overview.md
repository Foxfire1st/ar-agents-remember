# mcp/src/agents_remember/worktrees/activation

| Field | Value |
| --- | --- |
| sourceRoute | `mcp/src/agents_remember/worktrees/activation` |

## Governing Overview

[worktrees overview](../overview.md)

## Purpose

This focused route owns atomic-series implementation selection per canonical series contract. Every
series contract owns exactly one fingerprint-addressed activation record tracking its own
`reconciling -> active` transition, so two atomic masters that share one protected code/external-memory
source pair never share this state and never pause each other. It separates durable work existence
from current exposure, binds that contract's selection to reconciliation-before-admission, and owns
exact cancellation/terminal vacancy without placing lifecycle or commit evidence in the selector.

## Hot Path Summary

`atomic_series_activation.py` derives the per-contract fingerprint from the canonical contract path,
strictly observes one fingerprint-addressed record, refuses a record that is not this exact contract,
archives corrupt authority, and publishes replace-in-place `reconciling|active` state for that
contract alone. `atomic_series_activation_transaction.py` connects selection to the root-level
resumable sync transaction: select reconciling, reconcile exact sources, then expose active for the
addressed contract. A selection left mid-flight is reported as that state and never as the pass's own
success, with the stuck contract, its publication time, its revision and both exits named in the
summary. `atomic_series_admission.py` projects requested identity, `contractFingerprint`,
activation facts, contract-scoped retry preconditions, and read-only status actions without mutation
or any foreign-blocker concept. `atomic_series_activation_release.py` owns exact durable vacancy for
one contract, and the terminal bridge ensures cleanup releases that contract's own selection while
preserving every other contract's record.

CCR-R25 adds a pure public explanation layer to the selector. Status exposes the observed
per-contract activation fact, while admission responses retain exact requested identity, the contract
fingerprint, vacant/unreadable activation evidence, retry precondition, and a contract-bound read-only
status action. The projection never treats logical selection as a live process, never names another
master as a blocker, and never mutates activation bytes; selection, release, and synchronization
remain the existing transaction owners.

## Operating Model

1. A manager/worker dispatch or atomic start/attach selects the canonical series contract.
2. Selection records `reconciling` for that contract only; other atomic masters keep their own records
   and their own tasks, processes, worktrees, contracts, branches, and journals untouched.
3. The root sync transaction reconciles the exact current source pair and retains conflicts for
   contract-addressed continue/cancel.
4. Only an exact-current pair advances that contract to `active`; moved-again, incomplete, failed, or
   skipped memory remains reconciling, and a pass that itself succeeded beside a mid-flight record is
   reported as `atomic-series-reconciling` with the stuck contract, its publication time, its
   revision, and both exits named in the summary.
5. Explicit cancellation or exact terminal cleanup publishes durable `vacant` for that contract; no
   other contract's record is read or cleared.

## Invariants And Boundaries

- Task authoring never reads or waits on this route.
- Activation state is per contract: multiple live series are normal, sharing one protected source pair
  never couples two masters, and one selection never pauses or replaces another.
- Queue projection observes the selector but owns no transition or recovery.
- A reconciling record left by an incomplete source reconciliation is reported with the contract, its
  revision, and both exits; a successful pass beside it is never reported as that call's success.
- Contract presence, queue order, and old-path scanning never elect a master.
- Malformed regular bytes are archived; nonregular entries are quarantined without following them.
- The old flat `worktrees/atomic_series_activation*.py` paths have no compatibility forwarders.

## File-Level Onboarding Map

| Source File | Onboarding File | Status | Reason |
| --- | --- | --- | --- |
| `activation/__init__.py` | [`__init__.py.md`](__init__.py.md) | covered | Canonical activation package boundary |
| `activation/atomic_series_activation.py` | [`atomic_series_activation.py.md`](atomic_series_activation.py.md) | covered | Per-contract selector store and strict observation |
| `activation/atomic_series_admission.py` | [`atomic_series_admission.py.md`](atomic_series_admission.py.md) | covered | Pure public admission and diagnostic projection |
| `activation/atomic_series_activation_release.py` | [`atomic_series_activation_release.py.md`](atomic_series_activation_release.py.md) | covered | Exact per-contract durable vacancy |
| `activation/atomic_series_activation_terminal.py` | [`atomic_series_activation_terminal.py.md`](atomic_series_activation_terminal.py.md) | covered | Terminal exact-release bridge |
| `activation/atomic_series_activation_transaction.py` | [`atomic_series_activation_transaction.py.md`](atomic_series_activation_transaction.py.md) | covered | Reconciliation-before-exposure transaction |

## Evidence

### Repo-Internal References

- The package marker names selection and source reconciliation as this route's authority. [1]
- The selector keys one record per canonical contract, strictly observes it, publishes, quarantines, and projects only this contract's reconciling wait. [2]
- A record that is not this exact contract is refused rather than adopted. [3]
- Admission moves this contract from reconciling to active only through exact sync. [4]
- A mid-flight selection reports the stuck contract and both exits, and a succeeding pass beside it never reports its own success state. [5]
- Release publishes durable vacancy for this contract alone and refuses a missing exact selection. [6]
- Public admission explains this contract's activation and retry evidence without selector mutation or any other master's state, bounding its public diagnostic detail. [7]

## Needs Verification

- Commit-derived verification metadata awaits governed closeout; route membership and claims are
  reconciled to the frozen candidate, and generated indexes are refreshed in this curator pass.

## CCR-L42 Refresh Validation Parity

The parity candidate composes the sidecar and governing route body/history checks in `worktrees/modules/onboarding.py::validate_memory_refresh_attestations`; curator memory preparation and closeout call that shared validator independently for both surfaces. This route's existing ownership and source behavior remain unchanged by the validation wiring.
