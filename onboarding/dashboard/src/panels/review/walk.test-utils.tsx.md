# dashboard/src/panels/review/walk.test-utils.tsx

## Governing Overview

[Review route overview](overview.md)

## Purpose

Supply captured-body worlds, request logging and mounted-review readers for the walked-tree tests. `ReviewSurface` is the real mounted component and fetch is stubbed. The catalogue still uses its explicitly synthetic outline adapter; that augmentation does not alter the original capture files.

## Code Commentary

`bodyFor` serves catalogue entries, explicitly refuses the uncaptured summary through `SUMMARY_REFUSED`, and delegates review requests to the supplied world. Tree/source-content replies prefer a non-nullish custom tree answer; otherwise only an unscoped trees request gets the matching captured leaf-wide tree body, with remaining tree/source-content requests refused. `serve` logs all requests, rejects undefined or Error answers and structured-clones successful bodies. `reviews()` counts only `/api/review/intent`, so summary/catalogue requests are not selected-review requests.

The retained real-data world supplies task, two family and seven changed-member bodies. `open` supplies the body's selected kind/id to `ReviewSurface`; this is an explicit test target, not an assertion that an ordinary newly opened page automatically selects a subject. `labelBySubject`, `subjectOfLabel`, `selectedName` and `memberRow` now identify invariant subjects, not revision rows. The selected node is read from `review-tree`; the selected subject's reading is reached through `slotOf` and `review-subject-slot`.

`serveWorld` clears preferences, sets order to priority and view to all, resets the world and installs the logged stub. `installWorld` runs that setup before each test and cleans up the mounted view and global stub afterward. It defines no local timeout or hang-guard policy.

`settled` waits for no pending selected read, a selected node and focus on that node. `step` retries only the first press until the binding takes effect, then sends each later press once; it waits for the selection or status effect, settling and the exact expected selected-review request delta. No elapsed-time wait is added. `clickedSecondFamily` waits for the expected two-family order, opens the second family and waits for its selected review and settling.

## Invariants And Boundaries

This is fixture and journey support, not a new product invariant or execution result. The deliberately unavailable summary is distinct from measured zero.

The stored public-route receipt records the fixtures' producer, raw-response capture provenance and limitations. It remains evidence of those historical fixture bytes, rather than a new capture or production-writer result on this candidate.

## Evidence

- The fetch stub logs requests, clones answers and fails unexpected or transport-error replies; bodyFor owns route selection. [1]
- The retained changed-member sequence and captured subject bodies feed the default world. [2]
- The per-test world retains mutable answer, tree and entries plus the request log. [3]
- World setup clears preferences and resets priority order, all view and served responses. [4]
- Per-file installation resets before each test and cleans up the mounted view and global stub afterward. [5]
- Exactly one current tree node is read from review-tree, not the removed review-family-tree mount. [6]
- Settling waits for a nonpending selected response and then focus on its selected tree node. [7]
- A key press waits for its selection/status effect and exact selected-review request delta. [8]
- The second-family helper waits for order, opens the second family and awaits its review. [9]
- bodyFor preserves non-nullish custom tree priority and unscoped captured leaf-wide fallback; serve keeps logging, cloning and failure behavior. [11]
- Default world inputs keep the captured entries, leaf-wide trees, task and seven changed-member sequence. [12]
- Reset order is now priority and tree view remains all. [13]
- Suite installation has setup and cleanup, with no locally declared timeout. [14]
- The selected-node reader targets the new review-tree mount and current aria-current nodes. [15]
- Single later presses retain asserted selected-review request counts. [16]
- The summary route returns an explicitly unavailable response, never fabricated measured-zero summary counts. [17]
- Opening a helper journey supplies its selected kind/id explicitly from that captured body. [18]
- Member selection uses invariant IDs and the selected subject has its own review-subject-slot. [19]
- The stored public-route capture receipt names raw response provenance and fixture limitations; it is historical producer evidence, not a fresh run of this candidate. [10]

## Historical predecessor account

The former account is retained below as provenance. Removed exports, old restoration fields and old test-world identities are historical where the current account differs; earlier execution statements are not fresh results.

> # dashboard/src/panels/review/walk.test-utils.tsx
>
> ## Governing Overview
>
> [dashboard/src/panels route overview](../overview.md)
>
> ## Purpose
>
> The shared kit of the mounted walked-tree tests (`ReviewSurface.walk.test.tsx`, `ReviewSurface.walkFresh.test.tsx`, `ReviewSurface.walkPartial.test.tsx`, `ReviewSurface.walkStore.test.tsx`), also used by `walkedTree.test.ts` and by the key case at the end of `ReviewSurface.navigation.test.tsx`. It provides a served world made of captured bodies, a `fetch` stub that answers from it and logs every request, and small readers of the mounted reviewer. `ReviewSurface` is the real component; only `fetch` is stubbed.
>
> Serve the mounted walked-tree tests (`ReviewSurface.walk*.test.tsx`, `walkedTree.test.ts` and the navigation key case): a served world made of captured bodies, a `fetch` stub that answers from it and logs every request, and small readers of the mounted reviewer. `ReviewSurface` is the real component; only `fetch` is stubbed, and the old catalogue is augmented with the explicit synthetic outline adapter while every original capture keeps its bytes.
> ## Code Commentary
>
> ### Serving
>
> - `captured(name)` reads and parses a JSON file that lies beside the test file.
> - `serve(world)` stubs `fetch`. A request whose path ends in `/entries` gets `world.entries`; one ending in `/trees` or `/source-content` first uses a non-nullish `world.tree(url)` answer. Otherwise, a `/trees` request without `lane`, `file` or `invariants` query keys gets the captured leaf-wide tree answer; other tree or source-content requests get the typed `REFUSED` body; every other request is a review request and gets `world.review(url)`. An answer of `undefined` throws ("Unexpected review request"), and an `Error` value is thrown as a transport failure. Each answer is a `structuredClone` of the body, because the reviewer tells answers apart by identity. The function returns the request log: `all`, and `reviews()`, the requests to `/api/review/intent`.
> - `world` is the mutable description of what the test in progress serves: `answer`, `tree`, `entries` and the `requests` log. `serveWorld()` clears `localStorage`, sets the tree order to `triage`, resets the world to the real-data bodies and stubs `fetch`. `installWorld()` runs `serveWorld` before each test, then cleans up and removes the stub after each. The common Testing Library and Vitest setup owns hang guards.
> - `reviewCount()` is the number of review requests of the test in progress.
>
> ### The real-data world
>
> The default world is the served answers of the scratch leaf 260928-MIK-L33 (`walkReal.capture-provenance.json`): the catalogue, the leaf-wide tree answer (`walkReal.trees.captured.json`), the task-context answer, the reviews of the families FAM-R6R095RW (`R6R`) and FAM-2HBJREC2 (`HBJ`), and the reviews of the seven changed members of FAM-R6R095RW. `CHANGES` lists those seven in the order `j` visits them; the last, INV-2TQGXFAX (`SHARED`), belongs to both families. `R6R_ID`, `HBJ_ID`, `R6R_TITLE` and `HBJ_TITLE` are the families' identifiers and labels as the bodies carry them. `bodyOf(name)` loads any body of the set.
>
> ### Readers and steps
>
> - `open(subject)` mounts `ReviewSurface` on the subject of a body. `View` is its result type.
> - `families(view)` lists the family identifiers of the tree in displayed order; `familyBlock` returns one family's block; `memberOccurrences` counts the distinct members a block shows; `keptTags` returns the texts of the kept tags.
> - `selectedNode(view)` returns the one tree node marked `aria-current`, and fails when more than one is marked. `selectedName` names it by the member's label or as `family <id>`. `revisionOf(label)` gives the revision identifier of a member by its label.
> - `triageStatus(view)` reads the traversal's status text.
> - `press(key)` sends a key to the focused element (`J`, `K`).
> - `settled(view)` waits until no read is pending, a node is selected, and focus is on the selected node.
> - `step(view, key, requestsMade)` makes one key press and waits for its effect (a new selection mark or a new status), then for `settled`, then until the press has made exactly `requestsMade` review requests. The first press on a view is made again until it takes effect, because the keymap's binding is a passive effect; every later press is made once, so a press the reviewer drops fails the step. Nothing in it waits for time.
> - `clickedSecondFamily(view, shown)` waits until the tree shows the two families in the order `shown` (the first family before the second by default), clicks the second family's own row, and waits until its family review is shown and settled.
>
> ## Evidence
>
> - The real-data world: the changes in `j` order and the bodies by subject. (historical reference 2)
> - The mutable world of the test in progress. (historical reference 3)
> - Serving the world to one test, with the triage order and a clean preference store. (historical reference 4)
>
> - Serving the world to every test of a file and cleaning up the mounted view and transport stub. (historical reference 5)
> - The one selected node, as the reader sees it. (historical reference 6)
>
> - Settled: no pending read, a selected node, focus on it. (historical reference 7)
>
>
> - One key press, its effect, and the review requests it made. (historical reference 8)
>
>
> - The click on the second family's row after both families are shown in the expected order. (historical reference 9)
>
> - The receipt of the real-data bodies. (historical reference 10)
> - Per-test world with triage order and tree view reset (historical reference 13)
> - Suite installation with timeout and cleanup (historical reference 14)
> - Mounted-surface readers of the tree (historical reference 15)
> - Single presses with asserted request counts (historical reference 16)
>
> - serve logs requests, prioritizes non-nullish custom tree replies, supplies the captured leaf-wide answer only for unscoped /trees requests, refuses other unanswered tree/source-content requests, and clones answers. (historical reference 1)
> - The fetch stub preserves custom tree-answer priority, adds the unscoped leaf-wide captured reply, retains scoped/source-content refusal, and preserves request logging, cloning and unexpected-review failures. (historical reference 11)
> - The default real-data world includes the captured leaf-wide tree reply alongside the catalogue, task and review bodies; preserve the existing CHANGES target. (historical reference 12)
