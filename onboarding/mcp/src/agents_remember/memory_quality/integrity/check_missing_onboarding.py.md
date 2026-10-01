# mcp/src/agents_remember/memory_quality/integrity/check_missing_onboarding.py

## Governing Overview

[overview.md](../../../../overview.md)

## Purpose

`check_missing_onboarding.py` checks only the current Git worktree additions
for eligible source files that do not yet have their required onboarding pair.

## Code Commentary

### Logic

The script derives one isolated add-all candidate tree and diffs it against
`HEAD`, then resolves each added, copied, or renamed target through the same
storage/path-rule helpers used by drift detection. This makes the preflight
match the tree closeout would commit: a staged add that was later deleted does
not remain a false onboarding obligation, while untracked files still enter the
candidate. For CLI runs it derives the canonical repository name from Git's
common directory, so a linked worktree can be named after the task without
changing external-memory resolution. It intentionally does not scan the whole
historical repository.

`missing_onboarding_for_source` is now a three-way router (260731-EFA-L2): `disabled` returns
`None`, sidecar storage delegates to `_missing_sidecar_onboarding(onboarding_root, source_file,
storage_mode)`, `inline` delegates to `_missing_inline_onboarding(code_repository_root,
source_file, storage_mode)`, and anything else falls through to the single `unsupported` row. The
two helpers own one storage mode each: the sidecar one reports the mirrored path when that file
does not exist; the inline one reports `unsupported` on a `UnicodeDecodeError` and `missing` when
no inline block is found. Every `MissingOnboarding` state, `expected_onboarding` value and note
string is byte-identical to the pre-split version.

`main()` passes `--topology` / `--coordination-root` / `--settings-path` / `--onboarding-root`
to `resolve_coordination_context` inside a `CoordinationHints(...)`, matching the resolver's
current signature.

**The tree it measures now comes from the caller, not from the resolver (260915-KS-L23, D-34).** The
check splits the two inputs the way the contract-scoped memory-quality route already does: the
**settings** come from the resolved context, while the **measured tree** comes from
`--onboarding-root` when the caller supplied one and from `context.onboarding_root` otherwise. Before
the change the resolver's own root was used unconditionally, so an explicitly requested tree could be
silently replaced by the official memory repo and the command would answer confidently about the
wrong root. The two coincide for an official memory repo and differ for a leaf enclosure's memory
worktree, whose settings live in the official repo the enclosure was cut from; `--onboarding-root`'s
help text now states both supported shapes and the settings rule, and the `does not exist` refusal
names the root actually measured.

Since 260731-EFA-L3 the module runs no git subprocess of its own. It imports `run_git` from
`agents_remember.kernel.git_command` and keeps one helper, `require_git`, which adds the module's
contract that any git failure is fatal and — unlike the `require_git` helpers elsewhere — returns
the `CompletedProcess` instead of stripped text, because `worktree_added_sources` and
`code_repository_name_from_git` read NUL-delimited (`-z`) output that a `.strip()` would corrupt:

```python
def require_git(repo_root: Path, args: list[str]) -> subprocess.CompletedProcess[str]:
    result = run_git(repo_root, args)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or f"git {' '.join(args)} failed")
    return result
```

Raise-on-failure is unchanged behaviour: the deleted local copy already raised, it was just named
`run_git`. What the module gains is what its copy was missing — `env=git_environment()`, so an
ambient `GIT_DIR` cannot make `git diff --cached` / `git ls-files --others` answer out of a
different repository and report "no new files"; `timeout=GIT_LOCAL_TIMEOUT_SECONDS` (300s) instead
of no bound at all; and explicit `encoding="utf-8"` with `errors="surrogateescape"`, so a
non-UTF-8 filename in the `-z` listing decodes instead of raising.

### Conventions

The module is a pre-code-commit closeout helper. Agents run it while new files
are still visible in the worktree, create any reported sidecars, then commit
code and refresh the new sidecars to the real code commit hash.

### Invariants And Boundaries

- Disabled path-rule matches are ignored.
- The measured tree is the caller's `--onboarding-root` when one was supplied, and the resolved
  context's root only when it was not; the **settings** always come from the resolved context. The
  command must not silently substitute the official memory root for a tree the caller named, and it
  must not resolve settings from the measured worktree (which carries no `system/` of its own).
- Sidecar storage is detected by the boolean `is_sidecar_storage(storage_mode)`
  predicate (re-exported by the resolver), not by a truthy label string.
- Sidecar-managed files require `onboarding/<source-path>.md`.
- Inline-managed files require an inline onboarding block.
- Unsupported storage modes are reported instead of guessed.
- Candidate discovery uses `worktree_candidate_tree` with an isolated temporary index and never
  reads the real staged and unstaged layers as independent authorities.
- Git subprocesses use `stdin=subprocess.DEVNULL` and a scrubbed repository-selection environment.
  Both belong to `kernel.git_command.run_git`; this module must not grow a second runner.
- Linked-worktree basenames are not repository identifiers; the Git common
  directory is the repository identity source for CLI resolution.
- Sidecar existence and inline source reads use the shared filesystem helper so
  long Windows paths are checked consistently.

## Evidence

### Repo-Internal References

- Drift helpers provide sidecar path construction and inline block parsing. [1]
- Resolver helpers provide storage/path-rule decisions. [2]
- The checker owns source/onboarding absence classification; deleted case inventories are not current coverage evidence. [3]
- The kernel filesystem helper handles long-path sidecar and source probes. [4]
- `run_git` — the single runner `require_git` wraps — owns the selector scrubbing, the DEVNULL stdin and the timeout classes. [5]
