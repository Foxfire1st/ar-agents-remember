# mcp/src/agents_remember/application/structural/agent_tools.py

## Governing Overview

[Structural application services](overview.md)

## Purpose

Implements agent dispatch, parent/child messaging, retirement, and rename as structural operations.
It resolves trusted ambient caller identity and document+role targets before invoking existing
plane-owned lifecycle and inbox primitives. Manager and worker dispatch also reconcile the owning
master's contract-keyed atomic-series activation before an implementation seat can be exposed.

## Code Commentary

### Logic

`dispatch_agent_tool` validates a contained child seat, opens and binds a hosted occupant, then posts
the internally exact-pinned initial brief. `_message_tool` persists ordinary structural traffic for
post-time and delivery-time rebinding. Retire and rename functions authorize only structural child
or self relationships. `UnbriefedChild` keeps spawn/brief cleanup explicit.

Before spawning a manager or worker, `_implementation_series_admission_refusal` resolves the
canonical master (directly for a manager, through the leaf's parent for a worker), derives effective
execution nature, and skips selection only for an organizational master. Atomic dispatch calls the
same `ensure_master_series_contract` owner used by first-leaf start. That owner creates or recovers
durable series identity, selects the master in that contract's own activation record — keyed per
series contract, not per protected source pair — publishes that contract's own activation as
`reconciling` (no other master's record is touched), syncs the pinned source pair, reconciles it, and
returns implementation authority only after it becomes `active`. Retained conflicts or damaged
authority become a failed `StructuralOutcome` carrying the transaction payload; a refused candidate
is never spawned. Two
atomic masters commanded by one sprint may share a protected code/memory source pair and both stay
selected: a foreign master's record is never read or named here, and the only surviving activation
waiting reason is `atomic-series-reconciling` on the addressed contract.

Since 260821-ARSPAWN-L1 `dispatch_agent_tool` resolves the caller by kind through
`_resolve_dispatch_caller`, which is AMBIENT-FIRST (fix round 3): `resolve_ambient_caller` decides
the branch from the same environ — no plane identity (`AR_HOSTED_SESSION_ID` absent) selects the
ambient branch, which still validates the role against the document altitude via
`topology.validate_role` (`seat-role-altitude-mismatch` / `seat-role-unsupported` survive) and
spawns with `SpawnedBy(caller_kind="ambient")`; with plane identity present the plane path runs
`resolve_ambient_seat` + `resolver.authorize_child` unchanged, and stale/invalid/mismatched/
unbound plane identity refuses — never a silent downgrade. The earlier both-fail defensive guard
was removed as dead code: the two resolutions read the same environ, so exactly one branch applies
and fail-closed behavior is unchanged. Plane spawns pass `caller_kind="plane"` explicitly. A failed ambient initial brief retires the
just-spawned child as a SYSTEM closure (`retire_entry` with `by_session=None`, edge
`ambient-dispatch-rollback`, actor `system`) — the child id is the spawn result, never caller
input, so an ambient caller cannot retire an arbitrary session; plane rollback stays
`session_retire_tool`-gated. `StructuralMessageContext.sender` is optional so the ambient brief
post carries no sender (`_signal_route`/`derive_signal_owner` tolerate a `None` sender;
dispatch-brief rows stay exact-pinned). Spawn level is derived from the resolved task document—not
from the role name—so the polymorphic reviewer records `leaf`, `master`, or `portfolio` at its actual
review altitude. For a plane-owned reviewer dispatch, the caller's canonical document+role is also
passed as the child generation's structural parent and supplied to the dispatch transaction as the
expected parent. Ambient dispatch may create ordinary task roles, but cannot invent the missing
owner of a polymorphic reviewer manifestation.

`CCR-L42` parity validation is external to these dispatch operations: the current candidate retains the structural dispatch behavior documented above while curator preparation and closeout independently check this sidecar and its governing route through the shared memory-refresh validator.

### Conventions

Public results expose the structural target plus operation status or delivery detail. Runtime ids
stay local to the application transaction.

### Invariants And Boundaries

- Ambient evidence, never model input, identifies the caller.
- Dispatch-brief delivery is exact-pinned internally; ordinary messages are rebindable.
- A failed initial brief retires the unbriefed child instead of leaving a live unowned seat.
- Authorization follows architect→orchestrator→manager→leaf-role ownership.
- Manager and worker implementation dispatch require an active, reconciled atomic parent when their
  effective master nature is atomic; curator/reviewer messaging remains outside selection.
- Multiple live master contracts are valid, including two sharing one sprint's source branches.
  Dispatch consumes that one contract's own disposable activation selection and does not read a
  closeout queue as admission authority.
- No plane identity means an ambient caller, never a fallback: a stale, invalid, mismatched, or
  unbound plane identity refuses instead of silently downgrading.
- Ambient rollback is a system closure bounded to the spawn result — an ambient caller cannot
  retire an arbitrary session.
- Reviewer altitude comes from the target document, and reviewer ownership comes from the
  authorizing plane seat; neither is inferred from the shared role name.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured; repository tests and the approved L19 task are the evidence.


### Repo-Internal References

- Dispatch performs contained-seat authorization and exact initial brief handling, now by caller kind (plane vs ambient). [1]
- Manager and worker dispatch resolve the canonical master and surface activation/sync refusal before spawn. [2]
- The shared series bootstrap owner binds durable contract identity to that contract's own activation: it publishes that contract's own activation as reconciling without touching another master's record, then syncs the pinned source pair and returns implementation authority only once it is active. [3]
- Relationship messaging and lifecycle operations expose structural intent. [4]
- Dispatch caller resolution belongs to this current application entry point; removed fixtures do not establish live routing coverage. [5]
- Rollback retires an unbriefed child as the authority-gated actor (plane) or a system closure (ambient). [6]

### Cross-Repo References


## 260815-DAG-L4 Authority Boundary

L4 routes this file's existing application, configuration, task, model, registration, or memory responsibility through the shared task-derived integration authority. The change preserves the file's owning altitude while ensuring protected code and external-memory refs cannot be mutated through an ordinary workbench or unjournaled helper.

## 260821-ARSPAWN-L2 Idempotent Seat Transaction

`dispatch_agent_tool` derives the canonical `(taskDocumentRef, role)` address before it
consults any occupant. It holds the serving-owned seat serializer across spawn, pinned-brief
publication, durable receipt binding, and reconciliation, then delegates the state machine to
`execute_dispatch_transaction`. A retry returns the existing viable result, repairs a missing
catalog receipt from durable inbox evidence, or treats a retained receipt as queued after inbox
compaction. It retires and retries at most once only when positive evidence proves that the
private server-derived generation has no viable brief.

Unknown, contradictory, or post-append evidence returns `dispatch-reconciliation-refused`
without destructive cleanup. Transaction rollback directly closes only the generation returned
by the private spawn path; it never re-enters public retire authorization. Ordinary structural
messages persist document-and-role addresses and resolve the current occupant only at delivery,
so vacancy and replacement do not turn runtime session ids into public authority. Receipt mutation is
composed through `DispatchBriefReceiptStore`, keeping dispatch commit evidence separate from the
general terminal lifecycle surface while reusing the same atomic catalog storage boundary.
