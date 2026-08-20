# mcp/src/agents_remember/worktrees/scheduling_mode.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/scheduling_mode.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-19T22:32+02:00 |
| lastVerifiedCommitHash | `b523f53b193e9783e7c7e6410c772e7d64d8df17` |
| lastVerifiedCommitDate | 2026-08-19T21:54:50+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[MCP overview](../../../overview.md)

## Purpose

Resolves one sprint's scheduling authority: an authored `executionGraph` selects `dag` mode, and
its absence selects the `atomic-sequential` default (260815-DAG-L13-R1) — every commanded master
runs one at a time and fully integrates before the next master's series begins, regardless of any
declared execution nature. The module also owns the effective-nature resolution the rest of the
plane consumes, the sequential landing-lane ownership read, and the ignorable terminal
series-artifact fact.

## Code Commentary

### Logic

`resolve_scheduling_mode` requires an orchestration sprint and returns the mode plus the resolved
commanded masters; a graph-less sprint reports the atomic-sequential default with an explanatory
fact. `commanded_sprint_masters` derives membership under either mode — graph sprints validate
through `validate_execution_topology`, while the default derives membership from the canonical
`orchestrates` aliases (`commanded_masters`) and the series lane, not a graph, serializes them.
`effective_execution_nature` is the single resolution point: under a graph-less sprint every
commanded master executes atomically; under an authored graph the declared nature rules and a
nature-less commanded master stays a typed refusal naming `task_doc.author_execution_graph`
(`set_nature`); a nature-less standalone master is atomic by default (L13-R5e), so legacy masters
need no migration. `sequential_lane_owner` treats lane ownership as a stored fact: the master whose
series contract exists with a non-terminal cleanup cell owns the lane (terminal cleanup values —
completed, abandoned, reopened — release it; legacy multi-holder state resolves deterministically
to the first holder in canonical key order). `stale_series_artifact_fact` reports a terminal series
contract under an organizational master as an ignorable `staleSeriesArtifact` fact instead of
refusing the start (L13-R5b).

### Conventions

This module only reads canonical task documents and stored series contracts; it never mutates
them. Lane ownership is derived from the contract's cleanup cell, never from request data.

### Invariants And Boundaries

- A sprint carries at most one scheduling authority: authored graph or the atomic-sequential
  default.
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
| Mode resolution: graph selects dag, absence selects the atomic-sequential default. | `resolve_scheduling_mode` | mcp/src/agents_remember/worktrees/scheduling_mode.py:46-73 |
| Membership derivation under either mode. | `commanded_sprint_masters` | mcp/src/agents_remember/worktrees/scheduling_mode.py:76-91 |
| The single effective-nature resolution every consumer shares. | `effective_execution_nature` | mcp/src/agents_remember/worktrees/scheduling_mode.py:94-117 |
| Lane ownership is a stored, non-terminal series-contract fact. | `sequential_lane_owner`; `series_lane_holders` | mcp/src/agents_remember/worktrees/scheduling_mode.py:120-156 |
| Terminal series artifacts under organizational masters degrade to a reported fact. | `stale_series_artifact_fact` | mcp/src/agents_remember/worktrees/scheduling_mode.py:159-193 |
| The degraded queue readout consumes the mode and lane owner. | `_degraded_projection` | mcp/src/agents_remember/worktrees/queue/closeout_queue.py:323-367 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## Update History

- 2026-08-19T22:32+02:00 — 260815-DAG-L13: created for the scheduling-semantics correction — the
  atomic-sequential default for graph-less sprints, effective-nature resolution, sequential
  lane-owner derivation, and the ignorable terminal series-artifact fact. Verification remains
  closeout-owned.
