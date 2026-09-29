# mcp/src/agents_remember/models/knowledge_files/planned.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge_files/planned.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T23:27:43+02:00 |
| lastVerifiedCommitHash | `46ca74302e76cf40fb6370ea9ece16d8fa719f00`|
| lastVerifiedCommitDate | 2026-09-30T00:07:49+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[models route overview](../overview.md)

## Purpose

**The one spelling of MIK-R11's planned-effect forms.** It defines the declared subject form
(`invariant:<INV-ID>`, `family:<FAM-ID>` or `new:<hand-off label>`), the planned subject key
`planned:<declared subject>#<effect>`, the `requirementRef` form, the three planned dispositions and the ref
each takes, and `planned_item_open`, the stored-item predicate for the closeout gate (MIK-R09). The task
plane (`tasks/document.py`), the history row model (`history.py`), the worklist (`planned_effects.py`) and
the writer all import these forms from here, so they cannot drift apart.

## Code Commentary

### Logic

- **Constants.** `PLANNED_ITEM_KIND` (`planned_untouched`), `SUBJECT_UNKNOWN` (`subject_unknown`) and
  `PLANNED_DISPOSITIONS` (`realized_elsewhere`, `deferred`, `dropped`). `REFS_BY_DISPOSITION` maps each
  disposition to the ref keys it may carry: `row`/`invariant`, `requirement`/`leaf`, and `decision`.
- **Patterns.** The invariant and family ID patterns are taken from `ids.id_pattern` (unanchored by
  `_unanchored`); a hand-off label is one line with no surrounding whitespace. `DECLARED_SUBJECT_PATTERN`
  anchors the declared form; `PLANNED_SUBJECT_PATTERN` is `planned:(?P<subject>…)#(?P<effect>…)` with the
  effect restricted to `ADMITTED_EFFECT_LABELS`, the unchanged vocabulary. `REQUIREMENT_REF_PATTERN` is
  `<stable ID>@v<n>` (ruling Q5).
- **The key.** `planned_subject(subject, effect)` builds it; `parse_planned_subject` returns the
  `(subject, effect)` pair or `None`.
- **The predicate.** `planned_item_open(item, rows_by_subject)` is open unless the leaf has a history row
  whose subject is the item's own subject, that is, a planned row. A `no_impact` or any other row about the
  declared invariant never answers the item, because its subject is the record ID, not the planned key.

### Conventions

- The module is pure: no I/O and no knowledge read, so the task plane can import it and still read no
  knowledge (rule 4).

### Invariants And Boundaries

- **The subject key is built from the declared subject and effect, never from list position** (rule 5):
  `planned_subject` takes no index, so editing the declaration list never shifts a key.
- **The effect vocabulary is unchanged** (Preservation): the effect alternation is the admitted labels.
- **`planned_item_open` agrees with the worklist's `satisfiedBy`**; both are the subject lookup of the
  planned row.

### Todos

- None recorded.

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
| The module docstring: the forms and who shares them. | "the one spelling of those forms" | mcp/src/agents_remember/models/knowledge_files/planned.py:1-20 |
| The item kind, the unknown-subject fact and the dispositions. | `PLANNED_ITEM_KIND`; `SUBJECT_UNKNOWN`; `PLANNED_DISPOSITIONS` | mcp/src/agents_remember/models/knowledge_files/planned.py:44-46 |
| The ref keys each disposition takes. | `REFS_BY_DISPOSITION` | mcp/src/agents_remember/models/knowledge_files/planned.py:50-54 |
| The declared, planned and requirement-ref patterns. | `DECLARED_SUBJECT_PATTERN`; `PLANNED_SUBJECT_PATTERN`; `REQUIREMENT_REF_PATTERN` | mcp/src/agents_remember/models/knowledge_files/planned.py:61-70 |
| The planned subject key and its parse. | `planned_subject`; `parse_planned_subject` | mcp/src/agents_remember/models/knowledge_files/planned.py:73-83 |
| The stored-item predicate for the gate. | `planned_item_open` | mcp/src/agents_remember/models/knowledge_files/planned.py:86-97 |
| The history row model built on these forms. | `PlannedEffectRow` | mcp/src/agents_remember/models/knowledge_files/history.py:310-333 |
| The predicate agrees with `satisfiedBy` on every item. | `test_a_planned_row_answers_its_item_and_the_stored_predicate_agrees` | mcp/tests/test_planned_knowledge_effects.py:363-398 |

## Cross-Repo References

No meaningful cross-repo references found: the module is pure models.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T23:27:43+02:00 — 260928-MIK-L11 curator (uncommitted change set on `ar/260928-mik-l11`, code base `2c6f170ef07bf6767d582f76c9f9dd06bbdd06a4` plus the staged delta): created this card for the new file MIK-R11 adds, recording the architect ruling of 21:56:18 (Q5: `requirementRef` as `<ID>@v<n>`). The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
