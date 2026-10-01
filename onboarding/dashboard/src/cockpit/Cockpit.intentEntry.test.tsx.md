# dashboard/src/cockpit/Cockpit.intentEntry.test.tsx

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

Pins the ruled re-validation points of the task entry's Intent review counts against the **real
`CockpitShell`** (leaf `260921-ICR-L47`, Architect ruling 2026-09-28T16:27:28+02:00 on L47-R1-F2). No
dashboard signal moves when a leaf's knowledge is first written, so the entry keeps showing
`no knowledge yet` until (a) the task detail is opened or shown again, (b) the developer leaves the reviewer
back to the entry, or (c) the reviewer's own refresh runs. Each case reproduces the first-ingest sequence —
stale entry, the store gains knowledge with no read, then one trigger — and counts requests.

## Code Commentary

### Logic

- `seedTwoLiveLeaves` seeds two live leaves (`direct-leaf`, `other-leaf`) with their task documents,
  lifecycles and enclosures.
- `serve` stubs `fetch` for every route the journey touches. `knowledge.present` is the store: the summary
  answers `unavailable` (`candidate_dataset_absent`) until it flips, then `counted` `+2 −0`. It exposes
  `summaryReads(leaf)` and `catalogueReads()`.
- `openStaleEntry` opens the task, asserts `no knowledge yet` after exactly one summary read, flips the
  store, and asserts no further read happened.
- The four cases: (a) Memory → Operations re-reads once and shows `+2 −0`, switching to the other task and
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

No Domain Documentation source is configured for this test module.

No relevant domain documentation was found.

### Repo-Internal References

- The ruled triggers and the request-counting method. [1]
- Two live leaves seeded into the real store. [2]
- The route stub with the knowledge switch and the read counters. [3]
- The first-ingest sequence every case starts from. [4]
- (a) re-show, once per showing, no catalogue read. [5]
- (a) opening a task from another view reads once. [6]
- (b) leaving the reviewer re-validates. [7]
- (c) the reviewer's refresh re-validates. [8]
- The provider under test. [9]

### Cross-Repo References

No cross-repository behavior.

No meaningful cross-repo references found.
