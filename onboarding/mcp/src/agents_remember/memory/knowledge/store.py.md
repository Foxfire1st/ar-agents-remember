# mcp/src/agents_remember/memory/knowledge/store.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

The APSW-backed read surface over a memory tree's derived knowledge index. OpenedKnowledgeStore owns an index path, a bound namespace, the validated schema and a connection. It owns no row writer, approval decision, transport or Git resolution.

## Code Commentary

### Logic

OpenedKnowledgeStore is a frozen context-manager value. Its exit closes the owned handle and never suppresses a failure. It has no resource-lock path.

get_repository and get_invariant read the namespace's identities. list_invariants and list_families enumerate every recorded identity of their kind in stable identity order, without filtering or deriving one kind from another. get_revision reads an exact revision and its predecessor set and delegates seal verification to records.decode_revision_row.

snapshot_identity reports the opened index's logical identity and requires its repository row. generation resolves the validated schema by its exact name. open_existing_knowledge_store delegates to open_read_only_store; both open a present index through open_read_only_database without creating, repairing or writing it. The current store exposes no list_revision_ids method.

### Invariants And Boundaries

- Every exact revision read re-derives the payload seal over the row and predecessor edges.
- The supplied namespace scopes the read queries; the store manufactures neither a namespace nor acceptance.
- Both openers use a connection that cannot write. Only the index builder writes derived-index rows.
- close closes this owned read handle and leaves cache cleanup to its owner; it unlinks no WAL or journal peer.
- Family and membership reads live in their own reader modules and use this opened store.

### Historical boundary — MIK-R26

Canonical repository/invariant/revision creation, candidate locks, immediate-transaction wrappers, batch insert primitives, label mutation, lineage write guards and their mutation refusals were retired. The earlier no-unlink correction remains a bounded resource-ownership lesson: closing a handle is not authority to delete another connection's SQLite recovery files. None of that retired writer account grants a current mutation path here.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References


- The opened read store holds path, namespace, validated schema and read connection. [1]


- Closing the owned read handle unlinks no cache peers. [2]


- The exact revision read decodes the stored row and predecessor set. [3]


- Every invariant and family identity is enumerated in stable order. [4]


- The logical identity is read from the opened index and bound namespace. [9]


- Both retained openers open an existing index read-only without creating or repairing it. [15]


### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
