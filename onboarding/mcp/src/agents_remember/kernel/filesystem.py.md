# mcp/src/agents_remember/kernel/filesystem.py

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

## Evidence

### Docs References

No external documentation is needed for this standard-library path helper.

No relevant external documentation is needed for the local filesystem wrapper.

### Repo-Internal References

Same-repository closeout code and tests are the direct evidence for this helper.

- `c-09-git-worktree-manager` skill closeout planning uses the helper for changed-file filtering and onboarding metadata/catalog reads and writes; since MIK-R30 the card metadata refresh returns before any read or write on a converted memory tree. [1]
- The missing-onboarding pre-commit check uses the helper for sidecar existence and inline source reads. [2]

| The `read_ar_files` application entry point calls `read_text` for full reads and `read_text_range` for line-range reads. | `_read_source`; "filesystem.read_text(source_path)"; "filesystem.read_text_range(" | mcp/src/agents_remember/application/read_files.py:188-206; mcp/src/agents_remember/application/read_files.py:207-207; mcp/src/agents_remember/application/read_files.py:209-209; mcp/src/agents_remember/application/read_files.py:224-224; mcp/src/agents_remember/application/read_files.py:226-226 |

### Cross-Repo References

No cross-repository evidence is needed for this local helper.

No meaningful cross-repo references found.
