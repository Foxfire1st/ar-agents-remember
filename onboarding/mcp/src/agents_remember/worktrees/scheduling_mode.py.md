# mcp/src/agents_remember/worktrees/scheduling_mode.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/scheduling_mode.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-26T08:25+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[MCP overview](../../../overview.md)

## Purpose

Resolves one sprint's planning mode: an authored `executionGraph` selects `dag`, while its absence
selects the graph-less `atomic-sequential` default used for effective execution nature. Source-pair
activation separately decides which durable atomic master may expose implementation work. This
module no longer treats series-contract presence as scheduling ownership; it retains only mode,
commanded-membership, effective-nature, and ignorable terminal-artifact facts.

## Code Commentary

### Logic

`resolve_scheduling_mode` requires an orchestration sprint and returns the mode plus the resolved
commanded masters; a graph-less sprint reports the atomic-sequential default with an explanatory
fact. `commanded_sprint_masters` derives membership under either mode — graph sprints validate
through `validate_execution_topology`, while the default derives membership from the canonical
`orchestrates` aliases (`commanded_masters`).
`effective_execution_nature` is the single resolution point: under a graph-less sprint every
commanded master executes atomically; under an authored graph the declared nature rules and a
nature-less commanded master stays a typed refusal naming `task_doc.author_execution_graph`
(`set_nature`); a nature-less standalone master is atomic by default (L13-R5e), so legacy masters
need no migration. `stale_series_artifact_fact` reports a terminal series contract under an
organizational master as an ignorable `staleSeriesArtifact` fact instead of refusing the start
(L13-R5b). The removed `sequential_lane_owner`/`series_lane_holders` readers have no replacement in
this module: selection is owned by the strict source-pair activation authority.

### Conventions

This module only reads canonical task documents and terminal series artifacts; it never mutates
them. Consumers needing implementation admission must call the source-pair activation owner rather
than infer it from contract cleanup or task order.

### Invariants And Boundaries

- A sprint carries at most one scheduling authority: authored graph or the atomic-sequential
  default.
- Multiple non-terminal series contracts are valid and none owns selection merely by existing.
- The effective nature, not the declared cell, gates every atomic/organizational decision.
- A nature-less commanded master under an authored graph remains a hard refusal; the default only
  applies when no graph exists.
- Terminal series artifacts (cleanup completed/abandoned/reopened) own nothing and are reported,
  not silently honored.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies; the scheduling-default doctrine is
repository-internal.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Mode resolution: graph selects dag, absence selects the atomic-sequential default. | `resolve_scheduling_mode` | mcp/src/agents_remember/worktrees/scheduling_mode.py:45-72 |
| Membership derivation under either mode. | `commanded_sprint_masters` | mcp/src/agents_remember/worktrees/scheduling_mode.py:75-90 |
| The single effective-nature resolution every consumer shares. | `effective_execution_nature` | mcp/src/agents_remember/worktrees/scheduling_mode.py:93-116 |
| Terminal series artifacts under organizational masters degrade to a reported fact. | `stale_series_artifact_fact` | mcp/src/agents_remember/worktrees/scheduling_mode.py:119-153 |
| Source-pair selection is a separate strict authority with vacant/reconciling/active states. | `AtomicSeriesActivationObservation`; `observe_atomic_series` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:68-102; mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:170-187 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## Update History

- 2026-08-26T08:25+02:00 — Rebound `stale_series_artifact_fact` to its frozen source range; the
  scheduling/activation ownership split is unchanged.

- 2026-08-26T03:37+02:00 — Removed series-contract-census lane ownership. Scheduling mode retains
  planning/effective-nature facts while disposable source-pair activation exclusively owns
  implementation selection; multiple live series contracts are valid. Verification remains
  post-Dagger/closeout-owned.

- 2026-08-19T22:32+02:00 — 260815-DAG-L13: created for the scheduling-semantics correction — the
  atomic-sequential default for graph-less sprints, effective-nature resolution, sequential
  lane-owner derivation, and the ignorable terminal series-artifact fact. Verification remains
  closeout-owned.