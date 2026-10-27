# Lifecycle Operation Integration Overview

| Field | Value |
| --- | --- |
| sourceRoute | `mcp/src/agents_remember/worktrees/integration/lifecycle` |

## Governing Overview

[Integration overview](../overview.md)

## What This Area Is

This area owns durable lifecycle-operation addressability, journal storage, generation start and retry, public projection, legal controls, cancellation, and completed-disposition checks. Operations are generation-scoped: their accepted inputs and evidence determine which transitions and controls are available.

## Hot Path Summary

Read `lifecycle_operations.py` for start, observation, and generation replacement, and `lifecycle_operation_location.py` for the locator-to-enclosure chain. `lifecycle_operation_store.py` owns durable records and their revisions. `observation/status_wait.py` waits for meaningful change; `lifecycle_operation_projection.py` and the control projector derive a generation-coherent public view.

Recovery commit evidence contains code and memory-content outputs. Cache refresh is not a third recovery commit. Cancellation and recovery use actual Git/ref and worker evidence.

## Construction And Ownership

Public retry/recover advertises mechanically recoverable direct-create cuts from the accepted generation evidence. Real ref/input/history contradictions retain developer decision; no control invents a second code commit or bypasses its mutation owner.

Ordinary closeout journals require canonical `taskIntent`. An admitted direct-landing journal instead carries its canonical leaf binding on DirectLandingOperationInput; missing taskIntent alone does not withhold its mechanically supported controls. Legacy generations lacking both compatible intent and the direct binding retain the ordinary archive/reuse barrier and developer-decision path. Closeout claim and launch verify the same intent/dependency authority

An independent locator addresses an enclosure manifest, which supplies the canonical journal address for each operation kind. Location resolution cross-checks the locator and manifest without scanning for a substitute. An enclosure-root journal can be read independently of the task document; an unreadable contract is projected as a developer decision with no legal controls.

[The generation route](generation/overview.md) owns queued-record construction, integration-authority snapshots, and the pure same-generation resume transition. `creation.py` returns an in-memory candidate. Durable initial certification selection belongs to the store's creation/replacement boundary; the coordinator owns claims and launch. `resume.py` requires recorded termination to prove exit, retains termination and reconciled-mutation history, and preserves the accepted generation and immutable intent, returning queued for ordinary operations and running/direct-preflight for direct landing. Use the concrete child cards before changing these boundaries.

The public projector binds its identity to operation kind, contract path, generation, record revision, candidate fingerprint, and gate-policy identity. Results, approval and worker observations, recommended actions, and legal controls share that identity. Dependent identity mismatches produce an incoherent envelope. The result and decision rebinding helpers preserve component bindings; observation uses the decision binder for location and unreadable-contract decisions. Legal controls are calculated without mutating the journal, including the explicit cancellation control for `termination-required` records.

The store advances `recordRevision` once for an accepted mutation and advances `meaningfulRevision` only when canonical meaningful state changes. A newly created record starts at record revision 1. The bounded, read-only wait observes the meaningful cursor: timeout returns an unchanged snapshot, while successor generations, mismatched generations, invalid cursors, replacement, and unreadable journals have typed outcomes.

No refresh validator composes sidecar and governing-route body checks in this route any more: that composer was removed. The parity intent survives as a requirement on the surviving judges — curator preparation and closeout must apply the same rule to the same candidate — and on converted memory that rule is the onboarding-trace gate. The earlier claim that both callers invoked the removed composer has no current referent.

Public lifecycle recover admits the current canonical-leaf-bound doorless direct generation on its retained record, runs its real recovery executor and settles the kept closing receipt as landed when that call completes. Missing taskIntent alone does not strip this direct control; generations missing both compatible intent and admitted leaf input retain the legacy reuse barrier. A completed direct owner may retire, never supersede, under the shared record predicate and unchanged integrated/live-claim/worker-exit restrictions. Exact replay retains the generation; only a changed request may replace retired terminal evidence. Earlier door-carrying direct records remain readable but offer no controls.

## Invariants And Boundaries

Accepted generation identity and durable input remain immutable during ordinary store transitions. A claimed approval cannot become unclaimed. Exact duplicate requests converge; failed generations require explicit task-addressed retry/recover/resume rather than automatic replacement. Terminal replacement refuses retained, unproven worker authority. A cancelled closeout successor requires the current waiting door, cancelled journal disposition, and proven worker exit; that predicate does not search publication history for a unique predecessor.

Current closeout journal writes require canonical `taskIntent`. Closeout admission checks the waiting door's candidate tree and task intent against the admitted candidate. Ordinary missing-intent closeout records retain the coordinator/store reuse and legacy-text archival boundaries. An admitted direct generation instead carries the canonical leaf binding in its input; absence of taskIntent alone does not reject that binding. Direct landing has a narrower write rule: the store deliberately does not require a leaf task intent for that series-contract, branch-addressed delivery. These predicates must not be collapsed into a promise that every direct-landing write is intent-bound.

Cancellation requires worker-exit and exact no-output evidence. A failed quality phase may leave its accepted candidate staged while a later repair changes the working-tree candidate. Cancellation records both accepted and observed candidate states while requiring protected branch identity, HEAD/tree, and reflog identity to remain unchanged. Unattributed protected-ref movement requires a developer decision; ambiguous or proven commit output requires recovery in the retained generation.

For a direct landing that closes a history file, admission keeps a per-generation receipt before journal creation. Cancellation checks receipt readability before termination or publication. An unreadable receipt is `direct-landing-closing-receipt-unreadable` with next action `developer-decision`. After publishing cancellation, and on repeated applied cancellation, it settles the receipt as cancelled. Restoration preserves later edits and leaves a closing already proven landed in HEAD intact. Other operation kinds skip these receipt helpers. The no-output proof refuses ambiguous or proven commit output before cancellation proceeds.

Completed disposition requires exact completed, unintegrated ownership, no active integration publication claim, and released worker authority. A completed direct owner may retire, never supersede; ordinary closeout retains its separately admitted retirement/supersession route. Public journal-read failures use a shared decision owner for projection and control-error translation.

The journal and projector do not themselves execute certification or finalization. Current production service composition binds no prepared closeout continuation: that class, its producer and its service ports were removed by this leaf, and the ordinary transaction is the synchronous closeout route that runs the invariant gate and publishes the memory commit.

The standing integration intent is to preserve explicit approval, candidate identity, source movement refusal, and ref safety, with full-suite execution requiring an explicit developer request. The old blanket assertion that strict quality, memory quality, selected certification, curator coherence, and independent review all sit outside normal execution is not established by this route; selected certification remains a requested repository-profile route, while the prepared closeout continuation is not present in current production composition.

## Authority Discrepancies

The earlier de-entanglement description says the lock, door, operation, and journal planes were deleted and accepts lost concurrent writes. Current source contradicts that operative description: the lifecycle store serializes mutations through `exclusive_access`, the coordinator claims waiting doors, and cancellation and replacement retain worker-exit checks. The deletion account cannot authorize bypassing these current owners. The earlier architectural account is retained separately from these source facts and supplies no bypass authority.

The earlier source observation found `lifecycle_completed_disposition._completed_direct_owner` comparing an observed tuple of seven values with an expected tuple of eight, whose eighth value was `generation`; that equality could not recognize a completed direct landing's owner. This is a preserved pre-change diagnosis, not the current implementation or a new lifecycle verdict. The landed implementation uses `lifecycle_operation_identity.completed_direct_owner` as the shared doorless record predicate, and the disposition owner delegates to it while retaining the integration and worker-exit restrictions. Source inspection supplies no new execution or acceptance.

## File-Level Onboarding Map

The following coverage statuses are retained metadata, outside the operative promises above.

| Source File | Onboarding | Status |
| --- | --- | --- |
| `lifecycle_operations.py` | [lifecycle_operations.py.md](lifecycle_operations.py.md) | covered |
| `lifecycle_operation_location.py` | [lifecycle_operation_location.py.md](lifecycle_operation_location.py.md) | covered |
| `lifecycle_operation_store.py` | [lifecycle_operation_store.py.md](lifecycle_operation_store.py.md) | covered |
| `lifecycle_operation_projection.py` | [lifecycle_operation_projection.py.md](lifecycle_operation_projection.py.md) | covered |
| `lifecycle_operation_control_projection.py` | [lifecycle_operation_control_projection.py.md](lifecycle_operation_control_projection.py.md) | covered |
| `lifecycle_operation_control_evidence.py` | [lifecycle_operation_control_evidence.py.md](lifecycle_operation_control_evidence.py.md) | covered |
| `lifecycle_completed_disposition.py` | [lifecycle_completed_disposition.py.md](lifecycle_completed_disposition.py.md) | covered |
| `control/cancellation.py` | [control/cancellation.py.md](control/cancellation.py.md) | covered |

## Evidence

- The receipt check before anything moves, and the restore after publication. [1]
- Recovery state contains the actual two commit outputs. [2]
> Retained earlier citation wording: - Locator and manifest determine per-kind journal addresses independently of task-document reads. [5]
- Generation construction is in memory; retained resume preserves evidence and requires recorded exit; durable creation owns initial certification selection. [6]
- No-output cancellation preserves successor candidate differences and refuses moved protected output identities. [10]
- Direct-closing receipts precede journal admission, preserve later edits, and preserve closings already landed in HEAD. [11]

- Historical pre-change completed-disposition diagnosis: the former direct-owner tuple had unequal lengths. Current disposition delegates to lifecycle_operation_identity.completed_direct_owner and retains integration/publication-claim/worker-exit restrictions.  Anchor: lifecycle_completed_disposition.py [13]





- Default production services bind the ordinary memory-quality, citation, certification-memory, knowledge validation/crossing/gate and archive adapters; they do not install the removed prepared-closeout continuation or selected certificate producer. [15]


- The exact-generation observer returns bounded change/timeout outcomes. [4]


> Retained earlier citation wording: - Direct recovery is admitted independently of closeout doors and settles its retained receipt on completion.  Locator and manifest determine per-kind journal addresses independently of task-document reads. [5]

- Completed direct retire is offered using the shared record-based owner predicate. [6]

- Store transition validation requires recordRevision to advance once and meaningfulRevision to advance only when semantic state changes. [3]
- Public identity, component rebinding, incoherence handling, and termination controls derive from current generation evidence.  Anchor: lifecycle_operation_projection.py; lifecycle_operation_control_projection.py; observation/projection.py [7]
- Failed-generation replacement is explicit; cancelled closeout succession uses the current door, journal disposition, and exit proof.  Anchor: lifecycle_operations.py; lifecycle_operation_store.py [8]
- Closeout admission binds task intent; direct-landing writes are exempt from that leaf-intent requirement, although shared legacy predicates still mention direct landing.  Anchor: lifecycle_operations.py; lifecycle_operation_store.py [9]
- Current store mutation serialization and waiting-door claims contradict the blanket plane-deletion account.  Anchor: lifecycle_operation_store.py; lifecycle_operations.py [12]

- Direct recovery is admitted independently of closeout doors and settles its retained receipt on completion.  Locator and manifest determine per-kind journal addresses independently of task-document reads. [5]

- Converted memory is judged through the onboarding-trace gate, which reports missing traces and incomplete sides while unnecessary rows report only. External-memory helpers separately plan entity fingerprints and refresh route indexes; they do not restore the removed sidecar/route-body gate. [14]
