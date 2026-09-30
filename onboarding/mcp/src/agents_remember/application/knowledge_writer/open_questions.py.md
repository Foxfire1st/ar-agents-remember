# mcp/src/agents_remember/application/knowledge_writer/open_questions.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_writer/open_questions.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T12:05:38+02:00 |
| lastVerifiedCommitHash | `f9e1262283469df895c98dda5b9549a1bbad5b74`|
| lastVerifiedCommitDate | 2026-09-30T13:14:52+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[application route overview](../overview.md)

## Purpose

**A `raise` row's question, appended to the leaf's task document through `task_doc` (MIK-R14 rule 4).**
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
- **Idempotence.** A question whose key (`question_key`, `[<subject> raised by <leaf>]`) already starts an existing
  string question is not appended again: a rerun of the same `raise` returns success and writes nothing.
- **Modify-write** (`_edit`): `task_doc_tool(set_field)` publishes `openQuestions` as the existing questions plus the
  new one, addressed by the repository, the contract path and the document's slug. `openQuestions` is a
  `NORMATIVE_INTENT` field, so the change is the developer's to answer. `check` passes `dry_run=True`: the task owner
  validates the whole publication and writes nothing.
- **Refusals are returned, never raised.** An `AgentsRememberError`, `ValueError` or `OSError` from the task owner
  becomes "task_doc refused the openQuestions edit: …", so the writer refuses the `raise` and the item stays open.

### Conventions

- The task document is edited only through `task_doc`, never by writing the JSON directly, so the owner's CAS,
  validation and `.md` rendering apply.

### Invariants And Boundaries

- **A `raise` puts the question in the task document before any knowledge file is written; on failure it writes
  nothing.** Candidate invariant (the ordering half is `writer.py`'s). Realized here by the dry-run `check` at
  authoring time and the refusal-returning `append`; proved by
  `test_the_task_document_append_preserves_questions_through_task_doc` (a real `task_doc` publication in tmp: the
  earlier question is kept, the `.md` is re-rendered, the dry run writes nothing, the rerun is idempotent, a leaf
  with no document is refused) and by `test_raise_sets_the_status_and_appends_the_question_or_is_refused`.
- **Existing questions are preserved.** The edit is a read-modify-write of the whole list.

### Todos

- **Recorded limit (ruling 04:37:56 Q7):** the read and the `set_field` are two `task_doc` calls. The task owner's
  publication CAS covers only its own read, so a question another writer appends between the two calls could be
  lost. No `task_doc` append operation was added in this leaf.
- **L37 (review F10, ruling 05:31:11):** confirm that installed mode honours `knowledge-ingest --config` for a real
  `raise` after the cutover.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R14@v2` of task
`260928_maintained-invariant-knowledge` and its leaf document `14_reconsideration-surfacing.json`; they live outside
the code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module docstring: the read-modify-write in three steps and the unavailable port. | "row's question, appended to the leaf's task document" | mcp/src/agents_remember/application/knowledge_writer/open_questions.py:1-17 |
| The port over `task_doc`: `check` is the dry run, `append` the publication. | `TaskDocOpenQuestions`; "dry_run=True"; "dry_run=False" | mcp/src/agents_remember/application/knowledge_writer/open_questions.py:38-52 |
| The leaf's one document found strictly, with its questions. | `_current`; "found = strict_leaf_doc(self.task_root, self.leaf)" | mcp/src/agents_remember/application/knowledge_writer/open_questions.py:54-68 |
| A present key appends nothing; otherwise `set_field` with the whole list; refusals returned. | `_edit`; "task_doc refused the openQuestions edit" | mcp/src/agents_remember/application/knowledge_writer/open_questions.py:70-87 |
| No task owner: every question refused with the reason. | `UnavailableOpenQuestions` | mcp/src/agents_remember/application/knowledge_writer/open_questions.py:90-102 |
| The strict leaf-document lookup it reuses (L11). | `strict_leaf_doc` | mcp/src/agents_remember/tasks/leaf_decisions.py:39-51 |
| The task owner's tool entry point. | `task_doc_tool` | mcp/src/agents_remember/application/task_docs/task_doc_tools.py:220-278 |
| A real `task_doc` append that keeps the earlier question, re-renders, is idempotent and refuses a missing leaf. | `test_the_task_document_append_preserves_questions_through_task_doc` | mcp/tests/test_reconsideration_surfacing.py:503-542 |

## Cross-Repo References

The task document lives under the coordination root (`tasks/<repository>/<task>/`), outside the code and memory
repositories; this module reaches it only through `task_doc`.

| Finding | Anchor | Source |
| --- | --- | --- |
| The edit is addressed by repository, contract path and slug. | "TaskDocTarget(self.repo_id, contract_path=str(self.contract_path), slug=slug)" | mcp/src/agents_remember/application/knowledge_writer/open_questions.py:78-84 |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T12:05:38+02:00 — 260928-MIK-L14 curator (uncommitted change set on `ar/260928-mik-l14`, code base `b54d1b0331f67454bcf245a7a338b04900181c3c` plus the staged delta): created this card for the new file MIK-R14 adds, recording the Q7 race window (ruling 04:37:56) and the F10 carry to L37 (ruling 05:31:11). The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
