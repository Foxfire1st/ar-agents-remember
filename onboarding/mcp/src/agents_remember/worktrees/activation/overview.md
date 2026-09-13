# mcp/src/agents_remember/worktrees/activation

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/src/agents_remember/worktrees/activation` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-09-08T19:16:43+02:00 |
| lastVerifiedCommitHash |  `e0820b04a499cbfb2079c78485346c50917a238a`|
| lastVerifiedCommitDate |  2026-09-13T18:02:04+02:00|
| governingOverview | `../overview.md` |

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
addressed contract. `atomic_series_admission.py` projects requested identity, `contractFingerprint`,
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
   skipped memory remains reconciling.
5. Explicit cancellation or exact terminal cleanup publishes durable `vacant` for that contract; no
   other contract's record is read or cleared.

## Invariants And Boundaries

- Task authoring never reads or waits on this route.
- Activation state is per contract: multiple live series are normal, sharing one protected source pair
  never couples two masters, and one selection never pauses or replaces another.
- Queue projection observes the selector but owns no transition or recovery.
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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The package marker names selection and source reconciliation as this route's authority. | "Atomic-series selection and source-reconciliation authority." | mcp/src/agents_remember/worktrees/activation/__init__.py:1-1 |
| The selector keys one record per canonical contract, strictly observes it, publishes, quarantines, and projects only this contract's reconciling wait. | "def contract_fingerprint("; `observe_atomic_series`; `publish_atomic_series_selection`; `activation_waiting_reason` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:130-134; mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:145-152; mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:155-212; mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:275-287 |
| A record that is not this exact contract is refused rather than adopted. | `_require_record_identity` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:360-372 |
| Admission moves this contract from reconciling to active only through exact sync. | `activate_atomic_series_contract` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation_transaction.py:55-100 |
| Release publishes durable vacancy for this contract alone and refuses a missing exact selection. | `release_atomic_series_selection` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation_release.py:23-53 |
| Public admission explains this contract's activation and retry evidence without selector mutation or any other master's state, bounding its public diagnostic detail. | `atomic_series_admission_projection` | mcp/src/agents_remember/worktrees/activation/atomic_series_admission.py:33-74 |

## Needs Verification

- Commit-derived verification metadata awaits governed closeout; route membership and claims are
  reconciled to the frozen candidate, and generated indexes are refreshed in this curator pass.

## CCR-L42 Refresh Validation Parity

The parity candidate composes the sidecar and governing route body/history checks in `worktrees/modules/onboarding.py::validate_memory_refresh_attestations`; curator memory preparation and closeout call that shared validator independently for both surfaces. This route's existing ownership and source behavior remain unchanged by the validation wiring.


## Update History
- 2026-09-13T14:19:25+02:00 — Per-contract route rewrite: Purpose, Hot Path Summary, Operating Model, Invariants, the onboarding map reasons, and the reference table now describe one fingerprint-addressed activation record per canonical series contract with no cross-master exclusivity, no logical pausing of a former master, no cross-contract blocker framing, and no selection-versus-existence framing; citations rebound to the frozen source. No acceptance claim.
- 2026-09-10T02:27:58+02:00 — CCR-L42 parity curation: No route impact: curator preparation and closeout now run the shared sidecar and route body/history validators independently; this route's ownership and source semantics remain unchanged. No acceptance claim is made.
- 2026-09-08T19:16:43+02:00 — CCR-L38 CQ04 preparation rebound the shared admission route after oversized parser-detail projection was bounded; selector ownership remains unchanged and no acceptance claim is made.
- 2026-09-08T18:54:49+02:00 — CCR-L38 CQ01 preparation rebound selector route citations after bounded activation diagnostics landed; route ownership and mutation boundaries remain unchanged, with no acceptance claim.
- 2026-09-08T17:36:08+02:00 — CCR-L38 source-grounded preparation added `atomic_series_admission.py` to the activation route map and recorded its pure admission-projection boundary. The source remains uncommitted; verification metadata remains closeout-owned.
- 2026-09-08T16:24:06+02:00 — CCR-L38 preparation range refresh: regenerated selector observation/publication/waiting coordinates after the frozen activation additions. This is a mechanical source-range correction; verification metadata remains closeout-owned.
- 2026-09-08T16:05:21+02:00 — CCR-L38 source-grounded candidate pass: added the public activation/admission projection boundary while preserving selector mutation ownership and no-live-process inference. Verification metadata remains closeout-owned; no Gate 5 or acceptance claim.

- 2026-08-26T08:55+02:00 — Promoted all five activation package units from provisional to frozen
  covered status after pass 13.

- 2026-08-26T08:20+02:00 — Reconciled all five activation package units and route invariants to
  the frozen candidate; only commit-derived verification remains open.

- 2026-08-26T06:05+02:00 — Created for the structural-limit move of the four activation owners;
  semantic history stays in the moved file cards and no old-path compatibility route exists.
