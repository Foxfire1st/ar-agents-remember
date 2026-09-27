# dashboard/src/panels/review/ReviewWorkspace.family.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/ReviewWorkspace.family.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-27T00:59:43+00:00 |
| lastVerifiedCommitHash | `a5bec6c3b3b413cd3066d0e8d302b4854d1b513a` |
| lastVerifiedCommitDate | 2026-09-27T03:38:17+02:00|
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
`09329a7ee598920c519b06305b73ba8e48d72c88`; this module exists only in the leaf's **uncommitted working
tree**, so the stamp means "leaf base commit plus this leaf's working-tree delta" and does not claim that
the commit holds this content. Governed closeout owns the real stamp. (Corrected 2026-09-26 by the
260921-ICR-L36 curator: this paragraph named `5f14fc6790cafc3ad2ae612c2e67f176392dc1fe` while the header
above names `09329a7e…`. The header is the stamp; `5f14fc67` is the live walk's own proof commit, named in
the Todos below, and the paragraph had borrowed it. The two commits are different facts and the sentence
now says which is which.)

## Code Commentary

### Logic

Roster assertions distinguish cumulative read-item counts from loaded member-context counts. A captured response that answers another side/primary selection after a cursor request is now asserted as failure with the coherent display retained; it is not treated as a valid continuation. Valid independent walks and mounted state retention are exercised in ReviewReadCycle.family.test.tsx.

The comparison-focused cases isolate the shared catalogue hook so its additional request cannot consume a comparison fixture. The ordinary-entry catalogue/comparison interaction is covered separately by ReviewSurface.navigation.test.tsx. Assertions follow the compact labels, central display controls and changed-region default without weakening the existing record, paging or refusal contracts.

**The module carries twenty-one cases** (`grep -c '^  it('` on this candidate), all inside one
`describe("ReviewSurface family-centered workspace (ICR-R24@v3)")`. They fall into three groups: the
original layout cases (the tree, the centre, the explorer, the roster walk, the no-family-context body, the
expansion preference, keyboard traversal and the filter), the fix-round cases that pin a sentence's
direction or a distinction a repair could collapse, and the two page-request case that pins the reader's
workspace state across the pane switch. **The count is stated rather than implied, and it was wrong in the
other direction before this pass:** the module's own `grep -c` reads **20** at the leaf's base commit
`09329a7e`, which is what the L25 round-2 history entry already recorded ("the module's twentieth"), while
this card's body still said nineteen; 260921-ICR-L36 adds the twenty-first and the body now matches the
file. Nothing about the module's meaning changed when the number was corrected — but a card whose stated
count disagrees with its own `grep` is a card a reader stops trusting, which is why the number is fixed
here with the two cases that were missing from the enumerated list rather than silently incremented.

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

**The twenty-one cases and what each one pins:**

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
5. *sends the family's published cursor and refuses a response from another walk* — `family_members` is in
   `REVIEW_PAGED_COLLECTIONS` and deliberately **not** in `REVIEW_WALKABLE_COLLECTIONS`, so the collection
   picker offers no option that would fetch a refusal; the truncated roster states both of the owner's own
   measures; the click sends the published `pageOf=family_members` continuation unchanged, and an incompatible returned walk fails visibly while the coherent display is retained.
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
20. *(260921-ICR-L25, register B3)* *composes the narrow jump route above the family tree, with the tree
    intact* — `review-jump-to-selection` must precede `review-family-tree` in **document order**
    (`DOCUMENT_POSITION_FOLLOWING`), both families and their member rows are still rendered, and activating
    the control focuses `review-center-column`. It pins composition rather than a pixel, because a jsdom
    render has no layout and the pixels are the mounted capture's job. **This case was in the module and in
    the citation table below but not in this list until the 260921-ICR-L36 pass**, which is why the list read
    nineteen against a file that carried twenty.
21. *(260921-ICR-L36, fix round included)* *renders the family's changed expression excerpts,
    deduplicated, over the captured family* — the whole collection, over the real `WALK_FINAL` body, with
    the expectation **computed from that body** by a module-local helper rather than typed: the rendered row
    count is the body's **distinct** excerpt set and is asserted **not** to be its changed-row count, every
    rendered row's `data-collapsed-rows` is one of the body's own group sizes and the group sizes sum back
    to the row total the verdict states, and at least one row collapsed more than one row. It then reads the
    verdict sentence for both counts and for the notion it counted ("not the comparison's own measured change
    set"), and asserts A4's first half is untouched — the member-roster counts line still reports the read's
    own measured rows and the roster still exposes more than one member opener. The helper
    `familyExpressionArithmetic` (`:805-903`) is written **in the case's own module rather than imported from
    the component**, so the assertion is checked against the captured body and not against the
    implementation it tests, and every step narrows at runtime the way `firstFamilyId` does because a
    captured body is `unknown` on purpose.
    **The fix round replaced this case's divergent predicate and added the row-by-row check, and that is the
    part that matters.** The predicate is now **divergence of the reading**: for each excerpt key it compares
    the **sets of resolutions** the two sides gave (`distinct.size > 1`), so a key merely *seen* on two sides
    is not divergence — the case bites only where the two sides read the address differently. (The
    pre-repair predicate filtered keys whose distinct **side names** numbered more than one, which a
    genuinely divergent address never satisfied once `observed` was in the key; the independent verifier
    measured that as vacuous for the claim and this card recorded it. **That note is superseded**: the
    predicate now selects the real divergence, and the case fails when the key is reverted — `Tests 3 failed
    | 25 passed (28)` with `expected [ 'after' ] to deeply equal [ 'after', 'before' ]`.) For each divergent
    excerpt the case asserts the rendered `data-sides` equals the body's own side list **and** that the
    resolution line contains each side's reading string; and then, **for every rendered row**, it asserts the
    row's `data-sides` equals the sides the body resolves that excerpt on — the page's own both-sides
    sentence checked row by row against the body rather than read from the page.
    **The honest bound this case carries and the card must not drop:** the divergent path is evidenced
    against the **captured `familyReview.walkFinal` body through a labelled fixture**, and that label is the
    whole of its evidence. The divergence is exercised against the captured `familyReview.walkFinal` body through a **labelled
    fixture**, and that label is the whole of its evidence. Live data was searched: **the search reached 3
    families served by 1 leaf** (`260921-ICR-L34`, which returns `entries` with 3 families), and the other
    **35 leaves refused `candidate_dataset_absent`** — each records no comparison generation, so no knowledge
    operand exists for a subject to be listed from — and therefore **carry nothing to search. Absent is not
    measured:** those 35 were not searched and found clean; they were unreachable, and a family that cannot
    be listed cannot be shown to be divergence-free. **`260921-ICR-L36` is one of those 35**, so this leaf's
    own live data carries no divergent family either. Read from `f1/raw/live-truth.json` and reproduced
    independently by the verifier in `f1v/raw/vf1-live-scan.json` (`leavesAttempted: 36`, `leavesResolved:
    1`, `leavesRefused: 35`, `refusalCodes: ["candidate_dataset_absent"]`, `familiesServed: 3`,
    `familiesWithDivergence: 0`, `totalDivergent: 0`).
    The live family renders the same 2 excerpts as before, and no part of this card may be read as a claim
    that live data exercises the divergent path.

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
`review-page-option`, `review-page-bounds`, `review-scope-families`, and — since 260921-ICR-L36 —
`review-center-family-expressions`, `review-center-family-expression`,
`review-center-family-expression-resolution`, `review-center-family-expressions-verdict`), and the cases
read server-published values off data attributes (`dataset.familyState`, `dataset.contextState`,
`dataset.inventoryState`,
`dataset.rosterComplete`, `dataset.continuation`, `dataset.sides`, `dataset.diffLayout`, `dataset.fullFile`,
`dataset.selectionKind`, `dataset.family`, and on each excerpt row `dataset.collapsedRows`, `dataset.path`,
`dataset.sides`). `STATE`-style literals are never invented: every expected
sentence is either the capture's own or the owner's own string, and where a sentence is shared the case
asserts identity rather than similarity. Every case awaits the element it needs rather than a timeout, and
the two loops that search the DOM for a shape throw with the sentences they did see when they find none.

### Invariants And Boundaries

- **Real surface, real client, one stubbed global.** Only `fetch` is stubbed; the request is built by the
  shipped client, the response is decoded by the shipped transport, and the tree is the shipped component
  tree. No case passes a prop and then asserts on it.
- **The bodies are the real route's own captured bytes.** No payload is assembled in this module; the one
  hand-written body is a typed refusal for the source-content read, which no case asserts content about.
- **An expectation about a computed count is computed from the body, not typed and not imported.** The A4
  case reads its distinct-set, group-size and divergent-address expectations out of the captured body with a
  module-local helper, and the sibling unit lane (`familyExpressions.test.ts`) is the one that calls the
  shipped function. One lane checks the **wire**, the other checks the **arithmetic**; a case that did both
  against the same object would prove neither (260921-ICR-L36).
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
  (the centre's heading, counts, per-shape blocks and — since 260921-ICR-L36 — the family's deduplicated
  expression collection) and `SourceExplorer.tsx` (the population sentence); the
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
each of the twenty-one cases by its own name. Every anchor in a row below occurs on a line inside the range
that row cites; the anchor of a case row is that case's own `it(...)` name, which occurs on the line that
opens the case.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The module's own statement that this is `ICR-R24@v3` at the mounted surface: the family tree, the unified central reading path, the complete source explorer and the one family-roster walk control.** | "ICR-R24@v3 at the mounted surface" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:1-2 |
| **Real component and real client, with only `fetch` stubbed, and the captured bodies' provenance.** | `intentReview`; "is stubbed"; "familyReview.*.captured.json"; "probe-l24-family-body.py" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:4-12 |
| What these cases catch, including the two ways a repair could lie. | "WHAT THESE CASES CATCH"; "the two ways a repair could lie" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:14-21 |
| **What they do not claim: not browser evidence, Dagger-only Playwright configs, and a live publication explicitly out of scope.** | "WHAT THEY DO NOT CLAIM"; "These are not browser evidence"; "require-dagger-test-environment.mjs"; "not of a live page fed by a running publication" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:23-27 |
| The two collection constants the walk case pins, and the captured refusal body the no-family-context case mounts. | `REVIEW_PAGED_COLLECTIONS`; `REVIEW_WALKABLE_COLLECTIONS`; `RECORDS_PAGE_REFUSAL_RESPONSE` | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:35-37 |
| The three task identifiers and the seven captured bodies, read from the capture directory. | "const COMPLETE"; "const EMPTY_ROSTER"; "const WALK_FINAL" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:54-54; dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:59-60 |
| The loader that resolves a capture from this file's own directory rather than the process cwd. | "function captured" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:65-65 |
| The runtime narrowing that finds a family subject in a captured body and throws rather than mounting under a wrong one. | "function firstFamilyId" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:62-89 |
| The typed refusal the explorer's reads are answered with, so no case asserts on a file's bytes. | "const SOURCE_REFUSAL" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:91-103 |
| The one stubbed `fetch` for the whole surface: it records the URLs, routes `/source-content` to the refusal, and answers the rest with the captured queue in order. | "function serving"; "vi.stubGlobal"; "/source-content" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:109-131 |
| The test mount opens the real surface with the fixture task and selected subject context. | `mount` | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:143-155 |
| The teardown cleans the mounted tree and restores stubbed globals. | "afterEach(() => {" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:157-160 |
| The one `describe` every case below lives in. | "ReviewSurface family-centered workspace (ICR-R24@v3)" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:162-889 |
| Case 1: the recorded families, their authored guarantees, the full member statements with unchanged siblings included, the recorded sharing, and the opener on every member row. | "renders the recorded families, their authored guarantees and the full member statements" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:163-201 |
| Case 2: a guarantee comparison is drawn in the shape the two recorded revisions support — the same revision on both snapshots versus two different ones. | "opens a family review whose guarantee comparison is the shape the two recorded revisions support" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:203-236 |
| Case 3: a member's review keeps its family, and statement, membership, source attribution and authored judgment are five separate facts. | "keeps the family context when a member is selected and states the five facts separately" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:238-266 |
| Case 4: the complete source explorer is independent of the family selection. | "keeps the complete source explorer independent of the family selection" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:268-284 |
| **Case 5: a roster walks only from the cursor that family's own page published, and the collection picker offers no option that would fetch a refusal.** | "sends the family's published cursor and refuses a response from another walk" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:286-329 |
| Case 6: a body with no family context is rendered as that fact and never as a measured zero. | "renders a body that carries no family context as that fact, never as a measured zero" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:331-350 |
| Case 7: an expanded entry stays expanded across a diff-layout switch, and full-file is one value shared by the explorer and the centre. | "keeps an expanded entry expanded across a diff-layout switch" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:352-379 |
| Case 8: the current selection is exposed on the tree and arrow keys traverse the one roving-focus group. | "marks the current selection and traverses the tree by keyboard" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:381-404 |
| Case 9: the filter reports its own scope, keeps a matched family's members, and states that the composed contexts are unchanged when nothing matches. | "reports the filter scope without restating the comparison's totals" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:406-435 |
| **Fix round 1, direction one: a bounded roster says it carried none of the rows it measured, and never that the read measured zero.** | "says a bounded roster carried none of the measured rows, never that the read measured zero" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:438-459 |
| **Fix round 1, direction two: the measured zero is said only where the read really measured zero memberships.** | "still says the measured zero when the read really measured zero memberships" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:461-470 |
| **Fix round 1: a bounded member context is headed partial, its counts are the owner's rows and not this page's, and the centre's continuation control is clicked and its request asserted.** | "heads a bounded member context partial and counts the owner's rows, not this page's" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:472-506 |
| **Fix round 1: two distinct revisions carrying identical text are distinguished from one unchanged revision.** | "distinguishes two distinct revisions with identical text from one unchanged revision" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:508-529 |
| **Fix round 1: a member whose content the page did not carry is stated as that, not as a one-sided statement.** | "states a member whose content the page did not carry as that, not as a one-sided statement" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:531-549 |
| Uncarried roster content is not converted into an absent primary statement. | "does not turn an uncarried roster operand into an absent statement" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:550-566 |
| Bounded before-only membership remains context and does not assert invariant removal. | "retains a bounded before-only membership without claiming that the invariant was removed" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:568-580 |
| **Fix round 1: the centre's empty-roster line is the tree's own string for the same family — one implementation mounted twice.** | "prints one empty-roster sentence in both columns, not two that happen to agree" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:582-606 |
| **Fix round 3: the page that completes a multi-page walk is stated as the walk's last page, never as the whole roster.** | "states the page that completes a multi-page walk as the walk's last page, not as the whole roster" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:607-636 |
| **Fix round 5, V10: all five workspace values survive two page requests issued by the centre's own continuation control, and exactly three request URLs are seen.** | "keeps the reader's workspace state across two page requests through the centre's own control" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:637-690 |
| **260921-ICR-L25, register B3: the narrow jump route is composed ABOVE the family tree and the tree is intact — the case pins document order (`DOCUMENT_POSITION_FOLLOWING`), that both families and their member rows are still rendered, and that activating the control focuses the centre column. It pins composition rather than a pixel, because a jsdom render has no layout and the pixels are the mounted capture's job.** | "composes the narrow jump route above the family tree, with the tree intact" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:870-888 |
| **260921-ICR-L36 (fix round included): the family's rendered excerpt collection is the body's DISTINCT excerpt set and not its changed-row count, every row's `data-collapsed-rows` is one of the body's group sizes, every divergent excerpt's `data-sides` and per-side reading strings match the body's, and EVERY rendered row's `data-sides` equals the sides the body resolves it on. The predicate is divergence of the reading (distinct resolution sets across sides), not "seen on two sides".** | "renders the family's changed expression excerpts, deduplicated, over the captured family"; `review-center-family-expressions`; `review-center-family-expression-resolution`; `dataset.sides` | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:700-768 |
| **The arithmetic that case's expectation is read from, deliberately written in the case's module rather than imported from the component, so the assertion checks the body and not the implementation it tests. It computes the excerpt key the fixed module uses (`path \0 recorded`), the per-side resolution sets the divergent predicate compares, and the side list every rendered row is checked against.** | "function familyExpressionArithmetic" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:779-868 |
| The shared empty-roster function distinguishes absent family revisions, measured zero and page-local missing rows. | `emptyRosterSentence` | dashboard/src/panels/review/FamilyTree.tsx:222-236 |
| The owner of the completion sentence: `complete` is the read walk's flag, so a one-page walk is the whole selection while a final page is only its last position. | `completionNote`; "the page is the whole selection"; "this page completes the walk" | dashboard/src/panels/review/FamilyTree.tsx:211-216; dashboard/src/panels/review/FamilyTree.tsx:260-284; dashboard/src/panels/review/FamilyTree.tsx:275-284; dashboard/src/panels/review/FamilyTree.tsx:278-284; dashboard/src/panels/review/FamilyTree.tsx:278-308 |
| The tree's own roster line, whose test id the centre re-mounts under its own name. | `RosterLine`; `review-family-roster` | dashboard/src/panels/review/FamilyTree.tsx:182-209 |
| The tree's own continuation control, which publishes the cursor it was given and is the component the centre mounts a second time. | `RosterNext`; `review-family-roster-next`; `data-continuation={page.continuation}` | dashboard/src/panels/review/FamilyTree.tsx:250-282 |
| The central empty-roster presentation reuses the tree-owned sentence and preserves the page scope. | `FamilyMemberContext`; `emptyRosterSentence` | dashboard/src/panels/review/FamilyReviewCenter.tsx:533-594; dashboard/src/panels/review/FamilyTree.tsx:222-236 |
| The centre's bounded member-context heading and counts, decided from the read owner's own counts and the pages' completeness. | `memberContextHeading`; `memberContextCounts`; "loaded context contains ${carriedCarried} member row(s) of them" | dashboard/src/panels/review/FamilyReviewCenter.tsx:512-517; dashboard/src/panels/review/FamilyReviewCenter.tsx:519-531 |
| Roster revision content and authoritative selected-subject statements remain separate rendering responsibilities. | `MemberStatement`; `SelectedStatement` | dashboard/src/panels/review/FamilyReviewCenter.tsx:198-214; dashboard/src/panels/review/SubjectReview.tsx:53-114 |
| **The server-side rule the walk case pins: `family_members` is in the paged union because the server accepts it, and deliberately not among the walkable collections, because that collection is the set of per-family walks and a cursor-less request earns the server's own refusal.** | `ReviewPagedCollection`; `REVIEW_WALKABLE_COLLECTIONS` | dashboard/src/data/review.ts:78-78; dashboard/src/data/review.ts:88-88 |
| The one page request type a roster continuation builds. | `ReviewPageRequest` | dashboard/src/panels/review/ReviewReadCycle.ts:64-68 |
| The source explorer retains the complete inventory independently of semantic selection. | `SourceExplorer` | dashboard/src/panels/review/SourceExplorer.tsx:224-302 |
| The workspace hook preserves display state and the source opener needed for focus return. | `useWorkspaceState` | dashboard/src/panels/review/ReviewWorkspace.tsx:159-196 |

## Cross-Repo References

No cross-repository behavior is exercised here. The module mounts one repository namespace's surface over
one enclosure's captured bodies and carries no identity that ranges beyond it.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-27T01:19:05+00:00: Generated citation repair: "ReviewSurface family-centered workspace (ICR-R24@v3)" repointed to dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:162-889. No content impact: mechanical anchor-range projection bound to citation source snapshot 771605ffc6f78b7deb726bb881dc964bb91fad696d0375cef1a8d8e9ffd8ba84; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-27T01:19:05+00:00: Generated citation repair: "renders a body that carries no family context as that fact, never as a measured zero" repointed to dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:331-350. No content impact: mechanical anchor-range projection bound to citation source snapshot 771605ffc6f78b7deb726bb881dc964bb91fad696d0375cef1a8d8e9ffd8ba84; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-27T01:19:05+00:00: Generated citation repair: "keeps an expanded entry expanded across a diff-layout switch" repointed to dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:352-379. No content impact: mechanical anchor-range projection bound to citation source snapshot 771605ffc6f78b7deb726bb881dc964bb91fad696d0375cef1a8d8e9ffd8ba84; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-27T01:19:05+00:00: Generated citation repair: "marks the current selection and traverses the tree by keyboard" repointed to dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:381-404. No content impact: mechanical anchor-range projection bound to citation source snapshot 771605ffc6f78b7deb726bb881dc964bb91fad696d0375cef1a8d8e9ffd8ba84; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-27T01:19:05+00:00: Generated citation repair: "reports the filter scope without restating the comparison's totals" repointed to dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:406-435. No content impact: mechanical anchor-range projection bound to citation source snapshot 771605ffc6f78b7deb726bb881dc964bb91fad696d0375cef1a8d8e9ffd8ba84; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-27T01:19:05+00:00: Generated citation repair: "says a bounded roster carried none of the measured rows, never that the read measured zero" repointed to dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:438-459. No content impact: mechanical anchor-range projection bound to citation source snapshot 771605ffc6f78b7deb726bb881dc964bb91fad696d0375cef1a8d8e9ffd8ba84; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-27T01:19:05+00:00: Generated citation repair: "still says the measured zero when the read really measured zero memberships" repointed to dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:461-470. No content impact: mechanical anchor-range projection bound to citation source snapshot 771605ffc6f78b7deb726bb881dc964bb91fad696d0375cef1a8d8e9ffd8ba84; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-27T01:19:05+00:00: Generated citation repair: "heads a bounded member context partial and counts the owner's rows, not this page's" repointed to dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:472-506. No content impact: mechanical anchor-range projection bound to citation source snapshot 771605ffc6f78b7deb726bb881dc964bb91fad696d0375cef1a8d8e9ffd8ba84; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-27T01:19:05+00:00: Generated citation repair: "distinguishes two distinct revisions with identical text from one unchanged revision" repointed to dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:508-529. No content impact: mechanical anchor-range projection bound to citation source snapshot 771605ffc6f78b7deb726bb881dc964bb91fad696d0375cef1a8d8e9ffd8ba84; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-27T01:19:05+00:00: Generated citation repair: "states a member whose content the page did not carry as that, not as a one-sided statement" repointed to dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:531-549. No content impact: mechanical anchor-range projection bound to citation source snapshot 771605ffc6f78b7deb726bb881dc964bb91fad696d0375cef1a8d8e9ffd8ba84; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-27T01:19:05+00:00: Generated citation repair: "does not turn an uncarried roster operand into an absent statement" repointed to dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:550-566. No content impact: mechanical anchor-range projection bound to citation source snapshot 771605ffc6f78b7deb726bb881dc964bb91fad696d0375cef1a8d8e9ffd8ba84; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-27T01:19:05+00:00: Generated citation repair: "retains a bounded before-only membership without claiming that the invariant was removed" repointed to dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:568-580. No content impact: mechanical anchor-range projection bound to citation source snapshot 771605ffc6f78b7deb726bb881dc964bb91fad696d0375cef1a8d8e9ffd8ba84; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-27T01:19:05+00:00: Generated citation repair: "prints one empty-roster sentence in both columns, not two that happen to agree" repointed to dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:582-606. No content impact: mechanical anchor-range projection bound to citation source snapshot 771605ffc6f78b7deb726bb881dc964bb91fad696d0375cef1a8d8e9ffd8ba84; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-27T01:19:05+00:00: Generated citation repair: "states the page that completes a multi-page walk as the walk's last page, not as the whole roster" repointed to dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:607-636. No content impact: mechanical anchor-range projection bound to citation source snapshot 771605ffc6f78b7deb726bb881dc964bb91fad696d0375cef1a8d8e9ffd8ba84; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-27T01:19:05+00:00: Generated citation repair: "keeps the reader's workspace state across two page requests through the centre's own control" repointed to dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:637-690. No content impact: mechanical anchor-range projection bound to citation source snapshot 771605ffc6f78b7deb726bb881dc964bb91fad696d0375cef1a8d8e9ffd8ba84; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-27T01:19:05+00:00: Generated citation repair: "composes the narrow jump route above the family tree, with the tree intact" repointed to dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:870-888. No content impact: mechanical anchor-range projection bound to citation source snapshot 771605ffc6f78b7deb726bb881dc964bb91fad696d0375cef1a8d8e9ffd8ba84; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-27T01:19:05+00:00: Generated citation repair: "renders the family's changed expression excerpts, deduplicated, over the captured family" repointed to dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:700-768. No content impact: mechanical anchor-range projection bound to citation source snapshot 771605ffc6f78b7deb726bb881dc964bb91fad696d0375cef1a8d8e9ffd8ba84; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-27T01:16:27+00:00 — Re-read the renamed cursor/rejection case and the expression-arithmetic, count and collection references. The old capture proves explicit rejection, not a successful foreign walk; references now cite the actual test and owned constructs. Historical producer notes remain unchanged.

- 2026-09-27T00:59:43+00:00 — Curated loaded-context wording and rejection of an incompatible captured response. Existing family, guarantee, inventory and workspace-state obligations remain; actual compatible continuation coverage is kept in the adjacent read-cycle test.
- 2026-09-26T21:10:54+00:00: Generated citation repair: "const COMPLETE"; "const EMPTY_ROSTER"; "const WALK_FINAL" repointed to dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:54-54; dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:59-59; dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:60-60. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T21:10:54+00:00: Generated citation repair: "function captured" repointed to dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:65-65. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T21:10:54+00:00: Generated citation repair: "ReviewSurface family-centered workspace (ICR-R24@v3)" repointed to dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:162-890. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T21:10:54+00:00: Generated citation repair: "still says the measured zero when the read really measured zero memberships" repointed to dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:462-471. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T21:10:54+00:00: Generated citation repair: "prints one empty-roster sentence in both columns, not two that happen to agree" repointed to dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:583-607. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T21:10:54+00:00: Generated citation repair: "states the page that completes a multi-page walk as the walk's last page, not as the whole roster" repointed to dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:608-637. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T21:10:54+00:00: Generated citation repair: "keeps the reader's workspace state across two page requests through the centre's own control" repointed to dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:638-691. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T21:10:54+00:00: Generated citation repair: "composes the narrow jump route above the family tree, with the tree intact" repointed to dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:871-889. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T21:10:54+00:00: Generated citation repair: "renders the family's changed expression excerpts, deduplicated, over the captured family" repointed to dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:701-769. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T21:10:54+00:00: Generated citation repair: `divergent`; `groups`; "function familyExpressionArithmetic"; "the captured body records no changed expression in any family" repointed to dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:845-856; dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:809-809; dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:780-780; dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:867-867. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T21:10:54+00:00: Generated citation repair: `RosterLine` repointed to dashboard/src/panels/review/FamilyTree.tsx:182-209. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T21:10:54+00:00: Generated citation repair: `RosterNext` repointed to dashboard/src/panels/review/FamilyTree.tsx:250-282. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T20:57:44Z — Reconciled current source-owner citations and exact declarations; superseded wording is corrected in the affected reference rows.
- 2026-09-26T19:49:05Z — The comparison-focused cases isolate the shared catalogue hook so its additional request cannot consume a comparison fixture. The ordinary-entry catalogue/comparison interaction is covered separately by ReviewSurface.navigation.test.tsx. Assertions follow the compact labels, central display controls and changed-region default without weakening the existing record, paging or refusal contracts.
- 2026-09-26T03:50:00+02:00 — 260921-ICR-L36 curator, **final wording pass (the last correction), and two round-1 sentences this seat repeats are corrected or bounded here.** (1) **The replacement clause is not to be quoted as self-evidently true** (F-V1-3, low; a reword is in flight). The page's notion sentence reads *"every row below names the resolution of each side whose read resolved its address's recorded bytes, so an address the two sides read differently prints both readings rather than one."* The phrase *"resolved its address's recorded bytes"* **collides with the product's own name for `exact_recorded_blob`**: the clause holds under the reading the code implements — a side's read result is printed for the side that produced it, which the fix verifier asserted **row by row on the rendered page** — and fails under the literal reading, where every changed side is `recorded_blob_mismatch` and has not "resolved" its recorded bytes. The body now quotes it **with the reading named**, and says so. (2) **"No claim in the leaf rests on a fixture" is falsified, and this card does not say it** (F-V1-4, low — the one round-1 sentence the corrected pass did not cover). The **divergent-rendering** claim rests on the captured `familyReview.walkFinal` body through a **labelled fixture**, because live data carries no divergent family: the search reached **3 families served by 1 leaf**, with **35 leaves refusing `candidate_dataset_absent`** and therefore **absent, not measured**, `260921-ICR-L36` among them. Every `CONSTRUCTED` label in the unit lane is about that module's own inputs and is **not** a claim about the leaf's evidence. (3) **Routed, not absorbed:** **F-V1-6** and **F-V1-7** are the verifier's remaining low findings and belong to the worker/verifier seats; the subject-catalogue route's deliberate `candidate_dataset_absent`, the shell-level scroll decision with its 13 chrome elements, and **D63**, **D64**, **D68**, **D70** remain routed exactly as before. (4) **One report-side caveat that is NOT a card fact and is deliberately not propagated as settled:** the report's `dashboard/src` digest `08de88e7…` does not reproduce under a stated method (the verifier measured `fb387272…`), and three B4 content heights differ between the two seats by 20–70 px. No card here quotes a digest or a height, and none should: those numbers were measured by one seat and may differ by seat. No verification stamp was advanced; no commit was made.
- 2026-09-26T03:35:00+02:00 — 260921-ICR-L36 curator, **the authoritative statement of the divergent bound; it supersedes every earlier phrasing of it in this document, and the entry below is corrected in place for its refusal reason only (same seat, same uncommitted pass, minutes old, and a wrong reason code must not stand).** The orchestrator passed this seat a summary of the zero-divergence measurement whose scope was too wide — "scanned every family of all 36 leaves" — and the artifact does not support that scope. Measured from `temp/icr/f1/raw/live-truth.json` and reproduced independently by the verifier in `temp/icr/f1v/raw/vf1-live-scan.json`: **36 leaves attempted; 1 resolved (`260921-ICR-L34`, state `entries`, 3 families); 35 refused with code `candidate_dataset_absent`** (each records no comparison generation, so no knowledge operand exists for a subject to be listed from); **3 families served; 0 divergent addresses**. The rule this document now carries is the point of the correction: **absent is not measured.** The 35 were not searched and found clean — they were unreachable, and a family that cannot be listed cannot be shown to be divergence-free. **`260921-ICR-L36` is itself one of those 35**, so this leaf's own live data carries no divergent family either. The bounded conclusion that stands: the divergence is exercised against the captured `familyReview.walkFinal` body through a **labelled fixture** — now verified: the divergent address renders `before exact_recorded_blob · after recorded_blob_mismatch` with `data-sides = "before,after"`, and reverting `excerptKey` fails the shipped suite at `ReviewWorkspace.family.test.tsx:777` — and live data reached 3 families of 1 leaf with none divergent. **Also settled by that verification:** the false sentence is gone from the shipped bundle, the rendered page and the report, and the replacement sentence the cards quote was checked for truth about every row the page renders and none was found untrue. No verification stamp was advanced; no commit was made.
- 2026-09-26T03:20:00+02:00 — 260921-ICR-L36 curator, **same-pass correction of the entry below, which is left standing as the record of what this pass first wrote.** The entry below says the divergence scan "scanned every family of all 36 leaves and measured zero divergent addresses". **That is an over-claim about the population, and the artifact does not support it.** Read from the fix round's own `temp/icr/f1/raw/live-truth.json` and reproduced independently by the verifier in `temp/icr/f1v/raw/vf1-live-scan.json`, the measurement is: **36 leaves attempted, 35 refused `candidate_dataset_absent`** (each records no comparison generation, so no knowledge operand exists for a subject to be listed from — **absent is not measured**), **1 resolved** (`260921-ICR-L34`, which returns `entries` with **3 families**), and of those 3 families examined **0 carry a divergent address** (`familiesExamined: 3`, `familiesWithDivergence: 0`, `totalDivergent: 0`). **The zero is measured over 3 families, not over all 36 leaves** — 35 of them never answered — and the body of this document now says so, naming the examined population and citing both artifacts. The measured conclusion is unchanged and the bound it exists for is unchanged: no live family in the population the scan could reach records a divergence, so the divergent rendering is evidenced against the captured `familyReview.walkFinal` body through a fixture-backed API and is labelled as such. Only the population was overstated; no stamp was advanced; no commit was made.
- 2026-09-26T03:00:00+02:00 — 260921-ICR-L36 curator, **post-fix pass: the F1 repair round landed and item 21 is re-read against the fixed case.** The case's body changed in three ways and this card now states all three. (1) **The divergent predicate is replaced.** It is now divergence of the **reading** — for each excerpt key the helper compares the **sets of resolutions** the two sides gave (`distinct.size > 1`) — so a key merely *seen* on two sides is not divergence, and the case bites only where the two sides read the address differently. The pre-repair predicate filtered keys whose distinct **side names** numbered more than one, which a genuinely divergent address never satisfied once `observed` was in the key; the independent verifier measured that as vacuous and the entry below records it. **That note is superseded here rather than deleted**, and the case now demonstrably bites: reverting the key produces `Tests 3 failed | 25 passed (28)` with `expected [ 'after' ] to deeply equal [ 'after', 'before' ]`. (2) **A row-by-row check was added**: for every rendered row the case asserts `data-sides` equals the sides the captured body resolves that excerpt on, and for each divergent excerpt it asserts both the side list and that the resolution line contains each side's reading string — the page's own sentence checked against the body rather than read from the page. (3) **The honest bound is recorded**: the divergent path is evidenced against the captured `familyReview.walkFinal` body through a **fixture-backed API**, labelled as such, because the fix round scanned every family of all **36** leaves and measured **zero** divergent addresses — the live family renders the same 2 excerpts as before, and this card may not be read as claiming live data exercises the divergent path. **Nothing else about the module moved:** it still carries twenty-one cases, the captured bodies are still read rather than typed, and the two pre-existing contradictions this pass corrected (the false "nineteen cases" count and the stamp paragraph naming a commit its own header does not) stand corrected. **Citation accounting:** the case's row moved `:735-790` → `:735-803`, the helper's row `:792-862` → `:805-903`, the narrow-jump case `:864-882` → `:905-924` (it moved with the case above it), and the three cross-file rows into `FamilyReviewCenter.tsx` were re-derived there (`emptyRosterSentence` import `:45-45` unchanged, its mount `:1104-1105` → `:1134-1135`, `memberContextHeading` `:1026-1031` → `:1053-1061`, `memberContextCounts` `:1037-1046` → `:1063-1076`). **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted, so the governed closeout owns the real stamp. No commit was made.
- 2026-09-26T02:45:00+02:00 — 260921-ICR-L36 curator, **same-pass correction of the entry below, which is left standing as the record of what this pass first wrote.** The independent verifier's `verify-l36.md` (first line `pass-with-findings`) filed **F1** against one rendering claim this leaf's case 21 asserts, and the entry below repeats it: *a divergent address renders both sides' resolutions.* **That claim is false as measured.** The excerpt identity is `path \0 recorded \0 observed`, and a divergence changes `observed`, so the two sides of a divergent address mint **two different keys**; the side-pairing lookup finds one side only, and the mounted product renders `src/batch.py`, revision `d24e5187…`, with `sides: ["after"]` — one side. The verdict's own clause "each row below names both" is untrue for that row. The case's `divergentPaths` predicate is **vacuous for that claim**: it filters keys whose distinct **side names** number more than one, which a genuinely divergent address never satisfies (it never appears on both sides of one key); what it selects is addresses recorded on both sides with identical resolutions. **The body was corrected in this same pass** — item 21, the citation row for case 21 and the citation row for `familyExpressionArithmetic` each now state the defect instead of the refuted claim — and the true statement until the fix lands is: *the excerpt identity is deduplicated correctly, the change IS surfaced, and the per-side pairing of a divergent address is being fixed because the key separates the two sides it is meant to join.* **What the verifier upheld is not weakened by this:** the dedup arithmetic survived two independent re-derivations (8 membership rows, 8 changed row instances, 2 distinct keys, 6 collapsed, `8 − 2 = 6`), the over-collapse probe found no over-collapse, A3/A5/B4 reproduced exactly, and the before state is a measured zero. No verification stamp was advanced. No commit was made.
- 2026-09-26T02:35:00+02:00 — 260921-ICR-L36 curator (leaf `260921-ICR-L36`, memory worktree only; code worktree uncommitted at base `09329a7ee598920c519b06305b73ba8e48d72c88`, memory base `52c025e6f2c38d3207274d55e00a8889c0459bad`; worker report `temp/icr/report-l36.md`): **body update — the module's twenty-first case is recorded, and this card's own case count is corrected rather than incremented.** The new case (item 21) mounts the real surface over the captured `WALK_FINAL` body and holds A4's collection to the body's own arithmetic: the rendered row count is the body's **distinct** excerpt set and is asserted **not** to be its changed-row count, every rendered row's `data-collapsed-rows` is one of the body's own group sizes and they sum back to the verdict's row total, a divergent address renders both sides' resolutions, and A4's first half (the member roster) is asserted untouched. Its expectation is computed by a module-local helper (`familyExpressionArithmetic`, item's own range `:792-862`) rather than imported from the component, so the assertion checks the captured body and not the implementation it tests — and the card now says why that is deliberate. **A pre-existing contradiction in this card was corrected in the same pass, honestly:** the body said "The module carries nineteen cases" and "each of the nineteen cases by its own name" while `grep -c '^  it('` reads **20** at the leaf's base commit — and the L25 round-2 history entry three lines above already recorded "the module's twentieth". Item 20 (the narrow jump case) existed in the module and in the citation table but not in the enumerated list. The count is now **twenty-one** in all three places and items 20 and 21 were added, so the sentence and the file agree. **A second pre-existing contradiction was corrected too:** this card's own "Verification stamp" paragraph named `5f14fc6790cafc3ad2ae612c2e67f176392dc1fe` as the header's stamp while the header names `09329a7e…`; `5f14fc67` is the live walk's proof commit named in the Todos, and the paragraph had borrowed it. It now names the header's own value and says which commit is which. **Citation accounting:** every row whose range this leaf's insertion displaced was re-derived from each construct's declaration at this tip — the centre's `emptyRosterSentence` import `:44-44` → `:45-45` and its mount `:669-669` → `:1105-1105`, `memberContextHeading` `:577-582` → `:1026-1031`, `memberContextCounts` `:588-597` → `:1037-1046`, the per-shape blocks `:146-157`/`:229-229`/`:292-292` → `:147-158`/`:230-230`/`:293-293`, and the narrow-jump case `:735-753` → `:864-882` (it moved because the new case was inserted above it). **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted, so the governed closeout owns the real stamp. No commit was made.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `emptyRosterSentence`; "the read measured zero memberships for the selected family revision"; "this page carried no member row" repointed to dashboard/src/panels/review/FamilyTree.tsx:298-317; dashboard/src/panels/review/FamilyTree.tsx:305-305; dashboard/src/panels/review/FamilyTree.tsx:293-293. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `RosterLine` repointed to dashboard/src/panels/review/FamilyTree.tsx:246-273. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `memberContextHeading`; `memberContextCounts`; "loaded context contains ${carriedCarried} member row(s) of them" repointed to dashboard/src/panels/review/FamilyReviewCenter.tsx:577-582; dashboard/src/panels/review/FamilyReviewCenter.tsx:588-597; dashboard/src/panels/review/FamilyReviewCenter.tsx:595-595. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: "review-population-scope"; "it never removes one from this list" repointed to dashboard/src/panels/review/SourceExplorer.tsx:299-299; dashboard/src/panels/review/SourceExplorer.tsx:301-301. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `useWorkspaceState`; `openFromCenter` repointed to dashboard/src/panels/review/ReviewWorkspace.tsx:392-424; dashboard/src/panels/review/ReviewWorkspace.tsx:387-387. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T23:45+02:00 — 260921-ICR-L25 curator, round 2 (uncommitted change set on `ar/260921-icr-l25-ar`, code base `d9e7e6e79ce532d16c689435ae95a63aab430f94` plus the working-tree delta, memory base `39adea206651654dbfacf2ee1bb4e2f3763b515b`; round-2 report `report-l25-round2.md` = `9446232d…`): **body update — one case added (the module's twentieth), and the card now carries it.** The new case pins the B3 fix at the level a jsdom render can actually decide: `review-jump-to-selection` must precede `review-family-tree` in **document order** (`DOCUMENT_POSITION_FOLLOWING`), the tree must still carry both families and its member rows ("while keeping the full family/sibling tree intact"), and activating the control must focus `review-center-column`. It deliberately pins composition rather than a pixel — "a jsdom render has no layout, and the pixels are the mounted capture's job" — because the accepted design's own requirement is stated as a position near the top (P2-3), and the absolute y is the mounted capture's evidence. **Citation accounting:** the new row cites `:735-753` from the case's own `it(` through its closing brace. **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted, so the governed closeout owns the real stamp. No commit was made.
- 2026-09-24T00:43:00+02:00 — 260921-ICR-L24 curator (candidate `ar/260921-icr-l24`, uncommitted; base `5f14fc6790cafc3ad2ae612c2e67f176392dc1fe`): created this one-to-one card for the mounted-surface case module of the family-centered review workspace. It records that the module exercises the **real** `ReviewSurface` with the **real** `intentReview` client and stubs only `fetch`, that its bodies are the real route's own `familyReview.*.captured.json` bytes recorded by `temp/icr/probe-l24-family-body.py`, and each of the module's **nineteen** cases (counted with `grep -c '^  it('` on this candidate) by its own name and what it pins — including the fix-round cases: the empty-roster sentence in both directions, the bounded member-context heading with the owner's counts, the identical-text versus unchanged-revision distinction, the content-not-on-page shape, the page-versus-snapshot sentences, the shared-sentence identity, the completion sentence for a multi-page walk, and the two-page-request case that asserts all five workspace values survive. It states plainly that these are **not browser evidence** (the Playwright configs here are Dagger-gated by `dashboard/scripts/require-dagger-test-environment.mjs`), that a **static captured body** is what the surface is mounted over, and that the live walk's proof lives in enclosure `260921-icr-l31b-ar` at commit `5f14fc67` rather than in this module. Every row of the reference table was derived against this candidate and every anchor in a row occurs inside the range that row cites. **Stamp accounting:** no verification stamp was advanced beyond the leaf base commit — the candidate is uncommitted, so the stamp names the leaf's base plus the working-tree delta, and governed closeout owns the real stamp.
