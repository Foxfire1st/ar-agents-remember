# mcp/src/agents_remember/worktrees/modules/git.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/worktrees/modules/git.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-12T19:06+02:00                     |
| lastVerifiedCommitHash | `6f1a7e9028d5d4858cf9c645f2448d5395fafc6a` |
| lastVerifiedCommitDate | 2026-06-12T19:52:16+02:00|
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

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Memory baseline code reuses these facade-exported Git helpers. | [baseline.py](agents-remember/mcp/src/agents_remember/memory/baseline.py) |
| Worktree tests cover changed-path behavior for long filesystem paths. | [test_worktree_support.py](agents-remember/mcp/tests/test_worktree_support.py) |

## Update History

- 2026-06-12T19:06+02:00 — Issue #83: added `committed_changed_paths()` (tree-diff `base..HEAD` ∩ `verified..HEAD`, `is_file`-filtered) and generalized `head_text_or_none` into `commit_text_or_none(repo, ref, rel)` so closeout worklists and body-gate baselines cover pre-committed work.
- 2026-06-10T04:47+02:00 — Added `head_text_or_none()` (`git show HEAD:<rel>`, `None` when absent) for the issue #56 closeout body/history gates.
- 2026-06-10T00:40+02:00 — Added `longest_tracked_path_length()` (`git ls-tree -r --name-only <ref>` with HEAD fallback, 0 for unborn repos) for the worktree-start Windows long-path preflight.
- 2026-05-25T20:41+02:00: Created during worktree manager module extraction.
