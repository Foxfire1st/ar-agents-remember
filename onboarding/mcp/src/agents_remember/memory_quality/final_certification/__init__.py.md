# mcp/src/agents_remember/memory_quality/final_certification/__init__.py

## Governing Overview

[memory_quality overview](../overview.md)

## Purpose

Public package surface for the deterministic complete memory-quality catalog and its non-certifying readiness projection. It exposes the version, two catalog item models, catalog population and readiness function. The quality controller consumes this projection; the package does not execute certification or mutate code or memory.

## Code Commentary

### Logic

`__all__` exports only `FINAL_FULL_CATALOG_VERSION`, `FinalCatalogItemIdentity`, `FinalCatalogItemResult`, `complete_final_catalog`, and `final_catalog_readiness`. Catalog functions come from `catalog.py`; the two models come from `certification.final_certification_models`. The controller imports readiness through this package-owned seam.

### Conventions

The retained model imports use `agents_remember.certification.final_certification_models`; catalog imports use `agents_remember.memory_quality.final_certification.catalog`. This module uses no relative cross-module import.

### Invariants And Boundaries

- The package exposes closed catalog item models and deterministic catalog/readiness functions; readiness is never certification eligibility.
- `__all__` is the complete public surface; any new symbol must be added there deliberately.

### Todos

None.

## Evidence

### Repo-Internal References

- The facade re-exports the catalog version, complete population and non-certifying readiness function. [1]




- Only FinalCatalogItemIdentity and FinalCatalogItemResult remain re-exported typed item models. [5]
