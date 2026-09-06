# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operations.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operations.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T14:48:58+00:00 |
| lastVerifiedCommitHash | `fbc89847233b1c5959f56475f2cb51f936d5ef0b` |
| lastVerifiedCommitDate | 2026-09-02T07:47:04+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Lifecycle operation integration overview](overview.md)

## Purpose

Coordinates task-addressed lifecycle start, observe, retry, resume, cancel, and projection.

## Code Commentary

### Logic

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
cit:([`_prepare_closeout_claim`, `queued_operation_record`, `_recover_launch_and_project`], mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operations.py:488-523; mcp/src/agents_remember/worktrees/integration/lifecycle/generation/creation.py:33-71; mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operations.py:911-931).

Queued-record construction now lives in `generation/creation.py`; its candidate/task identity
and integrate dependency binding are unchanged. Durable generation publication and launch remain
owned by the coordinator and store.

### Conventions

Typed records and refusal payloads remain owned at the narrowest stable boundary. Callers consume
the public function or model instead of re-deriving its lower-level state machine. Dependency
declarations are recomputed from the exact admitted inputs whenever the record's door intent or
input changes.

### Invariants And Boundaries

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

## Docs References

The configured Domain Documentation registry is empty. No external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain source is required to establish this repository-owned implementation. | `STALE_HEARTBEAT_SECONDS` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operations.py:1-1118 |

## Repo-Internal References

The source file is the direct evidence for this unit; its governing overview records adjacent owners.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's concrete API, control flow, and validation boundary are implemented here. | `STALE_HEARTBEAT_SECONDS` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operations.py:1-1123 |
| Detached launch admits the Linux runtime, transfers the real child object to the reaper, and then records process identity. | `launch_detached_worker` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operations.py:883-938 |
| R03 dependency binding on claims and queued records plus launch re-requirement. | `_prepare_closeout_claim`; `queued_operation_record`; `_recover_launch_and_project` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operations.py:488-523; mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operations.py:911-931; mcp/src/agents_remember/worktrees/integration/lifecycle/generation/creation.py:33-71 |

## Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository reference applies. | `STALE_HEARTBEAT_SECONDS` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operations.py:1-1118 |

## 260831-CCR-R03 Dependency-Gated Launch

Closeout/integrate records now bind their declared inputs and launch refuses a stale declaration
(worker handover: notes/reports/260902-CCR-L03-worker-delivery.md).

## Update History

- 2026-09-06T14:48:58+00:00 — Repaired both queued_operation_record citations to its extracted owner at `c69d5171187fa1957025e393270db9f5a864ab14` after proving identical function AST; broader changed coordinator behavior remains for its source-card review. Prior verification stamps and all earlier history are preserved.


- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for fbc89847233b1c5959f56475f2cb51f936d5ef0b (CCR-R03@v1/L03): recorded the claim/queued-record dependency binding and the launch-time dependency re-requirement; prior claim, cancellation, and detached-launch prose preserved.

- 2026-08-29T16:27+02:00 — Reconciled detached launch with native-pidfd runtime admission and the
  separate lifecycle-owned `Popen` reaping boundary.

- 2026-08-26T16:57+02:00 — Removed direct claimed-door ancestry as cancelled-generation
  authority. Replacement now requires the current exact waiting door plus durable cancellation and
  worker-exit proof; exact candidate and first-ready checks remain claim-owned.
- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.