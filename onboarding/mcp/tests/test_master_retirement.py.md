# mcp/tests/test_master_retirement.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

### STOP-delta current source contract

World.retire calls raw task_doc_tool and its retirement assertions consume that whole application result directly. The obsolete _whole(answer[log]) wrapper is removed from these raw callsites. Existing readiness, preview, state, graph, identity, retry and rollback assertions remain separate from registered compact-answer controls.

These are current source/assertion-carrier meanings. The qualified attempt14 CODE verdict is inherited, not a Curator test run, native freeze-currentness certification or independent MEMORY acceptance. Earlier contrary accounts are historical only; unaffected contracts and typed provenance remain.

> **Retained historical source account — superseded by the current contract:**
> The integration cases of `task_doc.retire_master` on a sprint's master and of the shared missing-master message. The
> `World` fixture builds a scratch coordination root with a sprint that commands three masters (`master-a`, `master-b`,
> `master-c`) with a graph and edges, separate scratch code and external-memory repositories, and a series contract
> for a master. `World.retire` calls the public task-document application operation and reads its whole result,
> not the bounded MCP delivery answer. The module is in the `integration` lane.

## Code Commentary

### Current Contract

World.retire calls raw task_doc_tool and its retirement assertions consume that whole application result directly. The obsolete _whole(answer[log]) wrapper is removed from these raw callsites. Existing readiness, preview, state, graph, identity, retry and rollback assertions remain separate from registered compact-answer controls.

> **Historical attempt13 carrier account — superseded at the changed callsites:** World.retire retains its raw task_doc_tool seam. New _whole(answer[log]) consumers obtain rich readiness/preview/state/graph/retry facts from the retained record, not directly from every delivered mapping. These source-defined carriers are not a whole live server/session qualification. Existing retirement identity, protection and rollback assertions remain.

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

> **Retained historical source account — superseded by the current contract:**
> - `world.snapshot()` captures every file of the scratch task tree, and the cases assert it unchanged after a refusal.
> - `World.series` creates matching branches in the code and external-memory repositories and records the memory
>   content commits of its completed fixture. This exercises the supported memory contract without weakening the
>   opt-out or carryover guards.
> - Readiness assertions consume the application result. A long scratch path may make the bounded delivery answer
>   omit `readinessFacts`; that transport limit must not change the application behavior these cases examine.



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

- **Retained historical source account — superseded by the current contract:** The shared world supplies separate scratch code and external-memory repositories with completed memory bookkeeping. [9]
- **Retained historical source account — superseded by the current contract:** Retirement readiness assertions read the whole application result rather than the bounded delivery answer. [10]


- World.retire calls raw task_doc_tool and its retirement assertions consume that whole application result directly. The obsolete _whole(answer[log]) wrapper is removed from these raw callsites. Existing readiness, preview, state, graph, identity, retry and rollback assertions remain separate from registered compact-answer controls. Earlier carrier account retained literally as historical: World.retire retains its raw task_doc_tool seam. New _whole(answer[log]) consumers obtain rich readiness/preview/state/graph/retry facts from the retained record, not directly from every delivered mapping. These source-defined carriers are not a whole live server/session qualification. Existing retirement identity, protection and rollback assertions remain. [11]

- World.retire calls raw task_doc_tool and its retirement assertions consume that whole application result directly. The obsolete _whole(answer[log]) wrapper is removed from these raw callsites. Existing readiness, preview, state, graph, identity, retry and rollback assertions remain separate from registered compact-answer controls. [12]


