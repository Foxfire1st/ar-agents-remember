# mcp/src/agents_remember/worktrees/queue/closeout_projection.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/queue/closeout_projection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-26T08:30+02:00 |
| lastVerifiedCommitHash |  `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`|
| lastVerifiedCommitDate |  2026-08-26T08:10:26+02:00|
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

### Todos

None recorded.

## Docs References

The configured Domain Documentation registry is empty. No external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain source is required to establish this repository-owned implementation. | `_PRIORITY_RANK` | mcp/src/agents_remember/worktrees/queue/closeout_projection.py:1-853 |

## Repo-Internal References

The source file is the direct evidence for this unit; its governing overview records adjacent owners.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's concrete API, control flow, and validation boundary are implemented here. | `_PRIORITY_RANK` | mcp/src/agents_remember/worktrees/queue/closeout_projection.py:1-853 |
| Every live series is observed independently and activation waiting is threaded into its members. | `_projection_members`; `_observe_series_activation` | mcp/src/agents_remember/worktrees/queue/closeout_projection.py:466-531; mcp/src/agents_remember/worktrees/queue/closeout_projection.py:602-614 |
| The focused adapter converts strict selector observation into disposable source facts/waits/problems without lifecycle ownership. | `project_series_activation` | mcp/src/agents_remember/worktrees/queue/closeout_projection_activation.py:30-53 |

## Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository reference applies. | `_PRIORITY_RANK` | mcp/src/agents_remember/worktrees/queue/closeout_projection.py:1-853 |

## Update History

- 2026-08-26T08:30+02:00 — Rebounded the activation-projection adapter citation to the frozen
  focused module extent.

- 2026-08-26T03:37+02:00 — Removed global live-series owner/conflict inference and documented
  candidate-local activation observation for every live master. Queue remains a disposable observer
  with no selector or lifecycle evidence. Verification remains post-Dagger/closeout-owned.

- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.