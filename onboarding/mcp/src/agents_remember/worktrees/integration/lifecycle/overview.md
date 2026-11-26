# Lifecycle Operation Integration Overview

| Field | Value |
| --- | --- |
| sourceRoute | `mcp/src/agents_remember/worktrees/integration/lifecycle` |

## Governing Overview

[Integration overview](../overview.md)

## What This Area Is

This area owns operation journal addressability, storage, public projection and generation-bound controls for direct landings. Closeout and integration run synchronously through their own tools. Older journal records for those two kinds remain addressable for audit.

## Hot Path Summary

Read `lifecycle_operation_location.py` for the locator-to-enclosure chain and `lifecycle_operation_store.py` for durable records and revisions. The unmounted helper in `observation/status_wait.py` observes meaningful changes for an exact retained generation. The operation and control projectors derive a generation-coherent public view.

The lifecycle journal store validates file identity before reusing parsed records. Native tool calls share the parse cache within their request. Dashboard reads use a separate count-bounded process owner.

Recovery commit evidence contains code and memory-content outputs. Cache refresh is a separate observation. Direct cancellation and recovery check the observed Git state against the retained evidence.

## Construction And Ownership

The public projection offers `recover` for an eligible nonterminal direct-landing generation and adds `cancel` where the generation evidence permits it, subject to unchanged Git proof. A compatible `termination-required` record offers exact cancellation. An eligible completed record may offer `retire`, and an eligible cancelled record can offer a fresh `direct_landing` call. Evidence classified as requiring developer decision withholds controls. The request vocabulary is wider than these offers, and exact same-input replay has its own direct entry.

An admitted direct record can carry its canonical leaf on `DirectLandingOperationInput`. Control can reuse that binding when compatible task intent is absent. The status projection separately requires exact task intent before presenting legal controls.

An independent locator addresses an enclosure manifest, which supplies the canonical journal address for each operation kind. Location resolution cross-checks the locator and manifest without scanning for a substitute. An enclosure-root journal can be read independently of the task document; an unreadable contract is projected as a developer decision with no legal controls.

[The generation route](generation/overview.md) owns the pure same-generation resume transition. `resume.py` retains accepted input and mutation history and sets the next direct attempt to running at `direct-preflight`.

The public projector binds its identity to operation kind, contract path, generation, record revision, candidate fingerprint and gate-policy identity. It binds results, approval observations, recommendations and legal controls to that identity. Dependent mismatches are incoherent. The read-only control projection derives applicable controls for direct landings from the current record.

The store advances `recordRevision` once for an accepted mutation and advances `meaningfulRevision` only when canonical meaningful state changes. A newly created record starts at record revision 1. The unmounted read-only wait helper observes the meaningful cursor: timeout returns an unchanged snapshot, while successor generations, mismatched generations, invalid cursors, replacement, and unreadable journals have typed outcomes.

No refresh validator composes sidecar and governing-route body checks in this route any more: that composer was removed. The parity intent survives as a requirement on the surviving judges — curator preparation and closeout must apply the same rule to the same candidate — and on converted memory that rule is the onboarding-trace gate. The earlier claim that both callers invoked the removed composer has no current referent.

Public recover runs the admitted doorless direct generation on its retained record and settles the kept closing receipt as landed when recovery completes. A completed direct owner may retire under the shared record predicate and idle integration-claim rules. Exact replay retains the generation. Earlier door-bearing direct records remain readable without controls.

## Invariants And Boundaries

Accepted generation identity and durable input remain immutable during ordinary store transitions. A claimed approval cannot become unclaimed. Recovery of a direct landing uses the accepted generation and exact mutation evidence.

Historical closeout and integration journal controls refuse before mutation. For an exact match or when no journal record exists, the refusal points to the synchronous tool and the current contract path. A mismatched generation receives the identity refusal. The audit projection retains the saved status, phase and outcome for historical operations. Direct landing alone reconciles stored mutation evidence against live Git.

Direct cancellation requires exact no-output evidence. It can preserve a difference between accepted and observed candidates while the protected ref, HEAD/tree and reflog identity remain unchanged. Ambiguous or proven commit output requires recovery.

For a direct landing that closes a history file, admission keeps a per-generation receipt before journal creation. Cancellation checks receipt readability before publication. An unreadable receipt is `direct-landing-closing-receipt-unreadable` with next action `developer-decision`. The cancellation helper settles the receipt after publishing cancellation and when it receives an already cancelled record. The public control projection can offer a successor for an eligible cancelled direct generation. Restoration preserves later edits and leaves a closing already proven landed in HEAD intact. Other operation kinds skip these receipt helpers. The no-output proof refuses ambiguous or proven commit output before cancellation proceeds.

Completed direct retirement requires exact completed, unintegrated ownership and an idle integration claim. Public journal-read failures use a shared decision owner for projection and control-error translation.

The journal and projector do not themselves execute certification or finalization. Current production service composition binds no prepared closeout continuation: that class, its producer and its service ports were removed by this leaf, and the ordinary transaction is the synchronous closeout route that runs the invariant gate and publishes the memory commit.

The standing integration intent is to preserve explicit approval, candidate identity, source movement refusal, and ref safety, with full-suite execution requiring an explicit developer request. The old blanket assertion that strict quality, memory quality, selected certification, curator coherence, and independent review all sit outside normal execution is not established by this route; selected certification remains a requested repository-profile route, while the prepared closeout continuation is not present in current production composition.

## Journal Ownership

The lifecycle store serializes journal mutations through its exclusive access boundary. The retained store and locator also support audit reads for historical kinds.

The completed disposition owner delegates to `lifecycle_operation_identity.completed_direct_owner` for the doorless record predicate.

## File-Level Onboarding Map

The following coverage statuses are retained metadata, outside the operative promises above.

| Source File | Onboarding | Status |
| --- | --- | --- |
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

- No-output cancellation preserves successor candidate differences and refuses moved protected output identities. [10]

- Direct-closing receipts precede journal admission, preserve later edits, and preserve closings already landed in HEAD. [11]

- Completed disposition checks the shared direct-owner predicate and idle integration claim. [13]

- Default production services bind the ordinary memory-quality, citation, certification-memory, knowledge validation/crossing/gate and archive adapters; they do not install the removed prepared-closeout continuation or selected certificate producer. [15]

- The exact-generation observer returns bounded change/timeout outcomes. [4]

> Retained earlier citation wording: - Direct recovery is admitted independently of closeout doors and settles its retained receipt on completion.  Locator and manifest determine per-kind journal addresses independently of task-document reads. [5]

- Completed direct retirement is offered using the shared record-based owner predicate. [6]

- Store transition validation requires recordRevision to advance once and meaningfulRevision to advance only when semantic state changes. [3]

- The public projection binds component identity, checks coherent typed intent and derives applicable direct-landing offers from the generation's evidence. [7]

- Direct recovery uses accepted generation evidence and settles a completed receipt in the same call. [8]
- The control observer checks exact generation identity and refuses a retired record before reconciliation. [9]
- Store transition validation preserves journal identity during mutation. [12]

- The direct recovery handler operates its accepted generation and settles the receipt. The locator and manifest address all saved journal kinds. [5]

- Converted memory is judged through the onboarding-trace gate, which reports missing traces and incomplete sides while unnecessary rows report only. External-memory helpers separately plan entity fingerprints and refresh route indexes; they do not restore the removed sidecar/route-body gate. [14]
