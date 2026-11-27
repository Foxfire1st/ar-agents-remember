# mcp/src/agents_remember/cli/memory_briefs.py

## Governing Overview

[mcp](../../../overview.md)

## Purpose

CLI subcommand adapter (`agents-remember memory-briefs`) that manually refreshes derived Git-ignored `briefs/` in a converted external-memory checkout paired with its code checkout (for example after a manual `git pull`). It owns argument parsing, target resolution, legacy-layout refusal, and text/JSON output while delegating generation to `application/file_briefs/triggers.py`.

## Code Commentary

- `add_arguments` accepts either `--repo <id>` (with optional `--config` and path overrides) or explicit `--memory-root`, `--code-root`, and `--coordination-root`, plus optional `--code-commit` and `--json`.
- `run` returns `EXIT_OK` (`0`) on success and `EXIT_REFUSED` (`2`) on target resolution failure, unconverted memory layout, or refresh failure.
- Before calling `refresh_written_memory_folder`, `run` verifies `(target.memory_root / LAYOUT_MARKER_PATH).is_file()` and refuses unconverted directories with `LEGACY_FORMAT_CODE` (`"legacy-format"`) via `legacy_format_refusal`.
- `_resolve_from_repo` loads MCP settings via `require_config_path` or `discover_config` and `load_config`, requires a configured repository with a non-null `memory_root`, and defaults `code_commit` to `head_commit(code_root)`.
- `_report_payload` and `_emit` produce either JSON (`ok`, `memoryRoot`, `codeRoot`, `codeCommit`, `briefs`, `written`, `unchanged`, `removed`, `seconds`, optional `repo`) or a single-line human summary.

## Relationships

- Registered in `mcp/src/agents_remember/cli/__main__.py` (`add_arguments`, `run`); covered by `mcp/tests/test_kno_r07_briefs_and_pairing.py`.
- Depends on `application/file_briefs/triggers.py::refresh_written_memory_folder`, `cli/discovery.py`, `kernel/primitives/runtime_config.py`, `worktrees/cutover_lock.py`, and `worktrees/modules/git.py::head_commit`.
- Referenced in advisory `briefsProblem` notices emitted by `worktrees/landing_briefs.py` when a recorded landing has no matching pulled checkout.

## Evidence

- CLI parser registers `--repo`/`--config` and explicit root, `--code-commit`, and `--json` options. [1]
- `run` checks `LAYOUT_MARKER_PATH` and refuses unconverted checkouts with `LEGACY_FORMAT_CODE` (`EXIT_REFUSED = 2`) before refreshing briefs. [2]
- `_resolve_from_repo` resolves repository configuration, requires `memory_root`, and defaults `code_commit` to `HEAD`. [3]
