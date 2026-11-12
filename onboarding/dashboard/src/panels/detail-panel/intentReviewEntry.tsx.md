# dashboard/src/panels/detail-panel/intentReviewEntry.tsx

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
`+N −N`, from the same summary answer (`attribution`): `· K without an invariant`, or `· K without an invariant · U unknown` when some
changed file's attribution is unknown (K shown even when 0).

## Code Commentary

### Logic

- `IntentReviewEntry({ repo, master, leaf, live, facts, onOpen })` calls
  `useIntentReviewSummary(repo, master, leaf, facts)` and renders a button (`data-testid="open-intent-review"`,
  `data-intent-state` = the read phase) whose click opens `{ repo, master, leaf, review: {} }` for a live and a
  closed leaf alike — the page's own default, which on a landed leaf is the comparison it delivered rather than
  its last numbered record (MIK-R195). The entry used to ask every closed leaf for `review: { historical: true }`,
  which named the recorded comparison and left no delivered link able to escape it. The summary is a label on the
  control and never a gate on it.
- `IntentCounts` renders inside the button: `…` while loading; for `unavailable`, `briefProblem`'s word
  with `data-review-state` (the shared token) and `data-review-code`; for `counted`/`partial`,
  `+{added} −{removed}` (`data-added`/`data-removed`) plus `partial` when partial.
- `IntentDetails` renders beside the button: for `unavailable`, `problemSentence` in
  `EntryStateDetails`; for `partial`, how many subjects have no single current revision and that the
  reviewer shows each one; nothing for `counted`.
- **The lane's count (MIK-L32).** `AttributionCount` renders inside the button, after `IntentCounts`, as a separate
  `changeSetCounts` span (`data-testid="intent-review-attribution"`, `data-attribution-state`, `data-unexplained`,
  `data-unknown`). `attributionText` gives `· attribution partial` for a partially measured change set,
  `· attribution unknown` for an unmeasured one, `· K without an invariant · U unknown` when U > 0, `· K without an invariant` when only
  K > 0, and nothing for 0/0; nothing renders while loading or when the summary carries no `attribution` (a dataset
  comparison). `AttributionDetails` renders beside the button for a partial or unavailable attribution, in
  `EntryStateDetails` labelled "Attribution", naming the unmeasured paths or the reason. The count is shown whatever
  the intent counts' own state (ruling 2026-09-30T12:19:20 Q6).

- `OpenWorkCount` renders after `AttributionCount` inside the button. While loading, or when
  `read.unexplainedOpen` is undefined, it renders nothing. Otherwise a separate
  `data-testid="intent-review-open"` span says `· K open` for a truthy count or `· all answered` for zero.
  The summary owner passes the optional unexplained_open value through as unexplainedOpen for counted, partial or refused answers. It remains a separate supplied open-work fact, not a revision count or independent acceptance verdict.

### Conventions

Uses `changeSetBtn`/`changeSetCounts` styles so it sits visually with the change-set controls, but it is not
a `ChangeSetButton` and performs no change-set read.

### Invariants And Boundaries

- **Unavailable is not zero.** `IntentCounts` shows no revision counts for an unavailable comparison;
  an unmeasured or pending attribution never reads as zero. `OpenWorkCount` independently renders any
  defined nonloading `unexplainedOpen` value; this renderer does not gate it on the intent-count phase.
- **Unexplained is a separate fact.** The lane's count is its own element and is never added to `+N −N`.
- **The entry reads no subject catalogue, offers no subject picker and has no refresh control of its own.**
  Choosing a subject and re-reading the comparison belong to the reviewer.
- `facts` decides when the summary is re-read; it is built by the bar from this leaf's own lifecycle facts
  plus the re-validation generation.
- `realization_only`/`membership_only` are not displayed (worker observation O7). Presentation of those, and
  of acceptance-only revisions, belongs to the later presentation leaves (R35/L49).

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured for this module.

No relevant domain documentation was found.

### Repo-Internal References

### Cross-Repo References

No cross-repository behavior.

No meaningful cross-repo references found.

- Revision counts come from the comparison summary, not line totals/catalogue size; targeting is task-context, unavailable is not measured zero, and attribution stays separate. [1]
- IntentCounts displays loading/refusal or supplied revision counts, with a partial marker where appropriate. [2]
- IntentDetails places the actual refusal or unresolved-subject explanation beside the control rather than fabricating revision counts. [3]
- Attribution uses 'without an invariant' plus a separate unknown count, preserves partial/unavailable/zero-zero suppression, and retains its own detail block. [4]
- IntentReviewEntry retains one task-context summary control, which supplies `review: {}` for a live and a closed leaf alike — liveness reaches only the `(recorded)` label — and keeps no history request of its own; it now also mounts the independent open-work span. [5]
- Stored assertion bodies keep revision and attribution elements separate, use the current without-an-invariant wording, exercise partial/unknown/zero cases and assert one summary request; these are source assertions, not a new run. [6]
- LeafEntries mounts the control; DocChangeSetBar derives its facts from leaf lifecycle facts plus the shared revalidation generation. [7]
- Stored refusal/compact-entry cases retain one control, task-context open and no false revision counts while preserving the actual refusal explanation; these are not fresh execution. [8]
- OpenWorkCount suppresses loading/undefined values, renders a separate open/all-answered span otherwise and follows supplied optional unexplainedOpen even on a refused intent answer; it is not a MEMORY acceptance grade. [9]

- A closed leaf's entry opens the page's own default, so a landed leaf reaches the comparison it delivered rather than its last recorded number; the summary read, the count label and the one-control shape are unchanged. [10]
- The leaf-wide view names the leaf's highest recorded number and the delivered notice beside the comparison it resolved. 

- Retired at the fifth freeze d59c3493: mcp/src/agents_remember/application/review_tree_knowledge.py::_view - the bytes it recorded now occur 16 times in the file, so no single home can be named and it is not given to the likelier one. Retired means the anchor no longer stands, not that the cited subject was deleted.
