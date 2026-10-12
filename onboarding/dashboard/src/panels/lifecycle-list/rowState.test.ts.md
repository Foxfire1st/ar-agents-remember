# dashboard/src/panels/lifecycle-list/rowState.test.ts

## Governing Overview

[Panels overview](../overview.md)

## Purpose

Pure regression tests of what an Operations tree row says.

## Code Commentary

The tests distinguish unreported inference from actual lifecycle events, retain lifecycle ages, check the ordered priority words and need bands, keep overdue inbox dismissal beside a gate, preserve hidden progress/signals in hover text, and shorten IDs only inside their actual master. These are presentation assertions, not backend persistence or mounted visual proof.

## Evidence

- The assertions exercise document/lifecycle truth, priority and retained hover information on synthetic row facts. [1]
