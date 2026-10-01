# scripts/sync-skills.py

## Governing Overview

[overview.md](../overview.md)

## Purpose

`scripts/sync-skills.py` is the repository helper that keeps the root
canonical `skills/` tree synchronized with every generated skill copy shipped in
the MCP package data and harness starter packages.

## Code Commentary

### Logic

The script resolves the repository root from its own path, treats root
`skills/` as canonical, and declares a fixed list of sync targets:

- MCP package data under `mcp/src/agents_remember/package_data/runtime/skills`
- Claude Code, Codex, Cursor, VS Code/Copilot, Hermes, OpenClaw, Pi, and
  Antigravity starter package skill folders

It computes SHA-256 digests for every non-ignored file under the canonical tree
and each target, then reports missing, extra, and changed files. In normal mode
it copies the complete canonical tree to a sibling staging directory before renaming the live target aside and renaming staging into place,
then immediately runs the same check mode. With `--check`, it only verifies
targets and exits non-zero when any target differs. With `--list-targets`, it
prints the canonical source and all target paths.

### Conventions

`replace_tree` removes stale staging/retired leftovers, completes the new copy, then renames the old target aside and the staged tree into place before removing the retired tree. A copy failure before the first rename leaves the live target intact. The two renames are separate operations; this description does not claim an atomic directory exchange.

Ignore only local/generated filesystem noise: `.DS_Store`, cache directories,
`__pycache__`, and `.pyc` files. Keep targets explicit so new harness packages
must consciously opt into skill synchronization.

### Invariants And Boundaries

- Root `skills/` is the only canonical source.
- The script refuses to sync a target path that resolves to the canonical
  `skills/` directory.
- Sync mode replaces target skill directories wholesale; do not point a target
  at user-owned or non-generated content.
- The helper manages skill copies only. It does not sync hooks, MCP settings,
  instructions, docs, or provider/runtime assets.

### Todos

No open file-local todos.

## Evidence

### Docs References

No external documentation is needed for this repository-local helper.

No relevant external documentation found.

### Repo-Internal References

- The script defines `skills/` as canonical and enumerates all MCP package-data and harness starter skill-copy targets. [1]
- `--check` compares canonical and target file digests, reports missing/extra/changed paths, and exits non-zero when a target is out of sync. [2]
- Normal sync mode refuses self-sync, replaces each target skill folder, copies canonical skills into place, and then reruns the check. [3]
- The root AGENTS instructions tell contributors to edit root `skills/` first and run `python3 scripts/sync-skills.py` rather than editing generated skill copies directly. [4]

### Cross-Repo References

No sibling repository evidence is needed for this helper.

No meaningful cross-repo references found.
