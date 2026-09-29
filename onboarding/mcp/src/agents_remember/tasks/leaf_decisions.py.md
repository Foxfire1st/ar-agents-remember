# mcp/src/agents_remember/tasks/leaf_decisions.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/tasks/leaf_decisions.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T23:27:43+02:00 |
| lastVerifiedCommitHash | `46ca74302e76cf40fb6370ea9ece16d8fa719f00`|
| lastVerifiedCommitDate | 2026-09-30T00:07:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[tasks/overview.md](overview.md)

## Purpose

**The task owner's answers about a leaf's task document for MIK-R11: its declaration and its decisions.**
Both go through one strict lookup, `strict_leaf_doc`, which fails closed on identity doubt instead of
skipping what it cannot read. The worklist reads the leaf's `expectedKnowledgeEffects` through it
(`knowledge_worklist/leaf.leaf_expected_effects`), and the knowledge writer asks `leaf_decision_refusal`
whether a planned `dropped` row's cited decision resolves (bound by `cli/knowledge_write_route.leaf_decisions`).

## Code Commentary

### Logic

- **`strict_leaf_doc(task_root, leaf_id)`** returns the leaf's one `(path, TaskDocument)`, `None` when the
  leaf has no document, or raises `LeafDocumentUnresolved` (a `ValueError`):
  - it is `leaf_doc.resolve_terminal_leaf_doc` first: two documents claiming the leaf are ambiguous, and an
    unreadable document whose file stem is the leaf's is refused (`TerminalLeafResolutionError` is re-raised
    as `LeafDocumentUnresolved`);
  - beyond it, `_unreadable_claims` reads every `*.json` in the task root and refuses any document that
    fails to read while its raw JSON still names the leaf (`_names_leaf`: its `id`, or an
    `enclosures[].leafId`; a master never counts). The message names each file and its first error line.
  - An unreadable JSON file that names no leaf (a preview or other sibling artifact) is ignored, as the
    terminal resolver ignores it.
- **`leaf_decision_refusal(task_root, leaf_id, at)`** is `None` when the leaf's document holds exactly one
  decision entry whose `at` equals the citation. Otherwise it returns why not: the strict lookup's doubt, no
  task document, no entry at `at`, or several entries at `at` (ambiguous). Task-document decisions carry no
  ID, so the `at` is the citation (ruling Q5).

### Conventions

- The module answers as the task owner; the knowledge writer takes its answer through an injected
  `DecisionResolver`, so the writer never imports the task plane (layering).
- `leaf_doc.find_leaf_doc` (fail-soft) is unchanged; `leaf_maintenance_scope` still reads through it, a
  pattern carried to L09 (ruling F2).

### Invariants And Boundaries

- **An unreadable leaf document never reads as "nothing declared"** (ruling F2, 2026-09-29T22:35:34+02:00).
  Candidate invariant; realized by `strict_leaf_doc` raising `LeafDocumentUnresolved`, which the worklist turns
  into an `incomplete` run naming the input `leaf task document`; proved by the unreadable-document block of
  `test_a_leaf_reads_its_declaration_and_the_checklist_and_tool_show_the_marks`.
- **Ambiguity refuses** (ruling F1): two documents claiming the leaf, an unreadable claiming document, or two
  decision entries at the same `at` are refusals, never a first-match answer.

### Todos

- `leaf_maintenance_scope` keeps the fail-soft lookup; making it strict is carried to L09 (ruling F2).

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R11@v2` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`11_planned-invariant-effects-reconciliation.json`); it lives outside the code and memory repositories, so it
is named here and not cited as a row.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module docstring: one strict lookup for both answers. | "identity doubt instead of skipping what it cannot read" | mcp/src/agents_remember/tasks/leaf_decisions.py:1-20 |
| The doubt, as one exception type. | `LeafDocumentUnresolved` | mcp/src/agents_remember/tasks/leaf_decisions.py:35-36 |
| The strict lookup: the terminal resolver plus unreadable claims. | `strict_leaf_doc`; `resolve_terminal_leaf_doc` | mcp/src/agents_remember/tasks/leaf_decisions.py:39-51 |
| Unreadable documents that still name the leaf. | `_unreadable_claims`; `_names_leaf` | mcp/src/agents_remember/tasks/leaf_decisions.py:54-78 |
| The decision citation: exactly one entry at `at`. | `leaf_decision_refusal` | mcp/src/agents_remember/tasks/leaf_decisions.py:81-98 |
| The terminal resolver it builds on. | `resolve_terminal_leaf_doc` | mcp/src/agents_remember/tasks/leaf_doc.py:106-137 |
| The answers: resolved, none, ambiguous, no document, and the four doubt cases. | `leaf_decision_refusal` | mcp/tests/test_planned_knowledge_effects.py:431-452 |
| An unreadable leaf document makes the worklist incomplete. | "leaf task document" | mcp/tests/test_planned_knowledge_effects.py:579-587 |

## Cross-Repo References

The task root is in the coordination root, outside the code repository; the module reads it through the
task plane's own store (`tasks/store.read_task_doc`).

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T23:27:43+02:00 — 260928-MIK-L11 curator (uncommitted change set on `ar/260928-mik-l11`, code base `2c6f170ef07bf6767d582f76c9f9dd06bbdd06a4` plus the staged delta): created this card for the new file MIK-R11 adds, recording the architect rulings of 21:56:18 (Q5) and 22:35:34 (F1, F2). The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
