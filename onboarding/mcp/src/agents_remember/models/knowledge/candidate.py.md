# mcp/src/agents_remember/models/knowledge/candidate.py

## Governing Overview

[models route overview](../overview.md)

## Purpose

Defines portable snapshot and exact candidate-input identities, and a sealed resolved knowledge context.

## Code Commentary

`SnapshotIdentity` is repository_id, schema_version and logical_digest. `ExactCandidateInput` carries the exact tree plus any recorded commit/dirty facts; it does not make a tree an alias for HEAD. `KnowledgeContext` validates its digest and the namespace of the carried snapshot. `context_digest` derives the seal from the other fields. The canonical ChangeBatch, expected-record vocabulary, command union and mutation receipt were removed. A carried opaque reference is a resolved value, not proof that its Git object or task exists.

## Evidence

### Repo-Internal References

- `SnapshotIdentity` owns the current boundary described above. [26]
- `ExactCandidateInput` owns the current boundary described above. [27]
- `KnowledgeContext` owns the current boundary described above. [28]
- `context_digest` owns the current boundary described above. [29]
