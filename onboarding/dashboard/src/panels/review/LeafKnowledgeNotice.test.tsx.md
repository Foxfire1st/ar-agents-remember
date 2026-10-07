# dashboard/src/panels/review/LeafKnowledgeNotice.test.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

Tests of `LeafKnowledgeNotice` in `LeafKnowledgeChanges.tsx`: what the knowledge panel's place shows while
the leaf-wide tree read has no tree answer.

## Code Commentary

### Component cases

Each of the three component cases renders `LeafKnowledgeNotice` alone with one read state.

- "says that it is computing": for `loading`, the element with the test ID
  `review-leaf-knowledge-computing` contains "Computing the knowledge changes" and has the role `status`.
- "names the failure and its action when the read is unavailable": for `unavailable` with a
  `reviewer_busy` problem, the element with the test ID `review-leaf-knowledge-unavailable` contains
  "are unavailable: the reviewer is computing other worklists" and ends the action with "retry.".
- "draws nothing for a dataset review": for `not-converted` the rendered text is empty.

### Mounted surface cases

Two cases — one with a family selection, one with an invariant selection — mount the real
`ReviewSurface` with captured family/invariant payloads and a `fetch` stub whose plain `/trees`
request is held open. Each proves the held read is visible through the centre's status node (role
`status`, "Computing the knowledge changes", no closed `details` ancestor), then resolves the held
request with a refused `candidate_unresolved` answer and proves the same status node now reads "are
unavailable" and the centre shows the failure's "Restart the dashboard." next action — status
continuity from held read to final failure, not a fresh notice.

### Limits

This is mounted jsdom evidence of the notice and its status-node continuity. It is not browser,
screen-reader or completion-announcement proof, and it does not prove the accepted A1 completion
limit.

## Evidence

- The loading notice and its status role. [1]
- The unavailable notice with detail and action. [2]
- Nothing for a dataset review. [3]
- The component under test. [4]
- The held read and its final failure through the mounted surface, for both selections. [5]
