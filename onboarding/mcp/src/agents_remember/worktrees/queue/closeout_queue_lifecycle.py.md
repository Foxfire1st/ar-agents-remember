# mcp/src/agents_remember/worktrees/queue/closeout_queue_lifecycle.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/queue/closeout_queue_lifecycle.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-23T16:08+02:00 |
| lastVerifiedCommitHash | `1d446724d099517f6f52d596b47827ae2391a2a4` |
| lastVerifiedCommitDate | 2026-08-24T00:21:10+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[governing route overview](overview.md)

## Purpose

Owns the transitional pre-L3 queue transitions that bind a selected candidate to closeout
claim/certification, plus short queue/repository serialization used by atomic-series terminal
guards. L2 removed the former integration claim/consume and broad task-publication lifecycle
surface, but the remaining candidate states, owner fingerprint, and exact closeout commit fields
are still lifecycle-shaped queue data pending L3 removal.

## Code Commentary

### Logic

The service resolves the sprint/candidate queue binding from current topology, claims a selected
candidate for closeout, and certifies it only when exact commits and the contract-owned claimed
door agree. Conflict resolution retires one stale certified projection and publishes the exact
reset contract. The transitional row persists a one-way owner fingerprint and exact contract
closeout commits; L2 no longer treats those duplicated facts as authority for operation recovery,
worker state, cancellation, revision, or integration publication. Atomic-series terminal guards
still use short queue/repository serialization.

The atomic-series terminal publication gate resolves the **effective** execution nature
(`scheduling_mode.effective_execution_nature`) instead of the declared cell: a nature-less legacy
master executes atomically under the atomic-sequential default, while a graph-less sprint has no
queue authority to release. CLIVE L2 removes the former queue-owned integration claim/completion
and stale-sibling return seams from this module; integration now transfers once into the root
journal. Closeout claim/certification and atomic terminal serialization remain transitional until
L3.

### Conventions

Legacy absence is accepted only when no durable queue binding or state has ever existed. Once bound,
missing/damaged topology or state fails closed.

### Invariants And Boundaries

- The graph is recomputed while the queue lock is held for every claim/certify/final transition.
- Closeout certification requires the exact candidate commits and claimed door generation.
- Operation cancellation/recovery/revision, worker termination, and integration publication are
  journal-owned L2 seams outside this module. The remaining owner/commit fields here are
  transitional pre-L3 duplicates, not recovery authority.
- A stale certified projection is retired only through the explicit conflict-resolution
  transaction and exact reset-contract evidence.
- Atomic-nature gates read the effective nature: the atomic-sequential default resolves a
  nature-less master to atomic, and a graph-less sprint carries no queue authority to release.
- Atomic-series terminal mutation receives an ephemeral permit only while the sprint queue and
  repository authority are both held. The permit is bound to the exact operation, canonical
  contract path, issuing thread, active `ContextVar`, and issuer-owned live registry; normal exit,
  exceptional exit, copied contexts, and cross-thread replay all fail closed.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Closeout claim correlates the selected projection with the journal owner without copying lifecycle evidence. | `claim_queue_candidate_for_closeout` | mcp/src/agents_remember/worktrees/queue/closeout_queue_lifecycle.py:389-403 |
| Closeout certification is one explicit projection transition. | `certify_queue_candidate_closeout` | mcp/src/agents_remember/worktrees/queue/closeout_queue_lifecycle.py:406-422 |
| Conflict resolution retires one stale certified projection and binds the exact reset contract. | `prepare_queue_candidate_conflict_resolution` | mcp/src/agents_remember/worktrees/queue/closeout_queue_lifecycle.py:425-507 |
| Atomic-series terminal publication mints and revokes the exact non-replayable permit under queue/repository authority. | `publish_atomic_series_terminal_under_authority` | mcp/src/agents_remember/worktrees/queue/closeout_queue_lifecycle.py:188-211 |
| Terminal mutation verifies both context-local and issuer-owned permit liveness. | `require_atomic_series_terminal_permit` | mcp/src/agents_remember/worktrees/queue/closeout_queue_lifecycle.py:214-231 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## 260815-DAG-L4 Integration-Authority Impact

L4 makes task-derived integration refs mechanically non-ordinary: repository defaults, sprint supers, and active atomic-series refs are censused across code and external memory. Mutation is admitted only through exact lifecycle authority, named-ref compare-and-swap, queue/repository serialization, or a terminal capability; stale topology, aliases, ambient checkouts, and torn recovery fail closed.

## 260821-CLIVE-L2 Current Contract

The current source seams include `AtomicSeriesTerminalPermit`, `QueueBinding`, `contract_queue_binding`. The module still implements pre-L3 closeout claim/certification and atomic-series queue serialization. L2 removes integration claim/consume and keeps recovery/generation/worker evidence in the root journal; L3 owns deletion of the remaining lifecycle-shaped queue transitions and waiting-only rebuild.

### Reconciled Source Evidence

| Finding | Citations | Source Path |
| --- | --- | --- |
| The current module exposes `AtomicSeriesTerminalPermit`, `QueueBinding`, `contract_queue_binding` at this ownership boundary. | L69-L74; L103-L105; L131-L178 | `mcp/src/agents_remember/worktrees/queue/closeout_queue_lifecycle.py` |

## Update History

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: source moved to `mcp/src/agents_remember/worktrees/queue/closeout_queue_lifecycle.py` (new package route); the citation fixer repointed in-body references; import paths updated inside the module. Verified at code commit e5cb139f.


- 2026-08-19T22:32+02:00 — 260815-DAG-L13: effective-nature gating replaces declared-cell reads at
  the atomic terminal-publication and master-completion seams (nature-less legacy masters retire
  normally; graph-less sprints have no queue authority to release); the integration boundary names
  `recovery: worktree_sync` on stale-base refusals; integration claiming refuses while another
  candidate owns the lane; `complete_queue_candidate_integration` returns stale-by-evidence
  sibling facts; the unused `require_queue_candidate_current` helper was removed. Verification
  remains closeout-owned.

- 2026-08-18T09:10+02:00 — No content impact: renamed the atomic 'barrier' concept to 'blocker' throughout; behavior unchanged. Verification remains closeout-owned.

- 2026-08-17T12:30+02:00 — 260815-DAG-L5: integration completion now persists durable `integration_queue_completion_evidence` before consuming the candidate, and the completion event is emitted through `_integration_completion_event`. Verification remains closeout-owned.

- 2026-08-16T01:30+02:00 — Documented the exact, thread-bound, issuer-revoked atomic-series terminal permit and copied-context replay refusal; verification remains closeout-owned.

- 2026-08-15T23:38+02:00 — Reconciled this worktree owner's role in task-derived protected-ref authority, exact named-ref movement, and crash-safe recovery. Verification metadata remains closeout-owned.

- 2026-08-15T13:08+02:00 — No content impact: Ruff split the aliased lifecycle-owner import from
  the unaliased commit-tree import; both still resolve from one candidate-evidence owner.
- 2026-08-15T12:53+02:00 — No content impact: normalized the split candidate-evidence import;
  lifecycle transition ownership and ordering are unchanged.
- 2026-08-15T09:10+02:00 — Created for L3's task-publication and lifecycle queue seam; verification remains closeout-owned.
