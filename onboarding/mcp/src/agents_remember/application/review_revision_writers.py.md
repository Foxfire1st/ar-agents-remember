# mcp/src/agents_remember/application/review_revision_writers.py

## Governing Overview

[Route overview](overview.md)

## Purpose

Attach the recorded writer of each selected invariant or family revision using that comparison side’s own history index.

## Code Commentary

### Logic

with_revision_writers returns an unselected value unchanged; selected sides call read_side and return no writer for an absent/unaddressable side. Missing/legacy/unreadable indexes return unavailable.

_read_writer requires a complete history index and a record revision. It collects distinct owners of changed rows at exactly that revision. If none claim revision 1, the record’s origin supplies leaf, then wave, then task as its introducer.

A later revision with no claiming changed row is not_recorded. Other row dispositions do not count as writing, and incomplete history cannot assert that no writer exists.

### Invariants And Boundaries

It reads the already selected before/after indexes and infers no writer from Git, dates or the currently reviewed leaf. A recorded writer is history evidence, not an intent verdict.

## Evidence

- Selected-side composition and unavailable boundaries [1]
- Complete-history requirement, changed-row owners and first introduction [2]
- Exact writing predicate and origin precedence [3]
