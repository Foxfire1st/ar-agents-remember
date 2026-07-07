# test_provider_index_lifecycle.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_provider_index_lifecycle.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-07T20:45+02:00                     |
| lastVerifiedCommitHash | `915e841a45cec40283902b69fe98e761672904af` |
| lastVerifiedCommitDate | 2026-07-07T18:43:43+02:00|
| governingOverview      | `../overview.md`                              |

## Governing Overview

[overview.md](../overview.md)

## Purpose

`test_provider_index_lifecycle.py` pins the repaired provider index lifecycle
of task 260707-HFX-L2: small diffs UPDATE indexes, never a teardown. The
developer-pinned failure cycle: providers seed fine on the first leaf (the
integration branch has no changes yet); after that leaf integrates, the next
worktree's seed saw a HEAD mismatch and hard-crashed into a full teardown plus
re-index from scratch (the refresh-all fallback), while the watchers never
delta-updated. The suite (19 tests) covers seed divergence relatability, the mismatch
proceed/stash/refuse split, the catch-up honesty rules — watcher-readiness
gating, phantom-residual classification, `caughtUp` only for a clean delta —
with their metrics row, the watcher-readiness helpers themselves, the
mtime-sync divergence exclusion, and the end-to-end
leaf1-integrates→leaf2-seeds cycle with honest behind-worktree assertions.

## Code Commentary

### Logic

Shared fixture helpers (`_git`, `_init_repo`, `_commit_file`) build REAL git
repositories and worktrees in temp roots — the shared-object-database
relatability that the divergence functions depend on is the thing under test,
so nothing git-related is mocked.

- `SeedDivergenceTests` — `seed_commit_divergence` reports the classified
  changed entries and count for relatable heads (two commits in one repo) and
  returns `None` for unrelatable heads (a 40-zero commit id that exists
  nowhere).
- `SeedMismatchTests` — the developer cycle's seed half:
  `_seed_commit_mismatch` PROCEEDS (returns no refusal) on a relatable
  divergence and stashes `{entries, count, sourceHead, targetHead}` on
  `args._cgc_seed_divergence`; equal heads proceed WITHOUT stashing a
  divergence; unrelatable heads still refuse with `ok: False` and the
  "unrelated" reason text.
- `SeedCatchupTests` — the catch-up honesty rules, with
  `_wait_for_cgc_watcher_ready` mocked ready via the `_ready()` helper:
  a small divergence `os.utime`-touches exactly the delta files that exist on
  disk (a listed but absent file becomes a residual, the untouched neighbor
  keeps its old mtime — fresh mtime is what makes the watcher re-index) and
  lands a `PROVIDER_INDEX_STATE_SCHEMA` row with the touch count in the
  central `ProviderMetricsStore`; a CLEAN delta to a ready watcher claims
  `caughtUp: true` with no `staleIndex`; a NOT-ready watcher (mocked
  `ready: False`) means no touch at all (the file keeps its old mtime) plus
  the honest "not ready" `staleIndex`; deletions and renames classify as
  `deleted-phantom`/`rename-source-phantom` residuals (the rename's new path
  is still touched) with `caughtUp: false`; a divergence above
  `cgc_seed_delta_max_files` returns the `skipped` payload with the
  `staleIndex` block (`served: true`, `behindFiles`, the
  "explicit 'cgc refresh'" reindex pointer) and touches nothing; no
  divergence and dry runs are no-ops.
- `WatcherReadinessTests` — the readiness helpers themselves:
  `_cgc_watcher_container_name` expands the provider's
  `containerNameTemplate` (no `<placeholder>` left) and returns `None`
  without a provider block or repo id; `_wait_for_cgc_watcher_ready` is ready
  when the single wheel-verified `"monitoring"` marker line appears in the
  (mocked) `docker logs` output ("Monitoring for file changes"), times out
  with the "no watch-ready marker" reason without one, and reports not-ready
  for an unresolved container name and on a dockerless host
  (`ContextProviderError`).
- `MemoryMtimeSyncDivergenceTests` — the cycle's grepai half, on a real
  source repo + `git worktree add` fixture: a file whose content diverges on
  the worktree branch keeps its FRESH checkout mtime
  (`divergentLeftFresh == 1`, the watcher re-embeds the delta) while the
  unchanged file syncs to the source's old mtime (the cloned index is
  reused); equal heads sync everything with `divergentLeftFresh == 0`.
- `IntegrationCycleReproTests` — the developer's exact crash cycle end to end
  at the seam level: leaf 1 integrates (the source repo advances one commit),
  leaf 2's checkout is one commit behind, the seed PROCEEDS (no refusal, no
  refresh-all) and the catch-up stage (ready watcher mocked) reports the
  one-file divergence HONESTLY: the file integrated ahead of the behind
  checkout is a `deleted-phantom` residual — the cloned graph carries it, the
  tree lacks it — so `caughtUp` is `false` with the residual surfaced in
  `staleIndex`; zero teardowns anywhere in the flow.

### Conventions

`unittest` with tempfile roots per test; real `git init`/`git worktree add`
fixtures (configured user, `-b main`) because head relatability and the shared
object database are the units under test. The catch-up and mismatch tests
drive the private seams directly with `argparse.Namespace` stand-ins and mock
only the watcher-readiness wait (`_ready()`); `WatcherReadinessTests` mocks
the docker seams (`docker_command`/`run_command`) on the provider_setup
module; the mtime tests cast a `SimpleNamespace` to `WorktreeContract`. No
docker or network access is required anywhere.

### Invariants And Boundaries

- No test mocks git: relatable/unrelatable is proven against real object
  databases, including the worktree-shares-the-source-odb case.
- The proceed paths must be teardown-free: no refusal payload, no
  `refresh-all` — a HEAD difference is a state to catch up from; below the
  bound a CLEAN delta to a ready watcher claims `caughtUp` while residuals
  and a not-ready watcher surface as `staleIndex` — honest, never a teardown.
- No touch may reach an unready watcher (inotify has no replay): the
  not-ready test proves the file's mtime is untouched.
- The refuse path stays: unrelatable heads must keep refusing (foreign-graph
  protection), and every stale-served path must surface itself
  (`staleIndex`), never silently.

## Docs References

No external documentation is needed for these standard-library unit tests.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| `seed_commit_divergence` / `_seed_commit_mismatch` under test. | [cgc/seed.py](agents-remember/mcp/src/agents_remember/providers/cgc/seed.py) |
| `_seed_catchup_results` and the delta bound under test. | [provider_setup.py](agents-remember/mcp/src/agents_remember/providers/provider_setup.py) |
| The index-state schema/row the catch-up test asserts in the store. | [metrics.py](agents-remember/mcp/src/agents_remember/providers/metrics.py) |
| `_sync_worktree_memory_mtimes` and `_memory_divergence_paths` under test. | [worktrees/modules/start.py](agents-remember/mcp/src/agents_remember/worktrees/modules/start.py) |
| The fallback-default flip the sibling setup suite pins. | [test_provider_setup.py](agents-remember/mcp/tests/test_provider_setup.py) |

## Cross-Repo References

No sibling repository evidence is needed for these tests.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-07-07T20:45+02:00 — 260707-HFX-L2 review fixes: the suite grew to 19 tests —
  `WatcherReadinessTests` (container-name template expansion/unresolvable, the single
  wheel-verified "monitoring" marker, timeout, dockerless), the not-ready-means-no-touch honesty
  test, the phantom-residual classification test (deleted/rename-source), the
  clean-delta-caughtUp test, and the cycle test now asserts the behind-worktree outcome HONESTLY
  (`caughtUp: false` with the `deleted-phantom` residual surfaced). Verification metadata pinned
  until closeout stamps the HFX-L2 commit.
- 2026-07-07T19:30+02:00 — Created for 260707-HFX-L2 (provider index lifecycle): pins seed
  divergence relatable/unrelatable, the mismatch proceed/stash/refuse split, catch-up
  touch/stale/no-op + the index-state metrics row, the mtime-sync divergence exclusion (real git
  worktree fixtures), and the leaf1-integrates→leaf2-seeds repro cycle with zero teardowns.
  Verification metadata pinned to the branch base until closeout stamps the HFX-L2 commit.
