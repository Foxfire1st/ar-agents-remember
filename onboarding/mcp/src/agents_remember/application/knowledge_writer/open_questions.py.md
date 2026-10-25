# mcp/src/agents_remember/application/knowledge_writer/open_questions.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

**A `raise` row's keyed question, appended or replaced through the task owner (MIK-R14).**
`TaskDocOpenQuestions` implements the writer's `reconsideration.OpenQuestions` port over the task owner:
`check` is a dry run of the edit, `append` publishes it. `UnavailableOpenQuestions` is the port when no task owner
can be reached (no MCP authority settings): every question is refused with that reason. The CLI's `LeafQuestions`
(`cli/knowledge_write_route.py`) builds one lazily, only when a `raise` needs it.

## Code Commentary

### Logic

- **Read** (`_current`): the leaf's one task document is found strictly through L11's `strict_leaf_doc`. Two
  documents claiming the leaf, or the leaf's document in an unreadable state, are the owner's named refusals
  (`LeafDocumentUnresolved`); a leaf with no document is "the leaf … has no task document under …". Each existing
  question is kept as a document (a string, or the model dumped with `exclude_none`).
- **Keyed publication.** The key (`question_key`, `[<subject> raised by <leaf>]`) identifies the existing
  string question. Repeating identical text is idempotent; rewording the reason replaces that question
  instead of silently keeping the old wording or appending a duplicate.
- **Modify-write** (`_edit`): strict lookup selects the slug, then `task_doc_tool(put_open_question)` receives
  `{key, text}`, repository and contract. The task owner reads its current `openQuestions` and appends or
  replaces inside its own publication, preserving concurrent unrelated questions. The adapter does not
  replace the whole list with a stale caller-side copy. The question still asks the developer to answer;
  `check` passes `dry_run=True`, so the same owner validation runs without publication.
- **Batch and rollback boundary.** `append_many` sends every keyed question in one `put_open_question` call using the `questions` list; the owner validates the batch before publishing any member. The adapter’s early lookup selects the slug, but its returned question list is discarded: the authoritative read/prepare occurs inside the task owner’s repository-root file lock. The central publisher re-enters that lock and refuses same-call nested publication through its active marker. Failed copy refresh restores the pre-batch task sources before releasing the lock; a different thread/process then prepares and publishes its question against the restored source. No per-key inverse is used.
- **Destination.** The `destination` property names the resolved task-document path for writer reporting.
- **Refusals are returned, never raised.** An `AgentsRememberError`, `ValueError` or `OSError` from the task owner
  becomes "task_doc refused the openQuestions edit: …", so the writer refuses the `raise` and the item stays open.

### Conventions

- The task document is edited only through `task_doc`, never by writing the JSON directly, so the owner's CAS,
  validation and `.md` rendering apply.

### Invariants And Boundaries

- **Question publication precedes knowledge-file publication.** `check` validates the keyed edit as a dry
  run; a task-owner refusal prevents that question publication and refuses the writer run. Once a question
  is published, a later knowledge-filesystem failure is a separate-store failure: the writer reports the
  surviving question and idempotent retry, rather than claiming nothing anywhere changed.
- **Unrelated questions are preserved.** The task owner changes only the keyed string in its current list.
  Tests name the preserved-question, reworded-reason, dry-run, missing-document and retry boundaries; their
  presence is not an assertion that this card ran them.

### Todos

The former whole-list `set_field` lost-update limit is removed by the keyed task-owner publication; it is
not deferred work. No route reads `--config`: the command resolves its own trusted settings and, when it cannot, refuses the raise with the mounted `knowledge_write` call that can publish it (MIK-R194 rule 9). No installed
execution is inferred from this source contract or the adapter's tests.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R14@v2` of task
`260928_maintained-invariant-knowledge` and its leaf document `14_reconsideration-surfacing.json`; they live outside
the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The task owner publishes a keyed append or replacement and preserves intervening questions. [1]

- The port over `task_doc`: `check` is the dry run, `append` the publication. [2]

- The leaf's one document found strictly, with its questions. [3]

- The adapter submits put_open_question with key and text; dry-run and refusal-return behavior remain explicit. [4]



- The owner replaces the matching keyed question or appends to its current list without replacing unrelated entries. [10]

- A multi-raise submits one keyed batch to the same task owner, not a stale whole-list replacement. [11]
- Task-owner entry acquires the task-root file lock before preparation; active nested publication refuses before invoking the edit body. [12]


- No task owner: every question refused with the reason. [5]


- The strict leaf-document lookup it reuses (L11). [6]


- The task owner's tool entry point. [7]


- A real `task_doc` append that keeps the earlier question, re-renders, is idempotent and refuses a missing leaf. [8]


### Cross-Repo References

The task document lives under the coordination root (`tasks/<repository>/<task>/`), outside the code and memory
repositories; this module reaches it only through `task_doc`.


- The edit is addressed by repository, contract path and slug. [9]
