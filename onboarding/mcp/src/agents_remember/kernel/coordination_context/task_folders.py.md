# mcp/src/agents_remember/kernel/coordination_context/task_folders.py

## Governing Overview

[coordination_context overview](overview.md)

## Purpose

The one walk over a coordination root's task folders, and the archive segment it skips — coordination layout held at the kernel rank, so both `tasks/` and the control plane can use it without either reaching into the other: `tasks.task_paths` re-exports `ARCHIVE_DIR` and `task_folder_steps`, and receipt discovery walks the same folders while `controlplane` stays below `tasks` in `layers.toml`.

## Code Commentary

- A task folder is a direct child directory of `tasks/<repository>/`; `ARCHIVE_DIR` is the segment that is not one, and it is defined here once rather than in each caller. [1]
- `task_folder_steps` yields one step per child of a root, in `os.scandir` order: the folder path for a directory, `None` for a file or for the archive segment, so a caller advancing by steps keeps its position while skipping what is not a task. A root that is not a directory yields nothing; a directory that cannot be read is reported through `on_error`, or raised when the caller supplies no handler, and the step is `None` rather than a silent gap. [2]
- `canonical_task_folder_steps` walks two levels — a repository, then its task folders — with `follow_symlinks=False` so a linked directory is never entered, and reports each directory it visits with its depth through `on_directory`, which is how the receipt walk keeps its own budget and cursor without re-implementing the policy. [3]

## Evidence

- A task folder walk skips the archive segment and never follows a symlink into a folder it did not open
