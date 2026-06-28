# mcp/src/agents_remember/kernel/filesystem.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/kernel/filesystem.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-22T22:33+02:00                     |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1` |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
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

`read_text_range(path, start_line, end_line, *, encoding)` is the net-new ranged
reader added for the `read_ar_files` tool (slice 07); `read_text` stays the
whole-file read. It returns lines `[start_line, end_line]` (1-based, inclusive):
`start_line` below 1 clamps to 1, `end_line` clamps to EOF so a range past the
file's end yields what exists rather than erroring, a `start_line` beyond EOF
yields the empty string, and an inverted range (`end_line < start_line`) yields
the empty string. Honoring the "no silent truncation" rule is the caller's
responsibility: a `"full"` request must use `read_text`, never this helper.

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
| `c-09-git-worktree-manager` skill closeout planning uses the helper for changed-file filtering and onboarding metadata/catalog reads and writes. | closeout plan helpers | [git_worktree_manager.py](agents-remember/mcp/src/agents_remember/worktrees/git_worktree_manager.py) |
| The missing-onboarding pre-commit check uses the helper for sidecar existence and inline source reads. | missing-onboarding checks | [check_missing_onboarding.py](agents-remember/mcp/src/agents_remember/memory_quality/integrity/check_missing_onboarding.py) |
| Worktree support tests create and clean up deliberately long paths through this helper. | long-path regression tests | [test_worktree_support.py](agents-remember/mcp/tests/test_worktree_support.py) |
| The `read_ar_files` controller calls `read_text` for full reads and `read_text_range` for line-range reads. | ranged/full source read | [controllers/read_files.py](agents-remember/mcp/src/agents_remember/controllers/read_files.py) |

## Cross-Repo References

No cross-repository evidence is needed for this local helper.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-06-22T22:33+02:00 — Slice 07: documented the net-new `read_text_range` (1-based inclusive line slice; `start_line` clamped to 1, `end_line` clamped to EOF, `start_line` beyond EOF or an inverted range → empty string) added for the `read_ar_files` ranged source read; `read_text` stays the whole-file read. Body and references only — verification metadata pinned until closeout stamps the slice-07 code commit.
- 2026-05-24T18:51+02:00: Created for the closeout-tool fix after F-10 exposed long Windows path false negatives in onboarding closeout probes.
