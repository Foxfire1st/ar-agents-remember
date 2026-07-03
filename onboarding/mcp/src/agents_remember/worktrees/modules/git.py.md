# mcp/src/agents_remember/worktrees/modules/git.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/worktrees/modules/git.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-29T15:30+02:00                     |
| lastVerifiedCommitHash | `ad30dd38c3dcfa13fb85f44b281488499e92519a` |
| lastVerifiedCommitDate | 2026-07-03T08:10:19+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

Owns the Git subprocess adapter and small repository state helpers used by the
`c-09-git-worktree-manager` skill worktree lifecycle.

## Code Commentary

All Git commands run with `stdin=subprocess.DEVNULL` and an explicit
`safe.directory` override. The module exposes branch, commit, cleanliness,
worktree creation, commit-if-dirty, changed-path, and commit-content helpers
without owning workflow policy. `commit_text_or_none(repo, ref, rel)` returns a
path's text at any ref or `None` when absent — the closeout body gates use it
to diff sidecar content against the last verified memory commit;
`head_text_or_none` remains as the HEAD shorthand.

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

| Finding | Source Path |
| --- | --- |
| Memory baseline code reuses these facade-exported Git helpers. | [baseline.py](agents-remember/mcp/src/agents_remember/memory/baseline.py) |
| The L3 serving change-set API consuming `changed_files_with_counts` + `commit_text_or_none`. | [serving/changeset.py](agents-remember/mcp/src/agents_remember/serving/changeset.py) |
| Worktree tests cover changed-path behavior for long filesystem paths. | [test_worktree_support.py](agents-remember/mcp/tests/test_worktree_support.py) |

## Update History

- 2026-06-29T15:30+02:00 — operations-integration L3: added `changed_files_with_counts(repo, base, head=None)` (+ the `_rename_aware_path` helper), the change-set primitive behind the serving change-set API (`serving/changeset.py`): per-file `{path, insertions, deletions, status}` via `git diff --numstat --name-status --find-renames`, KEEPING deletions, binary→`None` counts, untracked→`A` in worktree mode, rename→post-rename path. Unlike `changed_worktree_paths`/`committed_changed_paths` it does not drop deletions. Verification metadata pinned to the task base until closeout stamps the L3 code commit.
- 2026-06-12T19:06+02:00 — Issue #83: added `committed_changed_paths()` (tree-diff `base..HEAD` ∩ `verified..HEAD`, `is_file`-filtered) and generalized `head_text_or_none` into `commit_text_or_none(repo, ref, rel)` so closeout worklists and body-gate baselines cover pre-committed work.
- 2026-06-10T04:47+02:00 — Added `head_text_or_none()` (`git show HEAD:<rel>`, `None` when absent) for the issue #56 closeout body/history gates.
- 2026-06-10T00:40+02:00 — Added `longest_tracked_path_length()` (`git ls-tree -r --name-only <ref>` with HEAD fallback, 0 for unborn repos) for the worktree-start Windows long-path preflight.
- 2026-05-25T20:41+02:00: Created during worktree manager module extraction.
