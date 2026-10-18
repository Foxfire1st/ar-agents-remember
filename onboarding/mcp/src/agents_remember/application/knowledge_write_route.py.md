# mcp/src/agents_remember/application/knowledge_write_route.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

**The file writer's route: what a leaf, a crossing or a wave writes, returned as a report (MIK-R54, MIK-R73
rule 1).** Both writer entry points run the functions here — `agents-remember knowledge-ingest` /
`knowledge-bootstrap` through `cli/knowledge_write_route.py`, and the mounted `knowledge_write` tool — and
both pass one `WriteSubmission`. The two routes therefore cannot disagree about the contract guard, the
authorization reference, the worklist checks or the refusals: the tool can do nothing the command cannot.

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
- `crossing_write_report` resolves the crossing memory worktree (`_crossing_memory_root`) and records the rows
  into the open `<task-id>-crossing-<n>` file, authoring no entry and no new record.
- `wave_write_report(target, submission)` runs the taskless wave write.
- The writer itself is `application.knowledge_writer.write_knowledge`; this module holds no argument parser and
  prints nothing. A caller receives the `WriteReport`, or a string naming why the invocation is refused.

### Conventions

- One `WriteSubmission` (`contract`/`target`, `authorization`, `commit`, `crossing`, settings) is the whole
  request; the report is the whole answer.
- Refusals are returned as typed refusals or strings with their own reason, never as exceptions across the
  route boundary.

### Invariants And Boundaries

- **The tool cannot exceed the command**: same contract guard, same authorization reference, same worklist
  checks, same refusals.
- **Converted memory only.** An unconverted tree is refused by name, because the canonical database writer is
  retired (MIK-R26) and there is no second writer.
- **`--commit` authorizes file writes only** — no Git operation, and no acceptance.
- **A `raise` uses the caller's settings**, which is exactly what makes the mounted tool able to publish a
  question where a stray command line would not.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured for this repository. The design authority is `MIK-R54`'s writer
and validator corrections and `MIK-R73@v1` rule 1, of task `260928_maintained-invariant-knowledge`; the
packets live outside the code and memory repositories and are named here, not cited as rows.

### Repo-Internal References

No numbered references are recorded for this new module. The checks it composes belong to the writer and the
worklist and are evidenced where those own them.

### Cross-Repo References

None: one memory worktree, named by the contract the caller supplies.
