# codegraphcontext-0.4.10-cgcignore-runtime-root.patch

## Governing Overview

[overview.md](../../../../../../../overview.md)

## Purpose

This patch asset documents the CodeGraphContext v0.4.10 monkey patch required for Agents Remember managed provider mode. It prevents CGC from unconditionally creating `.cgcignore` in the indexed source repo when an explicit runtime ignore path is available.

## Code Commentary

### Logic

The patch targets `codegraphcontext/core/cgcignore.py`. In the unpatched code, `local_cgcignore_path` defaults directly to `ignore_root / ".cgcignore"` and CGC writes the default ignore file there. The patch changes that branch to prefer `explicit_cgcignore_path` when provided, falling back to `ignore_root / ".cgcignore"` only when no explicit path exists. This lets Agents Remember place `.cgcignore` under `providers/runners/codegraphcontext/<repo-id>/.codegraphcontext/` instead of dirtying the indexed code repository.

### Conventions

The patch is version-specific. Lifecycle tooling should apply it only after installing the pinned CGC provider version and should verify the marker before indexing.

### Invariants And Boundaries

Managed CGC provider mode is not acceptable if indexing creates `.cgcignore`, `.codegraphcontext`, `CGC_REPORT.md`, database files, or logs in the source repo. This patch addresses the `.cgcignore` case for CGC v0.4.10.

## Evidence

### Repo-Internal References

- The patch replaces CGC's direct repo-local `.cgcignore` default with a branch that prefers `explicit_cgcignore_path`. [1]
