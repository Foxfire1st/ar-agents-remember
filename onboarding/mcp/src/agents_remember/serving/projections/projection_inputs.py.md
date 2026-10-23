# mcp/src/agents_remember/serving/projections/projection_inputs.py

## Governing Overview

[serving projections overview](overview.md)

## Purpose

Retains one bounded snapshot of each workspace-projection input domain and refreshes only domains
invalidated by the filesystem watcher.

## Code Commentary

Complete path samples refresh canonical task sources and document-consumer closure; incomplete samples reconcile fully. Documentary edits do not refresh unrelated structural domains. Closeout queues authenticate their own source generation; no lifecycle/series fold remains.


### Logic

Refresh domains are tasks/workspace/drift/providers/start-progress/tool-reports/HOST_ACTIVITY, plus the contract-scoped activation records under `controlplane` and the held-message queue under `temp`. Each pass derives permission rows and turn-end stamps from retained host facts, updates stall clocks, and reports the live native kinds' own occurrence ends to the dismissal owner. Native file-backed observations refresh on first look or relevant invalidation, while unfinished held and pause acquisition continues in bounded steps on the existing heartbeat; initialized, complete quiet views are retained. This adds no host read or timer. Ordinary full healing excludes HOST_ACTIVITY; only startup or explicit invalidation reads it. Display age advancement is separate from acquisition.
`ProjectionInputState.read` refreshes invalidated domains and recomputes admission sets from their owning changes, returning the retained aggregate. `ProjectionReaders.repo_surfaces` returns exactly `(route_coverage, ledgers)` and the read unpacks those two collections; `ProjectionInputs` has no `sidecar_staleness`. Domain collections are replaced as a whole so removals reclaim retained rows on their relevant refresh. [6]

The state also reuses one contract snapshot cache and the task-document payload cache rather than
re-enumerating and parsing unrelated workspace surfaces every second.

**Three frozen parameter objects carry the pass (260731-EFA-L2).** They are not shape for its own
sake — each bundles values that are only meaningful read against one another, and each private
`_refresh_*` method now takes the bundle rather than re-receiving its members:

- `RefreshPass(now, refresh, tasks_changed=False)` carries the clock, invalidation and
  structural task-change flag together. `_read_inputs` re-binds it with `dataclasses.replace`
  after `_refresh_tasks`; it does not mutate a frame that later refreshers share.
- `ActiveGroups(groups, changed)` carries both an admission set and whether it moved. The
  provider set comes from `admitted_worktree_groups(self._enclosures)` and the engine set from
  `active_enclosure_worktree_groups(self._enclosures)`: the set says what to read and the flag
  whether to reread, preventing both unconditional rereads and permanently retained stale groups.
- `ProjectionReaders(repo_surfaces, landing_state=None)` is the frozen I/O bundle; it has no
  lifecycle reader. `ProjectionInputState.read(config, readers, *, observer_root, pass_)` takes
  those bundles rather than independent clocks/readers. Refreshers retain their domain-specific
  arguments, including attention observations where an actual read must supply proof.
- `task_sources` and default-unknown host facts replace task_documents/series/session slots.

`_read_inputs` updates task/closeout slots and first/invalidated host facts, then contract admission. Only actually read kinds supply AttentionObservation proof: provider/setup/drift/start readers contribute completeness, existence, explicit health and fingerprints; the two notice kinds contribute the retained-set observation; and `_observe_native_kinds` (:750-786) supplies one observation per complete live native kind, derived from the same pass that publishes or withholds the row, with the ids `native_attention_items` and `stall_occurrences` produce. Unread/failed kinds prove no removal, and a row this same pass still publishes is never reported healthy. Workspace reconciliation locks read/rewrite and retains last successful acknowledgements on OSError; incomplete sibling proof does not hide valid changed drift.

`_advance_model_age` no longer carries a `# noqa: UP047` suppression — the whole gate now runs
without exemptions.

### Conventions

The projection worker is the single mutation owner. Fixed slots and whole-domain replacement make
retention and invalidation explicit rather than heuristic.

### Invariants And Boundaries

- Heartbeat advances ages and existing non-host provider/workspace owners, never host census.
- Repository surfaces are requested only on full passes or after their 120-second TTL
  (`_REPO_SURFACES_TTL_SECONDS`); all other passes retain the route-coverage and ledger
  slots without calling the surface reader. A missing snapshot is stale immediately.
  The injected production reader has its own 120-second cache, so a full input pass does not
  imply a fresh physical walk when that cache is still valid.
- `RefreshPass`, `ActiveGroups` and `ProjectionReaders` are frozen: pass updates use replacement,
  not mutation of a frame that a later refresher reads.
- Host requires startup/invalidation plus armed boot reconciliation.
- Contract admission changes refresh provider/engine input independently of sessions.
- Owning-domain closure replacement drops deleted/invalid sources, not a whole-corpus admission proof.
- Failure heals non-host plus pending domains without all-slot rollback.

### Todos

None known.

## Evidence

- Repository reader and retained input aggregate omit sidecar staleness and carry route coverage plus ledgers. [6]


### Docs References

No Domain Documentation source is configured.

### Repo-Internal References

- Full input passes or an expired/missing 120-second retained-surface snapshot reach the repo-surface reader; other passes retain its two collections unread. [3]
- The production repo-surface reader can itself reuse its 120-second cache. [4]
- The three parameter objects are frozen; the task-change frame is replaced, and provider/engine admission sets travel with their change flags. [5]



### Cross-Repo References

No meaningful cross-repository references found.

## 2026-08-26 Atomic Task Refresh Retry

A failed input pass sets `_task_refresh_pending`; the next read heals every non-host domain plus pending invalidations and clears the flag only after success. Full task refresh prepares sources before replacing task slots; incremental and later domain work can still mutate slots before another read fails. Failed passes return no new ProjectionInputs aggregate, but do not roll back every changed slot. Host intake remains startup/explicit-invalidation only during retry.

- Projection write edge consumes this retained input state. [1]
- The serialized worker maps watcher wakes to refresh kinds. [2]

## 20261023-L190-v2 The Live Kinds Report Their Own Ends

`_observe_native_kinds` (:750-786) runs immediately after the native attention read (:470-473), so the observation that reclaims an acknowledgement and the rows that publish (or withhold) its entry are one pass. It collects the ids the builders publish, then replaces the stall set with `stall_occurrences(self._native_attention, entries.tasks)` — a stall row appears only after the deadline, but its interval is live from the moment the task goes idle, and the acknowledgement names the interval.

Proof is gated per kind: `permissions_complete`, `held_complete`, and `_host_activity.known` for stalls. An incomplete kind contributes no observation at all, so `AttentionDismissalStore.reconcile` keeps its records; and an id this same pass still publishes is never reported healthy, so a live cause is acknowledged out of sight and not out of existence.
