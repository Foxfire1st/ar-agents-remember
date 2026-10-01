# mcp/src/agents_remember/models/knowledge_files/unexplained.py

## Governing Overview

[models route overview](../overview.md)

## Purpose

**The one spelling of MIK-R10's unexplained-change subjects and of the rule that answers them.** The worklist
(`application/knowledge_worklist/unexplained.py`), the history-row model (`history.UnexplainedChangeRow`), the
writer and the closeout gate (MIK-R09, L09) all import from here, so an item's subject, the subject of the
`no_invariant` row that answers it, and the open/satisfied predicate cannot drift apart. The module is pure: it
reads no tree and no Git.

## Code Commentary

### Logic

- **Constants.** `HUNK_ITEM_KIND` (`unexplained_hunk`), `FILE_ITEM_KIND` (`unexplained_file`),
  `NO_INVARIANT`, `ABSENT`, `COVERED`, `UNCOVERED`, and `COUNTED_CHANGE` (the `satisfiedBy` of an uncovered
  item whose card carries a counted onboarding change).
- **Hunk subjects (rule 2).** `hunk_subject` spells `hunk:<path>@<base>..<candidate>`, each side
  `sha256:<64 hex>` or `absent`; `parse_hunk_subject` reads it back. `hunk_item_id` is the registry's ID
  formula over the kind, the subject and the subject's own two identities, so the ID is a function of the
  subject alone and a `hunk:<item id>` row names exactly one subject (rule 6: an edit elsewhere in the file
  never changes it).
- **File subjects.** `file_subject` spells `file:<path>@<C-side object>`, `@absent` when C no longer holds the
  path; the object is a 40- or 64-hex Git ID.
- **Row subjects.** `ROW_SUBJECT_PATTERN` accepts `hunk:sha256:<64 hex>` (a hunk item's ID) or a file
  subject; `row_subject(item)` gives the row subject that answers a stored item.
- **The predicate (`unexplained_satisfied_by`, `unexplained_item_open`).** A **covered** item is answered
  only by the leaf's row with its `row_subject`. An **uncovered** item is answered only by the file's
  onboarding trace: a counted change (`facts.onboardingTrace.countedChange`) or the `onboarding:<path>` row.
  An unreadable card sidecar never satisfies a trace (MIK-R30), and an item whose coverage is not stated is
  open. An onboarding change never answers a covered item, and a `no_invariant` row never answers an
  uncovered one (rule 5; ruling 03:24:28 N2).

### Conventions

- Attach and author are not rows: an entry over the change links it, so the item is no longer raised. Only
  `no_invariant` is a row disposition here (rule 3).
- No I/O, no similarity matching and no suggestion (Exclusions).

### Invariants And Boundaries

- **The worklist's `satisfiedBy` and the gate's predicate agree by construction.** Candidate invariant;
  realized by `unexplained_satisfied_by` being the one function both call; proved by the `unexplained`
  helper of `test_unexplained_change_disposition.py`, which asserts agreement on every item of every case,
  and by the worker's and reviewer's real runs.
- **`no_invariant` answers only covered items.** Realized by the coverage split in
  `unexplained_satisfied_by`; proved by `test_an_uncovered_new_file_is_satisfied_by_its_onboarding_trace`.
- **Unconverted memory reads are unchanged.** Nothing reads this module on an unconverted leaf, which gets no
  worklist.

### Todos

- **L09:** the gate applies `unexplained_item_open(item, rows_by_subject)`, a subject-to-row-ID map (the same
  shape as MIK-R30's predicate takes).

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R10@v2` of task
`260928_maintained-invariant-knowledge` and its leaf document `10_unexplained-change-disposition.json`; they
live outside the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module docstring: both subjects and what satisfies an item by coverage. [1]
- The kinds, the disposition and the coverage states. [2]
- The subject patterns and the row-subject pattern. [3]
- The hunk subject spelled and parsed. [4]
- The item ID is a function of the subject alone. [5]
- The file subject, `@absent` when C lacks the path. [6]
- The row subject that answers an item. [7]
- Covered: the row; uncovered: the onboarding trace. [8]
- The gate's predicate. [9]
- The history row kind built on these patterns. [10]
- Every case checks that the stored predicate agrees with `satisfiedBy`. [11]

### Cross-Repo References

No meaningful cross-repo references found: the module is pure spelling and a predicate over stored items.

No cross-repo boundary is crossed by this file.
