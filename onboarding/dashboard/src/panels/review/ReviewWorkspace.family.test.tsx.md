# dashboard/src/panels/review/ReviewWorkspace.family.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/ReviewWorkspace.family.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-24T00:43:00+02:00 |
| lastVerifiedCommitHash | `63b476297708f779de8ed5c0bf3555b9d1de70c2` |
| lastVerifiedCommitDate | 2026-09-24T04:10:11+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The mounted-surface case module for the family-centered review workspace (`ICR-R24@v3`): the family tree,
the unified central reading path, the complete source explorer, and the one family-roster walk control.

**Real component, real client, only `fetch` stubbed.** `ReviewSurface` is the real component and
`intentReview` the real client, so every request below is built by the shipped client and every response
travels the way the browser's does — status, body, the shared decode in `data/reviewTransport.ts`, the
component tree, the read cycle in `ReviewReadCycle.ts`. Only `fetch` is stubbed, and the bodies it is
stubbed with are the real route's own: the `familyReview.*.captured.json` files hold the bytes
`serving/review.py` published over the real application owners and the real store for one real enclosure,
recorded by `temp/icr/probe-l24-family-body.py`. No assertion reads a prop this test itself passed, and no
payload is assembled here: a case that reached into the component with a hand-built value would prove
nothing about the wire contract, which is what these cases are about.

**What the cases caught.** The surface as it stood was a stack of diagnostic paragraphs over three panes: a
family's recorded guarantee, its roster of member revisions (unchanged siblings included) and the
intent-to-expression reading path were not rendered at all, so a reviewer could not see the family a
selected invariant belongs to or the guarantee its member statement is about. The module also pins the two
ways a repair could lie: rendering a family context the body does not carry as a measured "no family
recorded", and offering a control that fetches the server's own refusal (a cursor-less request for the
`family_members` collection, which is a **set** of per-family walks rather than one walk with a first page).

**Not browser evidence, and it says so.** The module's header states that the Playwright configs in this
repository are Dagger-only — `dashboard/scripts/require-dagger-test-environment.mjs` refuses host execution
— so the mounted-tree evidence here is evidence of the real client and the real component tree over real
server bytes, **not** of a live page fed by a running publication. The packet's mounted-browser structural
and visual review, and R25's assembled acceptance, are separate obligations. The **static captured body** is
what the surface is mounted over in every case below; the live walk's own proof lives in enclosure
`260921-icr-l31b-ar` at commit `5f14fc67`, not in this module.

**Verification stamp.** `lastVerifiedCommitHash` names the leaf's base commit
`5f14fc6790cafc3ad2ae612c2e67f176392dc1fe`; this module exists only in the leaf's **uncommitted working
tree**, so the stamp means "leaf base commit plus this leaf's working-tree delta" and does not claim that
the commit holds this content. Governed closeout owns the real stamp.

## Code Commentary

### Logic

**The module carries nineteen cases** (`grep -c '^  it('` on this candidate), all inside one
`describe("ReviewSurface family-centered workspace (ICR-R24@v3)")`. They fall into three groups: the
original layout cases (the tree, the centre, the explorer, the roster walk, the no-family-context body, the
expansion preference, keyboard traversal and the filter), the fix-round cases that pin a sentence's
direction or a distinction a repair could collapse, and the two page-request case that pins the reader's
workspace state across the pane switch.

**The harness is four pieces and no more.** `serving(queue)` stubs one `vi.stubGlobal("fetch", …)` for the
whole surface: it records every URL it was asked for and answers `/source-content` requests with
`SOURCE_REFUSAL` (a real typed refusal body, because the explorer's cases assert expansion state rather
than a file's bytes) and every other request with the next queued captured body. `mount(history?, familyId?)`
renders the real `ReviewSurface` with `REPO`/`MASTER`/`LEAF` and either an `invariant` selector or a
`family` selector, so a case about a family subject mounts a family. `captured(name)` resolves each body
from this file's own directory rather than the process cwd. `firstFamilyId(body)` narrows a captured body
at runtime — the bodies are `unknown` on purpose because they carry fields this client's mirror does not
declare — and throws loudly rather than mounting the surface under a wrong subject. `afterEach` runs
`cleanup()` and `vi.unstubAllGlobals()`.

**The bodies are read, never typed.** `COMPLETE`, `TRUNCATED`, `CONTINUED`, `IDENTICAL`, `ONE_SIDED`,
`EMPTY_ROSTER` and `WALK_FINAL` are read from the capture directory, so a changed capture fails this
module's own reading instead of silently re-pointing an assertion, and several cases additionally read
which row they are about out of the DOM before asking the centre, for the same reason.

**The nineteen cases and what each one pins:**

1. *renders the recorded families, their authored guarantees and the full member statements* — the context's
   own `partial` state is not upgraded, each family's guarantee is printed as the revision's own authored
   text, and the member rows name both-snapshot, before-only and after-only membership rather than dropping
   any; every member row carries an opener, a statement recorded under two families appears beneath each,
   and the recorded sharing is stated.
2. *opens a family review whose guarantee comparison is the shape the two recorded revisions support* — one
   family selected the **same** revision on both snapshots (the only shape allowed to say the guarantee is
   unchanged) and the other two different revisions, drawn as a real before/after diff; the case reads which
   is which from the rendered blocks rather than from a capture's row order.
3. *keeps the family context when a member is selected and states the five facts separately* — a member's
   review retains the guarantee it is about, and statement, membership/realization, source attribution and
   authored judgment are four further facts, each read from its own `data-fact` row.
4. *keeps the complete source explorer independent of the family selection* — the explorer's own population
   sentence, the "it never removes one from this list" statement and the `measured` inventory state are
   unchanged by selecting a family.
5. *walks a family roster only from the cursor that family's own page published* — `family_members` is in
   `REVIEW_PAGED_COLLECTIONS` and deliberately **not** in `REVIEW_WALKABLE_COLLECTIONS`, so the collection
   picker offers no option that would fetch a refusal; the truncated roster states both of the owner's own
   measures; the click sends the published `pageOf=family_members` continuation unchanged, and the continued
   response renders the walk's own scope.
6. *renders a body that carries no family context as that fact, never as a measured zero* — a captured body
   recorded before the family field existed mounts as `absent`, says "this body carries no family context"
   and "not a measured zero", renders no family list, and leaves the scope header and the explorer stating
   their own facts.
7. *keeps an expanded entry expanded across a diff-layout switch* — an opened inventory row reports
   `aria-expanded="true"`, the display-state line names the expanded path, and switching the diff layout to
   `inline` (published on the workspace root) leaves both unchanged; the full-file preference is then shown
   to be one value shared by the explorer's bar and the centre column.
8. *marks the current selection and traverses the tree by keyboard* — the selected family node carries
   `aria-current="true"`, and `ArrowDown`/`ArrowUp` move focus inside the one roving-focus group.
9. *reports the filter scope without restating the comparison's totals* — the filter scope line reports the
   composed family contexts, a filter is stated as a filter on this display only, a matched family keeps its
   members, and a filter matching nothing says the composed contexts are unchanged by it.
10. *(fix round 1)* *says a bounded roster carried none of the measured rows, never that the read measured
    zero* — every bounded roster prints the **page-scoped** sentence ("this page carried no member row",
    "0 of the 2 recorded membership row(s) it measured") and the continuation sentence, and never the word
    "measured zero"; the owner's own two measures are printed above it so the two clauses cannot disagree.
11. *(fix round 1)* *still says the measured zero when the read really measured zero memberships* — the other
    direction of the same sentence, and the only place "the read measured zero memberships" may be said.
12. *(fix round 1)* *heads a bounded member context partial and counts the owner's rows, not this page's* —
    the centre's heading is "Recorded member context (partial)", the counts state the read's own
    `4 … across 2 recorded side(s) (before 2 + after 2)` and "this page carried 0 member row(s) of them"
    plus the continuation sentence, the distinct-member line is scoped to the rows this page carried, the
    per-side lines are the tree's own components mounted in the centre, and the centre's continuation control
    is **clicked** and the request it issues asserted, because a control mounted without its handler renders
    identically and fetches nothing (fix round 2, V6).
13. *(fix round 1)* *distinguishes two distinct revisions with identical text from one unchanged revision* —
    two distinct revisions carrying the same authored text render as `different family revisions` with "A
    revision was authored between them; the text is what did not move." and never as unchanged; only the
    same-revision family may say the guarantee is unchanged.
14. *(fix round 1)* *states a member whose content the page did not carry as that, not as a one-sided
    statement* — the `not_on_page` shape is rendered as itself, with no one-sided, unchanged or changed
    wrapper beside it.
15. *(fix round 1)* *says a listed-but-uncarried row about the page, never that the snapshot records no row*
    — for a row recorded on both snapshots whose content one side did not carry, the note is about the page,
    names the side whose content is on this page, and never says the snapshot records no member row; the
    centre's continuation control then reaches the rest of that bounded walk.
16. *(fix round 1)* *says a bounded page's missing row about the page, never that the snapshot records none*
    — the one-side-only shape with the other side's roster a position in a bounded walk renders the bounded
    sentence and never "records no member row".
17. *(fix round 1)* *prints one empty-roster sentence in both columns, not two that happen to agree* — the
    centre's line is asserted **equal to** the tree's own string for the same family, which is what makes it
    one implementation mounted twice rather than two sentences that happen to read alike.
18. *(fix round 3)* *states the page that completes a multi-page walk as the walk's last page, not as the
    whole roster* — the final page of a four-page walk says it "completes the walk" and that the pages before
    it carried the rows this one did not, never "the page is the whole selection"; the rosters the read took
    whole still say so and never claim to be a step in a walk, and the surface read the route's own sentence
    for that side rather than inventing one. Before the walk's completion guard was corrected this request
    was answered with HTTP 500.
19. *(fix round 5, V10)* *keeps the reader's workspace state across two page requests through the centre's
    own control* — the reader sets a selected family, a filter, an inline diff layout and "changed regions
    only", and a five-value snapshot (`selectionKind`, `centreControls`, `filter`, `layout`, `fullFile`) is
    asserted identical **after each of two page requests**, both issued by the centre's own continuation
    control; the last assertion is that exactly three request URLs were seen.

### Conventions

Imports are grouped the way the rest of the dashboard's test modules group them: Node builtins
(`node:fs`, `node:path`), then `@testing-library/react` plus `vitest`. The module imports the two collection
constants from `../../data/review`, the captured refusal body from `./recordsPageRefusal.captured`, and the
real `ReviewSurface` from `./ReviewSurface` — it never imports a mock. Test ids are the assertions' only
handle on the DOM (`review-family-tree`, `review-family`, `review-family-guarantee`, `review-family-member`,
`review-family-member-open`, `review-family-member-shared`, `review-family-member-state`, `review-family-open`,
`review-family-list`, `review-family-filter`, `review-family-filter-scope`, `review-family-none-shown`,
`review-family-roster`, `review-family-roster-next`, `review-family-empty-roster`, `review-center`,
`review-center-family`, `review-center-guarantee-unchanged`, `review-center-guarantee-changed`,
`review-center-guarantee-identical-text`, `review-center-member`, `review-center-member-family`,
`review-center-member-heading`, `review-center-member-counts`, `review-center-member-distinct`,
`review-center-member-not-on-page`, `review-center-member-one-sided`, `review-center-member-one-sided-note`,
`review-center-roster`, `review-center-roster-next`, `review-center-facts`, `review-center-evidence`,
`review-center-family-empty`, `review-center-full-file`, `review-source-explorer`, `review-inventory`,
`review-population-scope`, `review-inventory-open`, `review-display-state`, `review-diff-layout`,
`review-full-file`, `review-workspace`, `review-roster-walk`, `review-page-collection`,
`review-page-option`, `review-page-bounds`, `review-scope-families`), and the cases read server-published
values off data attributes (`dataset.familyState`, `dataset.contextState`, `dataset.inventoryState`,
`dataset.rosterComplete`, `dataset.continuation`, `dataset.sides`, `dataset.diffLayout`, `dataset.fullFile`,
`dataset.selectionKind`, `dataset.family`). `STATE`-style literals are never invented: every expected
sentence is either the capture's own or the owner's own string, and where a sentence is shared the case
asserts identity rather than similarity. Every case awaits the element it needs rather than a timeout, and
the two loops that search the DOM for a shape throw with the sentences they did see when they find none.

### Invariants And Boundaries

- **Real surface, real client, one stubbed global.** Only `fetch` is stubbed; the request is built by the
  shipped client, the response is decoded by the shipped transport, and the tree is the shipped component
  tree. No case passes a prop and then asserts on it.
- **The bodies are the real route's own captured bytes.** No payload is assembled in this module; the one
  hand-written body is a typed refusal for the source-content read, which no case asserts content about.
- **A case that must know which row it is about reads that out of the DOM**, not out of a capture's row
  order, so a re-captured body cannot silently re-point it.
- **These are not browser evidence.** The Playwright configs here are Dagger-only, so this module proves the
  real client and component tree over real server bytes — not a live page fed by a running publication. The
  live walk's proof is in enclosure `260921-icr-l31b-ar` at commit `5f14fc67`; the mounted-browser review and
  R25's assembled acceptance are separate obligations, and this card does not claim them.
- **A page is never presented as the whole.** The bounded-roster, bounded-member-context, listed-but-uncarried
  and bounded-missing-row cases all exist because a page-scoped fact was printed as a store-scoped one, and
  each asserts both what is said and what must not be said ("measured zero", "records no member row",
  "one-sided recorded statement", "the page is the whole selection").
- **A control is only proven by the request it issues.** The centre's continuation control is clicked and its
  `pageOf=family_members` request, carrying the published cursor unchanged, is asserted — a mounted control
  without its handler renders identically and fetches nothing.
- **One sentence, two columns.** The shared-sentence case asserts equality with the tree's own string rather
  than resemblance, because a second sentence that merely happens to read the same would drift.
- **The reader's state is not a page's to reset.** The two-page-request case asserts all five workspace
  values (selection kind, the centre's continuation controls, the filter, the diff layout, the full-file
  disclosure) survive both requests, which is the observable half of `useWorkspaceState` being owned above
  the pane switch.
- **Boundary.** This module owns no production behaviour: the sentences it pins belong to `FamilyTree.tsx`
  (`emptyRosterSentence`, `completionNote`, the roster lines and the walk control), `FamilyReviewCenter.tsx`
  (the centre's heading, counts and per-shape blocks) and `SourceExplorer.tsx` (the population sentence); the
  page-collection union belongs to `data/review.ts` and the page request type to `ReviewReadCycle.ts`.

### Todos

None recorded. The obligations this module deliberately leaves open are named in its own header and kept
there: the mounted-browser structural and visual review, and R25's assembled acceptance, belong to other
owners — the live walk's proof lives in enclosure `260921-icr-l31b-ar` at commit `5f14fc67`, not here.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no entries).
The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the module's own statement of what it
exercises and of what it does not claim, the four pieces of its harness, the captured bodies it reads, and
each of the nineteen cases by its own name. Every anchor in a row below occurs on a line inside the range
that row cites; the anchor of a case row is that case's own `it(...)` name, which occurs on the line that
opens the case.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The module's own statement that this is `ICR-R24@v3` at the mounted surface: the family tree, the unified central reading path, the complete source explorer and the one family-roster walk control.** | "ICR-R24@v3 at the mounted surface" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:1-2 |
| **Real component and real client, with only `fetch` stubbed, and the captured bodies' provenance.** | `intentReview`; "is stubbed"; "familyReview.*.captured.json"; "probe-l24-family-body.py" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:4-12 |
| What these cases catch, including the two ways a repair could lie. | "WHAT THESE CASES CATCH"; "the two ways a repair could lie" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:14-21 |
| **What they do not claim: not browser evidence, Dagger-only Playwright configs, and a live publication explicitly out of scope.** | "WHAT THEY DO NOT CLAIM"; "These are not browser evidence"; "require-dagger-test-environment.mjs"; "not of a live page fed by a running publication" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:23-27 |
| The two collection constants the walk case pins, and the captured refusal body the no-family-context case mounts. | `REVIEW_PAGED_COLLECTIONS`; `REVIEW_WALKABLE_COLLECTIONS`; `RECORDS_PAGE_REFUSAL_RESPONSE` | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:35-37 |
| The three task identifiers and the seven captured bodies, read from the capture directory. | "const COMPLETE"; "const EMPTY_ROSTER"; "const WALK_FINAL" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:39-52 |
| The loader that resolves a capture from this file's own directory rather than the process cwd. | "function captured" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:54-60 |
| The runtime narrowing that finds a family subject in a captured body and throws rather than mounting under a wrong one. | "function firstFamilyId" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:62-89 |
| The typed refusal the explorer's reads are answered with, so no case asserts on a file's bytes. | "const SOURCE_REFUSAL" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:91-103 |
| The one stubbed `fetch` for the whole surface: it records the URLs, routes `/source-content` to the refusal, and answers the rest with the captured queue in order. | "function serving"; "vi.stubGlobal"; "/source-content" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:109-131 |
| The mount: the real surface, the real identifiers, and the family selector when the case is about a family subject. | "function mount"; "selectorKind={familyId === undefined ? \"invariant\" : \"family\"}" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:133-145 |
| The teardown that keeps the stubbed global from leaking into the next case. | `afterEach`; `vi.unstubAllGlobals()` | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:147-150 |
| The one `describe` every case below lives in. | "ReviewSurface family-centered workspace (ICR-R24@v3)" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:152-152 |
| Case 1: the recorded families, their authored guarantees, the full member statements with unchanged siblings included, the recorded sharing, and the opener on every member row. | "renders the recorded families, their authored guarantees and the full member statements" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:153-191 |
| Case 2: a guarantee comparison is drawn in the shape the two recorded revisions support — the same revision on both snapshots versus two different ones. | "opens a family review whose guarantee comparison is the shape the two recorded revisions support" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:193-226 |
| Case 3: a member's review keeps its family, and statement, membership, source attribution and authored judgment are five separate facts. | "keeps the family context when a member is selected and states the five facts separately" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:228-256 |
| Case 4: the complete source explorer is independent of the family selection. | "keeps the complete source explorer independent of the family selection" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:258-274 |
| **Case 5: a roster walks only from the cursor that family's own page published, and the collection picker offers no option that would fetch a refusal.** | "walks a family roster only from the cursor that family's own page published" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:276-320 |
| Case 6: a body with no family context is rendered as that fact and never as a measured zero. | "renders a body that carries no family context as that fact, never as a measured zero" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:322-341 |
| Case 7: an expanded entry stays expanded across a diff-layout switch, and full-file is one value shared by the explorer and the centre. | "keeps an expanded entry expanded across a diff-layout switch" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:343-370 |
| Case 8: the current selection is exposed on the tree and arrow keys traverse the one roving-focus group. | "marks the current selection and traverses the tree by keyboard" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:372-395 |
| Case 9: the filter reports its own scope, keeps a matched family's members, and states that the composed contexts are unchanged when nothing matches. | "reports the filter scope without restating the comparison's totals" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:397-426 |
| **Fix round 1, direction one: a bounded roster says it carried none of the rows it measured, and never that the read measured zero.** | "says a bounded roster carried none of the measured rows, never that the read measured zero" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:429-450 |
| **Fix round 1, direction two: the measured zero is said only where the read really measured zero memberships.** | "still says the measured zero when the read really measured zero memberships" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:452-461 |
| **Fix round 1: a bounded member context is headed partial, its counts are the owner's rows and not this page's, and the centre's continuation control is clicked and its request asserted.** | "heads a bounded member context partial and counts the owner's rows, not this page's" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:463-497 |
| **Fix round 1: two distinct revisions carrying identical text are distinguished from one unchanged revision.** | "distinguishes two distinct revisions with identical text from one unchanged revision" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:499-520 |
| **Fix round 1: a member whose content the page did not carry is stated as that, not as a one-sided statement.** | "states a member whose content the page did not carry as that, not as a one-sided statement" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:522-540 |
| **Fix round 1: a listed-but-uncarried row is said about the page, never as the snapshot recording no row.** | "says a listed-but-uncarried row about the page, never that the snapshot records no row" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:541-587 |
| **Fix round 1: a bounded page's missing row is said about the page, never as the snapshot recording none.** | "says a bounded page's missing row about the page, never that the snapshot records none" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:589-615 |
| **Fix round 1: the centre's empty-roster line is the tree's own string for the same family — one implementation mounted twice.** | "prints one empty-roster sentence in both columns, not two that happen to agree" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:617-641 |
| **Fix round 3: the page that completes a multi-page walk is stated as the walk's last page, never as the whole roster.** | "states the page that completes a multi-page walk as the walk's last page, not as the whole roster" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:642-671 |
| **Fix round 5, V10: all five workspace values survive two page requests issued by the centre's own continuation control, and exactly three request URLs are seen.** | "keeps the reader's workspace state across two page requests through the centre's own control" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:672-725 |
| **The owner of the shared empty-roster sentence: one exported function with both the measured-zero and the page-scoped branches, mounted by the tree and by the centre.** | `emptyRosterSentence`; "the read measured zero memberships for the selected family revision"; "this page carried no member row" | dashboard/src/panels/review/FamilyTree.tsx:276-303 |
| The owner of the completion sentence: `complete` is the read walk's flag, so a one-page walk is the whole selection while a final page is only its last position. | `completionNote`; "the page is the whole selection"; "this page completes the walk" | dashboard/src/panels/review/FamilyTree.tsx:260-273 |
| The tree's own roster line, whose test id the centre re-mounts under its own name. | `RosterLine`; `review-family-roster` | dashboard/src/panels/review/FamilyTree.tsx:232-242 |
| The tree's own continuation control, which publishes the cursor it was given and is the component the centre mounts a second time. | `RosterNext`; `review-family-roster-next`; `data-continuation={page.continuation}` | dashboard/src/panels/review/FamilyTree.tsx:324-355 |
| The centre's empty-roster line mounts the tree's own function, which is what makes the shared-sentence case an identity rather than a resemblance. | `review-center-family-empty`; `emptyRosterSentence(entry)` | dashboard/src/panels/review/FamilyReviewCenter.tsx:648-654 |
| The centre's bounded member-context heading and counts, decided from the read owner's own counts and the pages' completeness. | `memberContextHeading`; `memberContextCounts`; "this page carried ${carriedCarried} member row(s) of them" | dashboard/src/panels/review/FamilyReviewCenter.tsx:559-579 |
| The centre's per-shape blocks the identity, content-not-on-page and one-sided cases read. | "review-center-guarantee-unchanged"; "review-center-guarantee-identical-text"; "review-center-member-not-on-page"; "review-center-member-one-sided-note" | dashboard/src/panels/review/FamilyReviewCenter.tsx:146-157; dashboard/src/panels/review/FamilyReviewCenter.tsx:229-229; dashboard/src/panels/review/FamilyReviewCenter.tsx:292-292 |
| **The server-side rule the walk case pins: `family_members` is in the paged union because the server accepts it, and deliberately not among the walkable collections, because that collection is the set of per-family walks and a cursor-less request earns the server's own refusal.** | `family_members`; `REVIEW_WALKABLE_COLLECTIONS`; `comparison_page_unreadable` | dashboard/src/data/review.ts:71-88 |
| The one page request type a roster continuation builds. | `ReviewPageRequest` | dashboard/src/panels/review/ReviewReadCycle.ts:62-66 |
| The explorer whose population sentence case 4 asserts is unchanged by a selection. | "review-population-scope"; "it never removes one from this list" | dashboard/src/panels/review/SourceExplorer.tsx:287-290 |
| The workspace state the two-page-request case proves survives: the hook and the only setter that also restores focus. | `useWorkspaceState`; `openFromCenter` | dashboard/src/panels/review/ReviewWorkspace.tsx:377-390 |

## Cross-Repo References

No cross-repository behavior is exercised here. The module mounts one repository namespace's surface over
one enclosure's captured bodies and carries no identity that ranges beyond it.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-24T00:43:00+02:00 — 260921-ICR-L24 curator (candidate `ar/260921-icr-l24`, uncommitted; base `5f14fc6790cafc3ad2ae612c2e67f176392dc1fe`): created this one-to-one card for the mounted-surface case module of the family-centered review workspace. It records that the module exercises the **real** `ReviewSurface` with the **real** `intentReview` client and stubs only `fetch`, that its bodies are the real route's own `familyReview.*.captured.json` bytes recorded by `temp/icr/probe-l24-family-body.py`, and each of the module's **nineteen** cases (counted with `grep -c '^  it('` on this candidate) by its own name and what it pins — including the fix-round cases: the empty-roster sentence in both directions, the bounded member-context heading with the owner's counts, the identical-text versus unchanged-revision distinction, the content-not-on-page shape, the page-versus-snapshot sentences, the shared-sentence identity, the completion sentence for a multi-page walk, and the two-page-request case that asserts all five workspace values survive. It states plainly that these are **not browser evidence** (the Playwright configs here are Dagger-gated by `dashboard/scripts/require-dagger-test-environment.mjs`), that a **static captured body** is what the surface is mounted over, and that the live walk's proof lives in enclosure `260921-icr-l31b-ar` at commit `5f14fc67` rather than in this module. Every row of the reference table was derived against this candidate and every anchor in a row occurs inside the range that row cites. **Stamp accounting:** no verification stamp was advanced beyond the leaf base commit — the candidate is uncommitted, so the stamp names the leaf's base plus the working-tree delta, and governed closeout owns the real stamp.
