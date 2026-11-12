# dashboard/src/panels/review/explainer/ExplanationView.tsx

## Governing Overview

[Route overview](../../overview.md)

## Purpose

The explainer's end-to-end page for the bound comparison, drawn in the review page's reading column: the moved notice, the trusted stale list, the retained revisions and the page itself in its isolated frame.

## Code Commentary

- The column draws its fixed lines in order: the moved notice when the leaf moved, the trusted stale list unless a pair is being compared, the revision selector, then whatever the phase holds.
- The phase decides the body — a reading sentence, a card naming the problem with Retry, one empty card with a single Explain button, a still building placeholder that points at the chat, or the saved page.
- The saved page is the standfirst naming time, revision and binding, the basis legend, one isolated frame for the shown revision, the retired line and the claim list.
- Compare replaces that with two columns, each carrying its own standfirst, stale list, frame and claims, so one revision's staleness cannot stand for the other's.
- The view draws no top line and mounts no chat, and it never rebinds silently: Update names the comparison on screen, and regeneration either sends once to a live seat or opens the prefilled first-request form.
- Judgment chips and `Ungraded (n)` headings are mounted into the reading cards' DOM outside React, and cleanup removes exactly what was created.

## Evidence

- The phase chooses between the reading sentence, the named problem, the empty state, the build placeholder and the saved page [1]
- The empty state offers one button and states that nothing runs until asked [2]
- An unreadable answer names its reason and offers Retry instead of an empty page [3]
- The single saved page composes standfirst, legend, one frame, the retired line and the claims [4]
- A chosen or compared revision's own state is read on demand, not taken from the page's default [5]
- Judgment chips and ungraded headings are added to reading cards and removed on cleanup [6]
