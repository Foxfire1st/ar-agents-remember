# dashboard/src/panels/detail-panel/indexRows.tsx

## Governing Overview

[Area overview](../overview.md)

## Purpose

Own shared index-row props, reference-gated target resolution and served child-progress presentation independently of task-page composition.

## Code Commentary

`resolveRowTarget` uses entry.key for opaque selection only when entry.reference exists; an addressless row remains inert. Full-list positions define stable test/navigation IDs; no masterRef, lifecycle or slug fallback is inferred.

`TaskIndexProps` carries the parent entry, shared tasks map and onJump. Child progress reads served counts through childProgress/liveChildCount, not a second sub-task tally. No slice index or first-match document scan remains.

This module does not classify authored seat rows or restore a document/slice fallback. `task-groups` follows served children and their canonical stages; its sprint seat view is separate summary content. Here `ChildProgress` displays published completed/started counts over the live-child total and omits a zero-total progress figure. Neither helper authors task state, fetches a document or decides a grant.

## Evidence


- Row selection uses the opaque canonical entry key only when a document reference exists. [2]
- Child progress reads served counts and omits a zero-total figure, without a slice/document matcher. [3]
