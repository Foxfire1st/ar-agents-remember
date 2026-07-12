# test_serving_changeset.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_serving_changeset.py`      |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-12T12:55+02:00 |
| lastVerifiedCommitHash | `300664e63f2dbb5f0701d37bbc17ff5358960c77` |
| lastVerifiedCommitDate | 2026-07-12T18:11:57+02:00|
| governingOverview      | `../overview.md`                           |

## Governing Overview

[../overview.md](../overview.md)

## Purpose

`test_serving_changeset.py` is the test suite for the operations-integration L3
change-set API (`serving/changeset.py`) and its git primitive
(`worktrees/modules/git.changed_files_with_counts`): the per-file counts/status over real
git repos, the per-enclosure change-set + sidecar pairing, the BEFORE/AFTER file diff, and
the master NET series diff — all over real temp git repos + written contracts, so the
behaviour is exercised end-to-end rather than mocked.

## Code Commentary

### Logic

The regression suite now pins the real mixed-case persisted leaf-id shape,
rejects lookup across another master enclosure, and verifies the route-level
`includeLeaves=false` opt-out without invoking per-leaf summaries. Existing
real-git committed, working, and coherent master range assertions remain the
guards against changing diff semantics.

Real git repos are built per case (`_init_repo` / `_commit_all` via the `safe.directory`
`_git` helper), so the diff numbers are produced by git, not stubs:

- **`ChangedCountsTests`** pins `changed_files_with_counts`: a worktree diff covering a
  modify (`+1`), a delete (status `D`, kept — not dropped like the name-only helpers), an
  untracked add (status `A`), and a binary modify (`insertions`/`deletions` `None`); plus
  a committed rename (`git mv` across two commits) detected as status `R` under the
  post-rename path, with the old path absent.
- **`TaskChangesetTests`** drives `task_changeset` / `file_diff` over a code+memory
  worktree pair behind a `_write_leaf_contract`-written `WorktreeContract` and a
  hand-built `FileScope`. It asserts the code counts + `hasSidecar` split (a file with a
  sidecar vs an untracked add without), the memory changed set, the summed counters, and
  `file_diff` for a modified file (before+after), an added file (`before=None`), a deleted
  file (`after=None`), and the memory side (`kind="memory"`). `test_mainline_scope_has_no_changeset`
  is the 404 guard (a mainline `FileScope` → `FileNotFoundError`).
- **`MasterChangesetTests`** drives the series **NET** diff over a written master contract where
  the source branch remains at the base and the work branch carries ≥2 commits: `master_changeset`
  returns the net `git diff base..work-tip` for code and memory (NOT a doubled sum),
  `master_file_diff` returns before/after at base vs the same work tip, the per-leaf `leaves[]`
  breakdown is kept alongside, the landed fallback fast-forwards source and deletes the work branch
  to prove source-tip behavior remains, and an unknown master degrades to an empty net.
- **`LeafChangesetTests`** (L4a) drives `leaf_changeset` / `leaf_file_diff` over written leaf
  contracts (a shared `_write_leaf` helper places them under `tasks/R/t/enclosures/<leaf>/`):
  committed = base→`code_commit` resolved with **no live worktree** (a cleaned leaf, the durable
  path) and proving slugify (`leaf="260628-L4a"` → `leaf_id="260628-l4a"`); the committed fallback
  to the worktree HEAD (NOT the dirty tree) when `code_commit` is empty; working = HEAD→worktree
  uncommitted delta only; `working` without a live worktree → `FileNotFoundError`; an unknown leaf
  and a wrong-master scope both raise; and the committed/working `leaf_file_diff` before/after.
- **`LeafChangesetRouteTests`** (L4a) builds a `FastAPI` app via `register_changeset_routes` + a
  `TestClient` and pins the selector validation on `/api/changeset/task` + `/file-diff`: a `leaf`
  without `master` → `400`, a bad `mode` → `400`, a valid committed leaf → `200` (echoing `mode`),
  a `working` leaf with no worktree → `404`, and a committed `leaf_file_diff` → `200`.
- **`ScopeExtractionTests`** guards the L3 extraction: `scope.resolve_scope` /
  `run_scoped` / `language_for` are callable and `files.FileScope is scope.FileScope`
  (plus `files._resolve_within is scope._resolve_within`) — i.e. `files.py` re-exports the
  moved symbols so L1's callers/tests are unbroken.

### Conventions

Mirrors `test_serving_files.py`: `sys.path.insert(0, str(MCP_SRC))` so imports resolve to
this checkout, `unittest.TestCase` with a `tempfile.TemporaryDirectory` per case, and a
`_by_path` helper to index changed-file lists by path. Run with
`PYTHONPATH=mcp/src python -m pytest mcp/tests/test_serving_changeset.py -q`.

### Invariants And Boundaries

- The git-counts assertions use **real** repos (modify/add/delete/binary/rename) so the
  numstat + name-status parsing and the binary/rename edge cases are regression-guarded.
- The change-set assertions run over a real worktree pair behind a written contract, so
  the base→worktree range, the sidecar pairing, and the before/after content are end-to-end.
- The master assertions keep in-flight series commits on the contract work branch first, then
  delete that branch after fast-forwarding source, so both the work-tip resolver and landed fallback
  are regression-guarded against real git refs.
- The extraction test is the guard that the L3 `scope.py` split kept `files.py` callers
  (and L1's test imports) working.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The change-set API under test (`task_changeset`, `file_diff`, `master_changeset`). | [serving/changeset.py](agents-remember/mcp/src/agents_remember/serving/changeset.py) |
| The git primitive under test (`changed_files_with_counts`). | [worktrees/modules/git.py](agents-remember/mcp/src/agents_remember/worktrees/modules/git.py) |
| The shared scope layer the extraction test checks (`resolve_scope`, `run_scoped`, `FileScope`). | [serving/scope.py](agents-remember/mcp/src/agents_remember/serving/scope.py) |
| The files module re-exporting `FileScope`/`_resolve_within` (asserted here). | [serving/files.py](agents-remember/mcp/src/agents_remember/serving/files.py) |
| `WorktreeContract` / `write_contract` used to drive the change-set scope. | [worktrees/worktree_contract.py](agents-remember/mcp/src/agents_remember/worktrees/worktree_contract.py) |
| `McpRuntimeConfig` / `RepositoryScope` constructed by the master test. | [mcp/config.py](agents-remember/mcp/src/agents_remember/mcp/config.py) |
| The L1 files test whose harness/style this mirrors. | [test_serving_files.py](agents-remember/mcp/tests/test_serving_files.py) |

## Update History

- 2026-07-12T12:55+02:00 — 260712-TRH-L2: added regressions for mixed-case leaf normalization, exact master enclosure scoping, and the master summary opt-out while retaining the existing real-git range tests. Verification metadata pinned until closeout stamps the L2 code commit.

- 2026-07-04T23:43+02:00 — L8 content update: `MasterChangesetTests` now models an in-flight series with source at base and code/memory work branches ahead, asserts master counters equal the real base→work-tip git diff, checks `master_file_diff` AFTER content from the same work tip, and covers the landed fallback after source fast-forward plus work-branch deletion. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-03T12:50+02:00 — No content impact: L15 sorted the third-party import block (everything stays below the load-bearing sys.path.insert); no test logic change.
- 2026-06-29T23:00+02:00 — L4a: added `LeafChangesetTests` (committed/working leaf views — cleaned-leaf
  resolution + slugify, committed worktree-HEAD fallback, working uncommitted-only, no-worktree→404,
  unknown-leaf / wrong-master raise, leaf file-diff) and `LeafChangesetRouteTests` (FastAPI `TestClient`
  selector validation: leaf-needs-master 400, bad-mode 400, committed 200, working-no-worktree 404). Imports
  `FastAPI`/`TestClient`/`register_changeset_routes`/`leaf_*`. Verification metadata pinned until closeout
  stamps the L4a commit.
- 2026-06-29T17:00+02:00 — L4 follow-up: `MasterChangesetTests` now covers the series NET diff — net-not-sum,
  the base→tip `master_file_diff`, the per-leaf breakdown kept, and unknown-master→empty (replacing the old
  sum-of-leaves dedup assertions). Verification metadata pinned until closeout stamps the L4 follow-up commit.
- 2026-06-29T15:30+02:00 — Created for operations-integration L3: the `serving/changeset.py` test suite — `ChangedCountsTests` (modify/add/delete/binary + committed rename over real git), `TaskChangesetTests` (per-enclosure code+memory counts, `hasSidecar`, before/after file diff incl. add/delete/memory-side, mainline 404), `MasterChangesetTests` (accumulation + dedup of a shared path), and `ScopeExtractionTests` (the L3 scope.py extraction is re-exported by files.py). Verification metadata pinned to the task base until closeout stamps the L3 code commit.
