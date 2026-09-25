# dashboard/src/data/changeset.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/changeset.test.ts`           |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-09-22T11:00:00+02:00 |
| lastVerifiedCommitHash | `09329a7ee598920c519b06305b73ba8e48d72c88`       |
| lastVerifiedCommitDate | 2026-09-26T00:58:43+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[data overview](overview.md)

## Purpose

Vitest contract test for the `data/changeset` client. It stubs the global `fetch` and asserts that each
helper builds the exact L3 change-set endpoint URL with encoded query params. The test proves that a
non-ok response throws `FilesApiError`; the production clients and serving route separately own status
retention and the 400/404 response mapping.

## Code Commentary

### Logic

The URL contract tests cover the optional master `includeLeaves=false` query
shape alongside the existing task, file-diff, and leaf selectors, ensuring the
typed client does not silently drop the flag when a caller sets it. **260921-ICR-L33 note, because the
flag's story changed:** the R33.2 readers pass `includeLeaves: true` (and a contract case for that
spelling lives in the viewer's own suite), so `false` here pins a retained API path rather than the
path the product takes. The test file is byte-unchanged by that leaf, and this sentence described the
mechanism correctly before and after; the note exists so a reader does not infer the product's request
shape from the pinned flag.

- cit:([`stubFetch`, `afterEach`], dashboard/src/data/changeset.test.ts:6-12; dashboard/src/data/changeset.test.ts:14-14) installs a `vi.fn` `fetch`
  returning a minimal `Response`-shaped object and restores globals after each test.
- cit:(["includeLeaves=false"], dashboard/src/data/changeset.test.ts:16-32)
  covers the task, file-diff, and master URLs, including the optional `includeLeaves=false` selector:
  `/api/changeset/task?repo&scope`,
  `/api/changeset/file-diff?...&kind=memory&path=...` (note the `%2F`-encoded path), and
  `/api/changeset/master?repo&master`.
- cit:([`leafChangeset`, `leafFileDiff`], dashboard/src/data/changeset.test.ts:32-46) calls the leaf URLs on
  the same `task` / `file-diff` routes with the `leaf` + `mode` query.
- cit:(["not-found"], dashboard/src/data/changeset.test.ts:54-57) stubs a 404 `{status: "not-found"}`
  and asserts that `taskChangeset` rejects with a `FilesApiError` instance.
- cit:(["carries generation pins on the master URLs and omits unset pins"], dashboard/src/data/changeset.test.ts:59-77)
  pins the generation params on the master list and file-diff URLs (`codeBase`/`codeTip` carried,
  unset pins omitted so the request selects the declared integrated result).

### Invariants And Boundaries

Pure unit test: `fetch` is fully stubbed (no network), pinning URL construction + error mapping, not
server behavior. Globals are restored after every case so stubs never leak.

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Stubs `fetch` and unstubs globals after each test. | `fetch` | dashboard/src/data/changeset.test.ts:6-14 |
| Asserts the task / file-diff / master URLs (including `%2F` path encoding). | "includeLeaves=false" | dashboard/src/data/changeset.test.ts:16-32 |
| Asserts generation pins ride the master URLs and unset pins are omitted. | "carries generation pins on the master URLs and omits unset pins" | dashboard/src/data/changeset.test.ts:59-77 |
| Asserts a non-ok (404) response throws `FilesApiError`. | "not-found" | dashboard/src/data/changeset.test.ts:54-57 |
| The test imports and exercises taskChangeset and FilesApiError in its URL and error cases. | `taskChangeset`, `FilesApiError` | dashboard/src/data/changeset.test.ts:3-4; dashboard/src/data/changeset.test.ts:16-32; dashboard/src/data/changeset.test.ts:54-57 |
| Contract counterpart: the serving layer emits the 404/400 codes this test stubs. | "def _leaf_json(produce: Any, master: str, mode: str) -> Response:"; "leaf change-set needs master" | mcp/src/agents_remember/serving/changeset.py:633-633; mcp/src/agents_remember/serving/changeset.py:642-642 |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History
- 2026-09-25T23:58+02:00 — 260921-ICR-L25 curator, round 2 (uncommitted change set on `ar/260921-icr-l25-ar`, code base `d9e7e6e79ce532d16c689435ae95a63aab430f94` plus the working-tree delta, memory base `39adea206651654dbfacf2ee1bb4e2f3763b515b`; round-2 report `report-l25-round2.md` = `9446232d…`): **citation repair only, forced by the served contract this test's stubs mirror.** The row citing `serving/changeset.py`'s `_leaf_json` and its `leaf change-set needs master` refusal pointed at `:614`/`:623`, which the round-2 change set moved; both anchors now resolve where they live (`:633` for the handler, `:642` for the `400` body). **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted, so the governed closeout owns the real stamp. No commit was made.
- 2026-09-24T23:30:00+02:00 — 260921-ICR-L33 curator (candidate `ar/260921-icr-l33-ar`, uncommitted; code base `86639933d61528387ce106dbd4d7a334bd468671` plus the working-tree delta; adversarial round 2 `verify-l33.md` = `pass`): **one dated reader note added; no claim changed.** This test file is byte-unchanged by the leaf, and its `includeLeaves=false` case still passes and is still worth pinning. What changed is what that flag MEANS to a reader: both dashboard master-net readers now pass `includeLeaves: true` (R33.2), so the `false` case documents retained API surface rather than the product's request. The Logic paragraph says so. **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted and the governed closeout owns the real stamp.
- 2026-09-22T19:40:00+02:00 — 260921-ICR-L8 curator (candidate `ar/260921-icr-l8`, uncommitted; production line at this leaf's base `02957762709c9b515b4ff57f7f13524a7c0dfb8d`): **metadata-row removal.** The candidate-reading metadata rows this card carried were removed under the developer's 2026-09-22 rule: the field is not a real metadata field, has no purpose, and must not be written or carried anywhere. The reading those rows recorded is preserved in this entry's own words — the claims on this card were taken against the leaf candidate named above where they describe uncommitted work, and against the last real commit the card's stamp names where they describe shipped code. No claim, anchor, wording or citation range changed, no table shape changed, and no verification stamp was advanced.
- 2026-09-22T11:00:00+02:00 — 260921-ICR-L13 curator (candidate `ar/260921-icr-l13`, uncommitted; base `6695a2a12961ef340c8864d56f0a1ce12b51b3c5`): **one new pins case (58 → 78 lines).** The Logic and table record `carries generation pins on the master URLs and omits unset pins` (`:59-77`); the pre-existing URL/error rows are kept as recorded (this leaf appends after them, so their ranges stand). The serving-counterpart row is re-derived against this candidate (`_leaf_json` `:493` → `:614`, the `needs master` refusal `:502` → `:623`). Verification metadata is **not** advanced: the candidate is uncommitted and closeout owns the stamp. The 2026-09-21 mechanical projection bullet below that recorded the superseded ranges (`:493`, `:502`) is retired by this reading.

- 2026-08-11T15:20+02:00 — Replaced the ambiguous `status_code` evidence with the exact 400 and
  404 response expressions; the serving-contract claim is unchanged.
- 2026-08-04T11:42:15+02:00 — 260731-EFA-L6 S18-B04 — same-reviewer residual correction: bound the test imports and URL/error
  cases to the complete `taskChangeset`/`FilesApiError` test evidence through the scoped fixer.

- 2026-07-18T07:22+02:00 — FEUI-L8 manual route refactor: retargeted this direct data file card
  from the packed dashboard/src parent to the new nearest data authority overview. Source behavior
  is unchanged by this memory-only governance move; verification hash/date remain pinned.

- 2026-07-12T12:55+02:00 — 260712-TRH-L2: added the master query-shape assertion for `includeLeaves=false`; existing selector and error URL coverage remains intact. Verification metadata pinned until closeout stamps the L2 code commit.

- 2026-06-29T23:00+02:00 — L4a: added a case pinning the leaf URLs (`leafChangeset` + `leafFileDiff` ride
  the `task` / `file-diff` routes with a `leaf` + `mode` query). Verification metadata pinned until
  closeout stamps the L4a commit.
- 2026-06-29T16:40+02:00 — Created for operations-integration L4 (Change-Set Viewer): vitest contract
  test that stubs `fetch` and pins the `data/changeset` client's endpoint URLs and `FilesApiError`
  mapping. Verification metadata pinned to the task base until closeout stamps the L4 code commit.
