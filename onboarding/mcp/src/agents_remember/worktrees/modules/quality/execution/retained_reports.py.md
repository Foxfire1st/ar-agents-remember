# mcp/src/agents_remember/worktrees/modules/quality/execution/retained_reports.py

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Builds and copies the bounded report population required by selected predecessor gates into the caller’s fresh candidate sandbox.

## Code Commentary

### Logic

`retained_report_inventory` first validates the selected execution. It considers frozen publication declarations whose producer gates precede the selected first gate, then visits only evidence and artifact members of the retained results. Every report path must be canonical and relative, declared for that result’s producer gate, within the declared file bound and equal to the original publication’s SHA-256/size inventory.

Repeated paths converge only when digest and size agree; conflicting producers refuse. The inventory is sorted, limited to 4,096 distinct paths and bounded by the sum of applicable frozen publication byte declarations. Large retained coverage files use their actual profile-declared allowance rather than a separate guessed transport cap.

`snapshot_retained_reports` returns directly for a first-gate execution. Otherwise it resolves every selected original path through the confined immutable-publication reader before creating a fresh destination. Each source read is bounded to its declared size plus one byte and its actual size/hash is checked before exclusive file creation. The caller’s existing sandbox lifecycle owns cleanup of any partial transport.

### Conventions

Use the supplied original publication for every source path. No current-pointer lookup, generation scan or unrelated report enters the copied population. Destination freshness and sandbox cleanup remain the caller’s responsibility.

### Invariants And Boundaries

- The selected result members and frozen producer declarations jointly define transport membership.
- Inventory metadata is insufficient without physical source reopening and bounded read verification.
- Matching repeated paths are deduplicated; conflicting bytes never overwrite an earlier member.
- This owner copies evidence; it does not accept gates, select a lifecycle generation or allocate Dagger authority.

### Todos

None recorded for this file's bounded responsibility.

## Evidence

### Docs References

The resolved registry supplies no applicable external Domain Documentation source for this card.

### Repo-Internal References

- Each member retains its original publication and exact declared file identity. [1]
- Inventory derives membership and byte bounds from frozen producer declarations. [2]
- All source paths are resolved before fresh exclusive transport writes. [3]

### Cross-Repo References

No separately configured cross-repository source is used for this card.
