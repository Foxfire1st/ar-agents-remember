# dashboard/src/panels/detail-panel/intentReviewEntry.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/detail-panel/intentReviewEntry.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T14:18:54+02:00 |
| lastVerifiedCommitHash | `59daf5055eb1ceffba89170be64ac85cabf860f4` |
| lastVerifiedCommitDate | 2026-09-30T15:02:26+02:00|
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

**Since MIK-L32 the entry also shows the unexplained-changes lane's count (MIK-R32 rule 9)** as its own element after
`+N −N`, from the same summary answer (`attribution`): `· K unexplained`, or `· K unexplained · U unknown` when some
changed file's attribution is unknown (K shown even when 0).

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
- **The lane's count (MIK-L32).** `AttributionCount` renders inside the button, after `IntentCounts`, as a separate
  `changeSetCounts` span (`data-testid="intent-review-attribution"`, `data-attribution-state`, `data-unexplained`,
  `data-unknown`). `attributionText` gives `· attribution partial` for a partially measured change set,
  `· attribution unknown` for an unmeasured one, `· K unexplained · U unknown` when U > 0, `· K unexplained` when only
  K > 0, and nothing for 0/0; nothing renders while loading or when the summary carries no `attribution` (a dataset
  comparison). `AttributionDetails` renders beside the button for a partial or unavailable attribution, in
  `EntryStateDetails` labelled "Attribution", naming the unmeasured paths or the reason. The count is shown whatever
  the intent counts' own state (ruling 2026-09-30T12:19:20 Q6).

### Conventions

Uses `changeSetBtn`/`changeSetCounts` styles so it sits visually with the change-set controls, but it is not
a `ChangeSetButton` and performs no change-set read.

### Invariants And Boundaries

- **Unavailable is not zero.** No numbers are shown for an unread comparison; an unmeasured or pending attribution
  never reads as zero either.
- **Unexplained is a separate fact.** The lane's count is its own element and is never added to `+N −N`.
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
| What the numbers are, what the entry does not do, why unavailable is not zero, and why the lane's count is a separate fact. | "WHAT THE NUMBERS ARE"; "UNAVAILABLE IS NOT ZERO"; "UNEXPLAINED IS A SEPARATE FACT" | dashboard/src/panels/detail-panel/intentReviewEntry.tsx:1-24 |
| The brief states and the counts inside the button. | `IntentCounts`; `briefProblem`; `data-added` | dashboard/src/panels/detail-panel/intentReviewEntry.tsx:31-68 |
| The disclosure beside the button for unavailable and partial answers. | `IntentDetails`; `problemSentence` | dashboard/src/panels/detail-panel/intentReviewEntry.tsx:112-129 |
| The lane's count inside the button and its disclosure beside it (MIK-L32). | `attributionText`; `AttributionCount`; `AttributionDetails` | dashboard/src/panels/detail-panel/intentReviewEntry.tsx:70-110 |
| The control: its summary read, the task-context target and the recorded label. | `IntentReviewEntry`; `useIntentReviewSummary`; "Intent review (recorded)" | dashboard/src/panels/detail-panel/intentReviewEntry.tsx:131-171 |
| The count's states on the real summary: two elements, one request, never a zero. | "shows the real leaf's unexplained and unknown files beside +N −N, from the one summary read"; "renders %s as its own state" | dashboard/src/panels/detail-panel/intentReviewEntry.attribution.test.tsx:55-136 |
| Where the bar mounts it. | `LeafEntries`; `IntentReviewEntry` | dashboard/src/panels/detail-panel/changeSetBar.tsx:272-306 |
| The cases that pin one control, the request economy and the brief states. | "is one control with the comparison's changed-intent counts and nothing beside it"; "states missing knowledge briefly, never as +0 −0, with the owner's refusal in the disclosure" | dashboard/src/panels/detail-panel/reviewEntryRefusal.test.tsx:127-150; dashboard/src/panels/detail-panel/reviewEntryRefusal.test.tsx:171-198 |

## Cross-Repo References

No cross-repository behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-30T14:18:54+02:00 — 260928-MIK-L32 curator (staged change set on `ar/260928-mik-l32`, code base `07d6584afba8a9504e4a3cf2e80eac41f68b28a9`; review R1 pass-with-notes, fixes, R2 pass): **body update for MIK-R32 rule 9.** Purpose, a Logic bullet and two Invariants bullets record `AttributionCount`, `attributionText` and `AttributionDetails` (the lane's count as a separate element after `+N −N`, its partial and unknown states, nothing for 0/0, pending or a dataset comparison; ruling 2026-09-30T12:19:20 Q6). The header row now names the new comment block (`1-18` → `1-24`); two rows added (the functions and the new attribution test). The other rows were re-pointed by the exact base-to-staged shift (`24-61` → `31-68`, `63-80` → `112-129`, `82-120` → `131-171`). No verification stamp was advanced.
- 2026-09-28T17:06:50+02:00 — 260921-ICR-L47 curator (uncommitted candidate tree `72efa4bbc169b16afe8ef249499edf79cad9940d` over code base `58e22246cc09ef0ee12095e284a111a475081c38`): created this card for the compact Intent review control (`ICR-R24@v3`). The verification pair names the code base; closeout owns the real stamp.
