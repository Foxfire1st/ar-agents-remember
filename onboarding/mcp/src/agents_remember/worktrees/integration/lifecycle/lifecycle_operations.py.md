# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operations.py

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Coordinates task-addressed lifecycle start, observe, retry, resume, cancel, and projection.

## Code Commentary

### Logic

Series closeout remains recording-only and rejects enabled code or memory writes. That is the complete Git-leg vocabulary; a ledger-cache refresh has no operation input or commit leg to require. The existing claim, dependency, lease, and selected-preparation rules continue to own their own boundaries.

It claims waiting closeout candidates, creates or replaces generations, publishes initial doors,
starts detached workers, handles exact duplicate/retry cases, and exposes current projections. A
Linux launch first admits the exact runtime through the native-pidfd capability boundary; after
`Popen` succeeds, the real process object transfers to the lifecycle-owned child registry so a
dedicated waiter reaps it independently of later PID-based lifecycle observation. After a
generation is safely cancelled, replacement binds the current exact waiting door and still requires
proven worker exit; current candidate-tree and first-ready checks remain in the subsequent claim
transaction.

Under CCR-R03@v1 the closeout claim record and the queued integrate record are bound with their
typed dependency declaration (`lifecycle_operation_dependencies`), and the lifecycle launch gate
re-requires the current record's declared dependencies (`require_lifecycle_operation_dependencies`)
before a worker is launched
cit:(["def _prepare_closeout_claim(", "def queued_operation_record(", "def _recover_launch_and_project("], mcp/src/agents_remember/worktrees/integration/lifecycle/generation/creation.py:33-71; mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operations.py:445-481; mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operations.py:858-878).

Queued-record construction now lives in `generation/creation.py`; its candidate/task identity
and integrate dependency binding are unchanged. Durable generation publication and launch remain
owned by the coordinator and store.

### Conventions

Typed records and refusal payloads remain owned at the narrowest stable boundary. Callers consume
the public function or model instead of re-deriving its lower-level state machine. Dependency
declarations are recomputed from the exact admitted inputs whenever the record's door intent or
input changes.

#### Invariants And Boundaries

- A failed or terminal generation has an explicit convergent retry route; claim/door/generation publication is ordered and idempotent; queue state is scheduling input, not operation authority.
- Cancellation releases the old operation only after worker exit proof. A fresh generation follows
  current door and task truth rather than requiring a stale direct claimed-door edge.
- Linux launch refuses before spawning when the selected interpreter lacks native pidfd APIs.
- Every successfully spawned detached worker transfers its `Popen` to the single child owner for
  eventual reaping; PID/fingerprint evidence remains a separate lifecycle concern.
- Missing, unreadable, ambiguous, or conflicting authority fails loudly; this file does not add a
  fallback or compatibility shadow.
- Launch and projection require the record's declared dependencies to match its admitted inputs;
  a stale or missing declaration refuses before any worker starts.

### Todos

None recorded.

## Evidence

### Docs References

No external Domain Documentation source is configured for this slice. The current behavior is repository-owned and is supported by the source references below.

No configured external source applies.

### Repo-Internal References

The following current source boundaries establish the ledger-retirement behavior.

- `_require_series_recording_only` refuses enabled code or memory writes for recording-only series closeout. [1]
- `start_or_observe_closeout_operation` composes closeout admission through the journal-owned lifecycle route. [2]

The source file is the direct evidence for this unit; its governing overview records adjacent owners.

- Detached launch admits the Linux runtime, transfers the real child object to the reaper, and then records process identity. (`launch_detached_worker`) [3]
- R03 dependency binding on claims and queued records plus launch re-requirement. (`queued_operation_record`; `_prepare_closeout_claim`; `_recover_launch_and_project`) [4]

### Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

No additional cross-repository evidence applies.

## CCR-R12@v5 Current Admission Boundary

Closeout admission starts or observes the typed transaction after candidate, contract-door, and
source checks; it does not build a selected certification or quality prerequisite for the normal
route. Successor generations reuse explicit recovery authority and fresh provenance under a lease.
Integration admission similarly preserves source-pair identity and ref safety while leaving any
full-suite or certification work to an explicit developer request.

## 260831-CCR-R03 Dependency-Gated Launch

Closeout/integrate records now bind their declared inputs and launch refuses a stale declaration
(worker handover: notes/reports/260902-CCR-L03-worker-delivery.md).

## Current Landed Composition

Leaf start freezes complete certification admission before initial journal publication. An unchanged candidate revalidates selected currentness and unchanged-retry admissibility; a new candidate prepares a new frozen admission. Initial certification selection is passed atomically into journal create/replace, and an existing leaf claim must retain selected certification. A queued claim recovered before any worker identity was installed can resume its original launch. Series closeout is recording-only: it revalidates series authority and refuses enabled code or memory commit legs. Integration authority snapshots and queued-record construction live in `generation/creation.py`.
