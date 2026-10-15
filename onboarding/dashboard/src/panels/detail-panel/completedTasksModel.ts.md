# dashboard/src/panels/detail-panel/completedTasksModel.ts

## Governing Overview

[Area overview](../overview.md)

## Purpose

Supply completion facts and ephemeral ordering for completed task tables without migrating canonical documents.

## Code Commentary

A truthy completedAt wins; otherwise the newest finite Date.parse-compatible decision date with exactly the text Finalize task lifecycle. supplies the legacy fallback. That exact-text fallback does not additionally require product_record and retains valid pre-epoch dates. A truthy but invalid completedAt still wins selection and is unknown-last when sorted. Missing documents yield no time. completedEntries creates a call-local indexSlices matcher once when no matcher is supplied; callers can share one matcher with navigation. Row facts retain first-match slug semantics and full-list positions.

Sorting copies the input. Number order uses numeric English locale comparison rather than parsing task IDs; time order uses parsed dates and leaves absent/invalid dates last in both directions. Sorting and fallback are presentation only: they write neither timestamps nor task state.

## Evidence

- Completion time prefers completedAt with finite-date exact legacy finalizer-text fallback, and sorting is nonmutating/local. [1]

- completedEntries uses one default call-local slice index, or a supplied matcher shared with navigation, preserving first-match row facts and original positions. [2]
