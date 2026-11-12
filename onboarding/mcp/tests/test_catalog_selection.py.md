# mcp/tests/test_catalog_selection.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Checks that test-evidence catalog consumer metadata selects both removed and added consumers while ignoring comments, order-only changes, and non-consumer policy changes. It also proves global population files remain global inputs.

## Code Commentary

### Logic

`_catalog` builds a compact catalog fixture. The tests distinguish consumer-set changes from comment/order changes, policy/version/path changes, and global configuration ownership.

### Invariants And Boundaries

- Removed and added consumers both remain affected.
- Consumer ordering and comments do not create a selection delta.
- Global test inputs are distinguished from catalog consumer metadata.

### Todos

None recorded.

## Evidence

### Docs References

No configured Domain Documentation source applies.

- Consumer-selection behavior is defined by the retained tests. [1]

### Repo-Internal References

- The fixture emits the catalog shape consumed by the selection helper. [2]
- Consumer differences select both sides while comments/order and policy-only changes do not. [3]
- Global input ownership is asserted separately from consumer metadata. [4]

### Cross-Repo References

None; these are local selection contracts.
