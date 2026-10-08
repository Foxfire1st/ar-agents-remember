# mcp/src/agents_remember/models/knowledge_files/planned.py

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
- **The key.** `planned_subject(subject, effect)` builds it; `PLANNED_SUBJECT_PATTERN` declares its subject/effect grammar. This module has no `parse_planned_subject` function; history-model validation owns parsing.
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

## Evidence

### Repo-Internal References

- `planned_subject` implements the retained boundary described above. [9]
- `planned_item_open` implements the retained boundary described above. [10]
