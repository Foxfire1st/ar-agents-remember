# test_serving_changeset.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_serving_changeset.py`      |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-12T12:55+02:00 |
| lastVerifiedCommitHash | `eb7ea60ab9919f009fef58f81afe5861aa1709da` |
| lastVerifiedCommitDate | 2026-08-22T11:44:33+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| The change-set API under test (`task_changeset`, `file_diff`, `master_changeset`). | `task_changeset`; `file_diff`; `master_changeset` | mcp/src/agents_remember/serving/changeset.py:78-97; mcp/src/agents_remember/serving/changeset.py:100-125; mcp/src/agents_remember/serving/changeset.py:225-269 |
| The git primitive under test (`changed_files_with_counts`). | `changed_files_with_counts` | mcp/src/agents_remember/worktrees/modules/git.py:271-310 |
| The shared scope layer the extraction test checks (`resolve_scope`, `run_scoped`, `FileScope`). | `resolve_scope`; `run_scoped`; `FileScope` | mcp/src/agents_remember/serving/scope.py:96-107; mcp/src/agents_remember/serving/scope.py:147-193; mcp/src/agents_remember/serving/scope.py:207-227 |
| The files module re-exporting "Scope resolution (``FileScope`` / ``resolve_scope`` / ``run_scoped``) + the language"/"reuses them" (asserted here). | "def list_dir(scope: FileScope"; "reuses them" | mcp/src/agents_remember/serving/files.py:20-20; mcp/src/agents_remember/serving/files.py:163-163 |
| `WorktreeContract` / `write_contract` used to drive the change-set scope. | `WorktreeContract`; `write_contract` | mcp/src/agents_remember/worktrees/worktree_contract.py:230-289; mcp/src/agents_remember/worktrees/worktree_contract.py:484-485 |
| `McpRuntimeConfig` / `RepositoryScope` constructed by the master test. | `McpRuntimeConfig`; "class RepositoryScope:" | mcp/src/agents_remember/kernel/primitives/runtime_config.py:113-137; mcp/src/agents_remember/kernel/primitives/runtime_config.py:76-81 |
| The L1 files test whose harness/style this mirrors. | `PathGuardTests` | mcp/tests/test_serving_files.py:80-111 |

## 260731-EFA-L2 Delta — the scope-resolution fall-through

Five tests pinning which diff a file request resolves to when it names no leaf:

- no leaf answers the **master series** diff; no leaf **or** master falls through to the
  enclosure scope;
- a master file diff maps a path breach to `bad-path` and an unknown series to `not-found`;
- a scoped file diff **reports an unknown scope rather than guessing** one.

## Update History

- 2026-08-22T12:15+02:00 — 260821-CLIVE-L1: re-read the C2 change-set fixture claim after `write_contract` extracted canonical publication text into `contract_publication_text`; retained the wording because contract-backed scope authority is unchanged, and rebound only the `write_contract` declaration range. Verification is stamped to C2 by closeout.

- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-04T18:20+02:00 — 260731-EFA-L6 S18-B15 curator: resolved 4 citation findings, all duplicate
  sources: deduplicated the repeated ranges in the scope-layer row (21× `scope.py:96-107`, 6×
  `147-193`), the `WorktreeContract` row (6× `231-286`), and the config row (6× `config.py:68-73`),
  keeping one copy of each operative span plus the `run_scoped`, `write_contract`, and
  `McpRuntimeConfig` ranges. Scoped recheck clean.

- 2026-08-02T16:44:12+02:00 — 260731-EFA-L6 W1-B05 curator: anchored 6 citation items; scoped citation check now passes.

- 2026-07-31T15:32+02:00 — 260731-EFA-L2 curator: recorded the arms this leaf added; the rest of this card was re-read against the file and remains true. Call sites in this module now build parameter objects (see the route overview) — what the suite proves is unchanged. Verification metadata pinned until closeout stamps the code commit.

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
