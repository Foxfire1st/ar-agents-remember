# scripts/sync-skills.py

| Field                  | Value                         |
| ---------------------- | ----------------------------- |
| repository             | agents-remember-md             |
| path                   | `scripts/sync-skills.py`       |
| doc_type               | `file-level-onboarding`        |
| lastUpdated            | 2026-06-10T00:40+02:00         |
| lastVerifiedCommitHash |                               `9911a8054b6314e051b094456a72eeec668c4c84`|
| lastVerifiedCommitDate | 2026-06-09T22:29:02+02:00|
| governingOverview      | `overview.md`                  |

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
it removes each target skill folder and copies the canonical tree into place,
then immediately runs the same check mode. With `--check`, it only verifies
targets and exits non-zero when any target differs. With `--list-targets`, it
prints the canonical source and all target paths.

### Conventions

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

## Docs References

No external documentation is needed for this repository-local helper.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The script defines `skills/` as canonical and enumerates all MCP package-data and harness starter skill-copy targets. | L13-L55 | [scripts/sync-skills.py](agents-remember-md/scripts/sync-skills.py) |
| `--check` compares canonical and target file digests, reports missing/extra/changed paths, and exits non-zero when a target is out of sync. | L86-L161 | [scripts/sync-skills.py](agents-remember-md/scripts/sync-skills.py) |
| Normal sync mode refuses self-sync, removes each target skill folder, copies canonical skills into place, and then reruns the check. | L124-L132; L164-L172 | [scripts/sync-skills.py](agents-remember-md/scripts/sync-skills.py) |
| The root AGENTS instructions tell contributors to edit root `skills/` first and run `python3 scripts/sync-skills.py` rather than editing generated skill copies directly. | L95-L117 | [AGENTS.md](agents-remember-md/AGENTS.md) |

## Cross-Repo References

No sibling repository evidence is needed for this helper.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-06-10T00:40+02:00 — `sync_target` now uses crash-safe `replace_tree` (copy to `<target>.ar-sync-new`, rename live target aside, swap in, then remove the old tree; stale staging/retired leftovers are cleaned on re-run), and `extended_length()` applies the Windows `\\?\` prefix so syncs and `--check` walks work past 260-char paths even with `LongPathsEnabled=0`. Replaces the delete-then-copy that gutted `package_data` when a long-path crash hit mid-delete (2026-06-09 incident).

- 2026-06-03T18:58+02:00: Created onboarding for the new skill synchronization helper. Verification metadata is pending until the code commit exists.
