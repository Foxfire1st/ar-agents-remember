# mcp/src/agents_remember/worktrees/modules/quality/report_publication_paths.py

## Governing Overview

[worktrees/modules overview](../overview.md)

## Purpose

Owns no-follow publication path preflight, strict snapshot-bound report reopening, legacy projection removal, recursive inventory, and the existing historical-generation pruning implementation. The clean executor supplies the publication order and selected-generation protection set.

## Code Commentary

### Logic

`preflight_report_destination` rejects symlinks and irregular nodes at the supplied destination, generation and legacy-projection boundaries. `remove_legacy_report_projection` deletes only declared former projection paths. `report_tree_inventory` classifies nested files, directories and irregular entries without following links.

`published_report_path_from_manifest` rejects noncanonical report locators and malformed generation ids before constructing or reading the report path. It checks every directory from report parent back to destination and the final regular file, reads at most declared size plus one byte, and requires exact size and SHA-256 agreement with the one accepted snapshot. It never chooses a current/latest generation on the reader's behalf.

`_prune_report_generations` inventories all managed 64-hex generation names and refuses an irregular candidate before deletion. It keeps the current generation, every explicitly protected generation, and the two newest managed generations. The clean executor now obtains selected-certificate pins from `certification_evidence` and adds the previous current generation before calling this existing pruner. These mechanisms moved here from the executor; there is no second reader or pruning protocol.

### Conventions

The publisher owns inventory policy, pointer ordering and retention authority. This module supplies confined paths and filesystem operations; a path lookup is not certification of a gate result.

### Invariants And Boundaries

- Unsafe locator spellings are refused before any report open.
- Exact report size/digest and each inspected path component must agree with the accepted immutable snapshot.
- Historical-generation validation and pruning implementation live here; the caller supplies all protected identities.
- Legacy cleanup cannot recursively erase undeclared directories, and inventory retains nested relative identity.
- Path preflight detects the inspected filesystem state; it is not a claim of exclusion against an uncooperative concurrent filesystem writer.

### Todos

None recorded.

## Evidence

### Docs References

No Domain Documentation source is configured.

### Repo-Internal References

- Exact publication boundaries and legacy projection cleanup are confined. [1]
- Recursive inventory exposes irregular entries. [2]
- Report reopening validates the safe locator, path nodes, size and digest. [3]
- All managed generation candidates are preflighted before bounded retention pruning. [4]
- The publisher supplies selected-certificate and prior-current protection before moving the pointer. [5]

### Cross-Repo References

No cross-repository implementation dependency governs this file.
