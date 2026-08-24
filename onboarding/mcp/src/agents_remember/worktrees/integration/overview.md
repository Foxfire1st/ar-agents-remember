# mcp/src/agents_remember/worktrees/integration

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/src/agents_remember/worktrees/integration` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-08-24T14:43+02:00 |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb` |
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
| governingOverview | `../../../../overview.md` |

## Governing Overview

[mcp overview](../../../../overview.md)

## Purpose

The integration-authority package owns branch/ref authority, quality and publication fences,
organizational completion, and recovery. Its committed L2 structure now groups root-journal
generation/control/worker/location logic under `lifecycle/`, direct-landing execution and recovery
under `direct_landing/`, and the bounded removable schema-1 bridge under `legacy/`; the remaining
integration orchestration stays at this parent route. These are ownership-preserving package moves,
not compatibility copies of the former flattened modules.

## Hot Path Summary

Normal operation authority is locator -> immutable enclosure-root manifest -> canonical root journal. This route owns admission-time authoritative reread, generations and controls, exact Git/ref/process evidence, door/successor publication, direct landing, bounded legacy repair, and integration reconciliation.

Master integration, series closeout, closeout/reopen, and the memory carryover paths consume this
package: branch-backed authority checks (`require_*`), durable lifecycle operation leases, the
Dagger quality gate checkout, and organizational-completion integration/repair.

## Conventions

- The package keeps the `worktrees` layering altitude: it never imports the queue package's
  application layer.
- Authority refusals stay typed (`SprintLinkageError`/`CloseoutQueueError`-family or the
  `AgentsRememberError` family).

## Invariants And Boundaries

- Lifecycle operation identity/lease/store are runtime-authority surfaces (bounded, evictable).
- Integration never falls back to a host quality run; the Dagger graph owns acceptance.

## 260821-CLIVE-L1 Admission, Identity, And Recovery

Closeout integration separates four owners: the contract lifecycle lease serializes filesystem writers; closeout admission stabilizes and normalizes candidate/plan before lifecycle compatibility; candidate identity binds accepted effective input and Git provenance; mutation evidence and recovery projection own crash classification. The typed integrate caller owns integrate retention, authority, and candidate derivation, while lease-bound closeout admission is the sole closeout candidate owner. The shared controller requires the supplied candidate and explicit authority, then separates generation creation/conflict/terminal replacement from recovery/launch/projection; it cannot recapture closeout provenance or infer kind-specific authority from ambient state. For closeout, reconciliation precedes durable journal publication. Worker authority survives every non-terminal phase and may be cleared only after exact termination proof; a failed or denied termination retains the PID and blocks replacement. The store is strict schema 3.0 and relies on model/public fill-only boundaries for impossible leg-set or proven-commit rewrites while retaining transition-specific identity/state/pre-state checks. Duplicates validate against the immutable accepted plan, and generation retention requires commit-proven mutation or exact canonical contract-finalization publication. The disposable queue projection owns no retry, recover, cancel, revise, claim, or commit evidence.

## 260821-CLIVE-L2 Current Architecture

One admitted contract observation enters each public mutation flow; the mutation owner rereads that exact authority under its existing lease/lock. Journal input and proven output are immutable. Retry/recover remain same-generation, revise is safe-cancel plus write-ahead successor, and worker authority survives until termination proof. Direct landing journals every memory/ledger cut. Legacy schema-1 repair and pre-locator adoption are explicit removable routes. Terminal cleanup refuses until L5 archive proof.

The route decomposition mirrors those boundaries without adding new authority: normal lifecycle state is under `lifecycle/`, direct landing under `direct_landing/`, and the only schema-1 reader under `legacy/`. Parent-level integration modules coordinate Git/ref publication and organizational repair across those owners.

### Reconciled Source Evidence

| Finding | Citations | Source Path |
| --- | --- | --- |
| Locator-manifest-journal authority. | L117-L130; L133-L287; L290-L375 | `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_location.py` |
| Task-addressed controls. | L125-L136; L149-L254 | `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_controls.py` |
| Direct landing recovery. | L68-L165 | `mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_execution.py` |
| Bounded legacy bridge. | L80-L87; L107-L188 | `mcp/src/agents_remember/worktrees/integration/legacy/legacy_operation_bridge.py` |
| Public operation projection derives legal controls and recovery surfaces from retained journal evidence. | L54-L132; L135-L227 | `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_projection.py` |

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

## Update History

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: reconciled immutable doors, atomic journal claim transfer, strict terminal archive/successor authority, and removal of successor-intent WAL ownership. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: recorded the `lifecycle/`, `direct_landing/`, and `legacy/` package boundaries, repointed current evidence, and verified the governed route at code commit `1d446724d099517f6f52d596b47827ae2391a2a4`.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: refreshed current route intent and source evidence for the accepted full L2 candidate; verification provenance and contract-scoped quality enforcement remain architect-closeout-owned.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1 candidate-11: route ownership now records typed integrate versus lease-bound closeout callers, required shared-core values, and separated generation/recovery stages against accepted tree `4241908c`; verification metadata remains closeout-owned.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: created the `worktrees/integration`
  route — fourteen modules moved from `worktrees/` (flat). Verified at code commit e5cb139f.
