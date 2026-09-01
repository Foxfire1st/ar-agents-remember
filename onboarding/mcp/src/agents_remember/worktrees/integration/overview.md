# mcp/src/agents_remember/worktrees/integration

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/src/agents_remember/worktrees/integration` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-08-31T20:30+02:00 |
| lastVerifiedCommitHash | `47c8d102c2430d5337dbe207d4601efb4844fec0` |
| lastVerifiedCommitDate | 2026-09-01T08:53:56+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[worktrees overview](../overview.md)

## IAS Frozen Source-Pair Serialization Boundary

The source-pair selector and sync transaction run under the same repository integration authority
that serializes protected-source movement. Remote refresh is evidence gathered before the lock;
the admitted local source tips, pinned authority refs, contract re-read, selection transition, and
base-pair finalization are proven under authority. No ambient checkout or prior queue row becomes a
second source of truth.

Terminal lifecycle cleanup releases only an exact selected terminal pointer and does so before the
canonical contract identity can be destroyed. Lifecycle/commit evidence remains in the stable
operation journal and Git proof owners; the disposable closeout projection observes readiness only.

## Purpose

The integration-authority package owns branch/ref authority, quality and publication fences,
organizational completion, and recovery. Its committed L2 structure now groups root-journal
generation/control/worker/location logic under `lifecycle/`, direct-landing execution and recovery
under `direct_landing/`, and the bounded removable schema-1 bridge under `legacy/`; the remaining
integration orchestration stays at this parent route. These are ownership-preserving package moves,
not compatibility copies of the former flattened modules.

## Hot Path Summary

Normal operation authority is locator -> immutable enclosure-root manifest -> canonical root journal. `lifecycle_operation_location.py` owns path confinement and publication state; `lifecycle_operation_binding.py` owns only the pure canonical identity/digest bytes that publication proves. This route also owns admission-time authoritative reread, generations and controls, exact Git/ref/process evidence, door/successor publication, direct landing, bounded legacy repair, and integration reconciliation.

The final size/ownership split places door publication and recovery below `closeout/`, detached
worker launch/state/termination below `lifecycle/worker/`, cancellation mutation below
`lifecycle/control/`, and total journal observation below `lifecycle/observation/`. These packages
separate responsibilities without adding facades or alternate authority: mutation still requires
exact contract/journal/Git/process evidence, while observation remains read-only and task status or
queue state cannot hide retained operations.

Master integration, series closeout, closeout/reopen, and the memory carryover paths consume this
package: branch-backed authority checks (`require_*`), durable lifecycle operation leases, the
Dagger quality gate checkout, and organizational-completion integration/repair.

MCAR exact-pair admission centralizes live code-worktree and memory-worktree identity in
`closeout/memory_candidate_pair.py`. Configured repository authority remains strict and may
delegate only those duplicate candidate checks to that pair owner. Completed-integration reopen
policy is isolated in `closeout/integration_reopen.py`: it permits memory-only settings closeout
only when the source head is either the recorded base or the exact recorded integrated commit;
unrelated source movement still refuses.

## Conventions

- The package keeps the `worktrees` layering altitude: it never imports the queue package's
  application layer.
- Authority refusals stay typed (`SprintLinkageError`/`CloseoutQueueError`-family or the
  `AgentsRememberError` family).

## Invariants And Boundaries

- Lifecycle operation identity/lease/store are runtime-authority surfaces (bounded, evictable).
- Integration never falls back to a host quality run; the Dagger graph owns acceptance.
- Exact-pair consumers have one candidate-identity owner; disabling the duplicate configured check
  never disables repository-root, separation, task, or enclosure authority.
- External-memory ledger order is authoritative: the newest same-code row is current, while older
  exact rows remain audit history. Memory-only landing appends one current row; integration and
  organizational completion preserve and prove the required exact historical edges.

## Recovery Uses Current Ordered Authority

Direct-landing recovery recognizes an already-created external-memory ledger commit from the live
canonical ledger, not by reconstructing a unique mapping. The newest row must exactly map this
operation code commit to its memory-content commit; every accepted pre-operation row must remain an
immutable suffix; ledger metadata and canonical rendering must match; and the ledger commit must
prove the exact memory parent, before/after ledger blobs, and ledger-only changed path. Older exact
same-code rows remain valid audit history.

Cancelled closeout replacement likewise admits only the current waiting door together with the
cancelled journal disposition and proven worker exit. Door-publication history remains audit
evidence, not a uniqueness oracle for a predecessor that the current contract already identifies.
Neither rule adds a fallback reader: both narrow recovery to the current canonical authority plus
exact retained evidence.

## 260821-CLIVE-L1 Admission, Identity, And Recovery

Closeout integration separates four owners: the contract lifecycle lease serializes filesystem writers; closeout admission stabilizes and normalizes candidate/plan before lifecycle compatibility; candidate identity binds accepted effective input and Git provenance; mutation evidence and recovery projection own crash classification. The typed integrate caller owns integrate retention, authority, and candidate derivation, while lease-bound closeout admission is the sole closeout candidate owner. The shared controller requires the supplied candidate and explicit authority, then separates generation creation/conflict/terminal replacement from recovery/launch/projection; it cannot recapture closeout provenance or infer kind-specific authority from ambient state. For closeout, reconciliation precedes durable journal publication. Worker authority survives every non-terminal phase and may be cleared only after exact termination proof; a failed or denied termination retains the PID and blocks replacement. The store is strict schema 3.0 and relies on model/public fill-only boundaries for impossible leg-set or proven-commit rewrites while retaining transition-specific identity/state/pre-state checks. Duplicates validate against the immutable accepted plan, and generation retention requires commit-proven mutation or exact canonical contract-finalization publication. The disposable queue projection owns no retry, recover, cancel, revise, claim, or commit evidence.

## 260821-CLIVE-L2 Current Architecture

One admitted contract observation enters each public mutation flow; the mutation owner rereads that exact authority under its existing lease/lock. Journal input and proven output are immutable. Retry/recover remain same-generation, revise is safe-cancel plus write-ahead successor, and worker authority survives until termination proof. Direct landing journals every memory/ledger cut. Legacy schema-1 repair and pre-locator adoption are explicit removable routes. Terminal cleanup refuses until L5 archive proof.

The route decomposition mirrors those boundaries without adding new authority: normal lifecycle state is under `lifecycle/`, direct landing under `direct_landing/`, and the only schema-1 reader under `legacy/`. Parent-level integration modules coordinate Git/ref publication and organizational repair across those owners.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| Locator-manifest-journal authority and all publication I/O/state transitions. | `LifecycleOperationLocation`; `prepare_enclosure_publication` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_location.py:78-125; mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_location.py:180-265 |
| Pure immutable binding, canonical serialization, digests, and bounded conflict evidence. | `EnclosureBindingIdentity`; `enclosure_binding_payload`; `sha256_payload`; `location_conflict`; `byte_conflict` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_binding.py:24-165 |
| Task-addressed controls. | `LifecycleControlAction`; `LifecycleControlCommand`; `control_operation` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_controls.py:24-248 |
| Direct landing recovery. | `execute_direct_landing`; `execute_or_require_direct_landing_recovery` | mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_execution.py:70-167 |
| Bounded legacy bridge. | `LegacyOperationCommand`; `legacy_operation_action`; `legacy_bridge_removal_guard` | mcp/src/agents_remember/worktrees/integration/legacy/legacy_operation_bridge.py:79-191 |
| Public operation projection derives legal controls and recovery surfaces from retained journal evidence. | `operation_projection`; `_projected_operation_result`; `_operation_specific_projected_result` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_projection.py:54-227 |

## 260821-CLIVE Final Door-To-Journal Architecture

Closeout scheduling intent begins as an immutable contract-owned door generation. Public door
commands publish exact task/contract bytes under the short repository-scoped task CAS, then refresh
the disposable projection as a downstream effect. Starting closeout atomically transfers the exact
first-ready waiting door into the stable root operation journal; claim intent is durable before
worker launch. From that point, lifecycle, source-journal identity, commits, memory, ledger,
certification, integration, cancel, retire, supersede, and recovery evidence remain journal-owned
even if task changes invalidate the projection.

The landing and terminal lanes are also source-owned, not queue-owned. `atomic_series_landing.py`
checks current protected-ref collisions across active canonical series without persisting a blocker.
`atomic_series_terminal.py` issues only an ephemeral transaction-bound cleanup/abandon capability.
`terminal_enclosure_archive.py`, `lifecycle_enclosure_terminal.py`, and
`lifecycle_operation_location.py` require an exact bounded external archive, receipt, terminal
locator, and predecessor before the old enclosure root may be removed or a successor published.
Stable operation leases live outside the deletable root.

Recovery is deliberately narrow: an existing claimed generation resumes itself; direct-landing
outputs may be reconstructed only from exact lineage and deterministic bytes. Missing create-time
door intent, present-invalid location state, ambiguous mutation, or guessed successor state requires
developer decision. There is no raw-Git fallback, scan-based recovery, synthetic initial door,
standalone successor-intent WAL, or permanent compatibility reader. The deleted
`lifecycle_successor_control.py` responsibilities now live in task-addressed controls,
journal-door control, atomic terminal replacement, and the terminal enclosure/location transaction.

## 260824-PDLS Final Reconciliation

The accepted PDLS tree keeps lifecycle evidence in the root journal while splitting collision
classification, topology repair, legacy archive proof, queue-evidence parsing, and direct-landing
execution into their named owners. The split reduces repeated validation and fixture coupling; it
does not create a second authority route, queue-owned lifecycle evidence, or a compatibility reader.

## Update History

- 2026-08-31T20:30+02:00 — No route topology impact: 260831-DER restores fresh ordinary series
  integration as explicit no-door `not-applicable` authority while retaining exact leaf-door and
  journal recovery boundaries.

- 2026-08-30T06:26+02:00 — MCAR-L03 A005: documented the canonical exact-pair owner, the narrow
  configured-authority delegation, and completed-integration memory-only reopen boundary.

- 2026-08-28T14:15+02:00 — PDLS closeout: verified the direct-landing recovery, lifecycle
  translation, and exact clean-snapshot refactor against the landed candidate. The existing final
  reconciliation remains accurate; no new authority or compatibility path was introduced.

- 2026-08-26T19:27+02:00 — Reconciled the IAS closeout recovery repair: direct landing now proves
  newest-first ledger output while retaining accepted history as an immutable suffix, and cancelled
  closeout replacement uses the current waiting door plus cancellation and worker-exit proof rather
  than requiring a unique historical predecessor row.

- 2026-08-26T14:32+02:00 — Reconciled direct landing, integration proof, and organizational
  completion to valid newest-first same-code memory history.

- 2026-08-26T08:55+02:00 — Finalized the IAS source-pair serialization boundary label against
  the frozen pass-13 candidate.

- 2026-08-25T17:21+02:00 — PDLS final reconciliation recorded the accepted ownership splits and
  preserved the journal/door/queue authority boundary. Verification remains closeout-owned.

- 2026-08-25T08:27+02:00 — 260824-PDLS wave 004: reconciled the final closeout, control, observation, and worker package splits; moved preserved sidecars and added the cancellation/projection owners. Verified against emergency-landed code commit `cb6623775a04cbdeb0509dc26f08a8268189c3f6`; this is not Dagger certification.

- 2026-08-24T21:43+02:00 — File-size route refresh: separated pure enclosure binding and digest
  construction from the locator/manifest I/O state machine. No location authority, fallback, or
  compatibility reader moved into the new helper. Verified at source commit `23d35f77`.

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: reconciled immutable doors, atomic journal claim transfer, strict terminal archive/successor authority, and removal of successor-intent WAL ownership. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: recorded the `lifecycle/`, `direct_landing/`, and `legacy/` package boundaries, repointed current evidence, and verified the governed route at code commit `1d446724d099517f6f52d596b47827ae2391a2a4`.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: refreshed current route intent and source evidence for the accepted full L2 candidate; verification provenance and contract-scoped quality enforcement remain architect-closeout-owned.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1 candidate-11: route ownership now records typed integrate versus lease-bound closeout callers, required shared-core values, and separated generation/recovery stages against accepted tree `4241908c`; verification metadata remains closeout-owned.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: created the `worktrees/integration`
  route — fourteen modules moved from `worktrees/` (flat). Verified at code commit e5cb139f.
