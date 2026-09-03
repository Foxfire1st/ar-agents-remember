# mcp/src/agents_remember/worktrees/queue/closeout_projection.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/queue/closeout_projection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `99dc249bd507c20b09ece1169c2b1fa2af8e8c1b` |
| lastVerifiedCommitDate | 2026-09-02T05:53:10+02:00|
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
`project_series_activation` observes the independent source-pair selector and contributes only a
source fact, optional bounded problem, and candidate-local waiting reasons. The projection no longer
derives a global owner from contract presence or reports a multi-live-series conflict.

Since 260831-CCR (commit `99dc249b`) every projected member source fact binds the canonical
task-intent identity of its leaf: `_projection_members` (line 520-552) computes
`task_intent_identity(contract.task_root, leaf)` (line 526-527), records it as
`source_fact["taskIntent"]` (line 538), and passes it into the member context (line 551). A leaf
whose intent cannot be projected (master resolved, schema unsupported, taxonomy unclassified)
refuses the source with a `task`-kind `ProjectionSourceProblem` carrying the exact error type
and repair action (line 529-537), so the disposable projection never offers a member whose intent is
unknown.

### Conventions

Typed records and refusal payloads remain owned at the narrowest stable boundary. Callers consume
the public function or model instead of re-deriving its lower-level state machine.

### Invariants And Boundaries

- Projection input is rebuilt from current canonical sources; missing/invalid sources empty the projection; no lifecycle or commit history is retained here.
- Activation is an observed scheduling input, not queue-owned selection. Unselected, paused, or
  reconciling candidates wait; queue recomputation cannot publish or release the selector.
- Multiple live series contracts are normal and must not become a source problem by census alone.
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
| No external domain source is required to establish this repository-owned implementation. | `_PRIORITY_RANK` | mcp/src/agents_remember/worktrees/queue/closeout_projection.py:1-889 |

## Repo-Internal References

The source file is the direct evidence for this unit; its governing overview records adjacent owners.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's concrete API, control flow, and validation boundary are implemented here. | `_PRIORITY_RANK` | mcp/src/agents_remember/worktrees/queue/closeout_projection.py:1-889 |
| Every live series is observed independently; `_projection_members` supplies each member the already-derived v2 topology fingerprint, while activation waiting remains candidate-local. | `_projection_members`; `_observe_series_activation` | mcp/src/agents_remember/worktrees/queue/closeout_projection.py:464-552; mcp/src/agents_remember/worktrees/queue/closeout_projection.py:620-633 |
| Member source facts bind the canonical task-intent identity. | `task_intent_identity`; `source_fact["taskIntent"]` | mcp/src/agents_remember/worktrees/queue/closeout_projection.py:526-551 |
| The focused adapter converts strict selector observation into disposable source facts/waits/problems without lifecycle ownership. | `project_series_activation` | mcp/src/agents_remember/worktrees/queue/closeout_projection_activation.py:30-53 |

## Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository reference applies. | `_PRIORITY_RANK` | mcp/src/agents_remember/worktrees/queue/closeout_projection.py:1-889 |

## CCR-R02@v2 Intent-Bound Projection Sources

Per `requirements/CCR-R02-v2-normative-task-intent-identity.md`, projection membership is
intent-bound: every member exposes the exact canonical intent digest of its leaf, so the disposable
queue cannot recompute a stale identity or offer a member whose intent is absent. Part of the landed
L25 candidate `99dc249b`.

## Update History

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
