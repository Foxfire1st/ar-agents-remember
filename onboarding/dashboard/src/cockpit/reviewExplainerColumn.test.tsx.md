# dashboard/src/cockpit/reviewExplainerColumn.test.tsx

## Governing Overview

[Route overview](../overview.md)

The composed Operations case mounts CockpitShell, the review right rail and DocumentChat. It follows the selected explainer from Build through a live chat and an eligible transient open retry in one persistent iframe.

## Purpose

Specifies the cockpit seam: the review rail hands the column its leaf, the pane shows the explainer or its placeholder and never the task's Worker, and a page without an explainer keeps its own chat.

## Code Commentary

- The rail hands the column one address per review, and a review without a leaf has no explainer at all.
- Cold, open, finalized and planning targets all select the explainer or its placeholder, and the assertion covers the document-chat route never being read.
- The Operations page mounts the task document's Retire control for a leaf document and retires a cold explainer in place.
- The same iframe node and the same tray draft survive page and phase switches in both directions.
- A composed Operations case holds mid-build identity for over 8 seconds while hidden with zero `ar.open` calls, then emits exactly one `ar.open` on `live` in generation 1 without leaving Operations.

## Evidence

- A review without a leaf has no explainer address [1]
- An Operations leaf document shows Retire and retires a cold explainer [2]
- The frame node and the draft survive switching between Operations and Review [3]
- A page without an explainer keeps the document's own chat and reads no explainer state [4]

- The composed Operations case mounts CockpitShell, the review right rail and DocumentChat. It follows the selected explainer from Build through a live chat and an eligible transient open retry in one persistent iframe. [5]

- The composed CockpitShell/RightRail/DocumentChat mid-build case emits zero ar.open while hidden for > 8 s and exactly one ar.open on live without leaving Operations. [6]
