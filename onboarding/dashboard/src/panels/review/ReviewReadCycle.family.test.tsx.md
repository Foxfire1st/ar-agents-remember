# dashboard/src/panels/review/ReviewReadCycle.family.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/ReviewReadCycle.family.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-28T21:41:11+02:00 |
| lastVerifiedCommitHash | `ae2fd5c864aa2609ae45b5c7dbbaa693569aefc6`|
| lastVerifiedCommitDate | 2026-09-28T22:11:57+02:00|
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

Only fetch and the separately tested catalogue hook are isolated. Since L48 `useReviewReadCycle` requires the surface's `ReviewReadCache`, so the hook harnesses (`mountCycle` and the reset case) each construct a fresh cache; a fresh cache per mount means no case is answered from another case's reads. Successful review bodies come from the capture; deliberate corruptions are negative probes. The capture is `familyPaging.captured.json`, which still holds its capture at `a5bec6c3`: its member sources predate the structured `locator`, `resolved_ranges` and `locator_state` fields, and the current route's walk bodies differ from it in selection and roster, so it was not re-captured; the module header says so and points at the `not_recaptured` section of `familyReview.capture-provenance.json`. Re-capturing it belongs with the change that moves these cases to the current route's walk. Source-content requests receive their own explicit test refusal when a case measures selection rather than served bytes. This is mounted component evidence, not installed-browser or whole-product acceptance.

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
| **The capture's provenance: bodies from the public authorship and real review route, with `familyPaging.captured.json` still at its `a5bec6c3` capture and not re-captured.** | "a5bec6c3"; "familyReview.capture-provenance.json" | dashboard/src/panels/review/ReviewReadCycle.family.test.tsx:13-19 |
| The harness uses the captured HTTP bodies and existing read cycle, with its own fresh read cache. | `mountCycle`; `new ReviewReadCache()` | dashboard/src/panels/review/ReviewReadCycle.family.test.tsx:64-94 |
| Independent exact walks retain content and claims. | "retains exact content and claim identities while before and after walks advance independently" | dashboard/src/panels/review/ReviewReadCycle.family.test.tsx:96-135 |
| Failed admission retains the coherent display and failure details. | "retains the coherent display and fails a rejected continuation, including a structured page refusal" | dashboard/src/panels/review/ReviewReadCycle.family.test.tsx:137-205 |
| Unadvertised cursors are checked without weakening whole-review refusal. | "fails an unadvertised request cursor while preserving whole-review refusal semantics" | dashboard/src/panels/review/ReviewReadCycle.family.test.tsx:207-240 |
| The family-detail branch states loaded, complete and unavailable scope. | "states loaded claim scope in family details for a content-only page, completed walk and unavailable side" | dashboard/src/panels/review/ReviewReadCycle.family.test.tsx:344-402 |
| Refresh, changed questions and late responses cannot reuse old context. | "resets accumulated context on refresh, subject and history changes and drops late continuations" | dashboard/src/panels/review/ReviewReadCycle.family.test.tsx:404-457 |
| A late source expression becomes reachable beside preserved intent and workspace state. | "keeps selected intent, evidence, siblings, focus and open layout while a late source expression becomes reachable" | dashboard/src/panels/review/ReviewReadCycle.family.test.tsx:459-543 |
| The production owner admits or rejects continuation before retaining data: the read cycle decides when (`familyContinuationRead`), and since L48 the merge it applies lives in `familyWalkMerge.ts`. | `familyContinuationRead`; `mergeFamilyContinuation` | dashboard/src/panels/review/ReviewReadCycle.ts:249-270; dashboard/src/panels/review/familyWalkMerge.ts:104-157 |

## Cross-Repo References

No external repository or live service is exercised by these mounted cases.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository reference is required. | — | — |

## Update History
- 2026-09-28T21:41:11+02:00 — 260921-ICR-L48 curator (uncommitted candidate tree `ac73216e2a763b72844a63b8c36c81f9a8b5f0e8` over code base `cb1b942af60a7ed5006ac992075d2bf96aeb9fa7`): **body update — the harness supplies the read cache the hook now requires.** `mountCycle` and the reset case each pass a fresh `ReviewReadCache` into `useReviewReadCycle`; no assertion changed. The claims about continuation admission, reset on refresh/subject/history and dropped late continuations still hold: a continuation is only admitted for the same question key, and the cache keeps whole-subject answers only, never a page. Conventions records the cache; the production-owner row now names `familyWalkMerge.ts`, where the roster merge moved unchanged; every case row was re-derived after the harness insertions. No stamp advanced.

- 2026-09-28T16:55:00+02:00 — 260921-ICR-L44 curator (uncommitted change set on `ar/260921-icr-l44`, code base `55c62237132eaa56b0df28ae5a8420a8dc05303d`): the module header now states that `familyPaging.captured.json` still holds its `a5bec6c3` capture, predates the structured locator fields and was not re-captured; recorded that and added the header row, and re-measured the ranges it shifted. No case changed. No verification stamp was advanced.

- 2026-09-27T01:04:07+00:00 — Created the card for exact sparse continuation, displayed failure retention and truthful family-detail scope over captured public HTTP bodies. Verification hash/date remain blank until the real closeout commit.

