# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_projection.py

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Purely projects one retained lifecycle operation generation for public status consumers.

## Code Commentary

### Logic

The operation-specific result projection uses initial-door contradictions and direct-landing evidence, with no ledger byte/tree contradiction branch. Cache state does not replace the record-bound result, suppress a legal control, or recommend manual transaction recovery.

It combines the durable record with door, integration, direct, and organizational evidence, parses timestamps, and emits stable result/control-neutral fields.

Current missing-intent classification distinguishes recovery reuse from safe completion of an already requested cancellation. Missing canonical task intent cannot authorize retry or recovery. The bounded override names `lifecycle-operation-task-intent-unavailable`; terminal generations may retire and republish while active ones require their existing recovery authority or developer decision.

`_operation_cancellable` is record-free: it requires a present contract, no blocking intent flag and an exact `cancel` legal control. It does not reconstruct permission from irreversible-boundary or retained-generation heuristics. `_exit_proven_cancellation_pending` preserves the existing cancellation surface when requested cancellation has proven worker exit. See `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_projection.py:536-576`.

Malformed or non-mapping public result evidence becomes the bounded `incoherent` envelope with expected/observed facts, no legal controls, no recommended action and `cancellable: false`; it is not a reusable operation result or an unhandled assertion. The canonical task intent is exposed only when present. See `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_projection.py:480-517`.

### Conventions

Typed records and refusal payloads remain owned at the narrowest stable boundary. Callers consume
the public function or model instead of re-deriving its lower-level state machine.

#### Invariants And Boundaries

- Projection is read-only and cannot repair or advance state; ambiguous or stale inputs remain visible rather than being normalized away.
- Missing, unreadable, ambiguous, or conflicting authority fails loudly; this file does not add a
  fallback or compatibility shadow.
- A legacy missing-intent closeout/direct-landing generation projects the exact unavailable state
  and never advertises recover/retry/cancel for reuse.

### Todos

None recorded.

## Evidence

### Docs References

No external Domain Documentation source is configured for this slice. The current behavior is repository-owned and is supported by the source references below.

No configured external source applies.

### Repo-Internal References

The following current source boundaries establish the ledger-retirement behavior.

- `_operation_specific_projected_result` projects initial-door and direct-landing evidence without ledger decisions. [1]
- `_recommended_control` orders legal recommended controls without creating new authority. [2]

The source file is the direct evidence for this unit; its governing overview records adjacent owners.

- Missing-intent blocking, the public unavailable override, and cancellability. (`legacy_intent_blocks_recovery`; `_legacy_intent_override`; `_operation_cancellable`) [3]
- Exit-proven cancellation-pending state keeps its cancel surface. (`_exit_proven_cancellation_pending`; `_general_projected_result`) [4]
- The wire now carries the canonical intent identity when present. (`_coherent_operation_projection`; `_incoherent_operation_projection`) [5]

### Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

No additional cross-repository evidence applies.

## CCR-R02@v2 Legacy Intent Projection Barrier

Per `requirements/CCR-R02-v2-normative-task-intent-identity.md` and the L25 repair (commit
`99dc249b`), a closeout or direct-landing generation whose task-intent state is absence can no
longer project as an ordinary reusable generation merely because it is nonterminal; the public
projection reports `lifecycle-operation-task-intent-unavailable` with `retire-and-republish` and
wholly omits recover/retry/cancel except for the proven same-generation cancellation-pending path.


## 260831-CCR-L15 Meaningful Revision Propagation

Both envelope builders — the coherent adapter and the incoherent refusal adapter — now populate
`LifecycleOperationProjection.meaningfulRevision` from the exact durable record, so every
record-bound status snapshot (including a wait snapshot) carries the durable meaningful-state
cursor of the journal revision it projects.

- Coherent envelope carries the record cursor. (`_coherent_operation_projection`) [6]
- Incoherent refusal envelope carries the record cursor too. (`_incoherent_operation_projection`) [7]
- The envelope field being populated. (`meaningfulRevision`) [8]

## CCR-L42 current candidate

Recommended-control ordering now prefers `resume` before `recover` and `retry` when the public legal controls allow it; the projection remains record-bound and does not authorize a control by recommendation alone.
