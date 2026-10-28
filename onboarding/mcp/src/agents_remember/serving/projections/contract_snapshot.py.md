# mcp/src/agents_remember/serving/projections/contract_snapshot.py

## Governing Overview

[serving projections overview](overview.md)

## Purpose

`contract_snapshot.py` (260712-PTS-L2, master 260712-PTS) makes the leaf-enclosure-contract read a
**shared task-refresh** pass instead of three independent ones. Before this leaf, every
1-second projection tick enumerated `iter_leaf_enclosure_contracts` and re-parsed EVERY contract three
times — `read_enclosures`, `read_engine_process_facts`, and drift-snapshot pruning each ran their own
walk + `load_contract` pass; a py-spy sample on 2026-07-12 showed those three passes at 2.78s / 3.68s /
3.40s of total time in a 15s window. `ContractSnapshotCache.build` performs one pass when the
task-domain inputs refresh and publishes an immutable `ContractSnapshot` that all three consumers receive, backed by a
cross-tick parse cache keyed by stat identity so an unchanged contract file is not re-read or
re-parsed on later builds. `ProjectionInputState` retains that snapshot on unaffected ticks;
first use and a pending task refresh still require a build.

## Code Commentary

### Logic

`ContractSnapshot` is a frozen dataclass with a MappingProxyType path-to-contract mapping. Full builds preserve sorted enumeration order and report omitted enumerated failures/foreign members in skipped. Scoped builds retain cache insertion order, update eligible named paths (ignoring archived/notes names), and report named paths absent from the resulting mapping in skipped. Filesystem-derived membership, not recorded roots, governs admission.

`ContractSnapshotCache.build(tasks_root, only=None)` is the full enumeration + at-most-one-parse-per-contract
pass; `only` instead selects a scoped no-enumeration update retaining other cached entries: for each enumerated path it stats the file (`_safe_stat`), returns the cached parse when the
stat identity `(mtime_ns, size, ctime_ns)` is unchanged (`_cached_contract`), otherwise parses via
`load_contract` and stores a fresh `_ParseCacheEntry`. A parse failure (`ContractError`/`OSError`)
drops any stale cache entry, adds the path to `skipped`, and is NEVER cached — the file is
re-attempted on the next full build while still enumerated, or a scoped build including that eligible path (not archived/below notes), without requiring a stat change. A cached or freshly parsed contract
is still checked for foreign membership; foreign contracts are evicted and named in `skipped`,
never admitted to the mapping. After the loop,
entries whose paths left the enumeration are deleted, so retention is bounded by the live contract
set.

`_safe_stat` returning `None` (stat failed) must not introduce a new skip path — the readers never
stat'ed before this leaf — so the caller falls through to the uncached parse attempt, which applies
the original read/parse containment; a successful member parse with no stat is returned by _parse_live but not cached. Full build includes that return; scoped build discards the return and constructs its mapping from cached entries, so that parse is omitted there.

`build_contract_snapshot(tasks_root)` is the one-shot builder for standalone reader calls
(`contracts=None` at a reader's public signature): a throwaway `ContractSnapshotCache().build(...)`,
using the same current membership and failure filters without a cross-call cache.

### Conventions

The stat-identity **includes `ctime_ns`** (adversarial-review hardening, second leaf commit): a
`chmod 000` changes neither `mtime_ns` nor `size`, so without ctime the cache would serve the old
good parse FOREVER where the pre-cache readers degraded to skip-every-tick; and a rewrite whose
`(mtime_ns, size)` was pinned via `os.utime` would never be seen. `ctime` changes on both, while
staying untouched for genuinely unchanged files — the hardening costs zero extra parses.

Cache mutation is serialized on the projection worker; it is not modeled on a removed lifecycle-log cache.
Consumers receive the snapshot through a keyword-only `contracts: ContractSnapshot | None = None`
parameter so reader public signatures are unchanged.

### Invariants And Boundaries

- **Cache mutation happens only inside `build`, on the projection worker thread.** The projector
  serializes ticks by awaiting each `asyncio.to_thread` call, so builds never overlap; nothing else
  may mutate the cache.
- **The published snapshot is immutable — and consumers must never mutate the contracts.**
  `ContractSnapshot` is a frozen read-only view that can be handed to any consumer without locks,
  but the `WorktreeContract` instances inside it are shared across ticks by the parse cache: any
  future consumer that mutates a contract corrupts cross-tick state (the module docstring warns).
- **Parse failures are never cached.** An unreadable or malformed contract is skipped this build and
  retried on the next full build while still enumerated, or scoped build naming an eligible path; only successful parses enter the cache.
- **Retention is bounded by the live enumeration.** Full builds prune paths no longer enumerated; scoped builds ignore archived/notes names, delete other named missing paths, and retain unrelated entries without enumeration.
- **Deliberate non-consumer:** the landing refresher keeps its independent contract pass and never touches this worker-thread-owned cache. The removed supervisor sweep is not an active consumer or non-consumer owner.

### Todos

None.

## Evidence

### Docs References

No external Domain Documentation source is configured for this memory repo (`system/sources.md` has
no entries).

No relevant documentation found after checking live sources; no Domain Documentation entries are configured.

### Repo-Internal References

The snapshot reuses the worktree subsystem's own enumeration and parser (`iter_leaf_enclosure_contracts`,
`load_contract`) rather than re-implementing either; the projection store owns the shared task-refresh
build; the three consumers accept the snapshot via keyword-only injection.


- The immutable snapshot and builder hold only admitted members and name read/parse failures or foreign nonmembers in skipped. 



### Cross-Repo References

No meaningful cross-repo references found.

Same-repository projection concern only.

- Module docstring: one pass per tick, three prior walks, stat-identity cache, and the serialized-tick concurrency discipline.  Anchor: "One immutable leaf-enclosure-contract snapshot per projection tick" [1]


- Full builds enumerate/reconcile; scoped builds ignore archived/notes names, stat/parse other named paths and retain unrelated cached members. Failed or foreign parsed members are evicted; retry and live-set pruning claims require relevant/full builds. 


- `_cached_contract` reuses a parse only while all three stat fields hold; `_safe_stat` failure falls through to the uncached parse instead of introducing a new skip path; `build_contract_snapshot` is the standalone one-shot.  Anchor: "def build_contract_snapshot" 
- Snapshot construction uses the shared enclosure iterator and contract parser, rather than reimplementing either.  Anchor: "from agents_remember.tasks.task_paths import (", "from agents_remember.worktrees.worktree_contract import (" [5]
- `projection_store` owns the module-level `_contract_snapshot_cache` (with the three-walks rationale) and injects it into the per-tick `ProjectionInputState`.  Anchor: "class ProjectionTickState" [6]

- Task-domain refresh, first use or pending retry builds one snapshot; unaffected ticks retain it.  Anchor: `ProjectionInputState._refresh_tasks` [7]

- `read_enclosures` and `read_engine_process_facts` take the keyword-only injected snapshot; `contracts=None` builds a local one with identical behavior.  Anchor: "def read_enclosures" [8]

- Drift-snapshot pruning consumes the same snapshot, removing the third per-tick walk.  Anchor: "def prune_orphaned_drift_snapshots" [9]


Anchor: `ContractSnapshot` `build` [2]


Anchor: `ContractSnapshotCache` [3]

- `_cached_contract` reuses a parse only while all three stat fields hold; `_safe_stat` failure falls through to the uncached parse instead of introducing a new skip path; `build_contract_snapshot` is the standalone one-shot.  Anchor: "def build_contract_snapshot" [4]

- Retired at the fifth freeze d59c3493: mcp/src/agents_remember/serving/projections/contract_snapshot.py::build - the bytes it recorded now occur 12 times in the file, so no single home can be named and it is not given to the likelier one; mcp/src/agents_remember/serving/projections/contract_snapshot.py::ContractSnapshotCache - the bytes it recorded now occur 3 times in the file, so no single home can be named and it is not given to the likelier one; mcp/src/agents_remember/serving/projections/contract_snapshot.py:185-185 - the bytes it recorded now occur 2 times in the file, so no single home can be named and it is not given to the likelier one. Retired means the anchor no longer stands, not that the cited subject was deleted.
