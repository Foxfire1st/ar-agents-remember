# mcp/src/agents_remember/memory/knowledge/records.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

Decodes sealed invariant, family and membership rows from the derived index and computes their read-time content digests.

## Code Commentary

Typed columns, authorship and state-at-origin are decoded under their recorded schema. Revision and membership decoders verify the declared payload seals before returning values. The former row-building, source-anchor and predecessor write helpers were removed. This codec does not insert canonical records or authorize a writer; the index is a projection of admitted text knowledge.

## Evidence

### Repo-Internal References

- `decode_revision_row` owns the current boundary described above. [12]
- `decode_family_revision_row` owns the current boundary described above. [13]
- `decode_member_row` owns the current boundary described above. [14]
- `decode_typed_column` owns the current boundary described above. [15]
