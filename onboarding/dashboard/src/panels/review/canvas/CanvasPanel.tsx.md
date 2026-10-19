# dashboard/src/panels/review/canvas/CanvasPanel.tsx

## Governing Overview

[governing route overview](../../overview.md)

## Purpose

The reviewer's page panel: it shows a saved page first, offers one explicit Generate control, shows build progress and the builder's side conversation, and mounts the sandboxed frame above the untouched deterministic detail.

## Code Commentary

- `CanvasPanel` renders the saved-first state and the one explicit start; mounting the panel performs a read and starts no model.
- `usePanelGestures` handles the panel's own selection and focus gestures, so the frame and the panel do not steal each other's keys.
- The frame is mounted with the sandbox the host requires; the panel adds no privilege of its own.
- An evidence destination chosen in the page is handled by the panel's navigation hook, which preserves the mounted review's selection.

## Evidence

- Three controls can begin or resume authoring on this panel and each is explicit: Generate starts a first attempt for the comparison on screen and requires an admitted comparison; Replace presenter posts a successor attempt for an attempt the composition already holds; Resume continues an attempt whose host session is known. Nothing else on the panel starts or resumes authoring. [1]
- The panel mounts the sandboxed frame above the deterministic detail. [2]
