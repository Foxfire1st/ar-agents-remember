# dashboard/src/panels/review/ReviewSurface.navigation.test.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

Ordinary-entry navigation through the real shared catalogue and comparison clients, and the acceptance module for what happens **between** a selection and its answer: the mounted reviewer, the subject-bound pending and problem states, per-comparison reuse, the latest selection winning, focus the reader moved, a late catalogue, and the order in which a selection's focus request is answered. Only `fetch` is stubbed; the cases mount the real `ReviewSurface`.

The file holds 11 `it` blocks, one of them an `it.each` over a failed and a refused read.

## Code Commentary

### The cases

The first two cases answer immediately and prove eventual content:

- **Ordinary entry**: the fetched catalogue opens a recorded family, another family is selected in the same workspace, and the full source population, the display preferences and focus are kept. The case waits for its focus assertion, because selection focus is applied in a passive effect.
- **Unreadable knowledge** stays source-only, with no invented family and no prompt to select one.

The next cases run against `delayedServer`, which answers the catalogue and source content at once (or holds the catalogue on request) but holds every review reply until the case releases it: answered, refused by the owner, or lost in transport.

- **Mounted across family → invariant → family**: the workspace, navigation, family tree and open disclosures are the same DOM nodes throughout; only the reading area shows `review-reading-pending`, labelled with the requested subject; nothing of the previous subject appears under the new one; returning to a subject already read issues no review and no content request. At its end the case asserts the walked tree: the invariant's review showed further families, and after the first family's row is selected again those families are still in the tree, each marked `data-family-kept` and tagged "kept · last read for invariant …" with the invariant's label, while the selected family carries no such mark.
- **Latest of rapid selections**: A → B → C settles on C; a superseded answer is neither shown nor kept, so choosing B again asks again.
- **Late catalogue, reader working and reader idle** (two cases): after the bounded wait, an engaged reader is not moved; an idle reader lands on the first family without a remount.
- **The task-context answer the bounded wait released** is kept when the catalogue answers before it, and "All source changes" later reuses it without another request.
- **Failed and refused selection** (`it.each`): the shell stays mounted with its complete source explorer, and exactly one owner block is shown in the reading area, labelled with the requested subject. Retry asks for that subject again after a failure; after a refusal another subject is chosen directly.
- **Moved focus**: focus the reader moved while the subject was pending is kept when the answer lands, and a reader who stayed on the selecting control still lands on the selected node.

The last two cases force an order a loaded machine produces on its own: the reader selects again in the turn in which the previous answer's commit becomes visible, before React has run that commit's passive effects. A late effect of the earlier render must leave the new selection's focus request alone (`FocusRequest.after` in `ReviewWorkspace.tsx`).

- **By pointer**: the second family is clicked inside the wait that first sees the first family. Focus must land on the row the tree marks as the selection, which is the second family's row, and not on the page body.
- **By key**: on the real-data world of `walk.test-utils.tsx` (family FAM-R6R095RW with seven changes), a mutation observer presses `j` in the first microtask in which the first change's answer is shown. The second change must be selected with focus on its row, and a third press must reach the third change, so no press is lost.

### Conventions

- Semantic content comes from `familyReview.complete.captured.json`, which the file reads itself; the last case uses the world and the readers of `walk.test-utils.tsx` (`serveWorld`, `open`, `press`, `selectedNode`, `selectedName`).
- Request counts (`reviewReads`, `contentReads`, `catalogueReads`) are the module's measure of reuse.
- Async conditions use the shared Testing Library guard from `src/test/setup.ts`; test and hook hang guards come from `vitest.config.ts`. Product hold cases advance the imported `SUBJECT_HOLD_MS` on fake time and flush held replies in async `act`. These guards bound a hang; they assert no host speed.

### Boundaries

- The cases are scoped executable evidence. They do not certify the mounted product journey in a browser.
- jsdom has no layout engine. The rail's `scrollTop` retention these cases assert holds while a subject is pending; scroll position after an answer is not claimed here.

## Evidence

- The module's own statement of what it pins, why its replies are held, and what the two forced-order cases force. [8]
- The held-reply server: every review reply can be answered, refused or lost; catalogue and content reads are counted. [9]
- Mounted shell, subject-labelled pending area, zero-request return, and the families of the invariant's review kept and tagged after the first family is selected again. [10]
- Latest selection wins; a superseded answer is not kept. [11]
- Late catalogue with and without reader engagement. [12]
- The released task-context answer is kept and reused. [13]
- Failed or refused selection stated in the reading area for the requested subject. [14]
- Focus the reader moved while pending is kept. [15]
- Forced order by pointer: focus lands on the family chosen before the previous answer's effects have run. [16]
- Forced order by key: every `j` pressed in that turn is kept and focus lands on each selected row. [17]
- The guard the forced-order cases pin. [18]
- The real-data world the key case is served from. [19]
