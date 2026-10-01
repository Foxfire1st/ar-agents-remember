# dashboard/src/data/taskIdentity.ts

## Governing Overview

[data overview](overview.md)

## Purpose

Centralizes dashboard task-selection keys, canonical task-document references, structural equality,
and real task-tree construction. Qualified leaf keys remain a display/context helper; they are no
longer the hosted-seat address.

## Code Commentary

### Logic

`taskDocumentRefForDoc` turns a projected task document into the repository-qualified reference used
by the runtime, and `sameTaskDocumentRef` compares that identity. `buildTaskTree` constructs the
Operations/Chats task hierarchy from actual sprint, master, and leaf documents. Existing lifecycle and
leaf-key helpers continue to serve selection, labels, and leaf context packages without becoming a
parallel seat identity.

### Conventions

Selection keys are UI namespaces. Structural seats use `TaskDocumentRef`; labels and qualified leaf
keys are presentation/context values.

### Invariants And Boundaries

- Every structural reference points to a real projected task document.
- No synthetic logical seat id or master key is introduced.
- Leaf-key helpers must not be used to address a hosted occupant.
- Lifecycle ids remain optional runtime attachment, not task identity.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured.

### Repo-Internal References

- Projected documents become canonical task-document references. [1]
- Structural equality compares repository, path, and level. [2]
- The dashboard tree is built from real task documents. [3]

### Cross-Repo References

No cross-repository implementation dependency governs this file.
