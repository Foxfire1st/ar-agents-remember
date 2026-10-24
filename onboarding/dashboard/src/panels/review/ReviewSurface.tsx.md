# dashboard/src/panels/review/ReviewSurface.tsx

## Governing Overview

[review route overview](overview.md)

## Purpose

Compose one review page from the comparison-bound change-set model, selected-subject read cycle, tree, reading column and existing full comparison viewer.

## Code Commentary

`useSurface` holds one mounted whole-review cache, current page request, task-context fallback and subject read cycle. A retained answer appears only when its complete question key matches; a same-task admitted frame keeps page-level content mounted while a new subject waits or fails. `readingStatusOf` labels that requested subject with its own key and owner problem block, so the frame does not become its statement or record answer. The catalogue is quarantined against the comparison of the answer/frame. The mounted live memory watch uses the existing cycle.

The surface holds its record frame through `useReviewHistory(initialHistory)`, so the frame the target named is state the page can leave: the delivered action clears it and the page reads its own default again. Page details receive the page's resolved comparison as their `latest` figure and the delivered value as their own fact line.

`useReviewPage` owns the page selection and comparison-bound opening reads/model. ReviewSurface composes the top line, ReviewGrid tree and ReadingColumn. The root is the review keyboard zone and publishes target/comparison/history/pending attributes; it does not own page scrolling. The reading column receives the shared model, local width-derived layout, selected-subject slots, lane hunks, summary, notes, generated page and Technical details. Worklist temporarily replaces the change set. Tree and chat sidebar toggles and bracket keys use their existing owners.

`useBlockTraversal` selects comparison-bound model blocks while the full comparison overlay is closed. The marker scope uses the comparison on screen: the resolved comparison uses the task frame's inventory, while an older comparison uses its own measured lane paths and stays partial until those are read. Marker moves pass through page selection with their explicit tree-retention choice. Canvas evidence navigation also checks the shown comparison reference/number before selecting the exact requested subject.

A refresh resets the walked intent and leaves a scroll-only request tied to the current intent number. If that refresh's own read fails/refuses, its request is discarded; retrying that failed refresh makes the same refresh request again. Retrying another failed read only re-reads. The task-context recovery offer is restricted to an intent-only refusal and goes through page selection without keeping the tree.

`useReviewChangePage` captures the full task, comparison generation/number, inventory, lane and matching worklist when opening the existing ChangeSetViewer. It admits lane/worklist enrichment only while task/number and sameGeneration still match; movement during a loading lane yields explicit comparison_context_changed, retaining the old page context. A missing recorded comparison yields comparison_not_recorded without a substitute range. While open, the mounted reviewer is hidden/inert and its traversal is disabled. Closing clears only overlay state and schedules opener focus return without a review request.

Page controls receive the actual shown answer in Technical details. They offer only the shared walkable collections, use only a published next cursor, distinguish whole-review/bounded-page text and retain reset/refusal code, expected/observed identities and first-page recovery. They do not infer a cursor from a remainder count.

## Evidence

- ReviewSurface.tsx current behavior at this source owner. [65]
- ReviewSurface.tsx current behavior at this source owner. [67]
- ReviewSurface.tsx current behavior at this source owner. [68]
- ReviewSurface.tsx current behavior at this source owner. [69]
- ReviewSurface.tsx current behavior at this source owner. [70]

- The record frame is state the surface can leave, and the delivered action uses that. [71]
- Page details receive the resolved comparison and the delivered value. [72]

ReviewSurface now owns a Review | Explanation tab in the page's top line and replaces only the reading-column body with ExplanationView or the planned page; the tree, chat rail, bracket controls and deterministic Review content keep their existing owners. The former CanvasRegion is removed. useSurfaceExplainer reads the applicable planned/explainer state, publishes its judgments to the shared model and resolves claim/evidence returns through the comparison on screen before selecting with keepTree. A matching live moved notice renews deterministic reads and entry generation when no explainer work exists or the event offers no Update; a recorded-history view does not subscribe to that refresh. The ordinary Review body receives judgment chips and Ungraded headings through ReadingJudgmentMounts, with cleanup owned by that mount.

- ReviewSurface now owns a Review \| Explanation tab in the page's top line and replaces only the reading-column body with ExplanationView or the planned page; the tree, chat rail, bracket controls and deterministic Review content keep their existing owners. The former CanvasRegion is removed. useSurfaceExplainer reads the applicable planned/explainer state, publishes its judgments to the shared model and resolves claim/evidence returns through the comparison on screen before selecting with keepTree. A matching live moved notice renews deterministic reads and entry generation when no explainer work exists or the event offers no Update; a recorded-history view does not subscribe to that refresh. The ordinary Review body receives judgment chips and Ungraded headings through ReadingJudgmentMounts, with cleanup owned by that mount. [73]

- PageReading keeps the existing reading-column toggles, notes, summary, lane and technical details, replaces its body through readingReplacementOf and mounts judgment chips only for ordinary Review content. [66]
