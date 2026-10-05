# dashboard/src/test/paseoPluginPage.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

The support provides explicit plain-object storage/tab/page and SDK seams for canonical plugin tests.

## Code Commentary

pageLoad supplies exact parent/message delivery, DOM/timers, clocks and storage-writer watching. App-write helpers exercise provenance while plugin writes bypass app attribution. emptyHierarchyClient is a healthy subscribed empty host. Local versus session storage model shared-browser and per-tab state.

## Invariants And Boundaries

This injected seam is not a production adapter, new runtime registry or live browser proof.

## Evidence

The current source and test assertions below establish the documented ownership; test citations do not claim a rerun in this pass.

| Finding | Anchor | Source at frozen tree |
| --- | --- | --- |
| Current source owner or exact assertion described above. | `emptyHierarchyClient` | `dashboard/src/test/paseoPluginPage.ts:17-47` |
| Current source owner or exact assertion described above. | `pageLoad` | `dashboard/src/test/paseoPluginPage.ts:73-103` |
| Current source owner or exact assertion described above. | `recordedWrite` | `dashboard/src/test/paseoPluginPage.ts:186-198` |
