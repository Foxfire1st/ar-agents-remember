# mcp/src/agents_remember/memory/knowledge/logical.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

Computes the portable logical identity of a selected derived index using the declared schema and deterministic table contents.

## Code Commentary

The one current schema supplies the table/key order; rows are decoded into the logical body and hashed without physical page layout, file path or retrieval time. `logical_body_from_tables` is the current table-input renderer. `dataset_identity` opens read-only, validates the schema and binds exactly one repository before closing; `bound_repository` refuses no or ambiguous repository rows. The removed `logical_digest_of_tables` and `require_bound_repository` names are not current entry points. These readers provide index identity, not canonical dataset publication.

## Evidence

### Repo-Internal References

- `logical_body_from_tables` owns the current boundary described above. [16]
- `logical_digest` owns the current boundary described above. [17]
- `dataset_identity` owns the current boundary described above. [18]
- `bound_repository` owns the current boundary described above. [19]
