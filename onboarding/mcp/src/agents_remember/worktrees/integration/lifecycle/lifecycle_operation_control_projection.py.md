# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_control_projection.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_control_projection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T10:05+02:00|
| lastVerifiedCommitHash | `3b552f5a215648274dc5e6e4d5f0a01c2ee80be2` |
| lastVerifiedCommitDate | 2026-09-12T01:54:48+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Lifecycle operation integration overview](overview.md)

## Purpose

Derives public legal controls from durable lifecycle, door, repair, and integration evidence.

## Code Commentary

### Logic

It builds a context from the canonical record and contract, classifies recovery needs, and returns exact resume/retry/cancel/cleanup controls and arguments without mutation.

Since 260831-CCR (commit `99dc249b`) the recovery/retry controls of a legacy missing-intent
closeout or direct-landing generation are withheld: `_without_legacy_generation_reuse` (line
123-130) filters out every `recover`/`retry` control when the record is a
closeout/direct-landing operation whose `taskIntent` is not a `TaskIntentIdentity`
(`isinstance(record.taskIntent, TaskIntentIdentity)`, line 127-128). The filter is applied at
every return of `legal_operation_controls` (lines 83, 94, 120), so public control projection never
advertises recovery of a generation whose intent is absent. The intended exit-proven
cancellation-pending state keeps its `cancel` control (that is not a reuse action).

### Conventions

Typed records and refusal payloads remain owned at the narrowest stable boundary. Callers consume
the public function or model instead of re-deriving its lower-level state machine.

### Invariants And Boundaries

- Controls are projections of current durable evidence; unavailable actions stay absent and no control may imply a transition the journal cannot validate.
- Missing, unreadable, ambiguous, or conflicting authority fails loudly; this file does not add a
  fallback or compatibility shadow.
- A legacy missing-intent closeout/direct-landing generation never projects `recover`/`retry`;
  only terminal retire/republish routes remain reachable through other seams.

### Todos

None recorded.

## Docs References

The configured Domain Documentation registry is empty. No external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain source is required to establish this repository-owned implementation. | `LifecycleControlProjectionContext` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_control_projection.py:1-594 |

## Repo-Internal References

The source file is the direct evidence for this unit; its governing overview records adjacent owners.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's concrete API, control flow, and validation boundary are implemented here. | `LifecycleControlProjectionContext` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_control_projection.py:1-594 |
| Missing-intent closeout/direct-landing recovery and retry controls are withheld. | `_without_legacy_generation_reuse` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_control_projection.py:117-125 |

## Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository reference applies. | `LifecycleControlProjectionContext` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_control_projection.py:1-594 |

## CCR-R02@v2 Missing-Intent Control Barrier

Per `requirements/CCR-R02-v2-normative-task-intent-identity.md`, legacy absence cannot authorize
recovery; the L25 repair (commit `99dc249b`) removes `recover`/`retry` from the public legal
controls of every missing-intent closeout/direct-landing path while preserving the exit-proven
cancellation route.

## CCR-R18@v1 Exact Same-Generation Cancellation Cell

260831-CCR-L18 added an explicit `termination-required` branch in `legal_operation_controls` (line 98): a record whose status is `termination-required` projects exactly one `cancel` control (“Complete exact same-generation cancellation.”) instead of falling into the generic worker-exit-unproven retry path. The state matrix reserves that cell for `cancel` only, and the exit-proven cancelled state keeps its same-generation cancel behavior unchanged.

## CCR-L42 current candidate

Public controls now use `resume` for a closeout successor: recovery-required closeouts offer resume, failed or input-required closeouts expose resume before cancel when eligible, and cancelled closeouts expose resume. Non-closeout recovery and direct-landing successor semantics remain independent; no revise alias is introduced.

## Update History
- 2026-09-11T22:39:01+00:00: Generated citation repair: `_without_legacy_generation_reuse` repointed to mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_control_projection.py:117-125. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T00:20:36+02:00 — CCR-L42 current candidate reconciliation: Public controls now use `resume` for a closeout successor: recovery-required closeouts offer resume, failed or input-required closeouts expose resume before cancel when eligible, and cancelled closeouts expose resume. Non-closeout recovery and direct-landing successor semantics remain independent; no revise alias is introduced.

- 2026-09-04T10:05+02:00 — 260831-CCR-L18 Gate-5 memory pass: recorded the explicit `termination-required` → exact same-generation cancel control cell. Verified at code commit f93ac631ca161e5880db3a937728cb256686b13b.

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for 99dc249bd507 (CCR-R02@v2/L25):
  public legal controls now withhold `recover`/`retry` for legacy missing-intent
  closeout/direct-landing generations (`_without_legacy_generation_reuse`); documented the
  barrier and the preserved cancel path. Verified at code commit 99dc249bd507c20b09ece1169c2b1fa2af8e8c1b.

- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.
