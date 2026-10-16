# dashboard/src/cockpit/Cockpit.intentEntry.test.tsx

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

`Cockpit.intentEntry.test.tsx` proves the Operations intent-entry re-validation contract (260921-ICR-L47):
the entry's summary re-reads once per showing, opening a task from another view reads its entry exactly
once, and leaving and returning to the reviewer re-reads it while otherwise reads stay standing.

## Code Commentary

### Logic

- The cases mount `CockpitShell`; MIK-R79 made Chats the opening view, so they mount
  `CockpitShell initialView="operations"` and use **File Viewer** as the other full-bleed view to
  leave and return to Operations (replacing the Memory tab, which has no bar entry).
- The read-count assertions and the stale-entry setup are unchanged.

### Conventions

Vitest + Testing Library; the routes stub counts summary and catalogue reads per case.

### Invariants And Boundaries

The suite binds the re-validation generation wiring (`IntentEntryRevalidation`) to the Operations
view only; it does not assert the retired pages.

### Todos

No additional work is asserted by this card.

### Logic

- `seedTwoLiveLeaves` publishes two native TaskEntry rows (`direct-leaf`, `other-leaf`) with qualified references, reader summaries and their own bound worktrees. The body stub finds each summary by entry key; no lifecycle/document/enclosure join is seeded.
- `serve` stubs `fetch` for every route the journey touches. `knowledge.present` is the store: the summary
  answers `unavailable` (`candidate_dataset_absent`) until it flips, then `counted` `+2 −0`. It exposes
  `summaryReads(leaf)` and `catalogueReads()`.
- `openStaleEntry` opens the task, asserts `no knowledge yet` after exactly one summary read, flips the
  store, and asserts no further read happened.
- The four cases: (a) File Viewer → Operations re-reads once and shows `+2 −0`, switching to the other task and
  back adds one read per leaf and no duplicate, and no catalogue read happens; (a) opening a task from
  another view reads its entry exactly once; (b) opening the reviewer causes no entry re-read and one
  catalogue read, and `review-back` adds exactly one summary read; (c) `review-refresh` inside the reviewer
  adds exactly one summary read and no second catalogue read.

### Conventions

Terminal rendering is mocked; the store is reset and `fetch` unstubbed after each case. Requests are counted
by URL path and `leaf` parameter.

### Invariants And Boundaries

- Each trigger costs exactly one summary read; no trigger reads the catalogue before the reviewer is opened.
- Pinning the generation to 0 (the A2 behaviour) fails the (a), (b) and (c) cases; the open-once case is an
  economy guard and passes either way (`notes/reports/l47-evidence/a3/f2-without-revalidation-fails.txt`).
- It does not claim a live push while the same panel stays open; the ruling does not require one.

### Todos

None.

## Evidence

### Docs References

No domain documentation source is configured for this repository. The requirement packet
`MIK-R79@v1` (rule 16) fixes the opening view and the product bar; it lives outside the code and
memory repositories, so it is named here and not cited as a row.

No configured live documentation source was available for this pass.

No Domain Documentation source is configured for this test module.

No relevant domain documentation was found.

### Repo-Internal References

- The re-validation boundary the cases exercise. [10]
- The shell the cases mount on an injected view. [11]
- The mode-bar entry used to leave and return to Operations. [12]

- The ruled triggers and the request-counting method. [22]
- Two live leaves seeded into the real store. [23]
- The route stub with the knowledge switch and the read counters. [24]
- The first-ingest sequence every case starts from. [25]
- (a) re-show, once per showing, no catalogue read. [26]
- (a) opening a task from another view reads once. [27]
- (b) leaving the reviewer re-validates. [28]
- (c) the reviewer's refresh re-validates. [29]
- The provider under test. [30]

### Cross-Repo References

No cross-repo boundary is crossed by this file.

No cross-repository behavior.

No meaningful cross-repo references found.
