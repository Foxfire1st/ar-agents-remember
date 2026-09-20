# dashboard/src/panels/detail-panel/changeSetBar.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/detail-panel/changeSetBar.tsx`        |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-09-20T13:43:00+02:00 |
| lastVerifiedCommitHash | `4a0442d62eb842661a3dd04686c376d0f0dbc61f`                  |
| lastVerifiedCommitDate | 2026-09-20T14:22:54+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l45-ar` uncommitted source; base `fb719f8936d337c4685f2758d4ba3731cd8b7fc5` |
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
| **The gate itself: `live && subject`, with the subject's own recorded kind and id carried into the target.** | "Intent review" | dashboard/src/panels/detail-panel/changeSetBar.tsx:135-157 |
| The client the hook calls, which takes the task context and nothing else. | `intentReviewEntries` | dashboard/src/data/review.ts:252-260 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

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
