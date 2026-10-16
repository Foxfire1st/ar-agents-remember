# dashboard/src/data/taskReference.ts

## Purpose

Exact reference and opaque task selection encoding.

## Code Commentary

taskReferenceKey joins repository/path; taskSelectionKey prefixes that canonical key. taskEntrySelectionKey prefixes an opaque entry.key. Addressless rows have no document reference; no normalization or lifecycle fallback is inferred.

## Governing Overview

[Area overview](overview.md)

## Evidence

- Implementation [1]
