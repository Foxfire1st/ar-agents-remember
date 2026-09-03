# mcp/src/agents_remember/worktrees/integration/closeout/door_source.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/closeout/door_source.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `fbc89847233b1c5959f56475f2cb51f936d5ef0b` |
| lastVerifiedCommitDate | 2026-09-02T07:47:04+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Closeout integration overview](overview.md)

## Purpose

Reconstructs and validates the canonical closeout-door source used for scheduling and recovery.

## Code Commentary

### Logic

It resolves task and series identities, validates waiting publication evidence and candidate bindings,
and returns typed source/refusal facts without borrowing lifecycle authority from the queue. When a
sprint has a graph, `door_task_context` passes the already resolved authored graph into the shared
graph context and returns its bound immutable sprint snapshot, preventing the door from combining
topology facts from different graph resolutions.

Under CCR-R03@v1 `_declare_generation` builds the `closeout-door/v1` dependency
declaration from the exact candidate tree, memory candidate tree, task-topology fingerprint,
digest-bearing task intent, and the review/memory/ledger/admission/scheduling provenance
records, and includes it in the door generation identity; policy-owned admission/scheduling
provenance resolution moved into `_door_policy_provenance`.
`_transitioned_generation` re-requires the current generation declared dependencies
before defer/resume/withdraw transitions and projects the refusal as a typed
`CloseoutQueueError`.
cit:([`_transitioned_generation`], mcp/src/agents_remember/worktrees/integration/closeout/door_source.py:309-342)).

### Conventions

Typed records and refusal payloads remain owned at the narrowest stable boundary. Callers consume
the public function or model instead of re-deriving its lower-level state machine. Door dependency
declarations are computed through the shared `closeout_door_dependencies` builder so source and
currentness agree byte-for-byte.

### Invariants And Boundaries

- A door source must match exact task, contract, candidate, and generation identity; stale or missing publication never becomes an inferred waiting candidate.
- Graph-backed door facts use the same one-time bound graph generation as queue and coherence reads.
- Missing, unreadable, ambiguous, or conflicting authority fails loudly; this file does not add a
  fallback or compatibility shadow.
- Every declared transition first re-proves the generation's dependency declaration; a missing or
  stale declaration blocks defer/resume/withdraw with the exact typed refusal.

### Todos

None recorded.

## Docs References

The configured Domain Documentation registry is empty. No external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain source is required to establish this repository-owned implementation. | `DoorSourceContext` | mcp/src/agents_remember/worktrees/integration/closeout/door_source.py:1-490 |

## Repo-Internal References

The source file is the direct evidence for this unit; its governing overview records adjacent owners.

| Finding | Anchor | Source |
| --- | --- | --- |
| The door context binds an authored graph once and returns the sprint carrying that immutable graph generation. | `door_task_context`; `DoorSourceContext` | mcp/src/agents_remember/worktrees/integration/closeout/door_source.py:49-83 |
| Generation declaration includes the R03 dependency set and policy provenance resolution. | `_declare_generation`; `_door_policy_provenance` | mcp/src/agents_remember/worktrees/integration/closeout/door_source.py:381-482; mcp/src/agents_remember/worktrees/integration/closeout/door_source.py:483-513 |
| Transitions re-require the declared dependencies. | `_transitioned_generation` | mcp/src/agents_remember/worktrees/integration/closeout/door_source.py:309-342 |

## Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository reference applies. | `DoorSourceContext` | mcp/src/agents_remember/worktrees/integration/closeout/door_source.py:1-490 |

## 260831-CCR-R03 Dependency-Declared Door Source

Door source generations now carry the `closeout-door/v1` declaration and transitions fail closed on
dependency staleness (worker handover: notes/reports/260902-CCR-L03-worker-delivery.md).

## Update History

- 2026-09-03T17:35+02:00 - 260831-CCR-L27 Gate-5 memory pass (src-a): rewrote the Code Commentary cit forms as plain prose and fixed the `_door_policy_provenance` range to 483-513 (the file ends at 550).

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for fbc89847233b1c5959f56475f2cb51f936d5ef0b (CCR-R03@v1/L03): recorded the source-generation dependency declaration, the provenance-resolution refactor, and the transition dependency re-requirement; prior graph-binding and identity prose preserved.

- 2026-09-01T03:58+02:00 — 260831-CCR-L01 Attempt 8: graph-backed door reconstruction now binds
  the caller-resolved authored graph once and carries the immutable sprint graph into all source
  facts. Verification remains closeout-owned.

- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.
