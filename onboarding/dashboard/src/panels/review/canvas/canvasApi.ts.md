# dashboard/src/panels/review/canvas/canvasApi.ts

## Governing Overview

[governing route overview](../../overview.md)

## Purpose

The panel's typed transport to the canvas API: the frame-state, comparison, attempt, activity and conversation shapes it reads, and the refusal it raises when the server answers with one.

## Code Commentary

- `CanvasFrameState` is the saved-first answer the panel renders; the attempt, activity and conversation shapes carry the identifiers a reader sees.
- `CanvasRefusal` carries the server's own state, reason and detail, so a panel shows the refusal rather than inventing a failure.
- Every request goes through the one `API` prefix and returns a typed answer or a refusal.

## Evidence

- A server refusal is carried as its own typed error with the server's reason. [1]
- The frame, attempt, activity and conversation shapes the panel reads. [2]
