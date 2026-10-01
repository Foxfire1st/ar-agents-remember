# mcp/src/agents_remember/serving/projections/contract_snapshot.py

## Governing Overview

[serving projections overview](overview.md)

## Purpose

`contract_snapshot.py` (260712-PTS-L2, master 260712-PTS) makes the leaf-enclosure-contract read a
**once-per-projection-tick** shared pass instead of three independent ones. Before this leaf, every
1-second projection tick enumerated `iter_leaf_enclosure_contracts` and re-parsed EVERY contract three
times — `read_enclosures`, `read_engine_process_facts`, and drift-snapshot pruning each ran their own
walk + `load_contract` pass; a py-spy sample on 2026-07-12 showed those three passes at 2.78s / 3.68s /
3.40s of total time in a 15s window. `ContractSnapshotCache.build` performs the pass ONCE at tick
start and publishes an immutable `ContractSnapshot` that all three consumers receive, backed by a
cross-tick parse cache keyed by stat identity so an unchanged contract file is not re-read or
re-parsed on later ticks at all.

## Code Commentary

### Logic

`ContractSnapshot` is a frozen dataclass: `contracts` is a read-only mapping
(`MappingProxyType`) of contract path → parsed `WorktreeContract`, preserving the sorted enumeration
order of `iter_leaf_enclosure_contracts` (insertion-ordered) so consumers iterate exactly the paths,
contracts, and order they previously walked themselves; `skipped` is a `frozenset` of the paths whose
parse failed this tick — the same skip-never-fatal containment each reader applied inline before.

`ContractSnapshotCache.build(tasks_root)` is the one enumeration + at-most-one-parse-per-contract
pass: for each enumerated path it stats the file (`_safe_stat`), returns the cached parse when the
stat identity `(mtime_ns, size, ctime_ns)` is unchanged (`_cached_contract`), otherwise parses via
`load_contract` and stores a fresh `_ParseCacheEntry`. A parse failure (`ContractError`/`OSError`)
drops any stale cache entry, adds the path to `skipped`, and is NEVER cached — the file is
re-attempted on the next build, exactly the retry-every-tick containment the readers had when they
parsed inline (a transient `OSError` self-heals without waiting for a stat change). After the loop,
entries whose paths left the enumeration are deleted, so retention is bounded by the live contract
set.

`_safe_stat` returning `None` (stat failed) must not introduce a new skip path — the readers never
stat'ed before this leaf — so the caller falls through to the uncached parse attempt, which applies
the original containment; a successful parse with no stat is returned but not cached.

`build_contract_snapshot(tasks_root)` is the one-shot builder for standalone reader calls
(`contracts=None` at a reader's public signature): a throwaway `ContractSnapshotCache().build(...)`,
identical cost and behavior to the pre-L2 per-reader walk.

### Conventions

The stat-identity **includes `ctime_ns`** (adversarial-review hardening, second leaf commit): a
`chmod 000` changes neither `mtime_ns` nor `size`, so without ctime the cache would serve the old
good parse FOREVER where the pre-cache readers degraded to skip-every-tick; and a rewrite whose
`(mtime_ns, size)` was pinned via `os.utime` would never be seen. `ctime` changes on both, while
staying untouched for genuinely unchanged files — the hardening costs zero extra parses.

The module-level-cache discipline deliberately mirrors `projection_store._lifecycle_log_cache`, and
consumers take the snapshot through a keyword-only `contracts: ContractSnapshot | None = None`
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
  retried next build; only successful parses enter the cache.
- **Retention is bounded by the live enumeration.** Every build prunes cache entries whose paths are
  no longer enumerated.
- **Deliberate non-consumers:** the landing refresher (runs on the event-loop thread — sharing the
  cache would need locks) and the supervisor sweep (`serving/` territory) keep their own independent
  contract passes; they never touch this cache.

### Todos

None.

## Evidence

### Docs References

No external Domain Documentation source is configured for this memory repo (`system/sources.md` has
no entries).

No relevant documentation found after checking live sources; no Domain Documentation entries are configured.

### Repo-Internal References

The snapshot reuses the worktree subsystem's own enumeration and parser (`iter_leaf_enclosure_contracts`,
`load_contract`) rather than re-implementing either; the projection store owns the single per-tick
build; the three consumers accept the snapshot via keyword-only injection.

- Module docstring: one pass per tick, three prior walks, stat-identity cache, and the serialized-tick concurrency discipline. [1]
- `ContractSnapshot`: frozen read-only contracts mapping in enumeration order plus the `skipped` parse-failure set. [2]
- `ContractSnapshotCache`: `(mtime_ns, size, ctime_ns)` identity with the chmod/utime rationale, failure-never-cached retry, and live-set pruning; `build` implements the single pass. [3]
- `_cached_contract` reuses a parse only while all three stat fields hold; `_safe_stat` failure falls through to the uncached parse instead of introducing a new skip path; `build_contract_snapshot` is the standalone one-shot. [4]
- The enumeration and contract parser this module reuses (one parser per surface, owned by its producer). [5]
- `projection_store` owns the module-level `_contract_snapshot_cache` (with the three-walks rationale) and injects it into the per-tick `ProjectionInputState`. [6]
- `ProjectionInputState` holds the injected cache, builds the snapshot once per tasks refresh, and hands that one `ContractSnapshot` to `read_enclosures`, `read_engine_process_facts`/`refresh_engine_process_landing`, and drift-snapshot pruning. [7]
- `read_enclosures` and `read_engine_process_facts` take the keyword-only injected snapshot; `contracts=None` builds a local one with identical behavior. [8]
- Drift-snapshot pruning consumes the same snapshot, removing the third per-tick walk. [9]


### Cross-Repo References

No meaningful cross-repo references found.

Same-repository projection concern only.
