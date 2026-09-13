# mcp/src/agents_remember/worktrees/queue/closeout_projection.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/queue/closeout_projection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-11T12:02+02:00 |
| lastVerifiedCommitHash | `9f0309447d6820d90e59279abc84f87f1ccbb3b3` |
| lastVerifiedCommitDate | 2026-09-13T22:28:36+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Closeout queue overview](overview.md)

## Purpose

Builds the exact canonical source census for disposable closeout scheduling projections.

## Code Commentary

### Logic

It captures task, sprint, every live series contract, dependency, priority, readiness, activation,
and door source facts; unreadable sources become bounded problems and invalid-empty output rather
than stale rows. Multiple live series contracts are valid census input. For each live atomic master,
`project_series_activation(contract)` observes that master's own contract-keyed activation record and
contributes only a source fact, optional bounded problem, and candidate-local waiting reasons. The
projection no longer derives a global owner from contract presence or reports a multi-live-series
conflict, and another master's state is never a candidate's reason to wait.

Since the closeout-door cut (commit `fad9808e`) a series contributes its door source fact only when it
has a live door: `_series_source` reads `live_closeout_door(contract)` instead of the removed
`contract.closeout_door` field, and the per-contract ordering weight and the "absent door means no
source" branch were deleted with it. A series with no live door simply contributes no door source.

Since 260831-CCR (commit `99dc249b`) every projected member source fact binds the canonical
task-intent identity of its leaf: `_projection_members` (line 467-607) computes
`task_intent_identity(contract.task_root, leaf)` (line 528), records it as
`source_fact["taskIntent"]` (line 539), and passes it into the member context (line 552). A leaf
whose intent cannot be projected (master resolved, schema unsupported, taxonomy unclassified)
refuses the source with a `task`-kind `ProjectionSourceProblem` carrying the exact error type
and repair action (line 529-538), so the disposable projection never offers a member whose intent is
unknown.

### Conventions

Typed records and refusal payloads remain owned at the narrowest stable boundary. Callers consume
the public function or model instead of re-deriving its lower-level state machine.

### Invariants And Boundaries

- Projection input is rebuilt from current canonical sources; missing/invalid sources empty the projection; no lifecycle or commit history is retained here.
- Activation is an observed scheduling input, not queue-owned selection. Reconciling is the only
  candidate waiting reason — vacant and active are never waits, and a foreign master is never this
  candidate's blocker; queue recomputation cannot publish or release the selector.
- Multiple live series contracts are normal and must not become a source problem by census alone.
- Waiting-door admission is unbounded in population: since 260913-LCA-L6 the census no longer appends a problem when more generations wait than a constant allowed, so any number of waiting doors rebuilds. A waiting set whose door generation ids or task references repeat still refuses with the bounded `door`/`waiting-door-identity-conflict` problem, the surviving branch of `_require_waiting_door_identities`; the census's own problem payload stays bounded by `MAX_CLOSEOUT_SOURCE_PROBLEMS`.
- Missing, unreadable, ambiguous, or conflicting authority fails loudly; this file does not add a
  fallback or compatibility shadow.
- Member source facts always carry the exact current task-intent identity or an explicit typed
  refusal; queue rows never synthesize a digest.

### Todos

None recorded.

## Docs References

The configured Domain Documentation registry is empty. No external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain source is required to establish this repository-owned implementation. | `_PRIORITY_RANK` | mcp/src/agents_remember/worktrees/queue/closeout_projection.py:65-65 |

## Repo-Internal References

The source file is the direct evidence for this unit; its governing overview records adjacent owners.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's concrete API, control flow, and validation boundary are implemented here. | `_PRIORITY_RANK` | mcp/src/agents_remember/worktrees/queue/closeout_projection.py:65-65 |
| Every live series is observed independently from its own contract-keyed record; `_projection_members` supplies each member the already-derived v2 topology fingerprint, while activation waiting remains candidate-local. | `_projection_members`; `_observe_series_activation` | mcp/src/agents_remember/worktrees/queue/closeout_projection.py:467-607; mcp/src/agents_remember/worktrees/queue/closeout_projection.py:637-649 |
| Member source facts bind the canonical task-intent identity. | "intent = task_intent_identity(contract.task_root, leaf)"; "source_fact[\"taskIntent\"]" | mcp/src/agents_remember/worktrees/queue/closeout_projection.py:526-551 |
| The focused adapter converts strict per-contract selector observation into disposable source facts/waits/problems without lifecycle ownership. | `project_series_activation` | mcp/src/agents_remember/worktrees/queue/closeout_projection_activation.py:29-51 |
| Waiting-door admission refuses only an identity conflict (a repeated generation id or task reference); no population ceiling remains. | `_require_waiting_door_identities`; "waiting-door-identity-conflict" | mcp/src/agents_remember/worktrees/queue/closeout_projection.py:439-454 |

## Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository reference applies. | `_PRIORITY_RANK` | mcp/src/agents_remember/worktrees/queue/closeout_projection.py:65-65 |

## CCR-R02@v2 Intent-Bound Projection Sources

Per `requirements/CCR-R02-v2-normative-task-intent-identity.md`, projection membership is
intent-bound: every member exposes the exact canonical intent digest of its leaf, so the disposable
queue cannot recompute a stale identity or offer a member whose intent is absent. Part of the landed
L25 candidate `99dc249b`.

## Update History
- 2026-09-13T22:22+02:00 — L6 (260913-LCA): the census no longer refuses a wait set that exceeds a candidate ceiling. The `len(waiting) > MAX_CLOSEOUT_CANDIDATES` branch and its `waiting-door-cap-exceeded` problem are deleted while the identity-conflict branch of `_require_waiting_door_identities` is kept, so the invariant notes the unbounded population and the surviving refusal, and a reference row records that branch at 439-454. Source is a read-only uncommitted change set; verification metadata remains closeout-owned and no stamp advanced.
- 2026-09-13T14:19+02:00 — Per-contract activation curation: the census now calls `project_series_activation(contract)` for each live atomic master against that master's own contract-keyed record, so the card states that reconciling is the only candidate waiting reason (vacant/active are never waits and a foreign master is never a blocker). Rebound the `_projection_members` range to 467-607, the focused adapter to closeout_projection_activation.py:29-51, and re-read the task-intent prose line numbers (467-607 / 528 / 539 / 552 / 529-538). Verification metadata remains closeout-owned; no acceptance claim.
- 2026-09-11T23:05:00+00:00: The member-source-facts row anchored the bare symbol `task_intent_identity`, which resolved twice at verification and again now (the import and the call), and its second anchor `source_fact["taskIntent"]` was a backticked expression the anchor grammar cannot read. Both are now exact quoted source texts — the identity call and the `taskIntent` assignment — each occurring once inside `closeout_projection.py:526-551`; claim wording and extent unchanged.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `_PRIORITY_RANK` repointed to mcp/src/agents_remember/worktrees/queue/closeout_projection.py:65-65. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `_PRIORITY_RANK` repointed to mcp/src/agents_remember/worktrees/queue/closeout_projection.py:65-65. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `_PRIORITY_RANK` repointed to mcp/src/agents_remember/worktrees/queue/closeout_projection.py:65-65. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-11T12:02+02:00 — Closeout-door cut reconciliation at code commit `fad9808e`: recorded that a series contributes its door source fact through `live_closeout_door(contract)` rather than the removed `contract.closeout_door` field, and that the per-contract ordering weight and absent-door branch were deleted. Verification metadata remains pinned because only the cut-affected claim was reconciled; source documentation only, no acceptance claim.
- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for 99dc249bd507 (CCR-R02@v2/L25):
  the closeout projection now binds each member source fact to the leaf's canonical task-intent
  identity and refuses sources whose intent cannot be projected. Verified at code commit
  99dc249bd507c20b09ece1169c2b1fa2af8e8c1b.

- 2026-09-01T03:58+02:00 — 260831-CCR-L01 Attempt 8: re-read the reopened member-projection
  claim and documented its exact precomputed `semantic-topology/v2` identity input. Projection
  currentness now separates completion readiness from semantic topology; verification remains
  closeout-owned.

- 2026-08-26T08:30+02:00 — Rebounded the activation-projection adapter citation to the frozen
  focused module extent.

- 2026-08-26T03:37+02:00 — Removed global live-series owner/conflict inference and documented
  candidate-local activation observation for every live master. Queue remains a disposable observer
  with no selector or lifecycle evidence. Verification remains post-Dagger/closeout-owned.

- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.
