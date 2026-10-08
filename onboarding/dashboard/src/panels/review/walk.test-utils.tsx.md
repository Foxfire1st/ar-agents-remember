# dashboard/src/panels/review/walk.test-utils.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The shared kit of the mounted walked-tree tests (`ReviewSurface.walk.test.tsx`, `ReviewSurface.walkFresh.test.tsx`, `ReviewSurface.walkPartial.test.tsx`, `ReviewSurface.walkStore.test.tsx`), also used by `walkedTree.test.ts` and by the key case at the end of `ReviewSurface.navigation.test.tsx`. It provides a served world made of captured bodies, a `fetch` stub that answers from it and logs every request, and small readers of the mounted reviewer. `ReviewSurface` is the real component; only `fetch` is stubbed.

## Code Commentary

### Serving

- `captured(name)` reads and parses a JSON file that lies beside the test file.
- `serve(world)` stubs `fetch`. A request whose path ends in `/entries` gets `world.entries`; one ending in `/trees` or `/source-content` gets `world.tree(url)`, or a typed refusal when the world has none; every other request is a review request and gets `world.review(url)`. An answer of `undefined` throws ("Unexpected review request"), and an `Error` value is thrown as a transport failure. Each answer is a `structuredClone` of the body, because the reviewer tells answers apart by identity. The function returns the request log: `all`, and `reviews()`, the requests to `/api/review/intent`.
- `world` is the mutable description of what the test in progress serves: `answer`, `tree`, `entries` and the `requests` log. `serveWorld()` clears `localStorage`, sets the tree order to `triage`, resets the world to the real-data bodies and stubs `fetch`. `installWorld()` runs `serveWorld` before each test, then cleans up and removes the stub after each. The common Testing Library and Vitest setup owns hang guards.
- `reviewCount()` is the number of review requests of the test in progress.

### The real-data world

The default world is the served answers of the scratch leaf 260928-MIK-L33 (`walkReal.capture-provenance.json`): the catalogue, the task-context answer, the reviews of the families FAM-R6R095RW (`R6R`) and FAM-2HBJREC2 (`HBJ`), and the reviews of the seven changed members of FAM-R6R095RW. `CHANGES` lists those seven in the order `j` visits them; the last, INV-2TQGXFAX (`SHARED`), belongs to both families. `R6R_ID`, `HBJ_ID`, `R6R_TITLE` and `HBJ_TITLE` are the families' identifiers and labels as the bodies carry them. `bodyOf(name)` loads any body of the set.

### Readers and steps

- `open(subject)` mounts `ReviewSurface` on the subject of a body. `View` is its result type.
- `families(view)` lists the family identifiers of the tree in displayed order; `familyBlock` returns one family's block; `memberOccurrences` counts the distinct members a block shows; `keptTags` returns the texts of the kept tags.
- `selectedNode(view)` returns the one tree node marked `aria-current`, and fails when more than one is marked. `selectedName` names it by the member's label or as `family <id>`. `revisionOf(label)` gives the revision identifier of a member by its label.
- `triageStatus(view)` reads the traversal's status text.
- `press(key)` sends a key to the focused element (`J`, `K`).
- `settled(view)` waits until no read is pending, a node is selected, and focus is on the selected node.
- `step(view, key, requestsMade)` makes one key press and waits for its effect (a new selection mark or a new status), then for `settled`, then until the press has made exactly `requestsMade` review requests. The first press on a view is made again until it takes effect, because the keymap's binding is a passive effect; every later press is made once, so a press the reviewer drops fails the step. Nothing in it waits for time.
- `clickedSecondFamily(view, shown)` waits until the tree shows the two families in the order `shown` (the first family before the second by default), clicks the second family's own row, and waits until its family review is shown and settled.

## Evidence

- The `fetch` stub: routes by path, clones each answer, and logs requests. [1]
- The real-data world: the changes in `j` order and the bodies by subject. [2]
- The mutable world of the test in progress. [3]
- Serving the world to one test, with the triage order and a clean preference store. [4]

- Serving the world to every test of a file and cleaning up the mounted view and transport stub. [5]
- The one selected node, as the reader sees it. [6]

- Settled: no pending read, a selected node, focus on it. [7]


- One key press, its effect, and the review requests it made. [8]


- The click on the second family's row after both families are shown in the expected order. [9]

- The receipt of the real-data bodies. [10]
