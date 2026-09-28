# useReviewCatalogue.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/useReviewCatalogue.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-28T17:09:38+02:00 |
| lastVerifiedCommitHash | `e66f1f3894116e0bb37b49f178d8bfcb130a7e28`|
| lastVerifiedCommitDate | 2026-09-28T20:02:47+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview.md](overview.md)

## Purpose

Own the **reviewer's** subject-catalogue read: every recorded subject of the comparison being reviewed.
Since `260921-ICR-L47` (`ICR-R24@v3`) it belongs to the reviewer only; the task entry shows the
changed-intent summary (`data/reviewIntentSummary.ts`) and reads no catalogue.

## Code Commentary

### Logic

`useReviewCatalogue(comparison)` takes a `ReviewCatalogueKey` — `repo`, `master`, `leaf`, optional
`history` and optional `generation` — and calls `intentReviewEntries` for the task context. Its key is the
**comparison's identity alone**: `comparisonKey` = `repo/master/leaf/<history ?? "live">`, and the read
key adds `generation ?? 0`. So the catalogue is read once when the reviewer opens, again when that identity
moves (the navigation bumps `generation` when a refresh reached a different compared snapshot pair,
ICR-R17) or when the reader calls `refresh`, and **never** because an unrelated part of the workspace was
republished (the former `facts`/`stale` inputs tied to the global analytics document are removed).
`catalogueAnswer` maps an answer to the read state: the complete recorded subjects with the supplied totals
(or totals counted from the page when a body predates them), known-empty, the owner's refusal, or an
unreadable answer; a thrown request becomes `reviewProblemFromCause`. A sequence number drops superseded
completions, and an answer is exposed only when its `comparisonKey` matches the current one, so a generation
re-read of the same comparison keeps the listed subjects on screen (marked loading) until it lands.

### Conventions

Uses the existing owner interfaces and exact recorded identities; keeps transient task evidence outside
durable onboarding.

### Invariants And Boundaries

A pending read for another comparison exposes no old rows. Catalogue membership and counts come from the
read owner; this hook selects no database and creates no family or invariant. It is not called by the task
entry.

### Todos

No additional work is asserted by this card.

## Docs References

No Domain Documentation source is configured. The implementation-specific account is grounded in the repository source below.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain source could be checked. | — | — |

## Repo-Internal References

The named constructs own this behavior; reads and validation use their existing callers and models.

| Finding | Anchor | Source |
| --- | --- | --- |
| Who owns the read (the reviewer, not the entry) and why the key is the comparison's identity. | "It belongs to the reviewer, not to the task entry" | dashboard/src/data/useReviewCatalogue.ts:1-12 |
| The read state, now without the analytics `facts`/`stale` fields. | `ReviewCatalogueRead`; `comparisonKey` | dashboard/src/data/useReviewCatalogue.ts:23-34 |
| The comparison key: task context, record and generation. | `ReviewCatalogueKey`; `generation` | dashboard/src/data/useReviewCatalogue.ts:38-44 |
| The answer mapping. | `catalogueAnswer` | dashboard/src/data/useReviewCatalogue.ts:46-77 |
| The hook: keyed read, sequence guard, refresh. | `useReviewCatalogue`; `comparisonKey`; `targetKey`; `refresh` | dashboard/src/data/useReviewCatalogue.ts:79-111 |
| Its caller, which bumps the generation on a new snapshot pair. | `useReviewCatalogue`; `observeComparison` | dashboard/src/panels/review/ReviewNavigation.tsx:149-199 |

## Cross-Repo References

No independent cross-repository interface is introduced by this source.

| Finding | Anchor | Source |
| --- | --- | --- |
| No additional cross-repository evidence is required. | — | — |

## Update History

- 2026-09-28T17:09:38+02:00 — 260921-ICR-L47 curator (uncommitted candidate tree `72efa4bbc169b16afe8ef249499edf79cad9940d` over code base `58e22246cc09ef0ee12095e284a111a475081c38`): **body update — the catalogue read became the reviewer's and is keyed on the comparison (`ICR-R24@v3`).** The hook now takes a `ReviewCatalogueKey` (task context, record, generation) instead of `(repo, master, leaf, facts)`; the analytics-derived `facts`/`stale` fields are removed and `targetKey` became `comparisonKey`; the task entry no longer calls it. Purpose, Logic and Invariants were rewritten, and the reference rows re-derived from the candidate. No stamp advanced; closeout owns the real stamp.

- 2026-09-26T19:49:05Z — Created the shared catalogue reader card and documented target-bound pending reads.
