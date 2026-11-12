# mcp/src/agents_remember/worktrees/queue/closeout_projection.py

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
task-intent identity of its leaf: `_projection_members` (line 461-560) computes
`task_intent_identity(contract.task_root, leaf)` (line 522), records it as
`source_fact["taskIntent"]` (line 533), and passes it into the member context (line 546). A leaf
whose intent cannot be projected (master resolved, schema unsupported, taxonomy unclassified)
refuses the source with a `task`-kind `ProjectionSourceProblem` carrying the exact error type
and repair action (line 523-532), so the disposable projection never offers a member whose intent is
unknown.

Since 260913-LCA-L7 `_problem` classifies a capacity refusal from the code set its own raiser
published instead of from a substring of the code's spelling. The classifier tests membership of
`CAPACITY_REFUSAL_CODES` — the declaration shared with `closeout_queue_errors.py` — so
`closeout-queue-master-capacity-exceeded`, `closeout-queue-edge-capacity-exceeded` and the module's
own `source-problem-cap-exceeded` overflow code all report `invalid`: the source was read and is too
large for its bound. The previous substring test was `cap-exceeded`, which neither surviving capacity
code contains, so a sprint past its graph bound was reported as a source that could not be read. The
change is exactly this: the capacity family classifies correctly and the other vocabularies' markers
(`missing`, `not-found`, `invalid`, `mismatch`, `conflict`, `sprint-required`) are untouched, so a
genuinely unreadable source is still reported `unreadable` in the other direction.
`_bounded_problems` builds its overflow problem from the same `SOURCE_PROBLEM_CAP_EXCEEDED` constant
rather than a literal. No refusal code was renamed.

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

## Evidence

### Docs References

The configured Domain Documentation registry is empty. No external documentation claim is made.

- No external domain source is required to establish this repository-owned implementation. [1]

### Repo-Internal References

The source file is the direct evidence for this unit; its governing overview records adjacent owners.

- The module's concrete API, control flow, and validation boundary are implemented here. [2]
- Every live series is observed independently from its own contract-keyed record; `_projection_members` supplies each member the already-derived v2 topology fingerprint, while activation waiting remains candidate-local. [3]
- Member source facts bind the canonical task-intent identity. [4]
- The focused adapter converts strict per-contract selector observation into disposable source facts/waits/problems without lifecycle ownership. [5]
- A capacity refusal is classified `invalid` from the declaration that owns the code, while a genuinely unreadable source still reports `unreadable`. [6]
- Waiting-door admission refuses only an identity conflict (a repeated generation id or task reference); no population ceiling remains. [7]

### Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

- No meaningful cross-repository reference applies. [8]

## CCR-R02@v2 Intent-Bound Projection Sources

Per `requirements/CCR-R02-v2-normative-task-intent-identity.md`, projection membership is
intent-bound: every member exposes the exact canonical intent digest of its leaf, so the disposable
queue cannot recompute a stale identity or offer a member whose intent is absent. Part of the landed
L25 candidate `99dc249b`.
