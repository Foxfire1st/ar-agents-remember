# mcp/src/agents_remember/memory_quality/integrity/check_missing_onboarding.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/memory_quality/integrity/check_missing_onboarding.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T00:00+02:00                     |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `../../../../overview.md`                  |

## Purpose

`check_missing_onboarding.py` checks only the current Git worktree additions
for eligible source files that do not yet have their required onboarding pair.

## Code Commentary

### Logic

The script collects added, copied, renamed, and untracked files from Git status
sources, resolves each path through the same storage/path-rule helpers used by
drift detection, and reports missing sidecar or inline onboarding for eligible
new files. For CLI runs it derives the canonical repository name from Git's
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
- Sidecar storage is detected by the boolean `is_sidecar_storage(storage_mode)`
  predicate (re-exported by the resolver), not by a truthy label string.
- Sidecar-managed files require `onboarding/<source-path>.md`.
- Inline-managed files require an inline onboarding block.
- Unsupported storage modes are reported instead of guessed.
- Git subprocesses use `stdin=subprocess.DEVNULL` and a scrubbed repository-selection environment.
  Both belong to `kernel.git_command.run_git`; this module must not grow a second runner.
- Linked-worktree basenames are not repository identifiers; the Git common
  directory is the repository identity source for CLI resolution.
- Sidecar existence and inline source reads use the shared filesystem helper so
  long Windows paths are checked consistently.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Drift helpers provide sidecar path construction and inline block parsing. | "def classify_source" | mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/drift.py:163-163 |
| Resolver helpers provide storage/path-rule decisions. | "def resolve_coordination_context" | mcp/src/agents_remember/kernel/coordination_context_resolver.py:129-129 |
| Tests cover untracked, staged, excluded, and renamed file cases. | `MissingOnboardingTests` | mcp/tests/test_missing_onboarding.py:22-154 |
| The kernel filesystem helper handles long-path sidecar and source probes. | "def absolute_path" | mcp/src/agents_remember/kernel/filesystem.py:10-10 |
| `run_git` — the single runner `require_git` wraps — owns the selector scrubbing, the DEVNULL stdin and the timeout classes. | `run_git` | mcp/src/agents_remember/kernel/git_command.py:94-145 |

## Update History

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B21 curator: replaced the `n/a` rows with exact
  anchors and fixer-generated ranges; exact non-fixing check returns zero findings.

- 2026-07-31T20:53+02:00 — 260731-EFA-L3 curator: the module-local `run_git` copy was removed; the
  helper is now `require_git`, wrapping `kernel.git_command.run_git`. Documented the rename, why it
  still returns a `CompletedProcess` (NUL-delimited `-z` output), and the three guards the copy was
  missing (environment scrubbing, 300s timeout, explicit UTF-8/surrogateescape decoding). The
  `stdin=subprocess.DEVNULL` invariant was re-pointed at the runner that now enforces it.
- 2026-07-31T00:00+02:00 — 260731-EFA-L2 (gate honesty, `PLR0911` armed with no exemptions):
  `missing_onboarding_for_source` was split into per-storage-mode helpers
  `_missing_sidecar_onboarding` and `_missing_inline_onboarding`; `main()` was updated for the
  resolver's `CoordinationHints` signature. Every reported state/path/note is unchanged.
  Verification metadata pinned until closeout stamps the L2 commit.
- 2026-05-31T12:50+02:00 — Source swapped the `sidecar_storage_label(storage_mode)` truthy-label check for the boolean `is_sidecar_storage(storage_mode)` resolver predicate (import and call site); recorded the predicate in Invariants And Boundaries (1.0.0 review remediation).
- 2026-05-24T18:51+02:00: Updated after the CLI began deriving repository identity from Git common directories and using long-path-safe filesystem probes.
- 2026-05-24T03:24+02:00: Refreshed verification metadata after the source commit landed.
- 2026-05-24T03:22+02:00: Created before the source commit so the new file has an onboarding pair before closeout.
