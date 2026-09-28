# dashboard/src/panels/detail-panel/intentReviewEntry.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/detail-panel/intentReviewEntry.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-28T17:06:50+02:00 |
| lastVerifiedCommitHash | `e66f1f3894116e0bb37b49f178d8bfcb130a7e28` |
| lastVerifiedCommitDate | 2026-09-28T20:02:47+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The task entry's **one Intent review control**, `⇄ Intent review +N −N` (`⇄ Intent review (recorded)`
for a closed leaf) — the primary manifestation of `ICR-R24@v3` in leaf `260921-ICR-L47`. `+N` counts
invariant and joint-guarantee revisions only the comparison's after side holds as current (added, or the
new text of a revised one); `−N` counts those only the before side holds (retired, or the superseded
text). The numbers come from the comparison owner's summary read
([`data/reviewIntentSummary.ts`](../../data/reviewIntentSummary.ts.md)) — **never** from the change set's
line counts, which the entry showed when it reused the change-set button, and never from the size of the
subject catalogue.

## Code Commentary

### Logic

- `IntentReviewEntry({ repo, master, leaf, live, facts, onOpen })` calls
  `useIntentReviewSummary(repo, master, leaf, facts)` and renders a button (`data-testid="open-intent-review"`,
  `data-intent-state` = the read phase) whose click opens `{ repo, master, leaf, review: live ? {} : { historical: true } }`
  — always the task-context review, bound to the live candidate or to the leaf's recorded comparison
  (ICR-R12). The summary is a label on the control and never a gate on it.
- `IntentCounts` renders inside the button: `…` while loading; for `unavailable`, `briefProblem`'s word
  with `data-review-state` (the shared token) and `data-review-code`; for `counted`/`partial`,
  `+{added} −{removed}` (`data-added`/`data-removed`) plus `partial` when partial.
- `IntentDetails` renders beside the button: for `unavailable`, `problemSentence` in
  `EntryStateDetails`; for `partial`, how many subjects have no single current revision and that the
  reviewer shows each one; nothing for `counted`.

### Conventions

Uses `changeSetBtn`/`changeSetCounts` styles so it sits visually with the change-set controls, but it is not
a `ChangeSetButton` and performs no change-set read.

### Invariants And Boundaries

- **Unavailable is not zero.** No numbers are shown for an unread comparison.
- **The entry reads no subject catalogue, offers no subject picker and has no refresh control of its own.**
  Choosing a subject and re-reading the comparison belong to the reviewer.
- `facts` decides when the summary is re-read; it is built by the bar from this leaf's own lifecycle facts
  plus the re-validation generation.
- `realization_only`/`membership_only` are not displayed (worker observation O7). Presentation of those, and
  of acceptance-only revisions, belongs to the later presentation leaves (R35/L49).

### Todos

None.

## Docs References

No Domain Documentation source is configured for this module.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| What the numbers are, what the entry does not do, and why unavailable is not zero. | "WHAT THE NUMBERS ARE"; "UNAVAILABLE IS NOT ZERO" | dashboard/src/panels/detail-panel/intentReviewEntry.tsx:1-18 |
| The brief states and the counts inside the button. | `IntentCounts`; `briefProblem`; `data-added` | dashboard/src/panels/detail-panel/intentReviewEntry.tsx:24-61 |
| The disclosure beside the button for unavailable and partial answers. | `IntentDetails`; `problemSentence` | dashboard/src/panels/detail-panel/intentReviewEntry.tsx:63-80 |
| The control: its summary read, the task-context target and the recorded label. | `IntentReviewEntry`; `useIntentReviewSummary`; "Intent review (recorded)" | dashboard/src/panels/detail-panel/intentReviewEntry.tsx:82-120 |
| Where the bar mounts it. | `LeafEntries`; `IntentReviewEntry` | dashboard/src/panels/detail-panel/changeSetBar.tsx:272-306 |
| The cases that pin one control, the request economy and the brief states. | "is one control with the comparison's changed-intent counts and nothing beside it"; "states missing knowledge briefly, never as +0 −0, with the owner's refusal in the disclosure" | dashboard/src/panels/detail-panel/reviewEntryRefusal.test.tsx:127-150; dashboard/src/panels/detail-panel/reviewEntryRefusal.test.tsx:171-198 |

## Cross-Repo References

No cross-repository behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-28T17:06:50+02:00 — 260921-ICR-L47 curator (uncommitted candidate tree `72efa4bbc169b16afe8ef249499edf79cad9940d` over code base `58e22246cc09ef0ee12095e284a111a475081c38`): created this card for the compact Intent review control (`ICR-R24@v3`). The verification pair names the code base; closeout owns the real stamp.
