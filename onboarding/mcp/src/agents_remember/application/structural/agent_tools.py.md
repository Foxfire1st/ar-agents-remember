# mcp/src/agents_remember/application/structural/agent_tools.py

| Field | Value |
|---|---|
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/structural/agent_tools.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-31T12:00+02:00 |
| lastVerifiedCommitHash | `f2b7c648f540efb9d64ceea22e11e651cb5cc914` |
| lastVerifiedCommitDate | 2026-08-31T15:32:32+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Structural application services](overview.md)

## Purpose

Implements agent dispatch, parent/child messaging, retirement, and rename as structural operations.
It resolves trusted ambient caller identity and document+role targets before invoking existing
plane-owned lifecycle and inbox primitives. Manager and worker dispatch also establish the selected
atomic-series source pair before an implementation seat can be exposed.

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
durable series identity, selects the master for its exact protected source pair, reconciles it, and
returns implementation authority only after it becomes active. Retained conflicts or damaged
authority become a failed `StructuralOutcome` carrying the transaction payload; a refused candidate
is never spawned. Selecting a different live master pauses the former selection rather than treating
its contract as an exclusive global lane.

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
- Multiple live master contracts are valid. Dispatch consumes one disposable source-pair selection
  and does not read a closeout queue as admission authority.
- No plane identity means an ambient caller, never a fallback: a stale, invalid, mismatched, or
  unbound plane identity refuses instead of silently downgrading.
- Ambient rollback is a system closure bounded to the spawn result — an ambient caller cannot
  retire an arbitrary session.
- Reviewer altitude comes from the target document, and reviewer ownership comes from the
  authorizing plane seat; neither is inferred from the shared role name.

### Todos

None.

## Docs References

No Domain Documentation source is configured; repository tests and the approved L19 task are the evidence.


## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Dispatch performs contained-seat authorization and exact initial brief handling, now by caller kind (plane vs ambient). | `dispatch_agent_tool`; `_resolve_dispatch_caller` | mcp/src/agents_remember/application/structural/agent_tools.py:338-487 |
| Manager and worker dispatch resolve the canonical master and surface activation/sync refusal before spawn. | `_implementation_series_admission_refusal`; `_dispatch_owning_master` | mcp/src/agents_remember/application/structural/agent_tools.py:624-674; mcp/src/agents_remember/application/structural/agent_tools.py:677-693 |
| The shared series bootstrap owner binds durable contract identity to source-pair reconciliation-before-exposure. | `ensure_master_series_contract` | mcp/src/agents_remember/worktrees/modules/startup/start_contract.py:221-288 |
| Relationship messaging and lifecycle operations expose structural intent. | `message_parent_tool` | mcp/src/agents_remember/application/structural/agent_tools.py:828-833 |
| Dispatch caller resolution belongs to this current application entry point; removed fixtures do not establish live routing coverage. | `_resolve_dispatch_caller` | mcp/src/agents_remember/application/structural/agent_tools.py:403-442 |
| Rollback retires an unbriefed child as the authority-gated actor (plane) or a system closure (ambient). | `_retire_unbriefed_child` | mcp/src/agents_remember/application/structural/agent_tools.py:217-265 |

## Cross-Repo References


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

## Update History

- 2026-08-31T12:00+02:00 — ARSPAWN-L5 A005 review repair delegates seat serialization and
  transaction execution to `dispatch_transaction.execute_serialized_dispatch`, returning
  `dispatch_agent_tool` to a 90-line composition function. Verification remains closeout-owned.

- 2026-08-31T04:59+02:00 — 260821-ARSPAWN-L5 independent-review repair: documented
  document-derived spawn altitude, fail-closed invalid hosted identity, and the exact reviewer
  parent passed by plane dispatch into spawn and reconciliation. Verification remains closeout-owned.

- 2026-08-26T16:03+02:00 — Post-failure repair: recorded the dispatch-specific receipt collaborator,
  exact persistence seam used by ambient rollback forcing, and unchanged canonical-address boundary.
  Verification remains closeout-owned.


- 2026-08-26T12:30+02:00 — Reconciled 260821-ARSPAWN-L2 onto IAS: preserved the complete idempotent
  dispatch, evidence-aware retry, private rollback, and vacancy-safe addressing contract while
  retaining IAS-owned metadata and citation repairs. Verification remains closeout-owned.

- 2026-08-26T03:37+02:00 — Replaced the manager-only global-lane account with current manager and
  worker atomic-series admission: canonical master resolution, disposable source-pair selection,
  reconciliation-before-spawn, and structured retained-conflict/refusal results. Verification
  remains post-Dagger/closeout-owned.

- 2026-08-24T00:51+02:00 — No content impact: 260821-CLIVE-L2 the source only repoints the startup import and extracts the existing post-spawn briefing statements into `_brief_spawned_child`; dispatch ordering and documented child-briefing behavior are unchanged. Verified at code commit `1d446724`.

- 2026-08-21T03:45+02:00 — 260821-ARSPAWN-L1 fix round 3: `_resolve_dispatch_caller` restructured ambient-first — `resolve_ambient_caller` decides the branch directly (no plane identity → ambient with role-altitude validation; plane identity → `resolve_ambient_seat` + `authorize_child`, any refusal never downgrades); the both-fail defensive guard was removed as dead code (same environ). Verification metadata pinned until closeout stamps the 260821-ARSPAWN-L1 commit.

- 2026-08-21T02:50+02:00 — 260821-ARSPAWN-L1: `dispatch_agent_tool` resolves the caller by kind through `_resolve_dispatch_caller` — plane seats keep `resolve_ambient_seat` + `authorize_child` unchanged; only `ambient-seat-unavailable` downgrades to the ambient branch (role altitude still validated); stale/invalid/mismatched/unbound plane identity refuses instead of downgrading. Plane spawns pass `caller_kind="plane"`; ambient rollback retires the unbriefed child as a system closure (`retire_entry`, `by_session=None`, edge `ambient-dispatch-rollback`, actor `system`) bounded to the spawn result; `StructuralMessageContext.sender` is optional so the ambient brief post carries no sender. Verification metadata pinned until closeout stamps the 260821-ARSPAWN-L1 commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-19T22:32+02:00 — 260815-DAG-L13: manager series bootstrap resolves the effective
  execution nature (nature-less masters default to atomic; organizational only under an authored
  graph), and an atomic-sequential lane-blocked bootstrap surfaces as a `StructuralOutcome`
  carrying the ordering payload instead of raising. Verification remains closeout-owned.

- 2026-08-15T23:38+02:00 — Reconciled this file's L4 role in task-derived integration authority and protected code/memory boundaries. Verification metadata remains closeout-owned.
- 2026-08-14T06:30+02:00 — L23 final candidate review: structural dispatch now fails closed on
  stale task-derived lineage and requires a current candidate-bound route-review record before
  curator host creation. Verification remains closeout-owned.

- 2026-08-11T06:47+02:00 — 260731-EFA-L19: created for structural agent operations; replaces public exact-id orchestration operations rather than wrapping them as compatibility APIs.
