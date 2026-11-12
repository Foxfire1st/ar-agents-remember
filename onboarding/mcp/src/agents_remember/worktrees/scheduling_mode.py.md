# mcp/src/agents_remember/worktrees/scheduling_mode.py

## Governing Overview

[MCP overview](../../../overview.md)

## Purpose

Resolves one sprint's planning mode: an authored `executionGraph` selects `dag`, while its absence
selects the graph-less `atomic-sequential` default used for effective execution nature. That default
describes the sprint's shape — every commanded master executes atomically — and serializes nothing:
a graph-less sprint declares no dependencies, so independent masters proceed concurrently and no
master is held because another master is selected. Per-contract atomic-series activation separately
decides which durable atomic master may expose implementation work; selecting one master never pauses
or excludes a sibling. This module no longer treats series-contract presence as scheduling ownership;
it retains only mode, commanded-membership, effective-nature, and ignorable terminal-artifact facts.

## Code Commentary

### Logic

`resolve_scheduling_mode` requires an orchestration sprint and returns the mode plus the resolved
commanded masters; a graph-less sprint reports the atomic-sequential default with the fact
"executionGraph absent: atomic-sequential default — every commanded master executes atomically and no
dependency is declared, so nothing serializes the masters". `commanded_sprint_masters` derives
membership under either mode — graph sprints validate through `validate_execution_topology`, while
the default derives membership from the canonical `orchestrates` aliases (`commanded_masters`) — and
its own docstring states that neither contract presence nor the absence of a graph adds a dependency.
`effective_execution_nature` is the single resolution point: under a graph-less sprint every
commanded master executes atomically; under an authored graph the declared nature rules and a
nature-less commanded master stays a typed refusal naming `task_doc.author_execution_graph`
(`set_nature`); a nature-less standalone master is atomic by default (L13-R5e), so legacy masters
need no migration. `stale_series_artifact_fact` reports a terminal series contract under an
organizational master as an ignorable `staleSeriesArtifact` fact instead of refusing the start
(L13-R5b). The removed `sequential_lane_owner`/`series_lane_holders` readers have no replacement in
this module: selection is owned by the strict per-contract activation authority, where each series
contract owns its own `contract_fingerprint`-keyed record and a foreign master is never a waiting
reason.

The module's own docstrings now match the per-contract runtime. The module docstring says the
atomic-sequential default "describes the sprint's shape — every commanded master executes atomically
— and serializes nothing", that a graph-less sprint "declares no dependencies, so independent masters
proceed concurrently", and that "series-contract presence is never scheduling ownership" (lines 4-9).
The graph-less fact at lines 65-69 reads "executionGraph absent: atomic-sequential default — every
commanded master executes atomically and no dependency is declared, so nothing serializes the
masters", and `commanded_sprint_masters` says "neither contract presence nor the absence of a graph
adds a dependency — nothing serializes the masters" (lines 87-89). The retired per-source-pair
wording ("source-pair-selected atomic master exposes implementation work at a time") no longer occurs
in this module; the runtime rule is per series contract and the default serializes nothing.

### Conventions

This module only reads canonical task documents and terminal series artifacts; it never mutates
them. Consumers needing implementation admission must call the per-contract activation owner rather
than infer it from contract cleanup or task order. The atomic-sequential default is a sprint shape,
not a serialization mechanism: it introduces no dependency and no cross-master exclusion.

### Invariants And Boundaries

- A sprint carries at most one scheduling authority: authored graph or the atomic-sequential
  default, and the default describes the sprint's shape — every commanded master executes atomically
  — while serializing nothing.
- Neither series-contract presence nor the absence of a graph adds a dependency between commanded
  masters.
- Multiple non-terminal series contracts are valid and none owns selection merely by existing;
  per-contract activation never pauses or excludes a sibling master.
- The effective nature, not the declared cell, gates every atomic/organizational decision.
- A nature-less commanded master under an authored graph remains a hard refusal; the default only
  applies when no graph exists.
- Terminal series artifacts (cleanup completed/abandoned/reopened) own nothing and are reported,
  not silently honored.

### Todos

None recorded.

## Evidence

### Docs References

No configured Domain Documentation source applies; the scheduling-default doctrine is
repository-internal.

### Repo-Internal References

- Mode resolution: graph selects dag; absence selects the atomic-sequential default that describes the sprint's shape and serializes nothing. [1]
- Membership derivation under either mode, with neither contract presence nor graph absence adding a dependency. [2]
- The single effective-nature resolution every consumer shares. [3]
- Terminal series artifacts under organizational masters degrade to a reported fact. [4]
- Per-contract selection is a separate strict authority: the observation is addressed by `contract_fingerprint` with vacant/reconciling/active states, and the strict reader takes the contract. [5]

### Cross-Repo References

No meaningful cross-repository reference applies.
