# mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/discovery.py

## Governing Overview

[overview.md](../../../../../overview.md)

## Purpose

`discovery.py` retains text-only metadata parsing and path normalization for old-card readers/conversion. It performs no discovery walk, Git operation, mutation or drift grading.

## Code Commentary

### Logic

`parse_table_metadata_text` reads pipe rows from supplied text, skips header/separator keys and unwraps paired backticks from values. `normalize_overview_route` maps empty/root-placeholder forms to `.` and otherwise uses kernel scalar/path normalization. `rel` preserves string inputs and returns a root-relative POSIX path when possible, otherwise the absolute POSIX spelling.

### Invariants And Boundaries

- Pure parsing and path conversion: no Git calls, filesystem discovery, mutation or policy verdict.
- Kernel scalar/path normalization remains the dependency; mirroring is owned by the kernel path helper.

## Evidence

### Repo-Internal References

- Retained metadata-text/path and entity readers parse old-card or structural inputs without the removed sidecar classifier. [1]

- Path normalization is provided by the kernel resolver. [2]
