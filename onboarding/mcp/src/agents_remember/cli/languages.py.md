# mcp/src/agents_remember/cli/languages.py

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

CLI adapter for `agents-remember languages`, exposing `scan` and `warm` subcommands that inspect repository language detection and pre-warm pinned tree-sitter grammar wheels into the external language cache.

## Code Commentary

`add_arguments` registers the `languages` command group with two required subactions: `scan` (`--repo`, `--json`) and `warm` (`--repo`, `--cache-dir`, repeatable `--language`, `--dry-run`, `--json`). `_parse_args` binds the parsed `argparse.Namespace` into `LanguagesCliArgs`.

`run` dispatches `scan` to `language_scanner.scan_repository_languages(repo_root)` and `warm` to `language_scanner.warm_repository_languages(...)`, emitting either structured JSON (`--json`) or concise human-readable summaries (detected languages, ambiguous suffixes, cache directory, warmed/cached/failed language IDs). `warm` returns exit code `0` when `warm.ok` is true and `1` otherwise; any `AgentsRememberError` prints to `stderr` and returns exit code `1` (unknown actions return `2`).

## Relationships

Registered in `cli/__main__.py` under the finite command registry (`languages.add_arguments` / `languages.run`). Calls `language_scanner.py` for scanning and warming. Invoked by `scripts/bootstrap-mcp-venv.sh` (`agents-remember languages warm --repo "$repo_root"`) and `.dagger/src/agents_remember_quality/main.py` to pre-warm the host and CI grammar caches.

## Evidence

- `LanguagesCliArgs` and `add_arguments` define the `languages scan` and `languages warm` CLI flags (`--repo`, `--cache-dir`, `--language`, `--dry-run`, `--json`). [1]
- `run` executes repository language scanning or cache warming, formats JSON or text output, and maps `AgentsRememberError` or failed warm results to exit code 1. [2]
