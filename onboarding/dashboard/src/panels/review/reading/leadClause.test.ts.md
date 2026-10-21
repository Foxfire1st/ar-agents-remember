# dashboard/src/panels/review/reading/leadClause.test.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

Pin short-title lead-clause extraction without shortening an unhelpfully small lead.

## Code Commentary

### Logic

Pure assertions check extraction before an em dash, double hyphen, semicolon or colon. A title with no break remains whole, as does the short-leading Note: example.

### Invariants And Boundaries

The cases exercise text extraction only. They do not mount a heading, check its tooltip, or assert a numeric minimum lead length.

## Evidence

- Delimiter examples shorten the title, while no-break and short-lead examples stay whole. [3]
