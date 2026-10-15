# mcp/src/agents_remember/application/knowledge_worklist/equal_changes.py

## Governing Overview

[Application layer overview](../overview.md)

## Purpose

Groups exact before/candidate blob-pair changes for paths already classified as uncovered; it does not decide coverage or currentness.

## Code Commentary

The input paths are deduplicated and sorted. Paths absent on both sides are skipped. Within each equal blob-pair bucket, the first card-bearing path is representative, or the first path when no card exists. Only that representative and cardless members enter its group; another path with its own card keeps a separate judgment. Singleton groups are omitted, and group_representatives supplies the reverse map. Equality is two-sided blob equality, not a filename or generated-copy declaration.

## Invariants And Boundaries

Coverage must be supplied by its K_B owner. Neither equal bytes nor this grouping authorizes an invariant judgment or erases another card’s onboarding duty.

## Evidence Scope

This source account is not a test result or an execution, permission, CODE/MEMORY acceptance or landing claim. No Domain Documentation source is configured for this slice; implementation facts are grounded in the concrete source below, with no asserted external-system contract.

## Evidence

- Groups exact before/candidate blob-pair changes for paths already classified as uncovered; it does not decide coverage or currentness. Coverage must be supplied by its K_B owner. Neither equal bytes nor this grouping authorizes an invariant judgment or erases another card’s onboarding duty. [1]
