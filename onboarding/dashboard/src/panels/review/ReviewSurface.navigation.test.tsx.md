# ReviewSurface.navigation.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/ReviewSurface.navigation.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-28T21:40:44+02:00 |
| lastVerifiedCommitHash | `ae2fd5c864aa2609ae45b5c7dbbaa693569aefc6`|
| lastVerifiedCommitDate | 2026-09-28T22:11:57+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[overview.md](../overview.md)

## Purpose

Ordinary-entry navigation through the real shared catalogue and comparison clients, and — since
`260921-ICR-L48` (`ICR-R24@v3`) — the acceptance module for what happens **between** a selection and its
answer: the mounted reviewer, the subject-bound pending and problem states, per-comparison reuse, the
latest selection winning, focus the reader moved, and a late catalogue.

## Code Commentary

### Logic

The fetched catalogue opens a recorded family, allows selection of another family in the same workspace and retains full source population, display preferences and focus. An unreadable knowledge response stays source-only without fabricated families or an impossible selection prompt.

**The delayed-reply cases (L48).** The first two cases answer immediately and prove eventual content. The
cases after them run against `delayedServer`, which answers the catalogue and source content at once (or
holds the catalogue on request) but **holds every review reply** until the case releases it — answered,
refused by the owner (`outcome.body`), or lost in transport (`outcome.lost`). Holding the reply is what
lets a case observe the interval the leaf is about:

- **mounted across family → invariant → family**: the workspace, navigation, family tree and open
  disclosures are the same DOM nodes throughout; only the reading area shows `review-reading-pending`,
  labelled with the requested subject; nothing of the previous subject (reading, comparison identity,
  records) appears under the new one; returning to an already read subject issues no review and no
  content request;
- **latest of rapid selections**: A → B → C settles on C; a superseded answer is neither shown nor kept, so
  choosing B again asks again;
- **late catalogue, reader working / reader idle**: after the bounded wait, an engaged reader is not moved;
  an idle reader lands on the first family without a remount;
- **failed / refused selection** (`it.each`, L48-R1-F1): the shell stays mounted with its complete source
  explorer, and exactly one owner block is shown in the reading area, labelled with the requested subject;
  retry re-asks that subject (failed) and another subject can be chosen directly (refused);
- **moved focus** (L48-R1-F2): focus the reader moved while the subject was pending is kept when the
  answer lands, and unmoved focus still lands on the selected node.

The first existing case waits (`waitFor`) for its focus assertion, because the selection focus is applied
in a passive effect after an answer that arrives outside `act`.

### Conventions

Use the existing owner interfaces and exact recorded identities; keep transient task evidence outside durable onboarding. Only `fetch` is stubbed: the cases mount the real `ReviewSurface`, navigation, read cycle and cache, with semantic content from the captured L41 records. Request counts (`reviewReads`, `contentReads`, `catalogueReads`) are the module's measure of reuse.

### Invariants And Boundaries

Tests are scoped executable evidence. They do not certify the mounted product journey, whole-repository quality or semantic acceptance. jsdom has no layout engine: the rail's `scrollTop` retention these cases assert holds while a subject is pending; after an answer lands, a real browser scrolls the focused selected node into view (review R1 observation O-R1-2), so post-answer scroll retention is not claimed here.

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
| The module's own statement of what it pins and why its replies are held. | "The first two cases answer immediately"; `ReviewSurface` | dashboard/src/panels/review/ReviewSurface.navigation.test.tsx:1-23 |
| The held-reply server: every review reply can be answered, refused or lost; catalogue and content reads are counted. | `delayedServer`; `heldFor`; `answer` | dashboard/src/panels/review/ReviewSurface.navigation.test.tsx:256-306 |
| Mounted shell, subject-labelled pending area and zero-request return. | "keeps the reviewer mounted across family → invariant → family, pending only in the reading area, and reuses what it read" | dashboard/src/panels/review/ReviewSurface.navigation.test.tsx:316-410 |
| Latest selection wins; a superseded answer is not kept. | "settles on the latest of rapid selections and never shows a superseded answer" | dashboard/src/panels/review/ReviewSurface.navigation.test.tsx:412-458 |
| Late catalogue with and without reader engagement. | "does not move a reader who is working when the catalogue answers after the bounded wait"; "lands a reader who has not acted on the first family when the catalogue answers late, without remounting" | dashboard/src/panels/review/ReviewSurface.navigation.test.tsx:460-511 |
| Failed or refused selection stated in the reading area for the requested subject. | "keeps the workspace and navigation when a newly selected subject is %s, stating it for that subject" | dashboard/src/panels/review/ReviewSurface.navigation.test.tsx:523-601 |
| Focus the reader moved while pending is kept. | "leaves focus where the reader moved it while the selected subject was pending" | dashboard/src/panels/review/ReviewSurface.navigation.test.tsx:603-631 |

## Cross-Repo References

No independent cross-repository interface is introduced by this source.

| Finding | Anchor | Source |
| --- | --- | --- |
| No additional cross-repository evidence is required. | — | — |

## Update History
- 2026-09-28T21:40:44+02:00 — 260921-ICR-L48 curator (uncommitted candidate tree `ac73216e2a763b72844a63b8c36c81f9a8b5f0e8` over code base `cb1b942af60a7ed5006ac992075d2bf96aeb9fa7`): **body update — this module became the acceptance evidence for the mounted reviewer (`ICR-R24@v3`).** L48 added four delayed-reply cases (mounted across selection with zero-request return, latest selection wins, late catalogue with and without engagement) and A2 added three more (failed/refused selection via `it.each`, moved focus kept), all against a `delayedServer` that holds review replies open; the first existing case now waits for its passive-effect focus. Purpose, Logic, Conventions and Invariants were extended, and the single row (which cited import lines under a behaviour claim) was replaced by one row per case extent. The worker and reviewer recorded that the new cases fail on the base and A1 sources respectively. Invariants record review observation O-R1-2 as a scope limit of the scroll assertion, not a defect. No stamp advanced.

- 2026-09-26T19:49:05Z — Created the regression card for this source owner.
