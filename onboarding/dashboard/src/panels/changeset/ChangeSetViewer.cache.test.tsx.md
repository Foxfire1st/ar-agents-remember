# dashboard/src/panels/changeset/ChangeSetViewer.cache.test.tsx

## Governing Overview

[Route overview](overview.md)

## Purpose

Pin conditional working change-set polls through the real editor.

## Tested Boundary

Captured timer callbacks drive stubbed ETag responses. Unchanged polls retain parsed list/editor identity without decoding; changed text replaces the editor; current refusal clears retained success and later recovery restores counters. This is component source coverage, not a real server/browser result.

## Evidence

- List/editor retention and current refusal [1]
