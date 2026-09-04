# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_projection.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_projection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T20:19:44+02:00 |
| lastVerifiedCommitHash | `e375f2ebdc87f6843bc76168b646d606fa79caec` |
| lastVerifiedCommitDate | 2026-09-04T20:19:44+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Lifecycle operation integration overview](overview.md)

## Purpose

Purely projects one retained lifecycle operation generation for public status consumers.

## Code Commentary

### Logic

It combines the durable record with door, integration, direct, and organizational evidence, parses timestamps, and emits stable result/control-neutral fields.

Since 260831-CCR (commit `99dc249b`) the projection distinguishes legacy missing-intent
generations and blocks their recovery reuse:

- `intent_unavailable` (line 67-68) is true for a closeout/direct-landing operation whose
  `taskIntent` is not a `TaskIntentIdentity`; `legacy_intent_blocks_recovery` (line 70-71)
  is true unless the worker exit is unproven or an exit-proven cancellation is pending.
- When recovery is blocked, legal controls are not consulted (`if contract is not None and not
  legacy_intent_blocks_recovery`, line 79) and `_legacy_intent_override` (line 163-181) emits the
  exact public state `lifecycle-operation-task-intent-unavailable` with the summary "The legacy
  operation predates canonical task intent." and `nextAction: retire-and-republish`, plus the
  same failure and guidance strings.
- `_operation_cancellable` (line 185-201) is false for an intent-unavailable generation, so a
  legacy record is neither recoverable, retryable, nor cancellable through projection; only the
  intended exit-proven cancellation-pending state renders its existing `cancel` control unchanged
  (`_general_projected_result`, line 220-243, keeps the "Exact worker exit is proven" surface).
- `operation_projection` also projects `taskIntent` onto the wire when it is a canonical
  identity (line 120-121).

### Conventions

Typed records and refusal payloads remain owned at the narrowest stable boundary. Callers consume
the public function or model instead of re-deriving its lower-level state machine.

### Invariants And Boundaries

- Projection is read-only and cannot repair or advance state; ambiguous or stale inputs remain visible rather than being normalized away.
- Missing, unreadable, ambiguous, or conflicting authority fails loudly; this file does not add a
  fallback or compatibility shadow.
- A legacy missing-intent closeout/direct-landing generation projects the exact unavailable state
  and never advertises recover/retry/cancel for reuse.

### Todos

None recorded.

## Docs References

The configured Domain Documentation registry is empty. No external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain source is required to establish this repository-owned implementation. | `OperationProjectionContext` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_projection.py:1-319 |

## Repo-Internal References

The source file is the direct evidence for this unit; its governing overview records adjacent owners.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's concrete API, control flow, and validation boundary are implemented here. | `OperationProjectionContext` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_projection.py:1-319 |
| Missing-intent blocking, the public unavailable override, and cancellability. | `legacy_intent_blocks_recovery`; `_legacy_intent_override`; `_operation_cancellable` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_projection.py:67-71; mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_projection.py:163-181; mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_projection.py:185-201 |
| Exit-proven cancellation-pending state keeps its cancel surface. | `_exit_proven_cancellation_pending`; `_general_projected_result` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_projection.py:153-160; mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_projection.py:216-251 |
| The wire now carries the canonical intent identity when present. | `taskIntent` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_projection.py:120-121 |

## Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository reference applies. | `OperationProjectionContext` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_projection.py:1-319 |

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

| Finding | Anchor | Source |
| --- | --- | --- |
| Coherent envelope carries the record cursor. | `_coherent_operation_projection` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_projection.py:217-224 |
| Incoherent refusal envelope carries the record cursor too. | `_incoherent_operation_projection` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_projection.py:515-522 |
| The envelope field being populated. | `LifecycleOperationProjection.meaningfulRevision` | mcp/src/agents_remember/models/lifecycles/operation_projection.py:376-380 |

## Update History

- 2026-09-04T20:19:44+02:00 — 260831-CCR-L15 Gate-5 memory pass for e375f2ebdc87f6843bc76168b646d606fa79caec (lifecycle status-change waiting): recorded the adapters' propagation of `meaningfulRevision` from the durable record into coherent and incoherent envelopes.
- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for 99dc249bd507 (CCR-R02@v2/L25):
  the lifecycle operation projection now blocks recovery reuse for legacy missing-intent
  closeout/direct-landing generations, emits the `lifecycle-operation-task-intent-unavailable`
  override, carries `taskIntent` on the wire, and preserves the exit-proven cancellation-pending
  cancel path. Verified at code commit 99dc249bd507c20b09ece1169c2b1fa2af8e8c1b.

- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.
