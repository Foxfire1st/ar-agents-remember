# l-01-agent-lifecycles/lenses.md

## Purpose

This companion file defines the four `l-01-session-job-lifecycle` skill job lenses (bug, feature, triage, research). A lens is picked during `reframe-research`, is re-pickable, and tunes only three things: the opening move, the retrieval lean, and the `decide` default. It never changes the spine (now stated in the canonical phase enum: `request -> trust-checkpoint -> reframe-research -> decide -> build -> close`).

## Code Commentary

### Logic

A table maps each job to its opening move, its leading `c-04-retrieval-strategy-router` skill strategy, and its usual `decide` landing, followed by a short paragraph per job. `bug` reproduces and proves root cause (Relationship + Intent) and defaults to build. `feature` clarifies intent/scope/non-goals (design doctrine + Intent) and defaults to build. `triage` assesses severity/blast-radius/ownership (breadth scan) and frequently exits research-only by routing or spawning. `research` states the question (Semantics + onboarding) and exits research-only by design.

### Conventions

The lens is explicitly a hint, not a gate; the `decide` defaults are still real decisions, not automatic transitions. Research-only is the natural landing for triage and research, but any lens can re-route.

### Invariants And Boundaries

A lens never adds or removes a spine phase. Triage and research produce recommendations or spawned jobs rather than performing code changes themselves; escalate to a build only when that lens is the cheapest place to fix the issue.

### Todos

No current todo is recorded for this job-variants file.

### Docs References

No external domain documentation applies to this repository-local job-variants file.

No relevant external documentation found.

## Evidence

### Repo-Internal References

The lenses tune the shared spine defined in the companion files.

- The lenses tune the `reframe-research` opening move and the `decide` default of the shared spine. [1]

As of cycle 4 the feature lens no longer offers a chat build: size decides the minimal w-02 artifact vs a master + sub-task series (T7 conformance).

### Cross-Repo References

No sibling repository evidence is needed for this job-variants file.

No meaningful cross-repo references found.
