# mcp/src/agents_remember/application/knowledge_writer/handoff.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_writer/handoff.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T10:05:46+02:00 |
| lastVerifiedCommitHash | `cd3e943d740b490d391722389af0a6bca0ccf93e`|
| lastVerifiedCommitDate | 2026-09-29T10:38:08+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[application route overview](../overview.md)

## Purpose

**The curator hand-off document the file writer reads (MIK-R12 rule 1).** It is JSON in one of two
spellings: a bare **list** (the producer's hand-off list exactly as today, read as `{"entries": <list>}`), or
an **object** with up to three sections, `entries`, `records` and `history`. Reading resolves nothing: it
checks the document's own shape and collects every problem, so one refusal names them all.

## Code Commentary

### Logic

- **Entries** keep the producer's thirteen fields unchanged. Curator keys beside them decide what the entry
  becomes: `scope` and `admission` (optionally `status`) author a new invariant from the verbatim
  `statement`; `invariant_id` updates a stored invariant; `supersedes` takes `INV-…` IDs or entry IDs;
  `proofs: [{test, facet}]` records curator-confirmed proofs; every `target` becomes a realization entry.
  Targets reuse `EntryRealization`/`realization_refusal` (the rationale and role rules) and scope reuses
  `read_curator_scope`.
- `ROLE_SPELLINGS` maps the template's `incidental` to the file format's `support` (the L21 review ruling).
- An entry with no target, no `invariant_id` and no `admission` is a **ruling**. `_require_attached_rulings`
  refuses a ruling that no `records[]` item names in `entry` ("attach it to a record, or keep it
  task-local") and refuses `proofs` on it (architect ruling F2): nothing of an entry is ever dropped
  silently.
- **Records** are `{key, kind, entry?, id?, slug?, fields}`; `kind` is one of the ten record kinds of
  `RECORD_PREFIXES`; the writer owns `id`, `schema`, `origin` and `revision` (`WRITER_OWNED_FIELDS`) and
  refuses them in `fields`; a new record needs a `slug`.
- **History rows** are `{subject, disposition, reason, items?, covers?, effect?, because?, examined?}`. `id`
  and `revision` are writer-owned; unknown keys (a misspelled `cover`) and a non-list `because` are
  refused. A cover is an entry ID, `{id, locator?, remove?}` or `{handoff}`.
- `"handoff:<key>"` names the record the same document authors under that key wherever an ID is
  expected; `_require_distinct_handles` refuses two items sharing a handle.
- Test IDs are `path::name` (`path::Class::method` is the symbol `Class.method`, `_TEST_ID`);
  `EntryRequest.cited_tests` finds them in evidence text for the report.

### Conventions

- Every reader appends a `Problem(where, message)` and returns `None` rather than raising, so all problems surface together.

### Invariants And Boundaries

- The producer/curator split of the hand-off list is preserved: nothing here rewrites a producer field.
- A new invariant must carry `admission`; its meaning is MIK-R27's. A family row's `examined` is never
  defaulted.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R12@v2` of task
`260928_maintained-invariant-knowledge` (with its architect rulings in the task's leaf document
`12_category-authoring-through-the-curator-workflow.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

The document's sections and their readers.

| Finding | Anchor | Source |
| --- | --- | --- |
| The template's `incidental` is written as `support`. | `ROLE_SPELLINGS` | mcp/src/agents_remember/application/knowledge_writer/handoff.py:52-52 |
| One refusal reason: where, and what. | `Problem` | mcp/src/agents_remember/application/knowledge_writer/handoff.py:56-64 |
| An entry and its curator keys; a ruling authors no invariant. | `EntryRequest` | mcp/src/agents_remember/application/knowledge_writer/handoff.py:117-144 |
| Read the three sections, collecting every problem. | `read_handoff` | mcp/src/agents_remember/application/knowledge_writer/handoff.py:196-233 |
| A ruling no record names is refused, and so are proofs on it. | `_require_attached_rulings` | mcp/src/agents_remember/application/knowledge_writer/handoff.py:236-267 |
| Locators in the file form: symbol, line range, whole file. | `read_locator` | mcp/src/agents_remember/application/knowledge_writer/handoff.py:303-328 |
| Targets through the shipped realization rules. | `_targets` | mcp/src/agents_remember/application/knowledge_writer/handoff.py:331-364 |
| Proofs carry the curator's facet. | `_proofs` | mcp/src/agents_remember/application/knowledge_writer/handoff.py:382-405 |
| An entry: new invariant needs scope, admission and a statement. | `_entry` | mcp/src/agents_remember/application/knowledge_writer/handoff.py:418-463 |
| A record: kind, fields, and the writer-owned fields refused. | `_record` | mcp/src/agents_remember/application/knowledge_writer/handoff.py:470-503 |
| A history row: strict keys, writer-owned `id` and `revision`. | `_row` | mcp/src/agents_remember/application/knowledge_writer/handoff.py:531-568 |
| Four problems refused in one operation, each named. | `test_problems_refuse_the_whole_operation_and_each_is_named` | mcp/tests/test_knowledge_writer.py:341-366 |
| An entry that names no record is refused. | `test_an_entry_that_names_no_record_is_refused_and_nothing_of_it_dropped` | mcp/tests/test_knowledge_writer.py:531-553 |

## Cross-Repo References

No cross-repo boundary is crossed: the writer reads the paired code worktree and writes the paired memory
worktree of one repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T10:05:46+02:00 — 260928-MIK-L12 curator (uncommitted change set on `ar/260928-mik-l12`, code base `6ad4e076bbbc5d98b8c770fc374d56ddc4a2d695` plus the staged delta): created this card for the new file MIK-R12 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
