# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operations.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operations.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T00:53 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634` |
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No external Domain Documentation source is configured for this slice. The current behavior is repository-owned and is supported by the source references below.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external source applies. | — | — |

## Repo-Internal References

The following current source boundaries establish the ledger-retirement behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| `_require_series_recording_only` refuses enabled code or memory writes for recording-only series closeout. | `_require_series_recording_only` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operations.py:245-256 |
| `start_or_observe_closeout_operation` composes closeout admission through the journal-owned lifecycle route. | `start_or_observe_closeout_operation` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operations.py:210-242 |

The source file is the direct evidence for this unit; its governing overview records adjacent owners.

| Finding | Anchor | Source |
| --- | --- | --- |
| Detached launch admits the Linux runtime, transfers the real child object to the reaper, and then records process identity. (`launch_detached_worker`) | `launch_detached_worker` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operations.py:946-1041 |
| R03 dependency binding on claims and queued records plus launch re-requirement. (`queued_operation_record`; `_prepare_closeout_claim`; `_recover_launch_and_project`) | `queued_operation_record` | mcp/src/agents_remember/worktrees/integration/lifecycle/generation/creation.py:33-71 |

## Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No additional cross-repository evidence applies. | — | — |

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

## Update History

- 2026-09-15T00:53 UTC — LCA-L9 working-candidate curation: retired ledger Git authority in this file-specific boundary; preserved real Git and lifecycle safeguards and prior history. Source and diff reviewed, source-sha256=eb993abec4b9093403d878bc44c789944a5ff1806dfacad6ce3ed347af62fe6f. Existing verification commit/date remain unchanged until an actual source commit is available; no test or acceptance claim.

- 2026-09-11T23:05:00+00:00: Curator citation reconciliation: "def _prepare_closeout_claim(", "def _recover_launch_and_project(", "def queued_operation_record(" repointed to mcp/src/agents_remember/worktrees/integration/lifecycle/generation/creation.py:33-33, mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operations.py:445-445, mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operations.py:858-858. No content impact: mechanical anchor-range projection against citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `STALE_HEARTBEAT_SECONDS` repointed to mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operations.py:117-117. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `STALE_HEARTBEAT_SECONDS` repointed to mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operations.py:117-117. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `launch_detached_worker` repointed to mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operations.py:946-1041. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `STALE_HEARTBEAT_SECONDS` repointed to mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operations.py:117-117. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T07:41:10+00:00: Generated citation repair: `STALE_HEARTBEAT_SECONDS` repointed to mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operations.py:124-124. No content impact: mechanical anchor-range projection bound to citation source snapshot 794cfaf55738c596793ad49b95a946add84e2c03f1bf6499e2f00c6b84bd85ba; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T07:41:10+00:00: Generated citation repair: `STALE_HEARTBEAT_SECONDS` repointed to mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operations.py:124-124. No content impact: mechanical anchor-range projection bound to citation source snapshot 794cfaf55738c596793ad49b95a946add84e2c03f1bf6499e2f00c6b84bd85ba; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T07:41:10+00:00: Generated citation repair: `launch_detached_worker` repointed to mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operations.py:973-1068. No content impact: mechanical anchor-range projection bound to citation source snapshot 794cfaf55738c596793ad49b95a946add84e2c03f1bf6499e2f00c6b84bd85ba; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T07:41:10+00:00: Generated citation repair: `STALE_HEARTBEAT_SECONDS` repointed to mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operations.py:124-124. No content impact: mechanical anchor-range projection bound to citation source snapshot 794cfaf55738c596793ad49b95a946add84e2c03f1bf6499e2f00c6b84bd85ba; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T07:33:57+02:00 — CCR-R12@v5 scoped runtime curation against code commit `6f3e3fde75a1ca0202c9b07557cf86a7893e8532`: reconciled the normal transaction boundary and preserved earlier history. This records source documentation only; it makes no acceptance or certification claim.

- 2026-09-09T14:45+02:00 — CCR-L42 curator reconciliation: re-read affected claims against the frozen current source and corrected only their source anchors/ranges; verification stamps remain closeout-owned.

- 2026-09-09T02:42:21+02:00 — CCR-L24 inherited/current-source reconciliation 2026-09-09: Re-read the current card purpose, logic, invariants, and cited route against the frozen candidate source; no content or route change was required, and the existing claim bytes remain accurate. source-sha256=5e164bf5b308e20659e4e07b61a4cad895b1ad4bcafcfa139bdb6c366c6ba4ec; verification metadata remains unchanged because commit-owned realization is pending.

- 2026-09-06T22:41:21+00:00: Generated citation repair: `launch_detached_worker` repointed to mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operations.py:1002-1097. No content impact: mechanical anchor-range projection bound to citation source snapshot 250eac92295fa399589ccf1c9726bfb4cd28a1a0b20dca126769403fba09b52d; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-06T14:48:58+00:00 — Repaired both queued_operation_record citations to its extracted owner at `c69d5171187fa1957025e393270db9f5a864ab14` after proving identical function AST; broader changed coordinator behavior remains for its source-card review. Prior verification stamps and all earlier history are preserved.


- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for fbc89847233b1c5959f56475f2cb51f936d5ef0b (CCR-R03@v1/L03): recorded the claim/queued-record dependency binding and the launch-time dependency re-requirement; prior claim, cancellation, and detached-launch prose preserved.

- 2026-08-29T16:27+02:00 — Reconciled detached launch with native-pidfd runtime admission and the
  separate lifecycle-owned `Popen` reaping boundary.

- 2026-08-26T16:57+02:00 — Removed direct claimed-door ancestry as cancelled-generation
  authority. Replacement now requires the current exact waiting door plus durable cancellation and
  worker-exit proof; exact candidate and first-ready checks remain claim-owned.
- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.
