# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_projection.py

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Purely projects one retained lifecycle operation generation for public status consumers.

## Code Commentary

### Logic

Historical closeout and integration take the audit branch before any current intent or control classification. It retains the saved identity, failure and outcome after dropping embedded next-action fields. Recommendations, guidance and legal controls are absent. The live direct branch reads its result and applicable evidence, binds the recommendation and controls to the same record, and derives timestamps from that record.

The direct status branch requires canonical `TaskIntentIdentity` to advertise legal controls. Otherwise it supplies `lifecycle-operation-task-intent-unavailable` with the model's bounded guidance, even when the control handler itself can admit the direct input's canonical leaf binding. The application-level status witness used a stored canonical intent stamp for that reason.

`_operation_cancellable` derives the flag from a present contract, available intent and an exact `cancel` control. A compatible direct `termination-required` record can expose cancellation through the direct control predicate.

Malformed or non-mapping public result evidence becomes the bounded `incoherent` envelope with expected/observed facts, no legal controls, no recommended action and `cancellable: false`; it is not a reusable operation result or an unhandled assertion. The canonical task intent is exposed only when present. The projector binds this outcome in `_incoherent_operation_projection`.

### Conventions

Typed records and refusal payloads remain owned at the narrowest stable boundary. Callers consume
the public function or model instead of re-deriving its lower-level state machine.

#### Invariants And Boundaries

- Projection is read-only and cannot repair or advance state; ambiguous or stale inputs remain visible rather than being normalized away.
- Missing, unreadable, ambiguous, or conflicting authority fails loudly; this file does not add a
  fallback or compatibility shadow.
- A direct record with missing task intent exposes the unavailable state and no legal controls. Older closeout and integration keep the separate audit projection.

### Todos

None recorded.

## Evidence

### Docs References

No external Domain Documentation source is configured for this slice. The current behavior is repository-owned and is supported by the source references below.

No configured external source applies.

### Repo-Internal References

The following current source boundaries establish the ledger-retirement behavior.


- The live direct route projects its saved result and current action. Retained closeout and integration rows expose historical result and evidence for inspection. [1]

- `_recommended_control` selects an already projected legal action. [2]

The source file is the direct evidence for this unit; its governing overview records adjacent owners.

- The unavailable override explains missing intent. The cancellable flag requires available intent, a present contract and an exact cancel control. [3]

- An eligible direct termination-required row may offer exact cancel, derived from the direct control predicate. [4]


- The wire now carries the canonical intent identity when present. (`_coherent_operation_projection`; `_incoherent_operation_projection`) [5]


### Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

No additional cross-repository evidence applies.

## Historical CCR-R02@v2 legacy intent projection barrier

Before ordinary journal execution was retired, per `requirements/CCR-R02-v2-normative-task-intent-identity.md` and the L25 repair (commit
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

## Recommendation and authority

`_recommended_action` checks preferred actions in the controls already projected for the exact record. A recommendation carries no additional control authority.
