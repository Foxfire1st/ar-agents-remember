# dashboard/src/cockpit/reviewHash.ts

## Governing Overview

[Owning route overview](../overview.md)

## Purpose

Keep the review’s task address shareable while separately restoring its selected block and comparison in the current browser-history entry.

## Code Commentary

`parseReviewHash` accepts only #review? with nonempty repository/master/leaf; history=recorded sets the historical flag. `reviewHash` serializes only those task-address fields and that flag. It does not resolve task existence, authorization, selected blocks or source data.

`readReviewHashState` reads the page-owned sel string and a digits-only comparison value, otherwise returning null values. `writeReviewHashState` acts only on review hashes, changes just those two fields, preserves all other parameters and existing history state, and skips an identical result. It uses replaceState, so selecting a block/comparison creates no new history entry or hashchange event.

`useReviewHash` initializes from the current address and listens for hashchange. The same serialized task-review identity preserves the current target object; another addressed review replaces it. Leaving a review hash clears a current review target but does not clear an ordinary change-set target. Review and knowledge addresses select Operations or Knowledge and close Notes.

The returned setter uses pushState for entering or leaving a review and updates React state explicitly. Leaving through it chooses no new product view. The hook owns listener cleanup. A complete but unknown task address still reaches the server-owned refusal path; parsing alone proves neither existence nor permission.

## Invariants And Boundaries

Task navigation and page-state restoration have different owners and history behavior. The page stores a formatted block selection, not a trusted source path; blockIdentity and the comparison/read owners validate its meaning. The serializer’s task identity remains stable when page-only hash parameters change.

## Evidence

- Task identity parsing/serialization remains separate from page-owned selection. [6]
- Selection/comparison changes preserve task params and replace the current history entry. [7]
- The hook retains equal task targets and explicitly owns navigation state/listeners. [8]
