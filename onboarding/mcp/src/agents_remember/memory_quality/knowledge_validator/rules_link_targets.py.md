# mcp/src/agents_remember/memory_quality/knowledge_validator/rules_link_targets.py

## Governing Overview

[Area overview](../overview.md)

## Purpose

Registers paired-code existence validation for record anchor and route links.

## Code Commentary

The rule walks candidate record links, ignoring unsupported target kinds and absent anchor paths. Anchor paths require a file; route targets require a directory. Canonical serialized record/target pairs from every base distinguish carried links. Missing targets yield field-specific R22.6-link-target-path findings; merge reporting and its explanation apply only through the existing registry context.

## Invariants And Boundaries

No paired code means no path check here. Carried sync reporting is not a publication exemption: merge_requires_carried and the caller’s leaf-publication policy retain their own authority.

## Evidence Scope

This is a current source account, not an executed test, CODE/MEMORY grade, live producer grant or landing result. No Domain Documentation source is configured for this slice; no external-system guarantee is inferred.

## Evidence

- Registers paired-code existence validation for record anchor and route links. No paired code means no path check here. Carried sync reporting is not a publication exemption: merge_requires_carried and the caller’s leaf-publication policy retain their own authority. [1]
