# mcp/src/agents_remember/kernel/filesystem.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/kernel/filesystem.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-22T10:39+02:00 |
| lastVerifiedCommitHash | `7833df0b219bba560f67f6e1158c3f4f155e1ce6`
| lastVerifiedCommitDate | 2026-08-26T15:02:28+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation is needed for the local filesystem wrapper. | n/a | n/a |

## Repo-Internal References

Same-repository closeout code and tests are the direct evidence for this helper.

| Finding | Anchor | Source |
| --- | --- | --- |
| `c-09-git-worktree-manager` skill closeout planning uses the helper for changed-file filtering and onboarding metadata/catalog reads and writes. | "def changed_worktree_paths"; `onboarding_refresh_plan_for_context`; `refresh_entity_fingerprints_for_context`; `refresh_onboarding_metadata_for_context` | mcp/src/agents_remember/worktrees/modules/git.py:228-228; mcp/src/agents_remember/worktrees/modules/onboarding.py:77-118; mcp/src/agents_remember/worktrees/modules/onboarding.py:607-653; mcp/src/agents_remember/worktrees/modules/onboarding.py:854-895 |
| The missing-onboarding pre-commit check uses the helper for sidecar existence and inline source reads. | `_missing_sidecar_onboarding`; `_missing_inline_onboarding`; `filesystem.exists`; `filesystem.read_text` | mcp/src/agents_remember/memory_quality/integrity/check_missing_onboarding.py:111-124; mcp/src/agents_remember/memory_quality/integrity/check_missing_onboarding.py:127-150 |
| Worktree support tests create and clean up deliberately long paths through this helper. | `test_changed_worktree_paths_includes_long_files`; `test_onboarding_refresh_plan_detects_long_sidecar_paths` | mcp/tests/test_worktree_support_tests_1.py:1136-1149; mcp/tests/test_worktree_support_tests_1.py:1168-1185 |
| The `read_ar_files` application entry point calls `read_text` for full reads and `read_text_range` for line-range reads. | `_read_source`; "filesystem.read_text(source_path)"; "filesystem.read_text_range(" | mcp/src/agents_remember/application/read_files.py:188-206; mcp/src/agents_remember/application/read_files.py:207-207; mcp/src/agents_remember/application/read_files.py:209-209 |

## Cross-Repo References

No cross-repository evidence is needed for this local helper.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1 candidate-11 curation rebind: refreshed formatter-moved source coordinates against accepted tree `4241908c`; where applicable, replaced a deleted coordinator anchor with the sole current owner. Verification metadata remains pinned until governed closeout.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-03T03:56+02:00 — 260731-EFA-L6 W3-B10 curator: anchored 4 table citations and replaced 4 stale source references with exact helper implementations/tests; no unresolved Tier-3 claims.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T16:35+02:00 — No content impact: the only change to
  `mcp/src/agents_remember/kernel/filesystem.py` since the L2 base commit is the whole-tree `ruff
  format` pass in `00e8379`, which re-wrapped 3 line(s) with no token change whatsoever. Checked
  by parsing both revisions and comparing the abstract syntax trees (identical) and the comment
  tokens (identical), so no symbol, signature, default, decorator, control-flow branch, docstring,
  or assertion this card describes has moved, and every claim this card makes about its own source
  still holds.

- 2026-07-31T00:00+02:00 — 260731-EFA-L2 attestation: this file was touched ONLY by the
  whole-tree `ruff format` pass (commit `00e8379`) — line reflow, no behaviour, contract,
  structure or responsibility change. The sidecar was re-read against the current source and
  every claim in it still holds, so it was deliberately not rewritten. Verification metadata
  pinned until closeout stamps the L2 commit.
- 2026-06-22T22:33+02:00 — Slice 07: documented the net-new `read_text_range` (1-based inclusive line slice; `start_line` clamped to 1, `end_line` clamped to EOF, `start_line` beyond EOF or an inverted range → empty string) added for the `read_ar_files` ranged source read; `read_text` stays the whole-file read. Body and references only — verification metadata pinned until closeout stamps the slice-07 code commit.
- 2026-05-24T18:51+02:00: Created for the closeout-tool fix after F-10 exposed long Windows path false negatives in onboarding closeout probes.
