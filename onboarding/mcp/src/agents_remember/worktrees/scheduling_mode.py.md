# mcp/src/agents_remember/worktrees/scheduling_mode.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/scheduling_mode.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-26T08:25+02:00 |
| lastVerifiedCommitHash | `e0820b04a499cbfb2079c78485346c50917a238a` |
| lastVerifiedCommitDate | 2026-09-13T18:02:04+02:00|
| governingOverview | `../../../overview.md` |

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

## Docs References

No configured Domain Documentation source applies; the scheduling-default doctrine is
repository-internal.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Mode resolution: graph selects dag; absence selects the atomic-sequential default that describes the sprint's shape and serializes nothing. | `resolve_scheduling_mode` | mcp/src/agents_remember/worktrees/scheduling_mode.py:45-76 |
| Membership derivation under either mode, with neither contract presence nor graph absence adding a dependency. | `commanded_sprint_masters` | mcp/src/agents_remember/worktrees/scheduling_mode.py:75-94 |
| The single effective-nature resolution every consumer shares. | `effective_execution_nature` | mcp/src/agents_remember/worktrees/scheduling_mode.py:93-120 |
| Terminal series artifacts under organizational masters degrade to a reported fact. | `stale_series_artifact_fact` | mcp/src/agents_remember/worktrees/scheduling_mode.py:119-157 |
| Per-contract selection is a separate strict authority: the observation is addressed by `contract_fingerprint` with vacant/reconciling/active states, and the strict reader takes the contract. | `AtomicSeriesActivationObservation`; "contract_fingerprint: str"; `observe_atomic_series` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:91-127; mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:96-96; mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:145-152 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## Update History
- 2026-09-13T15:03:18+02:00 — Removed the round-1 source-side-debt note: the frozen module was corrected this round, so the card now describes the current wording instead of flagging it. Re-read the module in the code worktree: the docstring says the atomic-sequential default "describes the sprint's shape — every commanded master executes atomically — and serializes nothing" with "series-contract presence is never scheduling ownership" (lines 4-9); the graph-less `facts` entry reads "executionGraph absent: atomic-sequential default — every commanded master executes atomically and no dependency is declared, so nothing serializes the masters" (lines 65-69); and `commanded_sprint_masters` says "neither contract presence nor the absence of a graph adds a dependency — nothing serializes the masters" (lines 87-89). Body updated with the ruling — nothing serializes a graph-less sprint and per-contract activation never pauses or excludes a sibling — and every citation row re-verified against the changed file: `resolve_scheduling_mode` 45-76 (was 45-72), `commanded_sprint_masters` 75-94 (was 75-90), `effective_execution_nature` 93-120 (was 93-116), `stale_series_artifact_fact` 119-157 (was 119-153); the activation row is unchanged. Verification metadata remains closeout-owned; no acceptance claim.
- 2026-09-13T14:19+02:00 — Per-contract activation curation: this card now describes the activation authority the module defers to as per series contract — the record is keyed by `contract_fingerprint` and a foreign master is never a waiting reason — and rebinds the observation/reader citations to atomic_series_activation.py:92-127, :96-96 and :145-152. Recorded the source-side debt that this frozen module's own docstrings (lines 5-6, 63-64, 84-85) still carry the older "source-pair-selected" wording, so it is not read as the current rule; no source change is claimed. Verification metadata remains closeout-owned; no acceptance claim.
- 2026-09-08T18:54:49+02:00 — CCR-L38 CQ01 preparation rebound the scheduling/activation citations to the current observation dataclass and strict reader; scheduling ownership is unchanged and no acceptance claim is made.

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
