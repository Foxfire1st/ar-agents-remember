# mcp/src/agents_remember/application/knowledge_write_route.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

**The file writer's route: what a leaf, a crossing or a wave writes, returned as a report (MIK-R54, MIK-R73
rule 1).** Both writer entry points run the functions here — `agents-remember knowledge-ingest` /
`knowledge-bootstrap` through `cli/knowledge_write_route.py`, and the mounted `knowledge_write` tool — and
both pass one `WriteSubmission`. Both routes use the same contract, authorization and worklist checks. The caller supplies the runtime context for question publication and writer attribution.

The leaf route establishes the contract's recorded memory base before passing it to the writer's card comparison. An unavailable base leaves that comparison to the persisted-count or operation-base path.

## Code Commentary

### Logic

- `is_converted(memory_root)` answers on the memory tree's layout marker
  (`knowledge/layout.json`, `LAYOUT_MARKER_PATH`); `unconverted_write_refusal` names that marker and how the
  tree converts, so a legacy-format tree is refused by name rather than by a downstream error.
- `load_leaf_contract` reads the enclosure contract and answers the contract or a refusal string;
  `leaf_owner` and `handoff_label` name the record's owner and the hand-off document for `origin`.
- `leaf_write_report` assembles the leaf run: the converted check, the contract, the hand-off document
  (`read_handoff_document`), the leaf's decisions (`leaf_decisions` → `DecisionResolver`), the leaf's memory
  base (`_leaf_memory_base`), the persisted worklist (`read_leaf_worklist`, `WORKLIST_FILE_NAME`) and, when a
  `raise` row needs one, the question port (`LeafQuestions`).
- `LeafQuestions` publishes a raised question through `task_doc` with the settings the **caller** supplies —
  the command line's discovered settings or the mounted server's own — so a `raise` is never left without a
  task-document authority; without usable settings it is refused.
- `crossing_write_report` locates the open sync for the named crossing and appends rows to its open history file. It can resolve or reconfirm existing records. The writer refuses new records, handoff entries and rulings on this route. The settled code commit supplies both the snapshot and the writer's code base. A missing sync, a different crossing, an unfinished code side or a moved code branch refuses the write.
- `wave_write_report(target, submission)` runs the taskless wave write.
- Leaf, crossing and wave writes pass the resolved owner and one caller stamp to the writer. The stamp uses the runtime binding and launch receipt. Unresolved identity or a missing coordination root yields an unknown stamp with the reason.
- The leaf route captures the prior occurrence index and passes the written and removed memory paths to brief regeneration after the report reaches `written`. The report notes the regeneration outcome. A brief-writing problem leaves the primary writer state intact.
- The writer itself is `application.knowledge_writer.write_knowledge`; this module holds no argument parser and
  prints nothing. A caller receives the `WriteReport`, or a string naming why the invocation is refused.

### Conventions

- One `WriteSubmission` (`document`, `handoff_path`, `authorization_ref`, `commit`) is the whole request; the
  settings loader, the contract path and the hand-off label travel in the route value beside it, and the report
  is the whole answer.
- Refusals are returned as typed refusals or strings with their own reason, never as exceptions across the
  route boundary.

### Invariants And Boundaries

- The mounted tool and command use the same writer and apply the same contract, authorization and worklist checks.
- **Converted memory only.** An unconverted tree is refused by name, because the canonical database writer is
  retired (MIK-R26) and there is no second writer.
- **`--commit` authorizes file writes only** — no Git operation, and no acceptance.
- **A `raise` uses the caller's settings**, which is exactly what makes the mounted tool able to publish a
  question where a stray command line would not.

### Todos

No additional work is asserted by this card.

## Evidence

- Both entry points share leaf-write admission and pass the request's owner, question port and caller stamp to the writer. [3]
- The caller stamp comes from the runtime binding and receipt, with a reason when the coordination root is missing. [10]
- The crossing writer carries its owner and caller stamp with the settled code commit the open sync recorded. [11]
- The wave writer carries the wave owner and a caller stamp. [12]

### Docs References

No domain documentation source is configured for this repository. The design authority is `MIK-R54`'s writer
and validator corrections and `MIK-R73@v1` rule 1, of task `260928_maintained-invariant-knowledge`; the
packets live outside the code and memory repositories and are named here, not cited as rows.

### Repo-Internal References

The checks this route composes are evidenced with their owning writer and worklist.

### Cross-Repo References

None: one memory worktree, named by the contract the caller supplies.

## Current account — the mounted settings or the command's own route

`LeafQuestions` takes the mounted server's `config` or the command line's `CommandRoute`. `_mounted` checks the settings root. `_command` asks the route's loader and, when it returns a refusal clause, names the mounted `knowledge_write` call that can publish the same hand-off. Both build the task-document port in `_task_doc`. `leaf_write_report` passes the selected question route and resolves a caller stamp for the leaf's owner.

- The raise question's port is built from the mounted settings or from the command's own route, and only the command half's refusal names another route. [1]
- A command route whose loader answers a clause is refused with the mounted `knowledge_write` call, and a loaded settings root that differs keeps its own refusal. [2]

- After a written leaf report, the route refreshes briefs from changed and removed memory paths and records its outcome in notes. [13]
