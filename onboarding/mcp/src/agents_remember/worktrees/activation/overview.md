# mcp/src/agents_remember/worktrees/activation

| Field | Value |
| --- | --- |
| sourceRoute | `mcp/src/agents_remember/worktrees/activation` |

## Governing Overview

[worktrees overview](../overview.md)

## Purpose

This route owns contract-scoped activation for durable atomic-master work. It separates the existence of a canonical series contract from that contract's implementation selection: each contract has its own fingerprint-addressed snapshot of selection and release. Masters sharing a protected code/external-memory source pair do not share activation state. The selecting transaction reconciles sources before publishing `active`; the selector does not establish process liveness or supply lifecycle or commit evidence.

## Hot Path Summary

`atomic_series_activation.py` derives the fingerprint from the resolved canonical contract path, strictly observes the addressed snapshot, and publishes replace-in-place `reconciling|active` state. Missing snapshots are observed as vacant. Mismatched or malformed authority is unreadable; selecting repair preserves its evidence before replacement. A selected contract that is terminal is observed as vacant even before its stored record is durably released.

`atomic_series_activation_transaction.py` connects selection to the resumable sync transaction: publish `reconciling`, reconcile the addressed sources, check the contract's bases against the current source pair, then publish `active`. Incomplete reconciliation retains the selection and reports the stuck master and contract, publication time, revision, and the complete/cancel exits. A successful sync pass that still requires reconciliation is not implementation admission.

`atomic_series_admission.py` provides the pure public explanation layer. It projects requested identity, the observed contract fingerprint and activation facts when available, retry preconditions, and a contract-bound read-only status action when its address is available. It explains vacant or unreadable observations without mutating activation bytes or treating another master as a blocker. Status exposes the observed activation fact without creating or repairing the snapshot.

`atomic_series_activation_release.py` publishes durable vacancy only for an exact recorded selection. `atomic_series_activation_terminal.py` bridges successful, non-dry-run terminal series operations to exact release; unreadable or unproven selection evidence is preserved rather than repaired by cleanup.

## How It Is Built

1. Atomic-master bootstrap, used by manager dispatch and first-leaf start, enters the selecting reconciliation transaction. Attaching an ordinary leaf with a parent series also activates that parent. Direct series attach observes activation and checks terminal cleanup, branch existence, and lineage; it does not itself select or reconcile the series.
2. A new selecting sync publishes `reconciling` at this contract's address. Continue requires its exact reconciling owner; cancellation also permits replay against its exact last-released vacant record. These checks do not inspect another contract's selection.
3. The resumable sync transaction owns source reconciliation and retained conflicts for contract-addressed continue/cancel. Activation records do not replace its journal or authority.
4. Only a successful `synced` or `already-current` result whose contract bases match the current participating source tips advances selection to `active`. Failed, moved-again, or incomplete reconciliation retains `reconciling`. A successful pass whose external-memory base remains incomplete is reported as `atomic-series-source-pair-incomplete`; `_reconciling_result` changes a remaining `synced` or `already-current` state to `atomic-series-reconciling` and converts a zero return code to 2. The summary identifies the stuck contract, publication time, revision, and both exits.
5. Explicit sync cancellation publishes durable `vacant` for the exact selected or last-released owner. Pause uses the same exact release authority and can report an independently observed missing snapshot as already vacant without writing one. Terminal release writes vacancy when readable evidence proves the exact owner; absent, unreadable, or unproven evidence is preserved. No release reads or clears another contract's record.

### File-Level Onboarding Map

| Source File | Onboarding File | Status | Reason |
| --- | --- | --- | --- |
| `activation/__init__.py` | [`__init__.py.md`](__init__.py.md) | covered | Canonical activation package boundary |
| `activation/atomic_series_activation.py` | [`atomic_series_activation.py.md`](atomic_series_activation.py.md) | covered | Per-contract selector store and strict observation |
| `activation/atomic_series_admission.py` | [`atomic_series_admission.py.md`](atomic_series_admission.py.md) | covered | Pure public admission and diagnostic projection |
| `activation/atomic_series_activation_release.py` | [`atomic_series_activation_release.py.md`](atomic_series_activation_release.py.md) | covered | Exact per-contract durable vacancy |
| `activation/atomic_series_activation_terminal.py` | [`atomic_series_activation_terminal.py.md`](atomic_series_activation_terminal.py.md) | covered | Terminal exact-release bridge |
| `activation/atomic_series_activation_transaction.py` | [`atomic_series_activation_transaction.py.md`](atomic_series_activation_transaction.py.md) | covered | Reconciliation-before-exposure transaction |

## Invariants And Boundaries

- Task-document mutation does not read activation state. Durable task truth and current selection remain separate authorities.
- Activation state is per contract. Sharing a protected source pair does not couple two masters' selection records, and selecting one does not pause or replace another. Genuine wave dependencies belong to the sprint execution graph.
- Queue projection observes the selector and derives this contract's reconciling wait; it owns no selection, release, or repair transition.
- A mid-flight reconciliation response names the addressed contract, publication time, revision, and complete/cancel exits. A successful individual pass does not grant implementation admission while that selection remains reconciling.
- Contract presence, queue order, and old-path scanning do not elect a master through this selector.
- Selecting repair archives malformed regular bytes. Nonregular entries are moved into an opaque archive without reading through them; ordinary observation, status, admission projection, and terminal cleanup do not perform that repair.
- Explicit release refuses missing or unreadable selection authority. Terminal release preserves such evidence, and reports a release failure when an exception prevents durable vacancy.
- The old flat `worktrees/atomic_series_activation*.py` paths have no compatibility forwarders.

### Memory Refresh Validation

`worktrees/modules/onboarding.py::validate_memory_refresh_attestations` composes the sidecar refresh checks and governing route-overview body/history checks with separately supplied evidence. The memory-quality controller calls it for the unconverted onboarding layout; converted layouts take the onboarding trace gate instead. This validation is outside the activation selector's transition authority.

## Lifecycle Metadata

The following pre-existing verification note is retained as metadata, outside the operative promises above. Its closeout, candidate-reconciliation, and index-refresh assertions lack lifecycle authority in the assigned source evidence; they are not a statement of this proposal's verification or acceptance status.

- Commit-derived verification metadata awaits governed closeout; route membership and claims are
  reconciled to the frozen candidate, and generated indexes are refreshed in this curator pass.

## Evidence

- The package marker names selection and source reconciliation as this route's authority. [1]
- The selector keys one record per canonical contract, strictly observes it, publishes, quarantines, and projects only this contract's reconciling wait. [2]
- A record that is not this exact contract is refused rather than adopted. [3]
- Admission moves this contract from reconciling to active only through exact sync. [4]
- A mid-flight selection reports the stuck contract and both exits, and a succeeding pass beside it never reports its own success state. [5]
- Release publishes durable vacancy for this contract alone and refuses a missing exact selection. [6]
- Public admission explains this contract's activation and retry evidence without selector mutation or any other master's state, bounding its public diagnostic detail. [7]


- Selecting sync checks exact participating source bases before active exposure; incomplete memory retains its own refusal state. [8]
- Bootstrap and parent-leaf attach select; direct series attach only observes activation and checks resume prerequisites. [9]
- Terminal release preserves unreadable or unproven evidence and releases only the recorded exact owner. [10]
- Current memory-quality refresh composition applies on unconverted onboarding; converted layouts take the trace gate. [11]
