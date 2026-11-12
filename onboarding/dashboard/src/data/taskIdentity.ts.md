# dashboard/src/data/taskIdentity.ts

## Governing Overview

[data overview](overview.md)

## Purpose

Exact canonical reference equality and the role-chat qualified leaf registry key; selection encoding lives in taskReference.ts.

## Code Commentary

### Logic

sameTaskDocumentRef compares repository/path exactly. qualifiedLeafKey uses addressed entry repository, parent folder and id for role-chat context; addressless returns undefined. No lifecycle/series/tree resolver remains.

### Conventions

Selection keys are UI namespaces. Structural seats use `TaskDocumentRef`; labels and qualified leaf
keys are presentation/context values.

### Invariants And Boundaries

- References are not normalized or guessed from runtime ids.
- A leaf context key is not a hosted-occupant address.
- Membership and selection use served entries and taskReference helpers.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured.

### Repo-Internal References


### Cross-Repo References

No cross-repository implementation dependency governs this file.
