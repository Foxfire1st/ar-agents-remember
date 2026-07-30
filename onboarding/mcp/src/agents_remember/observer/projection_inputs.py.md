# mcp/src/agents_remember/observer/projection_inputs.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/observer/projection_inputs.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-30T12:51+02:00 |
| lastVerifiedCommitHash |  `3a8ff703d796dc585b86a458daaf9eb2af6b2b31`|
| lastVerifiedCommitDate |  2026-07-30T13:59:13+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Observer overview](overview.md)

## Purpose

Retains one bounded snapshot of each workspace-projection input domain and refreshes only domains
invalidated by the filesystem watcher.

## Code Commentary

### Logic

`ProjectionRefresh` distinguishes full, change, and heartbeat ticks across tasks, lifecycles,
workspace, drift, providers, start progress, and tool reports. `ProjectionInputState.read`
advances display ages, refreshes invalidated domains, recomputes admission sets when their source
domains change, and returns a complete immutable-shaped `ProjectionInputs` aggregate. Domain
collections are replaced as a whole, so deletions reclaim retained rows on their next relevant
refresh.

The state also reuses one contract snapshot cache and the task-document payload cache rather than
re-enumerating and parsing unrelated workspace surfaces every second.

### Conventions

The projection worker is the single mutation owner. Fixed slots and whole-domain replacement make
retention and invalidation explicit rather than heuristic.

### Invariants And Boundaries

- Heartbeats update time-derived ages without rereading heavy domains.
- Lifecycle-only changes do not reread tasks, drift, providers, or repository surfaces.
- Admission groups are recomputed when their task/lifecycle inputs change.
- Deleted rows are removed on the next refresh of their owning domain.

### Todos

None known.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Projection write edge consumes this retained input state. | [projection_store.py](agents-remember/mcp/src/agents_remember/observer/projection_store.py) |
| The serialized worker maps watcher wakes to refresh kinds. | [projector.py](agents-remember/mcp/src/agents_remember/serving/projector.py) |
| Domain invalidation regressions. | [test_projection_domain_invalidation.py](agents-remember/mcp/tests/test_projection_domain_invalidation.py) |

## Cross-Repo References

No meaningful cross-repository references found.

## Update History

- 2026-07-30T12:51+02:00 — 260727-CHATS-IM-L2 curator: created onboarding for
  domain-invalidated projection inputs and whole-domain reclamation. Verification metadata remains
  blank until commit.
