# dashboard/src/panels/file-viewer/viewerHistory.ts

## Governing Overview

[overview](overview.md)

## Purpose

Owns opened viewer entries, their current index and retained body reclamation.

## Code Commentary

Entries retain file identity, sidecar state, first-arrival anchor and saved scroll position. Code entries also retain render mode. Saving zero marks the position known. Opening after Back discards the forward branch. An 8 MiB UTF-8 body budget releases oldest noncurrent text bodies while retaining navigation metadata and every entry. The current body is never released, so an oversized current file can exceed that budget.

## Relationships

FileViewer reloads a revisited released body and its pairing. This budget limits retained text bodies, not history length, file input size or media bytes.

## Evidence

- Owns opened viewer entries, their current index and retained body reclamation. [1]
