# dashboard/src/cockpit/reviewExplainerColumn.test.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Specifies the cockpit seam: the review rail hands the column its leaf, the pane shows the explainer or its placeholder and never the task's Worker, and a page without an explainer keeps its own chat.

## Code Commentary

- The rail hands the column one address per review, and a review without a leaf has no explainer at all.
- Cold, open, finalized and planning targets all select the explainer or its placeholder, and the assertion covers the document-chat route never being read.
- The Operations page mounts the task document's Retire control for a leaf document and retires a cold explainer in place.
- The same iframe node and the same tray draft survive page and phase switches in both directions.

## Evidence

- A review without a leaf has no explainer address [1]
- An Operations leaf document shows Retire and retires a cold explainer [2]
- The frame node and the draft survive switching between Operations and Review [3]
- A page without an explainer keeps the document's own chat and reads no explainer state [4]
