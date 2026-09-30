# dashboard/src/panels/review/ReviewReadCycle.family.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/ReviewReadCycle.family.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T22:35:02+02:00 |
| lastVerifiedCommitHash | `3dc2ab0cf59cdc87ec478f6563d4ac6696871076`|
| lastVerifiedCommitDate | 2026-09-30T23:11:04+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[panels route overview](../overview.md)

## Purpose

Protect exact bounded family continuation through the real client/read hook and mounted review, using complete bodies captured from public authorship and the real HTTP route.

## Code Commentary

### Logic

The capture supplies before and after walks at a fixed page size. The positive flow preserves exact content and claims as those walks advance independently, including identical replay and repeated first pages from another side. Primary statement/evidence and the complete inventory remain their response owners' values.

The negative cases begin with coherent accumulated context. Wrong cursor, comparison, snapshot, subject, namespace, family revision, stale state, immutable content and structured page refusal must fail visibly without installing the rejected response. An unadvertised request cursor receives the same admission check. Whole-review refusal still suppresses the display through the existing outcome rule.

Mounted cases inspect the displayed statement, evidence, sibling rows, inventory, continuation and owner recovery text. The actual family-detail branch distinguishes content-only pages, a fully accumulated roster and unavailable scope. Refresh and changed subject/history reset accumulation; a late superseded response cannot restore an older question. Focus, layout and open-file state survive a legitimate continuation.

### Conventions

Only fetch and the separately tested catalogue hook are isolated. Since L48 `useReviewReadCycle` requires the surface's `ReviewReadCache`, so the hook harnesses (`mountCycle` and the reset case) each construct a fresh cache; a fresh cache per mount means no case is answered from another case's reads. Successful review bodies come from the capture; deliberate corruptions are negative probes. The capture is `familyPaging.captured.json`. **MIK-L31 re-captured it from the current route** (MIK-R31 rule 6, the L44-R1-F5 remainder: L44's producer, first build accepted, one attempt; the receipt's `mik_l31_recapture` entry at the L10-synced tree `18b77329`), so its member sources now carry `locator`, `resolved_ranges` and `locator_state`. Because family order follows the stored identities each build draws afresh, the late-source-expression case now opens the subject inside the capture's own `family_id` explicitly rather than relying on that family being listed first. The module header (lines 22-28, refreshed by a comment-only follow-up) says so, and says why the cases open the walked family by its `family_id`. Source-content requests receive their own explicit test refusal when a case measures selection rather than served bytes. This is mounted component evidence, not installed-browser or whole-product acceptance.

### Invariants And Boundaries

A rejected response is never a successful replacement. Exact identity and complete preserved populations matter; text coincidence and passing merge helpers alone do not establish display safety. The capture is regression evidence, never the repository's live knowledge foundation.

### Todos

None recorded.

## Docs References

No Domain Documentation source is configured. These implementation-specific contracts are supported by repository source.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain source could be checked. | — | — |

## Repo-Internal References

The cases below exercise the actual read cycle and rendered outcome boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The header's provenance paragraph: bodies from the public authorship and real review route; `familyPaging.captured.json` re-captured by MIK-L31 and recorded in the receipt; the walked family opened by its `family_id`.** | "re-captured by MIK-L31 with ICR-L44's"; "familyReview.capture-provenance.json"; "rather than relying on its position" | dashboard/src/panels/review/ReviewReadCycle.family.test.tsx:22-28 |
| The harness uses the captured HTTP bodies and existing read cycle, with its own fresh read cache. | `mountCycle`; `new ReviewReadCache()` | dashboard/src/panels/review/ReviewReadCycle.family.test.tsx:72-102 |
| Independent exact walks retain content and claims. | "retains exact content and claim identities while before and after walks advance independently" | dashboard/src/panels/review/ReviewReadCycle.family.test.tsx:104-143 |
| Failed admission retains the coherent display and failure details. | "retains the coherent display and fails a rejected continuation, including a structured page refusal" | dashboard/src/panels/review/ReviewReadCycle.family.test.tsx:145-213 |
| Unadvertised cursors are checked without weakening whole-review refusal. | "fails an unadvertised request cursor while preserving whole-review refusal semantics" | dashboard/src/panels/review/ReviewReadCycle.family.test.tsx:215-248 |
| The family-detail branch states loaded, complete and unavailable scope. | "states loaded claim scope in family details for a content-only page, completed walk and unavailable side" | dashboard/src/panels/review/ReviewReadCycle.family.test.tsx:352-410 |
| Refresh, changed questions and late responses cannot reuse old context. | "resets accumulated context on refresh, subject and history changes and drops late continuations" | dashboard/src/panels/review/ReviewReadCycle.family.test.tsx:412-465 |
| A late source expression becomes reachable beside preserved intent and workspace state; the walked family is opened by the capture's own `family_id`. | "keeps selected intent, evidence, siblings, focus and open layout while a late source expression becomes reachable" | dashboard/src/panels/review/ReviewReadCycle.family.test.tsx:467-568 |
| The production owner admits or rejects continuation before retaining data: the read cycle decides when (`familyContinuationRead`), and since L48 the merge it applies lives in `familyWalkMerge.ts`. | `familyContinuationRead`; `mergeFamilyContinuation` | dashboard/src/panels/review/ReviewReadCycle.ts:249-270; dashboard/src/panels/review/familyWalkMerge.ts:116-170 |

## Cross-Repo References

No external repository or live service is exercised by these mounted cases.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository reference is required. | — | — |

## Update History
- 2026-09-30T22:35:02+02:00 — 260928-MIK-L33 curator (staged change set on `ar/260928-mik-l33`, code base `c052b2593b85d9baf425cc1d5c46f384b13fc9ea`; review R1 changes-required, R2 and R3 pass-with-notes, each followed by a fix round, with the merge round after MIK-L34): No content impact: citation repair only; this document's own source is unchanged by MIK-L33. Rows citing MIK-L33's changed sources (`familyWalkMerge.ts`) moved with the leaf's inserted lines: 1 passing row(s) normalised by the fixer. No claim wording changed, and no verification stamp was advanced.
- 2026-09-30T10:52:00+02:00 — 260928-MIK-L31 curator (follow-up after the L31 worker's comment-only edits, staged; the change set is now 46 files over `48f680d5b95b8cb6eafff4f1ccd19c8f32e8c48c`): **resolved Todo:** the stale module header recorded at 10:05:09 was refreshed by the worker (comments only, lines 22-28, same length): it now names the MIK-L31 re-capture and the explicit `family_id` opening. Conventions and the provenance row are reworded to it (re-anchored on the new text, `24-24; 26-26` → `22-28`); the Todo is removed. No other row moved.
- 2026-09-30T10:05:09+02:00 — 260928-MIK-L31 curator (staged change set on `ar/260928-mik-l31`, code base `48f680d5b95b8cb6eafff4f1ccd19c8f32e8c48c`; review R3 pass-with-notes): body update. Conventions records that `familyPaging.captured.json` was re-captured from the current route by MIK-L31 (MIK-R31 rule 6) and that the late-source case now opens the walked family explicitly; the stale module header is recorded as a Todo. The provenance row and the late-source row are reworded (this pass's generated bullet for the provenance row removed).
- 2026-09-28T21:41:11+02:00 — 260921-ICR-L48 curator (uncommitted candidate tree `ac73216e2a763b72844a63b8c36c81f9a8b5f0e8` over code base `cb1b942af60a7ed5006ac992075d2bf96aeb9fa7`): **body update — the harness supplies the read cache the hook now requires.** `mountCycle` and the reset case each pass a fresh `ReviewReadCache` into `useReviewReadCycle`; no assertion changed. The claims about continuation admission, reset on refresh/subject/history and dropped late continuations still hold: a continuation is only admitted for the same question key, and the cache keeps whole-subject answers only, never a page. Conventions records the cache; the production-owner row now names `familyWalkMerge.ts`, where the roster merge moved unchanged; every case row was re-derived after the harness insertions. No stamp advanced.

- 2026-09-28T16:55:00+02:00 — 260921-ICR-L44 curator (uncommitted change set on `ar/260921-icr-l44`, code base `55c62237132eaa56b0df28ae5a8420a8dc05303d`): the module header now states that `familyPaging.captured.json` still holds its `a5bec6c3` capture, predates the structured locator fields and was not re-captured; recorded that and added the header row, and re-measured the ranges it shifted. No case changed. No verification stamp was advanced.

- 2026-09-27T01:04:07+00:00 — Created the card for exact sparse continuation, displayed failure retention and truthful family-detail scope over captured public HTTP bodies. Verification hash/date remain blank until the real closeout commit.

