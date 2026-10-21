# dashboard/src/panels/review/blockIdentity.ts

## Governing Overview

[Route overview](overview.md)

## Purpose

Name review entry blocks and code-without-invariant hunks consistently for selection, keyboard stops and tray references.

## Code Commentary

### Logic

Entry identity uses entry id, the after recorded side or the recorded before side, that side’s path/resolved range, and all four code/memory tree ids. A hunk uses path, before/after diff spans and the two code tree ids.

blockKey joins the identity fields with NUL separators, and sameBlock compares those keys.

formatSelection emits subject selectors or UTF-8/base64url JSON block payloads. parseSelection checks form, arity, nonempty text and ordered nonnegative integer ranges. inComparison checks two trees for a hunk and four for an entry.

### Invariants And Boundaries

Ranges are supplied by the comparison’s server-resolved side, never guessed or remapped here. Parsing proves syntax; callers separately check whether the parsed identity belongs to the displayed comparison.

## Evidence

- Exact recorded-side and tree identity [1]
- Stable equality key [2]
- URL payload checks and explicit comparison membership [3]
