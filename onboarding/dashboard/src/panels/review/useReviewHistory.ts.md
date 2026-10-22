# dashboard/src/panels/review/useReviewHistory.ts

## Governing Overview

[Owning route overview](../../../../overview.md)

## Purpose

Hold which record a review surface reads, and let the page leave that frame.

A target may name the record it is addressed to, and the surface then asks for that leaf's recorded comparison. The leaf's own Intent review entry no longer asks for it: it supplies `review: {}` for a live and a closed leaf alike, so a closed leaf opens the page's own default and the control is labelled `(recorded)`. The delivered link needs the opposite move, because the page's own default is the pair the leaf delivered, so the flag is state the page can clear rather than a prop fixed for the mount.

## Code Commentary

`useReviewHistory` seeds its state from the target's initial value and keeps the seed in a ref. A changed initial-history token on the same mounted surface re-seeds the frame; an unchanged token does not. The hook depends on no other input, so a different task arriving with the same token does not re-seed it. `leaveHistory` clears the frame through `setHistory(undefined)`, which is what lets the delivered action return the page to its own default.

The surface reads the returned frame for its comparison reads and passes `leaveHistory` to the page's delivered action.

## Invariants And Boundaries

The module holds one mutable fact — the recorded frame — and starts no read, no model and no role. It records no comparison and decides no review.

## Evidence

- The frame is state seeded from the initial-history token, re-seeded only when that token changes. [1]
- The page can leave the recorded frame, returning to its own default. [2]
