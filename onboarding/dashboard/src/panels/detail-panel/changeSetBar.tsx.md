# dashboard/src/panels/detail-panel/changeSetBar.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/detail-panel/changeSetBar.tsx`        |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-09-21T14:59:00+02:00 |
| lastVerifiedCommitHash | `8ff80ce08814856c9d6fec5b19093e6540fc6d7f`                  |
| lastVerifiedCommitDate | 2026-09-22T00:48:09+02:00|
| reviewedWorkingCandidate | candidate `ar/260921-icr-l2`, uncommitted; base `702714fc05363cb28eacaf101ba8384475a6aa56` |
| governingOverview      | `../overview.md`                                            |

## Governing Overview

[panels/ overview](../overview.md)

## Purpose

The change-set bar of the DetailPanel task-document reader, extracted from
`DetailPanel.tsx` by the 260731-EFA-L8 split. `ChangeSetButton` is the per-document
button, `DocChangeSetBar` the compact bar rendered above the reader content.

## Code Commentary

### Logic

The bar renders the change-set summary for the displayed document and exposes the
change-set viewer toggle; selection state stays in the panel's `useDetailPanelState`.


**The reviewer entry is now offered for every live leaf, and the server's subject is a refinement rather than a gate.** The condition changed from `live && subject` to `live`: the button carries `review: { selectorKind, selectorId }` when the entry read answers with a recorded subject, and `review: {}` when it answers with nothing or refuses — the task-context target, which opens the review on the task's complete source change inventory. `useReviewSubject`'s contract is unchanged (it still fetches nothing for a leaf that is not live and still treats a refusal or an empty list as a normal answer) but its *meaning* changed: an empty or refused answer no longer hides the reviewer, and the comment above the hook and the comment above the button both say so. The boundary the dashboard case asserts is the consequence: the entry is rendered as soon as the leaf is live, so a click that lands before the subject read answers opens the whole-task review and the subject refines the same button afterwards — deliberately, because the entry must not depend on a knowledge read that can refuse.

### Conventions

Small presentational components. The bar itself still performs no change-set fetch, but it now makes
**one** read of its own: the reviewer entry asks the server which subject this leaf can be reviewed
on. That read is a task-context `GET` (`data/review.ts`), not a change-set read, and it is the only
network call this module makes.

**260915-KS-L45 makes the reviewer entry reachable, and the subject now comes from the server
rather than from a prop no caller supplied.** The bar renders a third `ChangeSetButton` labelled
**Intent review** beside the two existing ones — never in their place — and it is offered when, and
only when:

1. the leaf's enclosure is **live**, decided by `leafIsLive(enclosures, activeWorktreeGroups, repo,
   leaf)`: one extracted predicate that both the working change-set action and the reviewer entry are
   gated on, so the two entries cannot come to disagree about what "live" means; and
2. `useReviewSubject` returned a `ReviewEntry` — the `selectorKind`/`selectorId` **props are gone**,
   and the hook asks `intentReviewEntries(repo, master, leaf)` for the leaf's reviewable subjects and
   keeps `result.entries?.[0]`.

The gate is not weakened by that: a refusal, an empty list, a rejected promise and a leaf that is not
live all leave the subject `undefined`, so **no subject means no button**, exactly as before. What
changed is where a subject could come from. The prop was the unreachable part: `taskReader.tsx` and the
master header pass `kind`/`repo`/`master`/`leaf`/`onOpen` and no selector, so `live && selectorId`
could never hold on any real navigation, and the screen was unreachable by design rather than by
policy. The hook's own comment records the invariant it keeps — the id returned is a recorded
identity inside the candidate the *server* resolved from canonical task context, so "this hook chooses
no candidate and invents no id: it asks, and a refusal or an empty list is a normal answer that leaves
the entry hidden" — and it fetches nothing at all for a leaf that is not live, because there is no
candidate to resolve and the working change-set is hidden for the same reason.

The button's target is `{ repo, master, leaf, review: { selectorKind: subject.selector_kind,
selectorId: subject.selector_id } }`: the reviewed subject's **recorded** identity comes from the
server's own resolution, never from the browser, because the browser does not choose the candidate.
The bar's own change-set fetching is unchanged — the reviewer entry's counter effect still reads only
the leaf or master request, so a review entry reports no counters.

### Invariants And Boundaries

The bar renders only the document currently displayed; it never fetches a change set
itself.

### Todos

None recorded.

## Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The change-set bar entry points. | `ChangeSetButton`; `DocChangeSetBar` | dashboard/src/panels/detail-panel/changeSetBar.tsx:21-46; dashboard/src/panels/detail-panel/changeSetBar.tsx:98-161 |
| **The one predicate both gated entries read, so the working change-set and the reviewer entry cannot disagree about what "live" means.** | `leafIsLive` | dashboard/src/panels/detail-panel/changeSetBar.tsx:164-179 |
| **The hook that makes the entry reachable: it asks the server for the leaf's reviewable subjects, keeps the first, and leaves the entry hidden on a refusal, an empty list or a rejected promise — fetching nothing at all for a leaf that is not live.** | `useReviewSubject` | dashboard/src/panels/detail-panel/changeSetBar.tsx:71-96 |
| **The gate itself: `live && subject`, with the subject's own recorded kind and id carried into the target.** | "Intent review" | dashboard/src/panels/detail-panel/changeSetBar.tsx:160-160 |
| The client the hook calls, which takes the task context and nothing else. | `intentReviewEntries` | dashboard/src/data/review.ts:312-320 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History
- 2026-09-21T19:16:12+00:00: Generated citation repair: "Intent review" repointed to dashboard/src/panels/detail-panel/changeSetBar.tsx:160-160. No content impact: mechanical anchor-range projection bound to citation source snapshot 4fbe69f2d182c46961e2554810a980cd29ac68e855e9213c9f6c1f2ac72173ec; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-21T14:59:00+02:00 — 260921-ICR-L2 curator (uncommitted change set on `ar/260921-icr-l2`, base `702714fc05363cb28eacaf101ba8384475a6aa56`): **the entry stopped depending on the subject.** The button is now gated on liveness alone; the server's recorded subject travels with the target as a refinement, and its absence (an empty list or an unreadable refusal) produces the task-context target `review: {}` instead of no button at all. That is the non-conforming example the packet names — "an empty subject list makes the source review disappear" — closed at the entry. The hook, its no-fetch-for-a-dead-leaf rule and its "a refusal is a normal answer" idiom are unchanged; what changed is what an empty answer *means*, and both comments now say it. One citation row was re-derived against this candidate. **Stamp accounting:** the verification rows still name the last real commit whose bytes this card was verified against, because nothing in this leaf is committed; claims whose evidence this leaf's change moved were re-read against the candidate and are stamp-class leftovers that only closeout can stamp.


- 2026-09-20T13:43:00+02:00 — 260915-KS-L45 curator (uncommitted change set on `ar/260915-ks-l45-ar`, base `fb719f89`): **the reviewer entry is reachable now, and this card's account of *why* it was not is the correction that matters.** The `selectorKind`/`selectorId` props are gone. A live leaf's subject is read from the server by the new `useReviewSubject` hook, which calls `intentReviewEntries(repo, master, leaf)` and keeps `result.entries?.[0]`; the gate is now `live && subject`, and the liveness half was extracted into `leafIsLive` so both gated entries read one predicate. The gate is not weakened: a refusal, an empty list, a rejected promise or a non-live leaf all leave `subject` undefined and **no subject means no button**. The card records why that matters — the prop was the unreachable part, because `taskReader.tsx` and the master header pass no selector, so `live && selectorId` could never hold on any real navigation — and records the invariant the hook's own comment states: the id is a recorded identity inside the candidate the server resolved, so the hook chooses no candidate and invents no id. The revision of the previous paragraph is retained in place below in substance: the entry is still added beside the working/committed actions and never in their place, its target still carries the subject's recorded identity rather than a filesystem path, and the reviewer entry still reports no counters. No verification stamp was advanced, because no commit contains this body.
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the
  change-set bar extracted from `DetailPanel.tsx`. Verification pinned to the leaf
  base until closeout stamps the code commit.
2026-09-18T18:10+02:00 — 260915-KS-L22 curator (uncommitted change set on `ar/260915-ks-l22`, base `2dcacb27`): **added the reviewer entry beside the change-set actions.** `DocChangeSetBar` gained
`selectorKind = "invariant"` / `selectorId` props and a third `ChangeSetButton` labelled *Intent
review*, rendered only when the enclosure is live and a `selectorId` is supplied — the same liveness
the working action is gated on, and never in the working or committed action's place. Its target
carries `review: { selectorKind, selectorId }`, the reviewed subject's recorded identity rather than
a filesystem path, because the browser does not choose the candidate. The new paragraph above states
that, and states the boundary the bar keeps: it still fetches nothing itself, and the new entry's
counter effect reads only the leaf or master request, so no counters are reported for a review. No
reference row was touched; ranges into this source belong to the citation-reprojection engine. The
metadata block above names this leaf's uncommitted candidate as what was read, and the two
verification stamps are left exactly as the last real verification set them. The body was changed
substantively and this entry is the history record, not a metadata-only refresh.
