# mcp/src/agents_remember/kernel/filesystem.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/kernel/filesystem.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-24T18:51+02:00                     |
| lastVerifiedCommitHash | `31846c1136f0fe75503a63fb557303a79fa022e8` |
| lastVerifiedCommitDate | 2026-05-24T23:07:31+02:00|
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

`filesystem.py` centralizes the filesystem operations that need Windows
extended-path handling when closeout and onboarding integrity code touches deep
mirrored source/onboarding paths.

## Code Commentary

### Logic

The module converts a `Path` to an absolute Windows extended path when running
on Windows, including UNC path handling, and otherwise leaves paths unchanged.
It exposes narrow wrappers for existence checks, file checks, directory
creation, and UTF-8 text reads/writes so callers do not scatter `\\?\` path
construction across closeout code.

### Invariants And Boundaries

- The helper is for concrete filesystem operations, not Git pathspecs.
- Non-Windows platforms receive the original `Path`.
- Relative paths are anchored to the current process directory before adding a
  Windows extended prefix.
- Callers still decide whether a path is allowed by repository or memory
  containment rules.

## Docs References

No external documentation is needed for this standard-library path helper.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation is needed for the local filesystem wrapper. | n/a | n/a |

## Repo-Internal References

Same-repository closeout code and tests are the direct evidence for this helper.

| Finding | Citations | Source Path |
| --- | --- | --- |
| C-09 closeout planning uses the helper for changed-file filtering and onboarding metadata/catalog reads and writes. | closeout plan helpers | [git_worktree_manager.py](agents-remember-md/mcp/src/agents_remember/worktrees/git_worktree_manager.py) |
| The missing-onboarding pre-commit check uses the helper for sidecar existence and inline source reads. | missing-onboarding checks | [check_missing_onboarding.py](agents-remember-md/mcp/src/agents_remember/memory_quality/integrity/check_missing_onboarding.py) |
| Worktree support tests create and clean up deliberately long paths through this helper. | long-path regression tests | [test_worktree_support.py](agents-remember-md/mcp/tests/test_worktree_support.py) |

## Cross-Repo References

No cross-repository evidence is needed for this local helper.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-24T18:51+02:00: Created for the closeout-tool fix after F-10 exposed long Windows path false negatives in onboarding closeout probes.
