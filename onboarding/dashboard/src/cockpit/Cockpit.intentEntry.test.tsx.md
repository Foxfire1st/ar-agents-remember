# dashboard/src/cockpit/Cockpit.intentEntry.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/cockpit/Cockpit.intentEntry.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-28T17:06:50+02:00 |
| lastVerifiedCommitHash | `e66f1f3894116e0bb37b49f178d8bfcb130a7e28` |
| lastVerifiedCommitDate | 2026-09-28T20:02:47+02:00|
| governingOverview | `dashboard/src/overview.md` |

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

## Docs References

No Domain Documentation source is configured for this test module.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The ruled triggers and the request-counting method. | "(a) the task detail is opened or shown again" | dashboard/src/cockpit/Cockpit.intentEntry.test.tsx:1-10 |
| Two live leaves seeded into the real store. | `seedTwoLiveLeaves` | dashboard/src/cockpit/Cockpit.intentEntry.test.tsx:97-126 |
| The route stub with the knowledge switch and the read counters. | `serve`; `summaryReads`; `catalogueReads` | dashboard/src/cockpit/Cockpit.intentEntry.test.tsx:131-197 |
| The first-ingest sequence every case starts from. | `openStaleEntry`; "no knowledge yet" | dashboard/src/cockpit/Cockpit.intentEntry.test.tsx:200-211 |
| (a) re-show, once per showing, no catalogue read. | "(a) re-validates when the task detail is shown again, once per showing, with no catalogue read" | dashboard/src/cockpit/Cockpit.intentEntry.test.tsx:213-232 |
| (a) opening a task from another view reads once. | "(a) opening a task from another view reads its entry exactly once" | dashboard/src/cockpit/Cockpit.intentEntry.test.tsx:234-245 |
| (b) leaving the reviewer re-validates. | "(b) re-validates when the developer leaves the reviewer back to the entry" | dashboard/src/cockpit/Cockpit.intentEntry.test.tsx:247-264 |
| (c) the reviewer's refresh re-validates. | "(c) re-validates when the reviewer's own refresh runs" | dashboard/src/cockpit/Cockpit.intentEntry.test.tsx:266-280 |
| The provider under test. | `IntentEntryRevalidation` | dashboard/src/data/intentEntryRevalidation.tsx:29-54 |

## Cross-Repo References

No cross-repository behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-28T17:06:50+02:00 — 260921-ICR-L47 curator (uncommitted candidate tree `72efa4bbc169b16afe8ef249499edf79cad9940d` over code base `58e22246cc09ef0ee12095e284a111a475081c38`): created this card for the cockpit-level re-validation cases added in L47-A3 (L47-R1-F2 under the 16:27:28 ruling). The verification pair names the code base; closeout owns the real stamp.
