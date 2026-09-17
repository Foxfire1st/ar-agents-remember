# mcp/src/agents_remember/worktrees/integration/closeout/door_source.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/closeout/door_source.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T00:53 |
| lastVerifiedCommitHash | `420669c459aab3650cdaa5b3e5271e71d7d94c0e` |
| lastVerifiedCommitDate | 2026-09-17T10:54:08+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No external Domain Documentation source is configured for this slice. The current behavior is repository-owned and is supported by the source references below.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external source applies. | — | — |

## Repo-Internal References

The following current source boundaries establish the ledger-retirement behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| `_declare_generation` constructs a door from content, task, and policy evidence without cached ledger inputs. | `_declare_generation` | mcp/src/agents_remember/worktrees/integration/closeout/door_source.py:381-388 |
| `_door_policy_provenance` resolves admission and scheduling provenance for the declared door. | `_door_policy_provenance` | mcp/src/agents_remember/worktrees/integration/closeout/door_source.py:478-483 |

The source file is the direct evidence for this unit; its governing overview records adjacent owners.

| Finding | Anchor | Source |
| --- | --- | --- |
| The door context binds an authored graph once and returns the sprint carrying that immutable graph generation. (`door_task_context`; `DoorSourceContext`) | `door_task_context` | mcp/src/agents_remember/worktrees/integration/closeout/door_source.py:65-69 |
| Generation declaration includes the R03 dependency set and policy provenance resolution. (`_declare_generation`; `_door_policy_provenance`) | `_declare_generation` | mcp/src/agents_remember/worktrees/integration/closeout/door_source.py:381-388 |
| Transitions re-require the declared dependencies. (`_transitioned_generation`) | `_transitioned_generation` | mcp/src/agents_remember/worktrees/integration/closeout/door_source.py:309-312 |

## Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No additional cross-repository evidence applies. | — | — |

## 260831-CCR-R03 Dependency-Declared Door Source

Door source generations now carry the `closeout-door/v1` declaration and transitions fail closed on
dependency staleness (worker handover: notes/reports/260902-CCR-L03-worker-delivery.md).

## Update History

- 2026-09-15T00:53 UTC — LCA-L9 working-candidate curation: retired ledger Git authority in this file-specific boundary; preserved real Git and lifecycle safeguards and prior history. Source and diff reviewed, source-sha256=065fc3216acbe69bb13098d722227517fb6d0e08463342c5c7619234b480c34f. Existing verification commit/date remain unchanged until an actual source commit is available; no test or acceptance claim.


- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the door is read live
  through `live_closeout_door` and a new `_live_task_document_ref` was added. Re-read the card: its
  source-of-truth prose is untouched and its three cited ranges still contain their constructs. No
  wording changed. Verification metadata remains closeout-owned.
- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification):
  `mcp/src/agents_remember/worktrees/integration/closeout/door_source.py` changed since the recorded
  verification commit. Re-read the card against the frozen on-disk source and re-checked its claims
  and cited ranges: nothing this card asserts is falsified by the change, so no wording changed.
  Verification metadata remains closeout-owned; no verification stamp advanced.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the source moved since
  the recorded verification commit (the door is now read live through `live_closeout_door`). Re-read
  the card: its claims stay consistent and its three cited ranges still cover their constructs. No
  wording changed; verification metadata remains closeout-owned.
- 2026-09-03T17:35+02:00 - 260831-CCR-L27 Gate-5 memory pass (src-a): rewrote the Code Commentary cit forms as plain prose and fixed the `_door_policy_provenance` range to 483-513 (the file ends at 550).

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for fbc89847233b1c5959f56475f2cb51f936d5ef0b (CCR-R03@v1/L03): recorded the source-generation dependency declaration, the provenance-resolution refactor, and the transition dependency re-requirement; prior graph-binding and identity prose preserved.

- 2026-09-01T03:58+02:00 — 260831-CCR-L01 Attempt 8: graph-backed door reconstruction now binds
  the caller-resolved authored graph once and carries the immutable sprint graph into all source
  facts. Verification remains closeout-owned.

- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.
