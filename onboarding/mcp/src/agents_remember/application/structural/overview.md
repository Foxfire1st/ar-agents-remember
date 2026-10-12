# Structural Application Services Overview

## Governing Overview

[`application/overview.md`](../overview.md)

## What This Area Is

This package composes document-and-role dispatch and structural lifecycle-gate operations while keeping runtime occupant, lifecycle and gate correlations private. Dispatch accepts a canonical task document, role and initial brief. A hosted caller is proven from process identity and authorized against task containment; an ambient launcher is resolved from the process environment and still faces role-altitude validation. Gate services separately support a request-carried declared role/document caller when no hosted seat exists.

`agent_tools.py` currently exposes dispatch and private initial-brief, receipt and rollback helpers. It does not expose the former parent/child messaging, public retirement or rename operations. The retained gate services are application code; their presence alone does not establish public MCP registration. This route must not create a second lifecycle implementation.

## Hot Path Summary

Dispatch resolves the canonical task document, proves the caller, derives dispatch provenance, and builds a transaction for one `(taskDocumentRef, role)` seat. `dispatch_transaction.py` holds the serializer across admission, spawn, durable initial briefing and bounded reconciliation. The MCP dispatch adapter projects the application result; the session registration module registers the single `dispatch_agent` entry for hosted and ambient callers.

Manager and worker admission resolves the owning master. Organizational work skips atomic-series creation; atomic work goes through the shared master-series contract owner before host creation. Curator admission validates the exact leaf-enclosure binding and calls the owning-altitude route-review authority. That authority can defer review for atomic children and for an atomic master until integration; a passing independent review is therefore not an unconditional dispatch-time prerequisite.

Initial briefs are internally pinned to the exact spawned occupant. Durable inbox evidence and the catalog receipt determine reconciliation: a viable brief converges, a missing receipt is repaired, and a surviving receipt supports a queued result after the inbox row is absent. The public result identifies the task document and role, with delivery state where available, rather than an occupant id.

## Construction And Ownership

| Path | Role |
|---|---|
| `agent_tools.py` | Dispatch composition, admission, exact initial briefing and transaction rollback |
| `dispatch_transaction.py` | Seat-scoped serialization and bounded spawn/reconcile transaction |
| `outcomes.py` | Stable structural result projection |
| `reviewer_parent.py` | Reviewer ownership and dispatch provenance |
| `gate_tools.py` | Retained structural lifecycle-gate raising, decision and listing services |
| `__init__.py` | Package marker |

Catalog qualification and relationship authorization belong in `serving/structural_seats.py`; process caller resolution belongs in `serving/ambient_seat.py`; lock and pinned-brief primitives belong in `serving/structural_dispatch.py`. Agent-facing request and response models belong in `models/structural/`. Internal serving and control-plane owners retain runtime-id administration. This package composes those owners rather than implementing a second lifecycle.

### Dispatch Construction

1. Resolve the requested task document and validate caller authority. A hosted caller uses direct-child authorization; an ambient launcher uses role-altitude validation without a hosted parent seat.
2. Derive provenance. Ambient leaf reviewers belong to their owning manager, master reviewers to the manager on that master, and sprint reviewers require a hosted owner rather than a guessed parent.
3. Acquire the canonical-seat serializer and run admission before spawning. Manager/worker admission uses the atomic-series owner where required; curator admission checks its enclosure contract and route-review authority.
4. Spawn the private generation and persist its exact initial brief and receipt.
5. Reconcile existing durable evidence or recover an initial-brief failure before deciding whether rollback is safe. The transaction permits one bounded respawn attempt after reconciliation requests a retry.
6. Return the structural outcome without exposing the private generation id.

The shared spawn-binding preflight resolves task references and checks lineage for structural roles. Its taskless-role set includes curator, so the generic binding path returns before lineage validation for that role. The curator-specific dispatch predicate checks enclosure binding and route review; it does not itself check a manager current-lineage preflight. The standing current-lineage and independent-review intent remains distinct from these source predicates; this account does not certify the discrepancy as coherent.

### Gate Construction

The gate context prefers the hosted seat. Only `ambient-seat-unavailable` permits a declared caller; any declaration contradicting a hosted seat is refused as `structural-caller-conflict`. Raising a gate resolves the caller's document and delegates to the existing gate owner. Deciding a gate authorizes the target document, selects exactly one open gate by document, repository and kind, then uses its private gate/lifecycle ids internally. Listing projects gates in the caller's document and direct-child scope without those private correlations.

### Atomic-Series Admission

Task documents remain the structural authority used to resolve the owning master and effective execution nature. Structural admission delegates atomic-series construction and reconciliation to the worktree owner; it does not author tasks or own queue scheduling. The shared series-contract owner creates or recovers the requested contract, reconciles its pinned source pair and returns implementation authority through that owner.

The standing boundary remains that task mutation is canonical, scheduling follows changed task truth, and sync conflicts stay with the worktree transaction for contract-addressed recovery. The old account that selection pauses another live master is not supported by the current dispatch owner: the shared contract owner's documented activation behavior touches the requested contract and explicitly says that no other master's record is touched. The wider task-mutation, scheduling-invalidation and conflict-recovery guarantees need their respective owners verified before they are presented here as fully established implementation facts.

## Invariants And Boundaries

- Structural dispatch inputs and result projections use task-document and role identity. Private runtime correlations remain internal to spawn, exact initial briefing, receipts and rollback.
- A present but stale, invalid, mismatched or unbound hosted identity refuses; dispatch does not downgrade it to ambient. An environment role without hosted identity also refuses.
- Initial dispatch briefing is exact-pinned internally. The structural resolver can produce authorized parent/child addresses without requiring a live occupant; those retained address APIs do not restore deleted public relationship-message tools.
- Current-seat selection fails closed on duplicate incumbents or duplicate staged heirs. One incumbent remains current while one heir is staged; the heir becomes selectable when the incumbent is absent. No same-role global lookup substitutes for the canonical document/role seat.
- The serializer combines a reclaimed in-process lock slot with a POSIX lock in one of 4,096 deterministic hash stripes. Collisions can serialize unrelated seats conservatively. There is no process-local fallback, and the implementation does not unlink lock files. Serializer setup/acquisition has its dedicated typed refusal.
- Durable pinned-brief evidence is the reconciliation commit point. Contradictory receipts, duplicate pinned briefs and unreadable evidence refuse rather than authorize destructive rollback. A non-dispatch occupant with no brief remains `seat-taken`.
- The standing safety intent is that unknown generation evidence never licenses cleanup. The current outer reconciliation path returns a retry request when its catalog occupant is missing or non-running; the inner evidence reader instead raises when its occupant disappears. Thus the previous blanket claim that every missing or terminal generation refuses is inaccurate. This discrepancy is disclosed for parent adjudication; the outer branch does not retire that missing/non-running occupant.
- Rollback is an internal transaction capability, distinct from public retirement policy. It reconciles durable evidence before retiring a proven unbriefed generation; retirement-event logging failure does not reverse catalog retirement.

## Memory Validation Boundary

The shared memory-refresh validator composes sidecar and governing-route body/history validation. The inspected memory-quality caller uses it on the unconverted-tree path, but first checks for onboarding-trace sides and returns through the trace gate when those sides exist. The old unconditional parity account must therefore be read with that conversion boundary. Closeout caller parity was not established by the bounded source inspection and remains an uncertainty, rather than fresh acceptance evidence.

## Retained Metadata

The following tables are retained metadata, outside the operative promises above. Their `covered` entries are preserved labels, not a newly verified onboarding or lifecycle status.

| Field | Value |
|---|---|
| sourceRoute | `mcp/src/agents_remember/application/structural/` |
| onboardingRoute | `mcp/src/agents_remember/application/structural/overview.md` |
| parentOverview | [`application/overview.md`](../overview.md) |

| File | Role | Why It Matters | Onboarding |
|---|---|---|---|
| `agent_tools.py` | application boundary | Prevents model-supplied runtime addressing | covered |
| `gate_tools.py` | authorization boundary | Prevents exact lifecycle/gate targeting by agents | covered |

| Source File | Onboarding File | Status | Reason |
|---|---|---|---|
| `application/structural/__init__.py` | [`__init__.py.md`](__init__.py.md) | covered | Package marker |
| `application/structural/agent_tools.py` | [`agent_tools.py.md`](agent_tools.py.md) | covered | Agent structural boundary |
| `application/structural/gate_tools.py` | [`gate_tools.py.md`](gate_tools.py.md) | covered | Gate structural boundary |

## Reading And Verification Bounds

Read this overview, the relevant file card, the structural-seat resolver card and the corresponding model card before changing a structural operation. This bounded package needs no child overview. Source inspection supplies no new test, native-host, whole-build, landing or memory acceptance. No current lifecycle status is inferred. The original excluded Needs Verification status line, "None.", is retained as metadata; it is not a fresh verification result.

## Evidence

- The structural dispatch adapter delegates to the application boundary; public dispatch registration is in the session registration owner. [1]
- Structural resolution qualifies document+role seats, authorizes containment and refuses ambiguity. [2]
- Dispatch proves hosted or ambient callers, builds private provenance and composes admission, spawn, exact briefing and rollback. [3]
- Serialization and bounded reconciliation use durable brief evidence; outer missing/non-running occupants request retry while inner disappearance refuses. [4]
- Retained gate services prefer hosted identity, conditionally accept declared callers, resolve authorized gates and hide private correlations. [5]
- Atomic manager/worker admission delegates to the shared series owner; curator review depends on owning altitude and can be deferred. [6]
- Generic spawn binding resolves references and checks structural-role lineage, but curator is in the taskless-role set and skips that lineage predicate. [7]
- Shared current-seat selection rejects duplicate claimants and prefers the incumbent over a staged heir. [8]
- Memory-refresh validation composes sidecar and route checks; its inspected memory-quality caller routes converted trees through the trace gate first. [9]
