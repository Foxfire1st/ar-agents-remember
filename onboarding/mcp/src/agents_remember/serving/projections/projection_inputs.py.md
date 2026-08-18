# mcp/src/agents_remember/serving/projections/projection_inputs.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/projections/projection_inputs.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-31T00:00+02:00 |
| lastVerifiedCommitHash |  `2597ff98306ba7c7963005092ac597c4972e63ce`|
| lastVerifiedCommitDate |  2026-08-18T15:45:32+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving projections overview](overview.md)

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

**Three frozen parameter objects carry the pass (260731-EFA-L2).** They are not shape for its own
sake — each bundles values that are only meaningful read against one another, and each private
`_refresh_*` method now takes the bundle rather than re-receiving its members:

- `RefreshPass(now, refresh, tasks_changed=False)` — the frame every domain refresher runs in.
  `read()` re-binds it once via `dataclasses.replace(pass_, tasks_changed=self._refresh_tasks(...))`,
  so the task-tree verdict reaches lifecycles, engine facts and drift as part of the same frame
  instead of as a separate argument each of them takes.
- `ActiveGroups(groups, changed)` — a worktree-group admission set plus whether it moved since the
  last pass. `read()` builds two: `providers` (from `admitted_worktree_groups`) and `engines`
  (from `active_enclosure_worktree_groups`). The set says what to read, the flag says whether to
  read at all; splitting them either re-reads every tick or never re-reads.
- `ProjectionReaders(lifecycle, repo_surfaces, landing_state=None)` — the pass's I/O seam, so a
  test can replace the whole outside-world set coherently.

`ProjectionInputState.read(config, readers, *, observer_root, pass_)` is the current signature —
`now`, `refresh`, `landing_state`, `lifecycle_reader` and `repo_surface_reader` are no longer
individual parameters. `_refresh_tasks(config, pass_)`, `_refresh_drift(config, pass_)` and
`_refresh_progress(config, pass_)` take only the pass; `_refresh_providers(config, pass_, groups)`
and `_refresh_engine_facts(config, pass_, groups, *, landing_state)` take the pass plus their own
admission set; `_refresh_lifecycles(observer_root, pass_, *, lifecycle_reader)` and
`_refresh_workspace(config, pass_, *, observer_root)` keep the one path each still needs.

`_advance_model_age` no longer carries a `# noqa: UP047` suppression — the whole gate now runs
without exemptions.

### Conventions

The projection worker is the single mutation owner. Fixed slots and whole-domain replacement make
retention and invalidation explicit rather than heuristic.

### Invariants And Boundaries

- Heartbeats update time-derived ages without rereading heavy domains.
- Lifecycle-only changes do not reread tasks, drift, providers, or repository surfaces.
- Admission groups are recomputed when their task/lifecycle inputs change.
- Deleted rows are removed on the next refresh of their owning domain.
- The pass is re-bound, never mutated: `RefreshPass` / `ActiveGroups` / `ProjectionReaders` are all
  frozen, so a refresher cannot change the frame a later refresher reads.

### Todos

None known.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Projection write edge consumes this retained input state. | `project_and_write` | mcp/src/agents_remember/serving/projections/projection_store.py:212-275 |
| The serialized worker maps watcher wakes to refresh kinds. | `Projector` | mcp/src/agents_remember/serving/projector.py:126-330 |
| Domain invalidation regressions. | `test_heartbeat_and_lifecycle_changes_skip_unrelated_heavy_readers`; `test_task_refresh_replaces_and_reclaims_retained_rows_at_two_sizes` | mcp/tests/test_projection_domain_invalidation.py:64-141; mcp/tests/test_projection_domain_invalidation.py:143-186 |

## Cross-Repo References

No meaningful cross-repository references found.

## Update History

- 2026-08-18T13:00+02:00 — No content impact: 260815-DAG-L8 added the closeout-queue projection surface (closeoutQueues); the behavior this card describes is unchanged.

- 2026-08-02T16:44:12+02:00 — 260731-EFA-L6 W1-B05 curator: anchored 3 citation items; scoped citation check now passes.

- 2026-07-31T00:00+02:00 — 260731-EFA-L2 (gate honesty, `PLR0913` armed with no exemptions):
  `ProjectionInputState.read` and every `_refresh_*` method were re-signed onto three new frozen
  parameter objects — `RefreshPass`, `ActiveGroups`, `ProjectionReaders`. The `read()` contract
  changed: `now` / `refresh` / `landing_state` / `lifecycle_reader` / `repo_surface_reader` are
  gone as individual parameters, replaced by `readers` and `pass_`. `_advance_model_age` lost its
  `# noqa: UP047`. Behaviour is unchanged — the refresh decisions, admission-set comparisons and
  whole-domain replacement are the same; only how the values reach each refresher moved.
  Verification metadata pinned until closeout stamps the L2 commit.
- 2026-07-30T12:51+02:00 — 260727-CHATS-IM-L2 curator: created onboarding for
  domain-invalidated projection inputs and whole-domain reclamation. Verification metadata remains
  blank until commit.
