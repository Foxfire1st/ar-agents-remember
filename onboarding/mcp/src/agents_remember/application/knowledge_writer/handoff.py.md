# mcp/src/agents_remember/application/knowledge_writer/handoff.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_writer/handoff.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T23:27:43+02:00 |
| lastVerifiedCommitHash | `46ca74302e76cf40fb6370ea9ece16d8fa719f00`|
| lastVerifiedCommitDate | 2026-09-30T00:07:49+02:00|
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
- **History rows** are `{subject, disposition, reason, items?, covers?, effect?, because?, examined?, ref?}`.
  `id` and `revision` are writer-owned; unknown keys (a misspelled `cover`), a non-list `because` and a
  non-object `ref` are refused. `ref` (MIK-R11) is carried to `RowRequest.ref` for a planned row; what it
  names is checked by `authoring._planned_row`, not here. A cover is an entry ID, `{id, locator?, remove?}` or `{handoff}`.
- `"handoff:<key>"` names the record the same document authors under that key wherever an ID is
  expected; `_require_distinct_handles` refuses two items sharing a handle.
- Evidence names a test in one of two forms (MIK-R28 rule 2), both read by `tests_named_in`: a test ID
  `path::name` (`path::Class::method` is the symbol `Class.method`, `_TEST_ID`), or a path plus symbol,
  the pytest selection `path -k name` (`_SELECTED_TEST`). A test module named with neither becomes a
  `TestFileMention`, which the writer reports `unresolvable`. `EntryRequest.cited_tests` delegates to
  `tests_named_in` for the report.

### Conventions

- Every reader appends a `Problem(where, message)` and returns `None` rather than raising, so all problems surface together.

### Invariants And Boundaries

- The producer/curator split of the hand-off list is preserved: nothing here rewrites a producer field.
- A new invariant must carry `admission`; its meaning is MIK-R27's. A family row's `examined` is never
  defaulted.

### Todos

None recorded.

## 260928-MIK-L28 Evidence Names A Test In Two Forms (MIK-R28 Rule 2)

`tests_named_in(evidence)` is the one parser of the tests a hand-off entry's evidence names. It collects
every `path::name` and every `path -k name` across all evidence strings first, then adds a
`TestFileMention` for each test module mentioned bare, skipping a path some string already names a test
in. The result is in order of appearance, once each. Reading resolves nothing: whether a named test exists
at C is the writer's to establish (`authoring._cited_test`).

- **The `path -k name` spelling (architect ruling, 2026-09-29).** The packet's "path plus symbol" is read
  as the pytest selection `path -k name` where the `-k` expression is exactly one identifier, optionally
  quoted, and the path is a `.py` file. An expression such as `a and not b` names no single test and is
  not read as one. The name may end at whitespace, `,;:.)]`, a backtick or a quote, so a Markdown-quoted
  selection is read. The structured `{path, symbol}` form of `proofs[].test` is unchanged.
- **Only test modules are reported bare.** A bare mention needs a `test_*.py` or `*_test.py` basename;
  `conftest.py`, `*_test_support.py` and other helpers are never reported.
- Only `.py` evidence is read, as for `path::name`. A test in another language can still be a proof
  through `proofs[].test`.

| Finding | Anchor | Source |
| --- | --- | --- |
| Both forms, the bare file, and expressions that are not read as one test. | `test_evidence_names_a_test_as_a_test_id_or_as_a_path_plus_symbol` | mcp/tests/test_knowledge_proofs.py:98-146 |
| A file named with a test anywhere in the evidence is not also reported bare. | `test_a_file_named_with_a_test_anywhere_in_the_evidence_is_not_also_reported_bare` | mcp/tests/test_knowledge_proofs.py:149-152 |

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
| One refusal reason: where, and what. | `Problem` | mcp/src/agents_remember/application/knowledge_writer/handoff.py:71-79 |
| An entry and its curator keys; a ruling authors no invariant; the tests its evidence cites come from `tests_named_in`. | `EntryRequest`; `cited_tests` | mcp/src/agents_remember/application/knowledge_writer/handoff.py:168-190 |
| The two test forms and the bare test module, read in order and once each. | `_SELECTED_TEST`; `_TEST_FILE`; `TestFileMention`; `tests_named_in` | mcp/src/agents_remember/application/knowledge_writer/handoff.py:57-60; mcp/src/agents_remember/application/knowledge_writer/handoff.py:65-68; mcp/src/agents_remember/application/knowledge_writer/handoff.py:123-131; mcp/src/agents_remember/application/knowledge_writer/handoff.py:134-156 |
| Read the three sections, collecting every problem. | `read_handoff` | mcp/src/agents_remember/application/knowledge_writer/handoff.py:244-281 |
| A ruling no record names is refused, and so are proofs on it. | `_require_attached_rulings` | mcp/src/agents_remember/application/knowledge_writer/handoff.py:284-315 |
| Locators in the file form: symbol, line range, whole file. | `read_locator` | mcp/src/agents_remember/application/knowledge_writer/handoff.py:351-376 |
| Targets through the shipped realization rules. | `_targets` | mcp/src/agents_remember/application/knowledge_writer/handoff.py:379-412 |
| Proofs carry the curator's facet. | `_proofs` | mcp/src/agents_remember/application/knowledge_writer/handoff.py:430-453 |
| An entry: new invariant needs scope, admission and a statement. | `_entry` | mcp/src/agents_remember/application/knowledge_writer/handoff.py:466-511 |
| A record: kind, fields, and the writer-owned fields refused. | `_record` | mcp/src/agents_remember/application/knowledge_writer/handoff.py:518-551 |
| A history row: strict keys (since MIK-R11 including `ref`, which must be an object), writer-owned `id` and `revision`. | "def _row(position: int, raw: Any, problems: list[Problem])"; "'ref' is an object naming one row" | mcp/src/agents_remember/application/knowledge_writer/handoff.py:579-619 |
| The row keys and the request field a planned row's `ref` travels in. | `_ROW_KEYS`; `RowRequest` | mcp/src/agents_remember/application/knowledge_writer/handoff.py:47-49; mcp/src/agents_remember/application/knowledge_writer/handoff.py:219-233 |
| Four problems refused in one operation, each named. | `test_problems_refuse_the_whole_operation_and_each_is_named` | mcp/tests/test_knowledge_writer.py:341-366 |
| An entry that names no record is refused. | `test_an_entry_that_names_no_record_is_refused_and_nothing_of_it_dropped` | mcp/tests/test_knowledge_writer.py:531-553 |

## Cross-Repo References

No cross-repo boundary is crossed: the writer reads the paired code worktree and writes the paired memory
worktree of one repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History
- 2026-09-29T23:27:43+02:00 — 260928-MIK-L11 curator (uncommitted change set on `ar/260928-mik-l11`, code base `2c6f170ef07bf6767d582f76c9f9dd06bbdd06a4` plus the staged delta): **body updated for MIK-R11.** The Logic bullet on history rows now names the `ref` key a planned row carries and its object-shape refusal. **The reopened `_row` claim was re-read and reworded** (strict keys now include `ref`) and re-anchored on line-exact quotes, because the generated-repair bullet that binds it is committed. One row added (`_ROW_KEYS`, `RowRequest`). Other rows were re-pointed by the installed fixer. No verification stamp was advanced.
- 2026-09-29T15:26:13+02:00 — 260928-MIK-L28 curator (uncommitted change set on `ar/260928-mik-l28`, code base `8b0254263c6998b1d4814b2e97c1bd231d39350f` plus the working-tree delta and untracked files): Added the section "260928-MIK-L28 Evidence Names A Test In Two Forms": `tests_named_in`, `_SELECTED_TEST`, `_TEST_FILE` and `TestFileMention`, with the architect ruling that the "path plus symbol" form is `path -k name` with one identifier, for `.py` files. The Logic bullet on test IDs now names both forms. The reopened `EntryRequest` claim was re-read against the working tree: the class still carries the curator keys and a ruling still authors no invariant, but `cited_tests` now delegates to `tests_named_in`, so the row now says so and anchors `cited_tests`; its generated repair bullet was removed because the claim was reworded. One new Repo-Internal row and two test rows. The other ranges were re-pointed by the installed `memory-citations --fix`. No verification stamp was advanced.
- 2026-09-29T13:25:13+00:00: Generated citation repair: `Problem` repointed to mcp/src/agents_remember/application/knowledge_writer/handoff.py:71-79. No content impact: mechanical anchor-range projection bound to citation source snapshot 669685dd91608eb0296af5d8546b06d1035099d9a0ff44914baa1ead631123fe; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T13:25:13+00:00: Generated citation repair: `read_handoff` repointed to mcp/src/agents_remember/application/knowledge_writer/handoff.py:242-279. No content impact: mechanical anchor-range projection bound to citation source snapshot 669685dd91608eb0296af5d8546b06d1035099d9a0ff44914baa1ead631123fe; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T13:25:13+00:00: Generated citation repair: `_require_attached_rulings` repointed to mcp/src/agents_remember/application/knowledge_writer/handoff.py:282-313. No content impact: mechanical anchor-range projection bound to citation source snapshot 669685dd91608eb0296af5d8546b06d1035099d9a0ff44914baa1ead631123fe; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T13:25:13+00:00: Generated citation repair: `read_locator` repointed to mcp/src/agents_remember/application/knowledge_writer/handoff.py:349-374. No content impact: mechanical anchor-range projection bound to citation source snapshot 669685dd91608eb0296af5d8546b06d1035099d9a0ff44914baa1ead631123fe; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T13:25:13+00:00: Generated citation repair: `_targets` repointed to mcp/src/agents_remember/application/knowledge_writer/handoff.py:377-410. No content impact: mechanical anchor-range projection bound to citation source snapshot 669685dd91608eb0296af5d8546b06d1035099d9a0ff44914baa1ead631123fe; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T13:25:13+00:00: Generated citation repair: `_proofs` repointed to mcp/src/agents_remember/application/knowledge_writer/handoff.py:428-451. No content impact: mechanical anchor-range projection bound to citation source snapshot 669685dd91608eb0296af5d8546b06d1035099d9a0ff44914baa1ead631123fe; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T13:25:13+00:00: Generated citation repair: `_entry` repointed to mcp/src/agents_remember/application/knowledge_writer/handoff.py:464-509. No content impact: mechanical anchor-range projection bound to citation source snapshot 669685dd91608eb0296af5d8546b06d1035099d9a0ff44914baa1ead631123fe; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T13:25:13+00:00: Generated citation repair: `_record` repointed to mcp/src/agents_remember/application/knowledge_writer/handoff.py:516-549. No content impact: mechanical anchor-range projection bound to citation source snapshot 669685dd91608eb0296af5d8546b06d1035099d9a0ff44914baa1ead631123fe; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T13:25:13+00:00: Generated citation repair: `_row` repointed to mcp/src/agents_remember/application/knowledge_writer/handoff.py:577-614. No content impact: mechanical anchor-range projection bound to citation source snapshot 669685dd91608eb0296af5d8546b06d1035099d9a0ff44914baa1ead631123fe; claim bytes unchanged; generated by ccr-r10@v1.

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T10:05:46+02:00 — 260928-MIK-L12 curator (uncommitted change set on `ar/260928-mik-l12`, code base `6ad4e076bbbc5d98b8c770fc374d56ddc4a2d695` plus the staged delta): created this card for the new file MIK-R12 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
