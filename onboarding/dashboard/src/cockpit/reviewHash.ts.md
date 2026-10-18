# dashboard/src/cockpit/reviewHash.ts

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

Bridge a review takeover to a shareable browser hash without putting the selected subject into browser history. The server remains responsible for resolving or refusing repository/master/leaf identities.

## Code Commentary

`parseReviewHash` recognizes only `#review?`, requires nonempty repo/master/leaf parameters and returns a task-context ChangeSetTarget. Only `history=recorded` sets historical true. `reviewHash` writes those task identities and the optional recorded flag; selectors, comparison number, change-set file and layout are deliberately absent.

`useReviewHash` initializes its target from the current hash. On hashchange, a newly addressed review replaces the target unless its serialized review identity equals the current review, in which case the existing object is retained. That identity check avoids resetting the mounted review for an address that says nothing new about its subject. A hash that stops naming a review clears only a current review target; an ordinary change-set target is not cleared by an unrelated hash. Review and Knowledge hashes also select Operations or Knowledge and close Notes.

The returned setter pushStates a review hash for review targets, clears an existing review hash to pathname+search for non-review/null targets, then sets React state explicitly—pushState itself does not dispatch hashchange. Leaving through this setter does not choose a new main view. Listener cleanup belongs to the hook. Parsing establishes syntax/address presence, not existence or authorization; missing parameters return null, while unknown nonempty task identities reach the reviewer's refusal path.

## Evidence

- Parser admits complete review task addresses and the one recorded flag. [1]
- Serializer carries no subject or change-set page selection. [2]
- Hash navigation preserves identical mounted review identity, switches addressed views, and cleans up. [3]
- Setter uses pushState and explicit React target updates. [4]
- Cockpit initializes Operations for a review hash and consumes hash-backed takeover state. [5]
