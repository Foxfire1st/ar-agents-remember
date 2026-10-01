# mcp/src/agents_remember/worktrees/integration/closeout/door_source.py

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Reconstructs and validates the canonical closeout-door source used for scheduling and recovery.

## Code Commentary

### Logic

Generation declaration binds code and memory trees plus task and policy provenance. The derived ledger is absent from both the dependency declaration and generation fingerprint; changing cache bytes does not declare a new candidate or stale the waiting door.

It resolves task and series identities, validates waiting publication evidence and candidate bindings,
and returns typed source/refusal facts without borrowing lifecycle authority from the queue. When a
sprint has a graph, `door_task_context` passes the already resolved authored graph into the shared
graph context and returns its bound immutable sprint snapshot, preventing the door from combining
topology facts from different graph resolutions.

Under CCR-R03@v1 `_declare_generation` builds the `closeout-door/v1` dependency
declaration from the exact candidate tree, memory candidate tree, task-topology fingerprint,
digest-bearing task intent, and the review/memory/admission/scheduling provenance
records, and includes it in the door generation identity; policy-owned admission/scheduling
provenance resolution moved into `_door_policy_provenance`.
`_transitioned_generation` re-requires the current generation declared dependencies
before defer/resume/withdraw transitions and projects the refusal as a typed
`CloseoutQueueError`.
cit:([`_transitioned_generation`], mcp/src/agents_remember/worktrees/integration/closeout/door_source.py:309-340)).

### Conventions

Typed records and refusal payloads remain owned at the narrowest stable boundary. Callers consume
the public function or model instead of re-deriving its lower-level state machine. Door dependency
declarations are computed through the shared `closeout_door_dependencies` builder so source and
currentness agree byte-for-byte.

#### Invariants And Boundaries

- A door source must match exact task, contract, candidate, and generation identity; stale or missing publication never becomes an inferred waiting candidate.
- Graph-backed door facts use the same one-time bound graph generation as queue and coherence reads.
- Missing, unreadable, ambiguous, or conflicting authority fails loudly; this file does not add a
  fallback or compatibility shadow.
- Every declared transition first re-proves the generation's dependency declaration; a missing or
  stale declaration blocks defer/resume/withdraw with the exact typed refusal.

### Todos

None recorded.

## Evidence

### Docs References

No external Domain Documentation source is configured for this slice. The current behavior is repository-owned and is supported by the source references below.

No configured external source applies.

### Repo-Internal References

The following current source boundaries establish the ledger-retirement behavior.

- `_declare_generation` constructs a door from content, task, and policy evidence without cached ledger inputs. [1]
- `_door_policy_provenance` resolves admission and scheduling provenance for the declared door. [2]

The source file is the direct evidence for this unit; its governing overview records adjacent owners.

- The door context binds an authored graph once and returns the sprint carrying that immutable graph generation. (`door_task_context`; `DoorSourceContext`) [3]
- Generation declaration includes the R03 dependency set and policy provenance resolution. (`_declare_generation`; `_door_policy_provenance`) [4]
- Transitions re-require the declared dependencies. (`_transitioned_generation`) [5]

### Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

No additional cross-repository evidence applies.

## 260831-CCR-R03 Dependency-Declared Door Source

Door source generations now carry the `closeout-door/v1` declaration and transitions fail closed on
dependency staleness (worker handover: notes/reports/260902-CCR-L03-worker-delivery.md).
