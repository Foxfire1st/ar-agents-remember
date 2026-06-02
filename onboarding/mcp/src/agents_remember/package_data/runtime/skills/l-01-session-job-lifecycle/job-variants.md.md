# l-01-session-job-lifecycle/job-variants.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-session-job-lifecycle/job-variants.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-02T03:30+02:00                     |
| lastVerifiedCommitHash | `53b17f574a53ae400f8abb9fda264fa9fa3e8dff` |
| lastVerifiedCommitDate | 2026-06-02T16:24:22+02:00|

## Purpose

This companion file defines the four `l-01-session-job-lifecycle` skill job lenses (bug, feature, triage, research). A lens is picked during `frame`, is re-pickable, and tunes only three things: the opening move, the retrieval lean, and the `decide` default. It never changes the spine.

## Code Commentary

### Logic

A table maps each job to its opening move, its leading `c-04-retrieval-strategy-router` skill strategy, and its usual `decide` landing, followed by a short paragraph per job. `bug` reproduces and proves root cause (Relationship + Intent) and defaults to build. `feature` clarifies intent/scope/non-goals (design doctrine + Intent) and defaults to build. `triage` assesses severity/blast-radius/ownership (breadth scan) and frequently exits read-only by routing or spawning. `research` states the question (Semantics + onboarding) and exits read-only by design.

### Conventions

The lens is explicitly a hint, not a gate; the `decide` defaults are still real decisions, not automatic transitions. Read-only is the natural landing for triage and research, but any lens can re-route.

### Invariants And Boundaries

A lens never adds or removes a spine phase. Triage and research produce recommendations or spawned jobs rather than performing code changes themselves; escalate to a build only when that lens is the cheapest place to fix the issue.

### Todos

No current todo is recorded for this job-variants file.

### Docs References

No external domain documentation applies to this repository-local job-variants file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

The lenses tune the shared spine defined in the companion files.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The lenses tune the `frame` opening move and the `decide` default of the shared spine. | n/a | [lifecycle.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/l-01-session-job-lifecycle/lifecycle.md) |

## Cross-Repo References

No sibling repository evidence is needed for this job-variants file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-06-02T03:30+02:00: Created file-level onboarding for the `l-01-session-job-lifecycle` skill job-variants companion file defining the bug/feature/triage/research lenses as frame-time hints over the shared spine.
