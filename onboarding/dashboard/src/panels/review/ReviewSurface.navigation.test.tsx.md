# dashboard/src/panels/review/ReviewSurface.navigation.test.tsx

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Held-reply navigation controls keep one mounted shell, exact subject slots, request reuse and current generation facts through explicit selections.

## Code Commentary

### Logic

- Ordinary entry reads task context once with no selectorId and no selected subject slot; only explicit family/member clicks select content. Unreadable knowledge draws source-only lane content with no invented subject or select prompt, and unavailable counts are stated as reasons rather than numeric values.
- Delayed family → invariant → cached family keeps the workspace, tree, column, family rows, open Technical details, selection focus and assigned tree scroll. Pending names only the requested subject and removes stale reading/comparison metadata. A cached return makes no review/content request, and independently read family B remains tagged kept.
- Rapid A → B → C answers settle only C; a superseded B answer is dropped and selecting B again reads again. Failed/refused subjects stay labelled unavailable in their own slot with one relevant problem, while shell rows remain usable. Retry asks the failed subject; returning from refusal to cached A needs no read.
- A controlled catalogue answers either before or after task context while the reader works in the filter. It fills the tree without selection, focus movement, remount or a second opening review; an explicit family click supplies the second review. There is no SUBJECT_HOLD_MS or idle-reader bound in these cases.
- Pointer and MutationObserver/key sequences force another choice before the prior answer passive effects. Focus lands on the latest family or reading-block row. Three j presses select three changed blocks, two for one invariant and one for another, with only task context and those two invariant reviews.
- The synthetic shared world keeps two family occurrences visible; repeated row clicks switch the selected family occurrence with one invariant read. A URL hash selection restores that exact family occurrence after unmount/remount.
- Memory/code generation changes quarantine old outline labels, summaries and rows until a matching catalogue arrives. A failed reread states its exact reason without reviving old rows; a superseded late catalogue cannot replace the newest matching generation. Release of matching facts preserves workspace/focus and adds no request.

### Invariants And Boundaries

The real page and client run over held captured replies, synthetic catalogue/outline facts and explicit generation perturbations. Assertions inspect requests, DOM identity, focus and assigned scroll state. This read-only pass did not execute tests or certify browser geometry, native producer output or elapsed host speed.

## Evidence

- Declared check and its fixture assertions. [25]
- Declared check and its fixture assertions. [26]
- Declared check and its fixture assertions. [27]
- Declared check and its fixture assertions. [28]
- Declared check and its fixture assertions. [29]
- Declared check and its fixture assertions. [30]
- Declared check and its fixture assertions. [31]
- Declared check and its fixture assertions. [32]
- Declared check and its fixture assertions. [33]
- Declared check and its fixture assertions. [34]
- Declared check and its fixture assertions. [35]
- Declared check and its fixture assertions. [36]
- Declared check and its fixture assertions. [37]
- Declared check and its fixture assertions. [38]

## Historical predecessor account

The earlier account follows as provenance. Current assertions and removed journeys are described above.

> # dashboard/src/panels/review/ReviewSurface.navigation.test.tsx
>
> ## Governing Overview
>
> [dashboard/src/panels route overview](overview.md)
>
> ## Purpose
>
> Ordinary-entry navigation through the real shared catalogue and comparison clients, and the acceptance module for what happens **between** a selection and its answer: the mounted reviewer, the subject-bound pending and problem states, per-comparison reuse, the latest selection winning, focus the reader moved, a late catalogue, and the order in which a selection's focus request is answered. Only `fetch` is stubbed; the cases mount the real `ReviewSurface`.
>
> The current file contains 15 test declarations, including the failed/refused and memory/code-generation `it.each` blocks. Declaration counts are static source facts, not execution results.
>
> ## Code Commentary
>
> ### The cases
>
> The first two cases answer immediately and prove eventual content:
>
> - **Ordinary entry:** the synthetic catalogue opens a captured family, another family is selected without remounting the workspace, display preferences remain and focus lands as asserted. The case explicitly asserts that no source explorer is mounted; it does not assert a rendered full inline source population.
> - **Unreadable knowledge** stays source-only, with no invented family and no prompt to select one.
>
> The next cases run against `delayedServer`, which answers the catalogue and source content at once (or holds the catalogue on request) but holds every review reply until the case releases it: answered, refused by the owner, or lost in transport.
>
> - **Mounted across family → invariant → family:** subject-bound pending output excludes stale reading/binding/currentness content while the workspace, navigation, centre, selected row, open provenance disclosure, focus and rail scroll are retained. A cached return makes no new review or content read. B is read independently before returning to cached A. After the invariant → A return, B remains `data-family-kept=true` with the visible tag `kept`; selected A is not marked kept.
> - **Latest of rapid selections**: A → B → C settles on C; a superseded answer is neither shown nor kept, so choosing B again asks again.
> - **Late catalogue, reader working and reader idle** (two cases): after the bounded wait, an engaged reader is not moved; an idle reader is not moved either — the late catalogue fills the navigation and selects nothing, the open keeps its single task-context read, and the reader's own click is the second read, with no remount.
> - **Late task-context answer:** a subjectless read released by the bounded wait can complete after the selected family, without replacing that family's reading; this case does not later click All changes to assert task-answer reuse.
> - **Failed/refused selection:** one subject-labelled problem is shown while shell/navigation rows remain mounted; stale selection/binding/currentness output is absent. Failure Retry asks the same subject again, while a refused selection can return to an already read family without another review.
> - **Moved focus**: focus the reader moved while the subject was pending is kept when the answer lands, and a reader who stayed on the selecting control still lands on the selected node.
>
> The last two cases force an order a loaded machine produces on its own: the reader selects again in the turn in which the previous answer's commit becomes visible, before React has run that commit's passive effects. A late effect of the earlier render must leave the new selection's focus request alone (`FocusRequest.after` in `ReviewWorkspace.tsx`).
>
> - **By pointer**: the second family is clicked inside the wait that first sees the first family. Focus must land on the row the tree marks as the selection, which is the second family's row, and not on the page body.
> - **By key**: using independent captures for two members of A and B's guarantee, a mutation observer presses `j` in the first microtask in which the first member's answer is shown. The second member must be selected with focus on its row, and a third press must reach B's guarantee, so no press is lost.
>
> ### Conventions
>
> - Semantic replies come from independently selected captures loaded through `currentCapture`; catalogue and outline facts are explicitly synthetic. The forced-key case imports `J`, `press` and `selectedNode` from `walk.test-utils.tsx` and serves its own captured selector replies.
> - Request counts (`reviewReads`, `contentReads`, `catalogueReads`) are the module's measure of reuse.
> - Async conditions use the shared Testing Library guard from `src/test/setup.ts`; test and hook hang guards come from `vitest.config.ts`. Product hold cases advance the imported `SUBJECT_HOLD_MS` on fake time and flush held replies in async `act`. These guards bound a hang; they assert no host speed.
>
> ### Boundaries
>
> - The cases are scoped executable evidence. They do not certify the mounted product journey in a browser.
> - jsdom has no layout engine. The rail's `scrollTop` retention these cases assert holds while a subject is pending; scroll position after an answer is not claimed here.
>
> The retained fetch-replay worlds measure request counts, selected DOM/focus and assigned scroll state, not a complete rendered source explorer. Added synthetic worlds assert two distinct shared-member occurrences reached by `j`/`k` and next/previous controls with one invariant read, plus old-generation outline quarantine, unavailable rereads and ignored superseded late catalogue answers for memory/code-generation changes.
> ## Evidence
>
> - The module's own statement of what it pins, why its replies are held, and what the two forced-order cases force. (historical reference 8)
> - The held-reply server: every review reply can be answered, refused or lost; catalogue and content reads are counted. (historical reference 9)
> - Latest selection wins; a superseded answer is not kept. (historical reference 11)
> - Late catalogue with and without reader engagement. (historical reference 12)
> - Failed or refused selection stated in the reading area for the requested subject. (historical reference 14)
> - Focus the reader moved while pending is kept. (historical reference 15)
> - Forced order by pointer: focus lands on the family chosen before the previous answer's effects have run. (historical reference 16)
> - Forced order by key: every `j` pressed in that turn is kept and focus lands on each selected row. (historical reference 17)
> - The guard the forced-order cases pin. (historical reference 18)
> - Shared-member world with outline and families (historical reference 20)
> - Outline reply with auxiliary refusal for the shared world (historical reference 21)
> - Mount of the shared world with request capture (historical reference 22)
> - Held next-catalogue with releases for late answers (historical reference 24)
>
> - B is independently read before cached A is restored; the later invariant-to-A return makes no review/content read and leaves B tagged kept. (historical reference 10)
> - The delivered late task-context reply does not displace the selected family. This case does not assert later task-answer reuse. (historical reference 13)
> - The forced-key case serves independent captured member and family selector answers; walk utilities supply keyboard and selection helpers. (historical reference 19)
> - Generation inputs begin with current family content and synthetic outline facts, then perturb comparison or code generation and outline content independently of sharedNavigationWorld. (historical reference 23)
