# useReviewCatalogue.ts

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

## Evidence

### Docs References

No Domain Documentation source is configured. The implementation-specific account is grounded in the repository source below.

No configured domain source could be checked.

### Repo-Internal References

The named constructs own this behavior; reads and validation use their existing callers and models.

- Who owns the read (the reviewer, not the entry) and why the key is the comparison's identity. [1]
- The read state, now without the analytics `facts`/`stale` fields. [2]
- The comparison key: task context, record and generation. [3]
- The answer mapping. [4]
- The hook: keyed read, sequence guard, refresh. [5]
- Its caller, which bumps the generation on a new snapshot pair. [6]

### Cross-Repo References

No independent cross-repository interface is introduced by this source.

No additional cross-repository evidence is required.
