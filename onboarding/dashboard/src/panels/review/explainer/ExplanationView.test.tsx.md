# dashboard/src/panels/review/explainer/ExplanationView.test.tsx

## Governing Overview

[Route overview](../../overview.md)

## Purpose

Measures the mounted explanation page against a stubbed transport: what the saved, failed and comparing states render, that a page opens with no model, and which channel a navigation revokes.

## Code Commentary

- The cases render the real view over a stubbed fetch that answers the state, revision and canvas-session routes and records every call.
- One channel per saved revision is required, with the sandbox and document address taken from the host's answer and no build, generate, message or Update call made.
- The stale list is required to survive a frame that cannot open at all, which is how its independence from the page is measured.
- The compare case fails one frame's second load and one frame's departure signal, and requires the sibling's document address to stay as it was.
- Claim chips and the legend are required to name all four bases and to hand a claim's block back to the page's selection owner.

## Evidence

- A saved page opens one isolated frame for its exact revision and starts nothing [1]
- The trusted stale list is drawn from the host's answer even when the frame cannot be shown
- Every claim is marked and all four bases are named in the legend
- A navigated or departed frame is revoked alone, and its sibling keeps its document [4]

- Retired at the fifth freeze d59c3493: dashboard/src/panels/review/explainer/ExplanationView.test.tsx:264-290 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 5f8398b32760677c370e3145add73cfa8388357b; dashboard/src/panels/review/explainer/ExplanationView.test.tsx:366-392 - the region it cited is not in the file at the candidate and no re-point was possible. Retired means the anchor no longer stands, not that the cited subject was deleted.
