# dashboard/src/panels/review/ReviewWorkspace.family.test.tsx

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
`serving/review.py` published over the real application owners and the real store for one real enclosure.
**Since MIK-L31 every body is from the current route** (MIK-R31 rule 6, the L44-R1-F5 remainder): `complete`
and `identical` were re-captured earlier by the producer named in `familyReview.capture-provenance.json`, and
`truncated`, `continued`, `oneSided`, `walkFinal` and `emptyRoster` were re-captured by MIK-L31 with L44's
producer (first build accepted, one attempt each; the receipt's `mik_l31_recapture` section, captured at the
L10-synced tree `18b77329`). All carry each member source's structured `locator`, `resolved_ranges` and
`locator_state`. Because the current route's bounded first page always carries the member its first items
represent, five expectations were moved to current-route truth (the worker's open question 3), and the one
rendering branch no real body reaches any more, "this page carried no member row", is kept and covered by a
labelled SYNTHETIC body (ruling 2026-09-30T05:36:19 Q3). The module header (lines 9-21, refreshed by a
comment-only follow-up) says so: two captures recorded in the receipt, the MIK-L31 one at the L10-synced tree
`18b77329` (`mik_l31_recapture`), counts that depend on a build's identity draw read from the body, and the one case
labelled SYNTHETIC as the only assembled body. The header names capture commits and the receipt rather than a leaf, per the
repository's source-comment scope rule. No assertion reads a prop this test itself passed, and no
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

**The module carries twenty-two cases** (`grep -c '^  it('` on this candidate), all inside one
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

**The twenty-two cases and what each one pins (twenty-one before MIK-L31 added the real-body roster case, 10):**

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
10. *(MIK-L31, real body)* *states a bounded roster page as the part of the measured rows it carried, never as
    zero* — over the re-captured `TRUNCATED` body, all four rosters print the owner's own measures ("records 2
    membership row(s); loaded context contains 1 of them"), no empty-roster sentence is printed, "measured zero"
    is never said, and the continuation is offered.
10a. *(fix round 1, kept by ruling Q3 over a SYNTHETIC body)* *says a bounded roster carried none of the
    measured rows, never that the read measured zero* — the body is the real `TRUNCATED` capture with every
    roster's member rows removed, labelled SYNTHETIC in the case and never offered as a route body; every
    bounded roster prints the **page-scoped** sentence ("this page carried no member row", "0 of the 2 recorded
    membership row(s) it measured") and the continuation sentence, and never "measured zero".
11. *(fix round 1)* *still says the measured zero when the read really measured zero memberships* — the other
    direction of the same sentence, and the only place "the read measured zero memberships" may be said.
12. *(fix round 1)* *heads a bounded member context partial and counts the owner's rows, not this page's* —
    the centre's heading is "Recorded member context (partial)", the counts state the read's own
    `4 … across 2 recorded side(s) (before 2 + after 2)` and "loaded context contains <n> member row(s) of them",
    where `<n>` is read from the body (the opened family's distinct loaded member revisions, asserted below 4 so a
    capture that carried every row cannot pass; MIK-L31, review F7 and R2-7), plus the continuation sentence, the distinct-member line is scoped to the rows this page carried, the
    per-side lines are the tree's own components mounted in the centre, and the centre's continuation control
    is **clicked** and the request it issues asserted, because a control mounted without its handler renders
    identically and fetches nothing (fix round 2, V6).
13. *(fix round 1)* *distinguishes two distinct revisions with identical text from one unchanged revision* —
    two distinct revisions carrying the same authored text render, since MIK-R31 rule 3 (the 13:40 decision), as
    "Wording unchanged · revision <before8> → <after8>" with the guarantee shown **once** and both revision IDs
    under details, never as "the guarantee is unchanged"; only the same-revision family may say that.
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
    one implementation mounted twice rather than two sentences that happen to read alike. Since MIK-L31 it runs
    over the measured-empty `EMPTY_ROSTER` body, the one the current route serves with an empty roster.
18. *(fix round 3)* *states the page that completes a multi-page walk as the walk's last page, not as the
    whole roster* — the final page of a four-page walk says it "completes the walk" and that the pages before
    it carried the rows this one did not, never "the page is the whole selection"; the rosters the read took
    whole still say so and never claim to be a step in a walk, and the surface read the route's own sentence
    for that side rather than inventing one. Since MIK-L31 the carried count is read from the body (the side
    with 72 recorded rows), asserted below 72. Before the walk's completion guard was corrected this request
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

The obligations this module deliberately leaves open are named in its own header and kept
there: the mounted-browser structural and visual review, and R25's assembled acceptance, belong to other
owners — the live walk's proof lives in enclosure `260921-icr-l31b-ar` at commit `5f14fc67`, not here.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no entries).
The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the module's own statement of what it
exercises and of what it does not claim, the four pieces of its harness, the captured bodies it reads, and
each of the twenty-two cases by its own name. Every anchor in a row below occurs on a line inside the range
that row cites; the anchor of a case row is that case's own `it(...)` name, which occurs on the line that
opens the case.

- **The module's own statement that this is `ICR-R24@v3` at the mounted surface: the family tree, the unified central reading path, the complete source explorer and the one family-roster walk control.** [1]
- **Real component and real client, with only `fetch` stubbed, and the header's provenance: the two captures recorded in the receipt (the MIK-L31 re-capture, `mik_l31_recapture`), and the one case labelled SYNTHETIC as the only assembled body.** [2]
- What these cases catch, including the two ways a repair could lie. [3]
- **What they do not claim: not browser evidence, Dagger-only Playwright configs, and a live publication explicitly out of scope.** [4]
- The two collection constants the walk case pins, and the captured refusal body the no-family-context case mounts. [5]
- The three task identifiers and the seven captured bodies, read from the capture directory. [6]
- The loader that resolves a capture from this file's own directory rather than the process cwd. [7]
- The runtime narrowing that finds a family subject in a captured body and throws rather than mounting under a wrong one. [8]
- The typed refusal the explorer's reads are answered with, so no case asserts on a file's bytes. [9]
- The one stubbed `fetch` for the whole surface: it records the URLs, routes `/source-content` to the refusal, and answers the rest with the captured queue in order. [10]
- The test mount opens the real surface with the fixture task and selected subject context. [11]
- The teardown cleans the mounted tree and restores stubbed globals. [12]
- The one `describe` every case below lives in, including the MIK-L31 real-body and synthetic roster cases. [13]
- Case 1: the recorded families, their authored guarantees, the full member statements with unchanged siblings included, the recorded sharing, and the opener on every member row. [14]
- Case 2: a guarantee comparison is drawn in the shape the two recorded revisions support — the same revision on both snapshots versus two different ones. [15]
- Case 3: a member's review keeps its family, and statement, membership, source attribution and authored judgment are five separate facts. [16]
- Case 4: the complete source explorer is independent of the family selection. [17]
- **Case 5: a roster walks only from the cursor that family's own page published, and the collection picker offers no option that would fetch a refusal.** [18]
- Case 6: a body with no family context is rendered as that fact and never as a measured zero. [19]
- Case 7: an expanded entry stays expanded across a diff-layout switch, and full-file is one value shared by the explorer and the centre. [20]
- Case 8: the current selection is exposed on the tree and arrow keys traverse the one roving-focus group. [21]
- Case 9: the filter reports its own scope, keeps a matched family's members, and states that the composed contexts are unchanged when nothing matches. [22]
- **MIK-L31: a bounded roster page over the real re-captured body states the part of the measured rows it carried, never zero.** [23]
- **Fix round 1, direction one, kept by ruling Q3 over a labelled SYNTHETIC body: a bounded roster that carried none of the rows it measured says so, and never that the read measured zero.** [24]
- **Fix round 1, direction two: the measured zero is said only where the read really measured zero memberships.** [25]
- **Fix round 1: a bounded member context is headed partial, its counts are the owner's rows with the loaded count read from the body (below 4), and the centre's continuation control is clicked and its request asserted.** [26]
- **Fix round 1, as MIK-R31 rule 3 renders it: two distinct revisions carrying identical text are "Wording unchanged" with both revisions named, the guarantee once, never one unchanged revision.** [27]
- **Fix round 1: a member whose content the page did not carry is stated as that, not as a one-sided statement.** [28]
- Uncarried roster content is not converted into an absent primary statement. [29]
- Bounded before-only membership remains context and does not assert invariant removal. [30]
- **Fix round 1, over the measured-empty body since MIK-L31: the centre's empty-roster line is the tree's own string for the same family — one implementation mounted twice.** [31]
- **Fix round 3: the page that completes a multi-page walk is stated as the walk's last page, never as the whole roster; since MIK-L31 its carried count is read from the body.** [32]
- **Fix round 5, V10: all five workspace values survive two page requests issued by the centre's own continuation control, and exactly three request URLs are seen.** [33]
- **260921-ICR-L25, register B3: the narrow jump route is composed ABOVE the family tree and the tree is intact — the case pins document order (`DOCUMENT_POSITION_FOLLOWING`), that both families and their member rows are still rendered, and that activating the control focuses the centre column. It pins composition rather than a pixel, because a jsdom render has no layout and the pixels are the mounted capture's job.** [34]
- **260921-ICR-L36 (fix round included): the family's rendered excerpt collection is the body's DISTINCT excerpt set and not its changed-row count, every row's `data-collapsed-rows` is one of the body's group sizes, every divergent excerpt's `data-sides` and per-side reading strings match the body's, and EVERY rendered row's `data-sides` equals the sides the body resolves it on. The predicate is divergence of the reading (distinct resolution sets across sides), not "seen on two sides".** [35]
- **The arithmetic that case's expectation is read from, deliberately written in the case's module rather than imported from the component, so the assertion checks the body and not the implementation it tests. It computes the excerpt key the fixed module uses (`path \0 recorded`), the per-side resolution sets the divergent predicate compares, and the side list every rendered row is checked against.** [36]
- The shared empty-roster function distinguishes absent family revisions, measured zero and page-local missing rows. [37]
- The owner of the completion sentence: `complete` is the read walk's flag, so a one-page walk is the whole selection while a final page is only its last position. [38]
- The tree's own roster line, whose test id the centre re-mounts under its own name. [39]
- The tree's own continuation control, which publishes the cursor it was given and is the component the centre mounts a second time (since MIK-L33 it also names its family, `data-family-label`). [40]
- The central empty-roster presentation reuses the tree-owned sentence and preserves the page scope. [41]
- The centre's bounded member-context heading and counts, decided from the read owner's own counts and the pages' completeness. [42]
- Roster revision content and authoritative selected-subject statements remain separate rendering responsibilities. [43]
- **The server-side rule the walk case pins: `family_members` is in the paged union because the server accepts it, and deliberately not among the walkable collections, because that collection is the set of per-family walks and a cursor-less request earns the server's own refusal.** [44]
- The one page request type a roster continuation builds. [45]
- The source explorer retains the complete inventory independently of semantic selection. [46]
- The workspace hook preserves display state and the source opener needed for focus return. [47]

### Cross-Repo References

No cross-repository behavior is exercised here. The module mounts one repository namespace's surface over
one enclosure's captured bodies and carries no identity that ranges beyond it.

No meaningful cross-repo references found.
