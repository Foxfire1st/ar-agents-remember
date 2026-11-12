# mcp/src/agents_remember/tasks/leaf_binding.py

## Governing Overview

[Tasks overview](overview.md)

## Purpose

Owns the canonical composite binding between one master row and one JSON-primary leaf document so
lifecycle and semantic-topology consumers cannot derive different leaf identities.

## Code Commentary

### Logic

`require_leaf_parent_row` selects exactly one numbered row from a master. `canonical_leaf_source`
turns that row's confined direct-child Markdown path into the canonical JSON ref. The stronger
`require_canonical_leaf_binding` requires the parent and candidate kinds, repository and directory,
candidate id, row number, row file, JSON stem, and exact source address to identify one and the same
leaf. Typed `CanonicalLeafBindingError` statuses distinguish missing, ambiguous, stem-only, split,
wrong-directory, and source-mismatch cases.

### Conventions

- Canonical task references are repository-qualified POSIX paths.
- A parent row's Markdown `.md` source maps to the corresponding JSON-primary `.json` document.

### Invariants And Boundaries

- A leaf parent is a canonical `task.json` master and the child is a direct `subTask` sibling.
- A leaf row cannot carry a sprint `masterRef`, an absolute/nested source, or an ambiguous identity.
- Stem coincidence alone is insufficient; number, file, address, and child id must agree.
- This pure task-domain owner performs no filesystem I/O or lifecycle mutation.

### Todos

None.

## Evidence

### Docs References

No external source is needed for this repository-owned identity contract.

### Repo-Internal References

- Typed source and binding records carry one exact composite identity. [1]
- Parent-row selection and source derivation reject ambiguous or non-canonical rows. [2]
- Full binding verifies parent, child, address, row, id, and stem together. [3]

### Cross-Repo References

None.
