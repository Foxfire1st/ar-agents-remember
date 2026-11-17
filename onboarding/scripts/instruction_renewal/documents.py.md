# scripts/instruction_renewal/documents.py

## Governing Overview

[Overview](../../overview.md)

## Purpose

Replaces generated JSON members while preserving surrounding authored document text.

## Code Commentary

The replacement helpers locate a top-level JSON value and replace that complete value, inserting a missing member when necessary. They do not rewrite authored neighboring members. The derived helper selects the derived member rather than treating generated values as new authoring authority.

## Relationships

The renewal planner uses these byte-producing helpers for authored documents with generated sections; it owns when the resulting bytes are published.

## Evidence

- Top-level member replacement preserves the surrounding document bytes. [1]
