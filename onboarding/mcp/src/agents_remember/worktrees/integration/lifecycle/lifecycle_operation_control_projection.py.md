# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_control_projection.py

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Derives public legal controls from durable lifecycle, door, repair, and integration evidence.

## Code Commentary

### Logic

Legal recovery controls consult initial-door and direct-landing evidence without a ledger-recovery classifier. Resume arguments contain code/memory messages, integration arguments contain no ledger subject, and a direct successor requests only its memory-content message. Cache absence or stale bytes therefore create no projected decision gate.

It builds a context from the canonical record and contract, classifies recovery needs, and returns exact resume/retry/cancel/cleanup controls and arguments without mutation.

Since 260831-CCR (commit `99dc249b`) the recovery/retry controls of a legacy missing-intent
closeout or direct-landing generation are withheld: `_without_legacy_generation_reuse`  filters out every `recover`/`retry` control when the record is a
closeout/direct-landing operation whose `taskIntent` is not a `TaskIntentIdentity`
(`isinstance(record.taskIntent, TaskIntentIdentity)`, line 127-128). The filter is applied at
every return of `legal_operation_controls` , so public control projection never
advertises recovery of a generation whose intent is absent. The intended exit-proven
cancellation-pending state keeps its `cancel` control (that is not a reuse action).

### Conventions

Typed records and refusal payloads remain owned at the narrowest stable boundary. Callers consume
the public function or model instead of re-deriving its lower-level state machine.

#### Invariants And Boundaries

- Controls are projections of current durable evidence; unavailable actions stay absent and no control may imply a transition the journal cannot validate.
- Missing, unreadable, ambiguous, or conflicting authority fails loudly; this file does not add a
  fallback or compatibility shadow.
- A legacy missing-intent closeout/direct-landing generation never projects `recover`/`retry`;
  only terminal retire/republish routes remain reachable through other seams.

### Todos

None recorded.

## Evidence

### Docs References

No external Domain Documentation source is configured for this slice. The current behavior is repository-owned and is supported by the source references below.

No configured external source applies.

### Repo-Internal References

The following current source boundaries establish the ledger-retirement behavior.

- `_recovery_evidence_controls` uses initial-door and direct-landing evidence without a ledger-recovery classifier. [1]
- `_resume_control` requests fresh messages for enabled code and memory legs. [2]
- `_integration_control` constructs integration arguments with no ledger commit subject. [3]
- `_direct_successor_control` constructs a direct successor from code identity and the memory-content message. [4]

The source file is the direct evidence for this unit; its governing overview records adjacent owners.

- Missing-intent closeout/direct-landing recovery and retry controls are withheld. (`_without_legacy_generation_reuse`) [5]

### Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

No additional cross-repository evidence applies.

## CCR-R02@v2 Missing-Intent Control Barrier

Per `requirements/CCR-R02-v2-normative-task-intent-identity.md`, legacy absence cannot authorize
recovery; the L25 repair (commit `99dc249b`) removes `recover`/`retry` from the public legal
controls of every missing-intent closeout/direct-landing path while preserving the exit-proven
cancellation route.

## CCR-R18@v1 Exact Same-Generation Cancellation Cell

260831-CCR-L18 added an explicit `termination-required` branch in `legal_operation_controls`: a record whose status is `termination-required` projects exactly one `cancel` control (“Complete exact same-generation cancellation.”) instead of falling into the generic worker-exit-unproven retry path. The state matrix reserves that cell for `cancel` only, and the exit-proven cancelled state keeps its same-generation cancel behavior unchanged.

## CCR-L42 current candidate

Public controls now use `resume` for a closeout successor: recovery-required closeouts offer resume, failed or input-required closeouts expose resume before cancel when eligible, and cancelled closeouts expose resume. Non-closeout recovery and direct-landing successor semantics remain independent; no revise alias is introduced.
