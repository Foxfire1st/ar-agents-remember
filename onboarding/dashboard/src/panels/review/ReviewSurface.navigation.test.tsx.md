# dashboard/src/panels/review/ReviewSurface.navigation.test.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

Ordinary-entry navigation through the real shared catalogue and comparison clients, and the acceptance module for what happens **between** a selection and its answer: the mounted reviewer, the subject-bound pending and problem states, per-comparison reuse, the latest selection winning, focus the reader moved, a late catalogue, and the order in which a selection's focus request is answered. Only `fetch` is stubbed; the cases mount the real `ReviewSurface`.

The current file contains 15 test declarations, including the failed/refused and memory/code-generation `it.each` blocks. Declaration counts are static source facts, not execution results.

## Code Commentary

### The cases

The first two cases answer immediately and prove eventual content:

- **Ordinary entry:** the synthetic catalogue opens a captured family, another family is selected without remounting the workspace, display preferences remain and focus lands as asserted. The case explicitly asserts that no source explorer is mounted; it does not assert a rendered full inline source population.
- **Unreadable knowledge** stays source-only, with no invented family and no prompt to select one.

The next cases run against `delayedServer`, which answers the catalogue and source content at once (or holds the catalogue on request) but holds every review reply until the case releases it: answered, refused by the owner, or lost in transport.

- **Mounted across family → invariant → family:** subject-bound pending output excludes stale reading/binding/currentness content while the workspace, navigation, centre, selected row, open provenance disclosure, focus and rail scroll are retained. A cached return makes no new review or content read. B is read independently before returning to cached A. After the invariant → A return, B remains `data-family-kept=true` with the visible tag `kept`; selected A is not marked kept.
- **Latest of rapid selections**: A → B → C settles on C; a superseded answer is neither shown nor kept, so choosing B again asks again.
- **Late catalogue, reader working and reader idle** (two cases): after the bounded wait, an engaged reader is not moved; an idle reader lands on the first family without a remount.
- **Late task-context answer:** a subjectless read released by the bounded wait can complete after the selected family, without replacing that family's reading; this case does not later click All changes to assert task-answer reuse.
- **Failed/refused selection:** one subject-labelled problem is shown while shell/navigation rows remain mounted; stale selection/binding/currentness output is absent. Failure Retry asks the same subject again, while a refused selection can return to an already read family without another review.
- **Moved focus**: focus the reader moved while the subject was pending is kept when the answer lands, and a reader who stayed on the selecting control still lands on the selected node.

The last two cases force an order a loaded machine produces on its own: the reader selects again in the turn in which the previous answer's commit becomes visible, before React has run that commit's passive effects. A late effect of the earlier render must leave the new selection's focus request alone (`FocusRequest.after` in `ReviewWorkspace.tsx`).

- **By pointer**: the second family is clicked inside the wait that first sees the first family. Focus must land on the row the tree marks as the selection, which is the second family's row, and not on the page body.
- **By key**: using independent captures for two members of A and B's guarantee, a mutation observer presses `j` in the first microtask in which the first member's answer is shown. The second member must be selected with focus on its row, and a third press must reach B's guarantee, so no press is lost.

### Conventions

- Semantic replies come from independently selected captures loaded through `currentCapture`; catalogue and outline facts are explicitly synthetic. The forced-key case imports `J`, `press` and `selectedNode` from `walk.test-utils.tsx` and serves its own captured selector replies.
- Request counts (`reviewReads`, `contentReads`, `catalogueReads`) are the module's measure of reuse.
- Async conditions use the shared Testing Library guard from `src/test/setup.ts`; test and hook hang guards come from `vitest.config.ts`. Product hold cases advance the imported `SUBJECT_HOLD_MS` on fake time and flush held replies in async `act`. These guards bound a hang; they assert no host speed.

### Boundaries

- The cases are scoped executable evidence. They do not certify the mounted product journey in a browser.
- jsdom has no layout engine. The rail's `scrollTop` retention these cases assert holds while a subject is pending; scroll position after an answer is not claimed here.

The retained fetch-replay worlds measure request counts, selected DOM/focus and assigned scroll state, not a complete rendered source explorer. Added synthetic worlds assert two distinct shared-member occurrences reached by `j`/`k` and next/previous controls with one invariant read, plus old-generation outline quarantine, unavailable rereads and ignored superseded late catalogue answers for memory/code-generation changes.
## Evidence

- The module's own statement of what it pins, why its replies are held, and what the two forced-order cases force. [8]
- The held-reply server: every review reply can be answered, refused or lost; catalogue and content reads are counted. [9]
- Latest selection wins; a superseded answer is not kept. [11]
- Late catalogue with and without reader engagement. [12]
- Failed or refused selection stated in the reading area for the requested subject. [14]
- Focus the reader moved while pending is kept. [15]
- Forced order by pointer: focus lands on the family chosen before the previous answer's effects have run. [16]
- Forced order by key: every `j` pressed in that turn is kept and focus lands on each selected row. [17]
- The guard the forced-order cases pin. [18]
- Shared-member world with outline and families [20]
- Outline reply with auxiliary refusal for the shared world [21]
- Mount of the shared world with request capture [22]
- Held next-catalogue with releases for late answers [24]

- B is independently read before cached A is restored; the later invariant-to-A return makes no review/content read and leaves B tagged kept. [10]
- The delivered late task-context reply does not displace the selected family. This case does not assert later task-answer reuse. [13]
- The forced-key case serves independent captured member and family selector answers; walk utilities supply keyboard and selection helpers. [19]
- Generation inputs begin with current family content and synthetic outline facts, then perturb comparison or code generation and outline content independently of sharedNavigationWorld. [23]
