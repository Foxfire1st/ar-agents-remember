# mcp/src/agents_remember/application/knowledge_consolidation_proposal/first_written.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

Determines when each live family record was first committed in the memory repository's Git history so never-consolidated families can be ordered by first writing rather than by their latest writer stamp or one-time conversion timestamp.

## Code Commentary

Runs one `git log --no-renames --diff-filter=A --format=%x00%cI --name-only -- knowledge/records/families` command (`_FIRST_ADDS`) via `kernel.git_command.run_git`, using a NUL byte (`_COMMIT_MARK`) to separate ISO commit timestamps from added file paths. `_family_of` strips the `<slug>.json` tail from `<PREFIX>-<ID>-<slug>.json` (or `<PREFIX>-<ID>.json`) so a slug rename still maps to the same record ID, and retains only IDs present in the caller's `families` set. Keeps the earliest commit timestamp per family. Families written only in the working tree are omitted, and if `memory_root` is not a Git checkout or `run_git` fails (`OSError`, `subprocess.SubprocessError`, or non-zero exit), `first_written` returns `{}` so callers fall back to writer stamp and ID order.

## Relationships

Called by `view._proposal` for the unnamed (`oldest`) proposal way; its output feeds `proposal.PassTimes.first_written`. Reads `KNOWLEDGE_ROOT` and `RECORD_DIRECTORIES["family"]` from `models.knowledge_files.documents` and executes Git via `kernel.git_command.run_git`.

## Evidence

- `_FIRST_ADDS` queries Git once over `FAMILY_DIRECTORY` with `--no-renames`, `--diff-filter=A`, NUL-prefixed commit ISO timestamps, and `--name-only`. [1]
- `first_written` tracks the earliest add-commit `datetime` per known family and returns an empty dict on Git failure or non-zero exit. [2]
- `_family_of` parses the `<prefix>-<id>` record identifier from family filenames so slug changes preserve record identity, filtering to known families. [3]
