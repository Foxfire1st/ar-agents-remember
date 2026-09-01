# mcp/src/agents_remember/tasks/leaf_binding.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/tasks/leaf_binding.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-01T03:58+02:00 |
| lastVerifiedCommitHash |  `47c8d102c2430d5337dbe207d4601efb4844fec0`|
| lastVerifiedCommitDate |  2026-09-01T08:53:56+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No external source is needed for this repository-owned identity contract.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Typed source and binding records carry one exact composite identity. | `CanonicalLeafBindingError`; `CanonicalLeafSource`; `CanonicalLeafBinding` | mcp/src/agents_remember/tasks/leaf_binding.py:14-43 |
| Parent-row selection and source derivation reject ambiguous or non-canonical rows. | `require_leaf_parent_row`; `canonical_leaf_source` | mcp/src/agents_remember/tasks/leaf_binding.py:46-102 |
| Full binding verifies parent, child, address, row, id, and stem together. | `require_canonical_leaf_binding` | mcp/src/agents_remember/tasks/leaf_binding.py:104-252 |

## Cross-Repo References

None.

## Update History

- 2026-09-01T03:58+02:00 — 260831-CCR-L01 Attempt 8: created the canonical composite leaf-binding
  card. Verification remains closeout-owned.
