# dashboard/src/panels/review/worklistGroups.test.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/worklistGroups.test.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T09:59:20+02:00 |
| lastVerifiedCommitHash | `b54d1b0331f67454bcf245a7a338b04900181c3c`|
| lastVerifiedCommitDate | 2026-09-30T11:03:56+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**The worklist grouping cases (2).** The worklist is the real served tree view of the converted scratch leaf
(`../../data/reviewTrees.captured.json`); the unexplained items are built by `hunk()` in exactly the shape of
MIK-R10's `unexplained_hunk` items (`facts.path`, `facts.coverage.state`, `facts.row`), because the captured leaf
has none.

## Code Commentary

### Logic

- **Planning marks and planned effects:** over the real worklist, INV-2TQGXFAX is `planned` and FAM-2HBJREC2
  `unplanned` (`planningMarks` gives `touched invariant · planned`), and the `planned_untouched` items are listed
  apart.
- **Unexplained grouping and the row lookup:** unexplained items across files and coverage states are grouped by
  file, then by coverage state, with a count per file; a history row whose subject is an item's `facts.row` is found
  for that item (`rowSubjects`).

### Conventions

- Pure functions over data; no DOM.

### Invariants And Boundaries

- The derived unexplained items are labelled as shaped after MIK-R10 in the file header; they are not a capture.

### Todos

No additional work is asserted by this card.

## Docs References

No domain documentation source is configured; the requirement packets live outside the repositories.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The real worklist and the MIK-R10-shaped unexplained items. | "'../../data/reviewTrees.captured.json'"; `hunk` | dashboard/src/panels/review/worklistGroups.test.ts:1-31 |
| The two cases. | "marks knowledge items planned or unplanned and lists the declared effects no row delivered"; "groups unexplained items by file and coverage state and finds their rows by facts.row" | dashboard/src/panels/review/worklistGroups.test.ts:32-86 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T09:59:20+02:00 — 260928-MIK-L31 curator (staged change set on `ar/260928-mik-l31`, code base `48f680d5b95b8cb6eafff4f1ccd19c8f32e8c48c`; review R3 pass-with-notes): created this card for the new test module (the carried L10 grouping, L11 marks and the PS-1 lookup). The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
