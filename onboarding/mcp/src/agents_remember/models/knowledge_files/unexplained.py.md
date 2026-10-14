# mcp/src/agents_remember/models/knowledge_files/unexplained.py

## Governing Overview

[models route overview](../overview.md)

## Purpose

**Shared spellings and low-level row lookup for MIK-R10's unexplained changes.** The worklist,
`history.UnexplainedChangeRow`, writer and gate use these subjects. This pure module reads no tree or
Git, and its subject-to-row-ID lookup does not validate onboarding source currency or disposition
eligibility. The candidate worklist and `application/knowledge_gate/predicates.unexplained_row_open`
perform those higher-level checks; shared spelling alone is not proof that their answers agree.

## Code Commentary

### Logic

- **Constants.** `HUNK_ITEM_KIND` (`unexplained_hunk`), `FILE_ITEM_KIND` (`unexplained_file`),
  `NO_INVARIANT`, `ABSENT`, `COVERED` and `UNCOVERED`. `COUNTED_CHANGE` is no longer a constant or export;
  the ordinary uncovered-item answer is an authored onboarding row ID, not `counted-change`.
- **Hunk subjects (rule 2).** `hunk_subject` spells `hunk:<path>@<base>..<candidate>`, each side
  `sha256:<64 hex>` or `absent`; `parse_hunk_subject` reads it back. `hunk_item_id` is the registry's ID
  formula over the kind, the subject and the subject's own two identities, so the ID is a function of the
  subject alone and a `hunk:<item id>` row names exactly one subject. Rule 6 keeps a covered hunk's
  `no_invariant` answer stable after an edit elsewhere; it does not guarantee that a source-bound
  onboarding judgment remains current after another source edit.
- **File subjects.** `file_subject` spells `file:<path>@<C-side object>`, `@absent` when C no longer holds the
  path; the object is a 40- or 64-hex Git ID.
- **Row subjects.** `ROW_SUBJECT_PATTERN` accepts `hunk:sha256:<64 hex>` (a hunk item's ID) or a file
  subject; `row_subject(item)` gives the row subject that answers a stored item.
- **The low-level helpers (`unexplained_satisfied_by`, `unexplained_item_open`).** A **covered** item
  looks up its `row_subject`; an **uncovered** item looks up the file's `onboarding:<path>` subject in
  the caller-supplied row-ID map. A counted card edit alone is not a returned answer. An unreadable
  trace sidecar or unstated coverage returns no answer. This lookup assumes the caller supplied
  eligible rows; it does not inspect source bindings. The ordinary candidate worklist and gate
  require a current authored onboarding row for uncovered files (`updated` plus a real counted
  card change, or an unchanged-contract `no_impact` judgment); `no_invariant` remains covered-only.

### Conventions

- Attach and author are not rows: an entry over the change links it, so the item is no longer raised. Only
  `no_invariant` is a row disposition here (rule 3).
- No I/O, no similarity matching and no suggestion (Exclusions).

### Invariants And Boundaries

- **Candidate worklist/gate agreement is checked at the currentness boundary.**
  `test_unexplained_change_disposition.unexplained` parses `HistoryFile`, builds `GateContext`, and
  compares `predicates.unexplained_row_open` with stored `satisfiedBy` on every item. The gate uses
  this module's helper for covered lookup, but its own onboarding-row currency for uncovered files.
  This is a static assertion description, not a fresh run or a one-helper agreement warrant.
- **`no_invariant` answers only covered items.** Realized by the coverage split in
  `unexplained_satisfied_by`; proved by `test_an_uncovered_new_file_is_satisfied_by_its_onboarding_trace`.
- **Unconverted memory reads are unchanged.** Nothing reads this module on an unconverted leaf, which gets no
  worklist.

### Todos

- The current gate owner is `application/knowledge_gate/predicates.unexplained_row_open(item, context)`.
  `unexplained_item_open(item, rows_by_subject)` remains only the pure Boolean lookup wrapper; it
  cannot establish source-bound onboarding currentness.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R10@v2` of task
`260928_maintained-invariant-knowledge` and its leaf document `10_unexplained-change-disposition.json`; they
live outside the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The subject patterns and the row-subject pattern. [3]
- The hunk subject spelled and parsed. [4]
- The item ID is a function of the subject alone. [5]
- The file subject, `@absent` when C lacks the path. [6]
- The row subject that answers an item. [7]
- The history row kind built on these patterns. [10]

### Cross-Repo References

No meaningful cross-repo references found: the module is pure spelling and a predicate over stored items.

No cross-repo boundary is crossed by this file.

- Shared subject spellings and coverage-split lookup; higher-level worklist/gate checks own source currency. [1]
- The kinds, `no_invariant`, `absent` and coverage states; the removed `COUNTED_CHANGE` symbol is not current evidence. [2]
- Covered: row-subject lookup; uncovered: onboarding-subject row-ID lookup, never a counted-edit answer. Source currency is checked outside this pure helper. [8]
- The pure Boolean lookup wrapper is not the current gate owner; the source-bound gate predicate is `application/knowledge_gate/predicates.unexplained_row_open`. [9]
- Every case checks `predicates.unexplained_row_open` over parsed history/GateContext against the worklist's stored `satisfiedBy`, including onboarding source currency. [11]
- Current source delta inspected statically: Remove counted-change export/answer and one-helper agreement warrant; distinguish pure lookup from currency, preserving subject spellings and markers. [12]
