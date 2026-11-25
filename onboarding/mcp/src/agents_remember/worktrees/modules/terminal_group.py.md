# mcp/src/agents_remember/worktrees/modules/terminal_group.py

## Governing Overview

[modules overview](overview.md)

## Purpose

Owns checked preview, evidence/message/tool-call move-out, provider-runtime safety checks, and whole-folder removal of a terminal task's `worktree_group` directory, while preserving legacy series directory compatibility.

## Code Commentary

- `_group_observation` refuses removal when any parent of `worktree_group` is a symlink, the target is not a real directory, the group equals the repository's shared worktree root (`<coordination_root>/worktrees/<repo_name>`), or its parent lacks write/exec access; an absent folder reports `already-absent`.
- `preview_group_removal` handles legacy series groups (`contract.kind == "series"` at `<task_root>/enclosures`), checks provider-runtime residue when `teardown_providers=False` (`_preview_provider_skip`), scans recursive deletion permissions via `_directory_blocker` (excluding separately removed worktrees and provider-runtime), and runs dry-run `_move_out` (role reports, group messages, kept tool calls) plus outside-scratch preview.
- `prepare_terminal_group` previews blockers, invokes `archive_terminal_agents` (for non-legacy groups) and evaluates `terminal_agent_blockers` whenever the group would be removed, and runs live `prepare_group_removal` (`_move_out(dry_run=False)`) before returning `GroupPreparation`.
- `remove_terminal_group` runs `_collect_before_removal` (re-collecting reports and keeping tool-call lines), removes outside scratch and report locators (`remove_group_report_locators`), and deletes `contract.worktree_group` as one tree via `worktree_services().provider_lifecycle.remove_tree`; `teardown_terminal_providers` skips teardown when `provider-runtime`, `settings`, or `provider-settings.json` is a symlink.

## Relationships

- Consumed by `worktrees/modules/cleanup.py`, `worktrees/modules/abandon.py`, `worktrees/modules/terminal_cleanup.py`, `worktrees/modules/terminal_abandon.py`, and `worktrees/modules/terminal_retry.py`.
- Calls `worktrees/role_reports.py`, `worktrees/group_messages.py`, `worktrees/modules/kept_tool_calls.py`, `worktrees/modules/terminal_agents.py`, and `worktrees/modules/outside_scratch.py`.

## Evidence

- `preview_group_removal` dispatches legacy series groups, checks provider-skip and recursive directory permission blockers, and combines outside-scratch and dry-run move-out checks. [1]
- `remove_terminal_group` collects reports and tool calls, removes outside scratch and report locators, and removes the whole `worktree_group` via `provider_lifecycle.remove_tree`. [2]
- `_group_observation` guards against symlinked parents, non-directory paths, the repo's shared worktree root, and unwritable parents, reporting `already-absent` when missing. [3]
- `prepare_terminal_group` sequences removal preview, terminal agent archiving/blocker checks, and live move-out into a `GroupPreparation` result. [4]
