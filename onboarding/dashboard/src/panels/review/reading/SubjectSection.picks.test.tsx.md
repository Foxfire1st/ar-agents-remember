# dashboard/src/panels/review/reading/SubjectSection.picks.test.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Guard the review page's tray reference identities and comparison sides.

## Code Commentary

### Logic

Builds the page change-set model under a minimal ReadingContext, clicks invariant, block and family tray controls, and reads trayStore references. It checks invariant text IDs and comparison numbers, candidate memory for a live invariant, base memory for a removed invariant, family text IDs, and omission of client-guessed invariant revision IDs from invariant/block references.

### Invariants And Boundaries

The tests inspect local tray picks only. They do not resolve those references on the server, hydrate source content, or send anything to a chat.

## Evidence

- Minimal reading context and isolated tray collection. [4]
- Record picks use text IDs/comparison sides and do not guess invariant revisions. [5]
