# dashboard/src/panels/review/explainer/explainerModel.ts

## Governing Overview

[Route overview](../../overview.md)

## Purpose

The pure decisions behind the explanation page — labels, phase, shown and compared revisions, what is pinned and removable, the stale summary and its regeneration message — so none of those distinctions live in JSX.

## Code Commentary

- A planned binding reads planned and never a number, an absent binding reads no binding, and a recorded one keeps the label its host wrote.
- The phase names what exists: a read in flight, nothing yet, a build, a saved page, or an unavailable answer.
- The pinned revision is never offered for removal, nor is one already removed, and only the task total's refusal offers removal at all.
- The stale summary keeps the true total and the reason staleness is unavailable; regeneration is offered only when something is stale and the host supplied no message of its own.
- The standfirst takes the shown row's own binding and time rather than the environment's current binding, and appends retired when the explainer was retired.
- Global revisions are listed before focused ones, and the default shown revision is the latest retained global one when one exists.

## Evidence

- A planned binding is labelled planned and never a number, and an absent one is stated as such [1]
- One phase function decides reading, unavailable, none, building or saved [2]
- The removal set excludes the pinned revision and any already removed one [3]
- Only the task total's refusal offers the removal control [4]
- The regeneration label and message are built from the stale parts and stale grades, and absent when nothing is stale [5]
- The standfirst states time, revision, binding, kind and retirement from the shown row [6]
