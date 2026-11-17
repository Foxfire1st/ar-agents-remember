# mcp/tests/test_knowledge_index_access_time.py

## Governing Overview

[Route overview](../overview.md)

## Purpose

Checks index usage bookkeeping, dataset-witness preservation and age/size eviction.

## Code Commentary

An access changes only usage and preserves the identity memo, witnessed by test_access_changes_only_usage_and_preserves_identity_memo

One eviction counts tree-only files and every build namespace together.

## Boundaries

These tests cover usage markers and eviction; build-identity reuse has its own test module.

## Evidence

- An access changes only usage and preserves the identity memo, witnessed by test_access_changes_only_usage_and_preserves_identity_memo [1]
