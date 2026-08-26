# mcp/src/agents_remember/worktrees/modules/git.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/worktrees/modules/git.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-22T10:39+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

Owns small repository-state helpers used by the `c-09-git-worktree-manager`
skill worktree lifecycle. It no longer owns a Git subprocess adapter: since
260731-EFA-L3 every helper here calls the single `run_git` in
`kernel/git_command.py`.

## Code Commentary

**The module-local `run_git` is gone (260731-EFA-L3).** This file used to define
its own copy — `kernel.git_command.run_git` with the environment guard, the
timeout and the explicit encoding all dropped — and every destructive worktree
operation reached git through it. The file now opens with
`from agents_remember.kernel.git_command import run_git` and a comment naming
what that cost:

```
# This module used to define its own `run_git` -- the kernel's function with the
# environment guard, the timeout and the explicit encoding all dropped -- and every
# destructive worktree operation (commit, merge --ff-only, reset --hard, rebase,
# branch -f, branch -D, worktree remove --force, push origin --delete) ran through
# it. With GIT_DIR exported those landed in whatever repository GIT_DIR named. The
# helpers below now call the one guarded runner; nothing else about them changed.
```

The helpers are otherwise unchanged; what they gained from the swap is
everything `run_git` guarantees:

- the repository-selector scrub — `git_environment()` copies the ambient
  environment minus `GIT_REPOSITORY_SELECTOR_ENV` (`GIT_DIR`, `GIT_WORK_TREE`,
  `GIT_INDEX_FILE`, `GIT_OBJECT_DIRECTORY`, `GIT_ALTERNATE_OBJECT_DIRECTORIES`,
  `GIT_COMMON_DIR`, `GIT_NAMESPACE`, `GIT_PREFIX`), so an exported `GIT_DIR` can
  no longer redirect `require_git(repo, ["commit", ...])` into another repository;
- the `stdin=subprocess.DEVNULL` + `-c safe.directory=<repo>` pair this module
  always had, plus `encoding="utf-8"` / `errors="surrogateescape"`, which the
  local copy lacked;
- a timeout. No helper here passes `timeout=`, so all of them take `run_git`'s
  default class, `GIT_LOCAL_TIMEOUT_SECONDS = 300` — the local band that bounds
  `rebase`/`merge`/`status`. Nothing in this module is unbounded any more, and a
  git call that exceeds 300s raises `subprocess.TimeoutExpired` out of the helper
  instead of hanging; no helper catches it.

The shared runner deliberately keeps `errors="surrogateescape"` so raw Git path
identity survives decoding. The facade now separates that internal representation
from transport-facing failure text: `_transport_safe_git_diagnostic` applies UTF-8
`backslashreplace` only when `require_git` is about to raise, preserving valid Unicode
while rendering an invalid byte as a literal escape such as `\udc81`. Raw successful
stdout and stderr remain untouched; only a failed command's `RuntimeError` diagnostic
is made safe for Pydantic/FastMCP JSON serialization.

The module exposes branch, commit, cleanliness,
worktree creation, commit-if-dirty, changed-path, and commit-content helpers
without owning workflow policy. `commit_text_or_none(repo, ref, rel)` returns a
path's text at any ref or `None` when absent — the closeout body gates use it
to diff sidecar content against the last verified memory commit;
`head_text_or_none` remains as the HEAD shorthand.

Closeout's certified-index path uses two deliberately separate helpers.
`run_pre_commit_hook_if_configured(repo)` resolves Git's effective hook path, skips cleanly when
no pre-commit hook exists, and otherwise invokes it through `git hook run pre-commit`.
`commit_verified_staged(repo, message)` commits only the existing index with `--no-verify`; it
never calls `add -A`, so a working-tree edit made after the strict wrapper cannot leak into the
commit and the already-run hook cannot restart after pytest. Ordinary `commit_if_dirty` retains
its original stage-and-commit behavior for callers that have not certified an index.

`committed_changed_paths(repo, base_commit, verified_commit)` (issue #83)
collects the paths changed by commits closeout has not verified yet: the
tree-diff `base..HEAD` intersected with `verified..HEAD` when a distinct
verified commit exists, so content the synced source branch already carries and
content a previous closeout already verified both drop out. The shared
`filesystem.is_file` filter keeps committed deletions out of the worklist,
matching `changed_worktree_paths` dirty-deletion behavior.

`changed_files_with_counts(repo, base, head=None)` (operations-integration L3) is the
change-set primitive behind the serving change-set API (`serving/changeset.py`). It
parses `git diff --numstat --name-status --find-renames` over `base..head` (or
`base..worktree` when `head` is `None`) into per-file
`{path, insertions, deletions, status}`. Unlike the name-only `changed_*_paths` above it
**keeps deletions** (status `D`), reports per-file insertion/deletion counts (`None` for
binary files, whose numstat shows `-`), and in worktree mode appends untracked files as
additions (status `A`). `_rename_aware_path` reconstructs the post-rename path from a
numstat rename field (`a => b` / `p/{a => b}/q`) so the counts join the `--name-status`
`R` row by the new path.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The one `run_git` every helper here calls: the `GIT_DIR`-family scrub, the DEVNULL stdin guard, and the three timeout classes. | `run_git` | mcp/src/agents_remember/kernel/git_command.py:94-145 |
| Memory baseline code reuses these facade-exported Git helpers. | "def run_drift" | mcp/src/agents_remember/memory/baseline.py:85-85 |
| The L3 serving change-set API consuming `changed_files_with_counts` + `commit_text_or_none`. | "def task_changeset" | mcp/src/agents_remember/serving/changeset.py:80-80 |
| Worktree tests cover changed-path behavior for long filesystem paths. | `test_changed_worktree_paths_includes_long_files` | mcp/tests/test_worktree_support_tests_1.py:1150-1163 |
| The extracted closeout staging owner runs the configured hook before its strict Dagger wrapper and later commits the certified index through this Git facade. | `gate_staged_code`; `commit_verified_staged` | mcp/src/agents_remember/worktrees/modules/git.py:188-198; mcp/src/agents_remember/worktrees/queue/closeout_staged_quality.py:77-129 |
| The hook-failure regression proves the raw runner retains a surrogateescaped byte while the facade exception is UTF-8 JSON serializable. | `test_failed_hook_diagnostic_with_invalid_bytes_is_json_serializable` | mcp/tests/test_git_command.py:337-354 |

## 260815-DAG-L4 Integration-Authority Impact

L4 makes task-derived integration refs mechanically non-ordinary: repository defaults, sprint supers, and active atomic-series refs are censused across code and external memory. Mutation is admitted only through exact lifecycle authority, named-ref compare-and-swap, queue/repository serialization, or a terminal capability; stale topology, aliases, ambient checkouts, and torn recovery fail closed.

## Update History

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1 candidate-11 curation rebind: refreshed formatter-moved source coordinates against accepted tree `4241908c`; where applicable, replaced a deleted coordinator anchor with the sole current owner. Verification metadata remains pinned until governed closeout.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-15T23:38+02:00 — Reconciled this worktree owner's role in task-derived protected-ref authority, exact named-ref movement, and crash-safe recovery. Verification metadata remains closeout-owned.
- 2026-08-14T05:26Z — L23 final curator: re-anchored the configured-hook/certified-index contract
  after staged quality moved to its cohesive module; Git ownership is unchanged. Verification
  remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-12T03:31+02:00 — 260731-EFA-L22 closeout repair: preserved surrogateescape inside the
  shared Git runner but escaped invalid bytes at `require_git`'s diagnostic boundary, preventing a
  malformed failed-hook message from crashing MCP response serialization. Added the exact invalid-byte
  hook regression reference. Verification metadata remains pinned until closeout stamps the repair.

- 2026-08-10T12:46+02:00 — L9 closeout-order repair: added the configured-hook runner and the
  exact-index `commit_verified_staged` helper. The latter never restages and uses `--no-verify`
  because the hook was already executed before the pytest-final wrapper. Verification metadata
  stays pinned until closeout stamps the repair commit.

- 2026-07-31T20:50+02:00 — 260731-EFA-L3 curator: the module-local `run_git` was deleted and every
  helper now calls `kernel.git_command.run_git`, so the old Purpose ("Owns the Git subprocess
  adapter") and the old Code Commentary opening ("All Git commands run with
  `stdin=subprocess.DEVNULL` and an explicit `safe.directory` override") were both false — the local
  copy also dropped the `GIT_DIR`-family scrub, the encoding and any timeout. Rewrote both to
  describe the shared runner, the eight `GIT_REPOSITORY_SELECTOR_ENV` names it pops, and the
  `GIT_LOCAL_TIMEOUT_SECONDS = 300` default that now bounds every helper (none passes `timeout=`,
  none catches `subprocess.TimeoutExpired`). Added the `kernel/git_command.py` reference row.
  Verification metadata pinned until closeout stamps the L3 commit.
- 2026-06-29T15:30+02:00 — operations-integration L3: added `changed_files_with_counts(repo, base, head=None)` (+ the `_rename_aware_path` helper), the change-set primitive behind the serving change-set API (`serving/changeset.py`): per-file `{path, insertions, deletions, status}` via `git diff --numstat --name-status --find-renames`, KEEPING deletions, binary→`None` counts, untracked→`A` in worktree mode, rename→post-rename path. Unlike `changed_worktree_paths`/`committed_changed_paths` it does not drop deletions. Verification metadata pinned to the task base until closeout stamps the L3 code commit.
- 2026-06-12T19:06+02:00 — Issue #83: added `committed_changed_paths()` (tree-diff `base..HEAD` ∩ `verified..HEAD`, `is_file`-filtered) and generalized `head_text_or_none` into `commit_text_or_none(repo, ref, rel)` so closeout worklists and body-gate baselines cover pre-committed work.
- 2026-06-10T04:47+02:00 — Added `head_text_or_none()` (`git show HEAD:<rel>`, `None` when absent) for the issue #56 closeout body/history gates.
- 2026-06-10T00:40+02:00 — Added `longest_tracked_path_length()` (`git ls-tree -r --name-only <ref>` with HEAD fallback, 0 for unborn repos) for the worktree-start Windows long-path preflight.
- 2026-05-25T20:41+02:00: Created during worktree manager module extraction.
