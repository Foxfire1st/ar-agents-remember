# mcp/src/agents_remember/worktrees/task_document_copies.py

## Governing Overview

[Nearest governing overview](overview.md)

## Purpose

Publishes rendered, read-only leaf documents with an index inside the enclosure group, outside its Git trees.

## Code Commentary

`prepare_task_document_copies` writes the leaf's rendered Markdown under `task-documents/` preserving its canonical relative path plus an `INDEX.json` carrying the canonical reference, JSON and copy digests and publication time — before the launch's first turn. `_publish_copy_writes` applies all files atomically with rollback to prior bytes. Copy content and placement are unchanged by refresh selection. Every destination must stay inside the working folder as real files; a copy root whose resolved path falls inside either Git worktree is refused, and edits to copies are never read back.

`refresh_task_document_copies` walks only the parent task folders of the written documents, not the repository's other tasks. The shared iterator prunes notes and archives. `_read_task_artifact_cell` selects contracts before full parsing: a readable cell naming a different document is ignored without loading its contract. Filesystem-resolved membership is determined by the contract's physical enclosure position, not its recorded roots. A foreign contract is skipped and named even when its worktree group has gone; it supplies no copy writes.

A readable contract naming the changed document still fails on a parse error. A file that cannot be read, or carries no artifact cell and fails to parse, cannot establish whose enclosure it is. `_RefreshWork.finish` names and skips these unrecognized files only when at least one own enclosure has staged copy writes. With none staged, it raises the first error naming its file, allowing the canonical publication transaction to restore the written sources. This conditional tolerance does not promise that every damaged own enclosure can be identified without a roster. Staged copies are published only after that decision, through the same rollback path.

## Evidence

- A leaf role's own rendered document is prepared as a real enclosure file with one index entry. [1]
- Public writes select the written task's copies before staging and atomic publication. [2]

- Atomic copy publication restores prior copied bytes if publication fails. [3]

- Raw artifact selection excludes readable siblings and foreign nonmembers before full contract loading. [4]
- Unrecognized files are tolerated only past staged own copies; otherwise their error is raised. [5]
