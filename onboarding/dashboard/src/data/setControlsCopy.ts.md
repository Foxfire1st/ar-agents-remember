# dashboard/src/data/setControlsCopy.ts

## Governing Overview

[data overview](overview.md)

## Purpose

Central copy source for set waiting, acceptance, clamp, queue, route, promotion, cycling, and
session-transition messages.

## Code Commentary

### Logic

Formats every chip and live-region sentence from typed inputs. Clamp copy retains requested and
effective values; unsupported and route failures preserve server detail; route retry wording is
limited to retryable outages; session failure and awaiting-input messages name the seat label.

### Conventions

Acceptance words are literal visible text, never color-only semantics. Copy functions are pure so
header chips, toasts, and announcements cannot drift into competing vocabularies.

### Invariants And Boundaries

The module presents evidence but never classifies it; reducers and route classifiers own that
decision. Requested and effective values remain distinct in every relevant sentence.

### Todos

None recorded.

## Evidence

### Docs References

No Domain Documentation source is configured.

No external domain citation applies.

### Repo-Internal References

- Shared copy and announcement formatters. [1]
- Presentation-model consumer. [2]
- I/O and live-region consumer. [3]

### Cross-Repo References

No meaningful cross-repo boundary is owned here.

No cross-repo evidence applies.
