# mcp/tests/test_master_retirement.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

The integration cases of `task_doc.retire_master` on a sprint's master and of the shared missing-master message. The
`World` fixture builds a scratch coordination root with a sprint that commands three masters (`master-a`, `master-b`,
`master-c`) with a graph and edges, a scratch code repository, and a series contract for a master; the cases drive
the public `task_doc` tool. The module is in the `integration` lane.

## Code Commentary

### Logic

- **Dry run and real run.** The dry run lists the removed membership, the one graph node and the removed edges and changes
  nothing; the real run leaves a valid sprint, a plain abandoned row that carries the proof at the master's place, the
  folder under `0_archive/`, the Mermaid graph equal to the preview's, and no ref moved.
- **Unfinished successors.** An outgoing edge to a successor that is not `Completed` refuses and lists the edge until the
  request names it in `removeEdges`.
- **Open work.** Pending cleanup with no open work is a readiness fact and permits the dry-run retirement.
  The readiness module separately exercises actual open leaf work and unfinished or unreadable current operation authority.
  This file preserves and revalidates a valid terminal historical generation.
- **Restoration.** A failed folder move restores the sprint's exact source pair and leaves no archive folder. An evidence
  or document change between admission and publication refuses with a publication conflict, and the hook deletes nothing.
- **Interruption and retry.** After an interrupted move the sprint is valid with the master still in place; the same
  request resumes, a request with another reason is refused as differing from the retained proof, a changed master source
  refuses, and a repeated request after completion reports `retirementResumed`.
- **Partial hook failure.** One dataset copy is deleted and another fails: the result is `ok=false`,
  `retired-with-hook-failures`, the sprint is valid, and nothing is edited or moved a second time by the retries, which
  delete only the remaining copy and finish with `ok=true`.
- **The record is protected.** A generic `replace` that erases the retirement proof is refused and changes nothing.
- **Missing master message.** With the master moved under `0_archive/` by hand, `validate_execution_topology`,
  `commanded_masters` and `validate_sprint_linkage` refuse with the same message, naming the master, the archive path and
  `task_doc.retire_master`.
- **Graph limits.** A sprint's only graphed master refuses naming the reason and `attach_master`; the last master of a
  graph-less sprint retires and its retry still works; a master nested inside another task's folder is refused in the dry
  run and the real run with the master, the enclosing folder and `0_archive/<name>` named and nothing changed.
- **Symlink escape.** An archive path that escapes through a symlink refuses before publication.

### Conventions

- `world.snapshot()` captures every file of the scratch tree, and the cases assert it unchanged after a refusal.

### Invariants And Boundaries

- These cases prove that the sprint stays valid at every point of a retirement, that a retirement stays valid after a
  partial cleanup failure and a repeated identical request finishes it, that a nested master is refused, and that a
  retirement proof cannot be edited through a generic task-document operation.

## Evidence

- The dry run lists the exact edits and the real run keeps the sprint valid. [1]
- A failed move restores the sprint's source pair and the folder. [2]
- An interrupted request resumes, and a changed reason is refused. [3]
- A partial hook failure is reported truthfully and the same request retries only the cleanup. [4]

- A generic edit cannot erase a retained retirement proof. [5]
- The missing-master message is identical across the topology readers. [6]
- A nested master is refused before anything changes. [7]

- Pending cleanup without open work is a fact and permits preview. [8]
