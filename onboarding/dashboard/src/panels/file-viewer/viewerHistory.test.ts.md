# dashboard/src/panels/file-viewer/viewerHistory.test.ts

## Governing Overview

[overview](overview.md)

## Purpose

Checks viewer navigation metadata and retained body reclamation.

## Code Commentary

The assertions cover fitting-history identity, preservation of every entry, body and sidecar cost, the oversized-current exception and saving a known scroll position. Released bodies keep their navigation metadata.

## Relationships

FileViewer consumes these helpers and reloads released content. These cases do not establish process-restart or browser-reload persistence.

## Evidence

- Checks viewer navigation metadata and retained body reclamation. [1]
