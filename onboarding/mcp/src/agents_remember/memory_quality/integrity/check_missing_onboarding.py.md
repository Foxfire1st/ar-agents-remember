# mcp/src/agents_remember/memory_quality/integrity/check_missing_onboarding.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/memory_quality/integrity/check_missing_onboarding.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-24T18:51+02:00                     |
| lastVerifiedCommitHash | `a8ee8440dfa920d1153a4bb4bb43cc77534c3c90` |
| lastVerifiedCommitDate | 2026-05-25T15:22:52+02:00|
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

### Conventions

The module is a pre-code-commit closeout helper. Agents run it while new files
are still visible in the worktree, create any reported sidecars, then commit
code and refresh the new sidecars to the real code commit hash.

### Invariants And Boundaries

- Disabled path-rule matches are ignored.
- Sidecar-managed files require `onboarding/<source-path>.md`.
- Inline-managed files require an inline onboarding block.
- Unsupported storage modes are reported instead of guessed.
- Git subprocesses use `stdin=subprocess.DEVNULL`.
- Linked-worktree basenames are not repository identifiers; the Git common
  directory is the repository identity source for CLI resolution.
- Sidecar existence and inline source reads use the shared filesystem helper so
  long Windows paths are checked consistently.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Drift helpers provide sidecar path construction and inline block parsing. | [drift.py](agents-remember-md/mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/drift.py) |
| Resolver helpers provide storage/path-rule decisions. | [coordination_context_resolver.py](agents-remember-md/mcp/src/agents_remember/kernel/coordination_context_resolver.py) |
| Tests cover untracked, staged, excluded, and renamed file cases. | [test_missing_onboarding.py](agents-remember-md/mcp/tests/test_missing_onboarding.py) |
| The kernel filesystem helper handles long-path sidecar and source probes. | [filesystem.py](agents-remember-md/mcp/src/agents_remember/kernel/filesystem.py) |

## Update History

- 2026-05-24T18:51+02:00: Updated after the CLI began deriving repository identity from Git common directories and using long-path-safe filesystem probes.
- 2026-05-24T03:24+02:00: Refreshed verification metadata after the source commit landed.
- 2026-05-24T03:22+02:00: Created before the source commit so the new file has an onboarding pair before closeout.
