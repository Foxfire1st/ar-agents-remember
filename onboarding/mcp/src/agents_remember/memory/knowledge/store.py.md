# mcp/src/agents_remember/memory/knowledge/store.py

## Governing Overview


[memory route overview](../overview.md)

## Purpose


The APSW-backed read surface over a memory tree's derived knowledge index. OpenedKnowledgeStore owns an index path, a bound namespace, the validated schema and a connection. It owns no row writer, approval decision, transport or Git resolution.

## Code Commentary


### Logic

OpenedKnowledgeStore is a frozen context-manager value. Its exit closes the owned handle and never suppresses a failure. It has no resource-lock path.

get_repository and get_invariant read the namespace's identities. list_invariants and list_families enumerate every recorded identity of their kind in stable identity order, without filtering or deriving one kind from another. get_revision reads an exact revision with an empty predecessor set — text records are numbered revisions of one file and hold no predecessor edge (MIK-R74 rule 1) — and delegates seal verification to records.decode_revision_row.

- `list_invariants` returns every invariant identity the namespace records — `repository_id`, `invariant_id`,
  `display_label`, `label_provenance` — decoded through `records.decode_invariant_row` and **ordered by the
  identity's own column**, so two runs over one snapshot agree without a tiebreak this reader chose. The source
  docstring states the reason a subject enumerator has to exist at all: "a reader that must be handed a subject
  before it can list the candidates cannot enumerate a candidate it was not pointed at."
- `list_families` is the same enumeration for the surface's other admitted subject kind, read the same way
  rather than derived from the invariant list, because a family identity is not a projection of an invariant and
  the two subject kinds are peers.

Neither is a selection rule: both return **every** recorded identity, apply no filter and compute no count. What
the review's entry list does with them — comparing each identity and dropping the ones the comparison refuses —
belongs to `application/knowledge_review.py`, not here.

snapshot_identity reports the opened index's logical identity and requires its repository row. generation resolves the validated schema by its exact name. open_existing_knowledge_store delegates to open_read_only_store; both open a present index through open_read_only_database without creating, repairing or writing it. The current store exposes no list_revision_ids method.

**`close()` unlinks nothing, and that is the correction this leaf made.** The method used to close the connection
and then call `discard_closed_wal_peers`, whose docstring claimed it ran only when the last connection was closed
— an enforcement the code did not have. It was not harmless: SQLite removes its WAL and SHM peers itself when the
last connection closes cleanly, but a **reader** holding a read transaction blocks the checkpoint, so a writer's
committed frames can still be only in the WAL when a closing writer unlinks it. The committed batch was then
absent from the main file and the database was left unreadable until it was rebuilt. The call was therefore
**removed rather than made conditional**, because the function cannot know whether another connection — in this
process or another — still holds the database; a candidate's durability contract is that no journal or WAL file is
ever deleted to make the database look clean, and SQLite already does the right thing on a clean close.

### Invariants And Boundaries

- Every exact revision read verifies the stored seal as recorded; decoded revisions carry no predecessors.
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



- `get_revision` reads one revision row by repository and revision id and decodes it with the stored seal verified; a text record holds no predecessor edge, so the decoded revision carries no predecessors. [3]



- Every invariant and family identity is enumerated in stable order. [4]


- The logical identity is read from the opened index and bound namespace. [9]


- Both retained openers open an existing index read-only without creating or repairing it. [15]


- **The close that unlinks nothing**, and the reason the peer unlink was removed rather than made conditional. [16]

- The read surface, including the seal-verifying single-revision read. [17]

- **The two enumerating reads the Intent Reviewer's entry list is built on: every recorded invariant and family identity, ordered by the identity's own column, with no filter and no count — because a reader that must be handed a subject cannot enumerate a candidate it was not pointed at.** [18]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
