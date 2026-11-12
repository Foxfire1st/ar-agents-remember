# dashboard/src/dev/Reference.tsx

## Governing Overview

[Governing route overview](../overview.md)

## Purpose

Displays the imported mc2 design reference beside development views.

## Code Commentary

### Logic

Imports the HTML as raw text and passes it to an iframe through srcDoc. A surrounding bar labels the canonical design endpoint.

### Conventions

The component owns presentation of the reference; DevApp selects it for /dev/reference.

### Invariants And Boundaries

The iframe content comes from the imported snapshot. This component provides no source-editing control; its read-only label is not a sandbox declaration.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation is configured. This card describes repository source only.

### Repo-Internal References

These constructs establish the behavior described above.

- Raw reference import and iframe presentation [1]
- Development route selects this reference component [2]

### Cross-Repo References

No cross-repository behavior is implemented in this file.
