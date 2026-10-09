# mcp/src/agents_remember/application/knowledge_writer/handoff.py

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
  names is checked by `authoring._planned_row`, not here. A cover is an entry ID, `{id, path?, locator?, remove?}` or
  `{handoff}`; `path` (since MIK-R06, L06 ruling Q6) names the source file a `moved` row relocates the entry to.
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
- **A malformed cover path is refused as a named problem, never an uncaught error** (L06 review F1). Candidate
  invariant; realized by `_cover_path` (`require_repository_path` inside a `try`); proved by the refusal cases
  of `test_a_moved_row_whose_after_names_another_path_relocates_the_entry`.
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

- Both forms, the bare file, and expressions that are not read as one test. [1]
- A file named with a test anywhere in the evidence is not also reported bare. [2]

## 260928-MIK-L06 A Cover May Name The Path Its Entry Moves To (MIK-R06, Ruling Q6)

A directory move needs `moved` invariant rows whose `after` anchor names the new file (MIK-R07 rule 4,
MIK-R12 rule 2). The architect ruled the writer's inability to move an entry to another file a conformance
gap of landed L12 and had L06 close it minimally (ruling Q6, 2026-09-29T21:49:19+02:00). This module's part
is the hand-off shape:

- `CoverRequest.path` carries the source path the entry moves to; `_cover` reads it through two helpers,
  `_cover_locator` (the locator, split out so the function stays within ruff's return-count limit) and
  `_cover_path`. A bad locator and a bad path on one cover are now both reported.
- `_cover_path` refuses, as named problems (ruling 2026-09-29T22:40:22+02:00):
  - a path that is not a repository path: empty, absolute, `..`, `.`, an empty segment or not a string
    ("a cover's path is not a repository path: …", review F1), checked with
    `models/knowledge_files/shapes.require_repository_path`;
  - a cover carrying both `remove` and `path` ("a cover either removes its entry or moves it to a path",
    review N7).
- Which dispositions may carry a path is `authoring._covers`'s decision (only `moved`), not this module's.

- The module docstring: a moved row's cover may name another source path, and a cover may carry a rationale that replaces the entry's in place. [3]
- The cover request, its `path` and its `rationale`. [4]

- A cover read: its ID, locator, path and rationale, with every problem reported. [5]

- The path check: remove plus path, and a path that is not a repository path, are named problems. [6]
- The four refusals and the relocation, end to end. [7]

## 260928-MIK-L37 A Cover May Carry A Rationale

`CoverRequest.rationale` carries a realization entry's revised rationale; the entry keeps its ID. `_cover` reads it
through `_cover_rationale`, beside the locator and the path. A blank rationale ("a cover's rationale is a non-empty
text") and a rationale on a cover that removes its entry ("a cover either removes its entry or revises its
rationale") are named problems. A cover is an entry ID, `{id, path?, locator?, rationale?, remove?}` or `{handoff}`.

- The cover request and its rationale. [23]
- A cover's rationale: non-empty, and never beside remove. [24]

## The Effect Input Gate (MIK-R48)

`family_effect_refusal` is the input gate for the effect vocabulary: a changed
family row without a valid authored effect is refused, an effect on a rerouted,
assigned, no_impact or retired row is refused naming the row, the field and the
disposition, and the gate never derives a label from wording, reason,
disposition, counts, members or a member's effect.

- The gate requires the effect on changed rows and refuses it elsewhere. [25]

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R12@v2` of task
`260928_maintained-invariant-knowledge` (with its architect rulings in the task's leaf document
`12_category-authoring-through-the-curator-workflow.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The document's sections and their readers.

- The template's `incidental` is written as `support`. [8]
- One refusal reason: where, and what. [9]
- An entry and its curator keys; a ruling authors no invariant; the tests its evidence cites come from `tests_named_in`. [10]
- The two test forms and the bare test module, read in order and once each. [11]
- Read the three sections, collecting every problem. [12]
- A ruling no record names is refused, and so are proofs on it. [13]
- Locators in the file form: symbol, line range, whole file. [14]
- Targets through the shipped realization rules. [15]
- Proofs carry the curator's facet. [16]
- An entry: new invariant needs scope, admission and a statement. [17]
- A record: kind, fields, and the writer-owned fields refused. [18]
- A history row: strict keys (since MIK-R11 including `ref`, which must be an object), writer-owned `id` and `revision`. [19]
- The row keys and the request field a planned row's `ref` travels in. [20]
- Four problems refused in one operation, each named. [21]
- An entry that names no record is refused. [22]

### Cross-Repo References

No cross-repo boundary is crossed: the writer reads the paired code worktree and writes the paired memory
worktree of one repository.

No cross-repo boundary is crossed by this file.
