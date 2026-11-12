# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_control_projection.py

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Derives public legal controls from durable lifecycle, door, repair, and integration evidence.

## Code Commentary

### Logic

Legal recovery controls consult initial-door and direct-landing evidence without a ledger-recovery classifier. Resume arguments contain code/memory messages, integration arguments contain no ledger subject, and a direct successor requests only its memory-content message. Cache absence or stale bytes therefore create no projected decision gate.

It builds a context from the canonical record and contract, classifies recovery needs, and returns exact resume/retry/cancel/cleanup controls and arguments without mutation.

The legacy reuse filter withholds recover/retry for closeout/direct-landing generations missing compatible taskIntent only when no admitted direct input leaf binding supplies the replacement. _without_legacy_generation_reuse preserves doorless direct controls when _direct_generation_bound finds DirectLandingOperationInput.leafTaskDocumentRef. Missing both bindings retains the barrier; genuine ref/input/history contradictions and developer decisions are not bypassed. Cancellation controls remain separate. Any readable direct record carrying a door publication returns no controls before other branches. Completed direct disposition uses the same completed_direct_owner predicate as admission: only authorized, unintegrated, worker-exited ownership with an idle integration claim may retire; exact retired ownership re-offers retire idempotently. Direct supersede is never offered and its refusal names a new direct_landing request. The existing cancelled-generation successor is a separate boundary.

### Conventions

Typed records and refusal payloads remain owned at the narrowest stable boundary. Callers consume
the public function or model instead of re-deriving its lower-level state machine.

#### Invariants And Boundaries

- Controls are projections of current durable evidence; unavailable actions stay absent and no control may imply a transition the journal cannot validate.
- Missing, unreadable, ambiguous, or conflicting authority fails loudly; this file does not add a
  fallback or compatibility shadow.
- Missing-intent closeouts and legacy direct generations without admitted leaf input withhold recover/retry. Current canonical-leaf-bound doorless direct generations keep their real controls; earlier door-bearing direct records offer none.

### Todos

None recorded.

## Direct-create recovery controls

Direct-create recoverability is classified from persisted same-generation code/ref/memory evidence. A mechanically recoverable cut advertises public recovery; real contradictions keep developer-decision. Controls are a projection of current evidence, not permission to bypass the mutation owner.

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


- Missing compatible taskIntent withholds legacy reuse only when admitted direct leaf input is also absent; direct canonical-leaf binding preserves controls. [5]


### Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

No additional cross-repository evidence applies.

## CCR-R02@v2 Missing-Intent Control Barrier

Per the ordinary CCR intent boundary, legacy absence alone cannot authorize reuse. The MIK-R94 direct exception binds leafTaskDocumentRef on accepted input; only generations missing both compatible intent and that direct binding lose recover/retry. Exit-proven cancellation and genuinely ambiguous-generation decisions remain.

## CCR-R18@v1 Exact Same-Generation Cancellation Cell

260831-CCR-L18 added an explicit `termination-required` branch in `legal_operation_controls`: a record whose status is `termination-required` projects exactly one `cancel` control (“Complete exact same-generation cancellation.”) instead of falling into the generic worker-exit-unproven retry path. The state matrix reserves that cell for `cancel` only, and the exit-proven cancelled state keeps its same-generation cancel behavior unchanged.

## CCR-L42 current candidate

Public controls now use `resume` for a closeout successor: recovery-required closeouts offer resume, failed or input-required closeouts expose resume before cancel when eligible, and cancelled closeouts expose resume. Non-closeout recovery and direct-landing successor semantics remain independent; no revise alias is introduced.


- Direct-landing recoverability is classified from the persisted generation's typed accepted input, exact code commit/tree, memory repository/ref and accepted or intended live memory evidence. [6]


- Exact completed direct owners are offered retire subject to disposition eligibility; direct supersede is unavailable. [7]
- Earlier door-bearing direct records remain readable but offer no controls. [8]
