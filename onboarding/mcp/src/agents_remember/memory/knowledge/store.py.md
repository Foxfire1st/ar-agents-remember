# mcp/src/agents_remember/memory/knowledge/store.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

The concrete APSW-backed knowledge store and its one atomic insert-only mutation. The store owns a connection
contract and a candidate mutation; it owns no transport, no approval decision and no Git resolution.

It is also the package's **shared plumbing**: the exclusive candidate lock and the one-immediate-transaction
wrapper live here and are reused by the sibling graph modules, which take the opened store as their first
argument instead of opening a transaction of their own. Since `KS-R03` it additionally exposes the
**in-transaction primitives** the candidate-change batch composes (`insert_invariant_identity`,
`insert_revision_aggregate`, and the module-level `insert_invariant` / `insert_revision` /
`require_same_invariant_predecessors` / `require_acyclic_lineage` / `find_lineage_cycle`), plus
`snapshot_identity()` and `immediate_transaction()`.

## Code Commentary

### Logic

`OpenedKnowledgeStore` is a frozen dataclass holding the database path, the bound `repository_id`, the validated
`KnowledgeSchemaIdentity`, the live `apsw.Connection` and the resource-lock path. It is also a context manager
whose `__exit__` always closes and returns `False` (never suppressing a failure).

Reads: `get_repository`, `get_invariant`, `list_revision_ids` (ordered by revision id) and `get_revision`, which
loads the twelve declared columns and passes them to `records.decode_revision_row` with the predecessor set from
`_predecessors_of`, so every read re-derives the seal.

Two enumerating reads exist for the Intent Reviewer's own use, and they are the only reason a reader can be
handed a subject it was not already pointed at:

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

Mutations, each under `_exclusive_candidate_lock` and inside `_within_immediate`:

- `create_repository` inserts the namespace row; an existing identical row is `no_change`, an existing row with a
  different authority home is refused (`repository_rebind_refusal`).
- `create_invariant` checks scope and delegates the insert to the module-level `insert_invariant` with
  `confirm_repeat=True`. **Two callers ask two different questions about one stored row, and the flag is the
  difference:** the single-record operation treats an identical repeat as a *confirmation* (`no_change`) and
  refuses only a repeat carrying a different label (`duplicate_identity`), while a candidate-batch command passes
  `confirm_repeat=False` and refuses *any* stored identity with the same code — a batch authors new identities, so
  a stored row under one it believed it was creating means the caller's read is stale. The row digest, not the
  label text, is what a later edit names.
- `create_revision` checks scope, seals the draft through `records.sealed_revision_from_draft` (a `ValueError`
  becomes `invalid_payload_refusal`), then the module-level `insert_revision` performs, in order: owning-identity
  availability, the identity reuse check (an already-stored revision → `duplicate_identity`, where the
  single-record operation's `no_change` answer is decided *before* this call by `_insert_revision` comparing the
  stored `payload_digest`), `require_same_invariant_predecessors` (dangling → `invalid_reference`, cross-invariant
  → `invalid_reference` naming both invariants), `require_acyclic_lineage`, the revision INSERT, the predecessor
  edge INSERTs, and `require_referential_integrity` — the last one **skipped when the batch declared pending
  predecessors**, because a predecessor another command has not written yet is a legal deferred-FK violation until
  `COMMIT`.
- `set_invariant_label` delegates the one mutable identity field to `labels.set_invariant_label`, which owns the
  guard.

**The lineage rule no longer lives in this file.** The traversal left `store.py` for
`memory/knowledge/lineage.py`, so one owner serves both the invariant graph (here) and the family graph
(`families.create_family_revision`): `_LINEAGE_EDGES_SQL` → `lineage._INVARIANT_EDGES_SQL`, `_post_insert_lineage`
→ `lineage.post_insert_graph`, `_lineage_edges` → `lineage.invariant_edges`, `_graph_cycle_vertices` →
`lineage.cycle_vertices`, `_descendants` → `lineage.descendants`, and the module-level `_CycleScan` class →
`lineage._CycleScan`. `_require_no_lineage_cycle` was **renamed `_require_acyclic_lineage`** and its body now
calls `lineage.find_cycle`; the refusal it raises is unchanged. What remains here is the invariant half plus the
lock, the transaction wrapper and the openers.

The rule itself is unchanged and still stated once above the guard: `create_revision` refuses with
`lineage_cycle` when inserting the candidate would leave **any** revision in this invariant's lineage graph on a
cycle — equivalently when the candidate itself would be on a cycle, or when a retained revision reachable from the
candidate through predecessors is already on one. It is evaluated over the **post-insert** graph and **before any
row is written**, so a refusal leaves the tables exactly as they were.

`_require_acyclic_lineage` implements both branches from the shared finding: membership of the candidate in the
cycle-vertex set → `candidate_on_cycle=True`; otherwise the reached cycle vertices → `candidate_on_cycle=False`.
`lineage_cycle_members` is the *membership query*, not the write rule: it delegates to `lineage.edges_on_cycle`,
returns the child endpoints of the edges on a cycle through the revision, and returns `()` for a revision that
merely descends from a stored cycle.

`_within_immediate` runs the action inside one `BEGIN IMMEDIATE`: a `KnowledgeRefused` becomes the caller's typed
refusal via `on_refusal`, an `apsw.Error` is mapped through `map_sqlite_error`, and a `KnowledgeStorageError`
propagates because a defect the caller could "handle" as a refusal would be reported as an expected outcome. Its
`failure` keyword is **required** and carries the caller's `SqliteFailureContext` (operation, table, record id),
because a mapped constraint failure cannot know which operation or table it came from; all eleven call sites —
the three here and the eight graph operations — supply it.

`open_knowledge_store` creates or validates the schema at the path; `open_existing_knowledge_store` refuses a
missing path and validates without creating or repairing.

**`close()` unlinks nothing, and that is the correction this leaf made.** The method used to close the connection
and then call `discard_closed_wal_peers`, whose docstring claimed it ran only when the last connection was closed
— an enforcement the code did not have. It was not harmless: SQLite removes its WAL and SHM peers itself when the
last connection closes cleanly, but a **reader** holding a read transaction blocks the checkpoint, so a writer's
committed frames can still be only in the WAL when a closing writer unlinks it. The committed batch was then
absent from the main file and the database was left unreadable until it was rebuilt. The call was therefore
**removed rather than made conditional**, because the function cannot know whether another connection — in this
process or another — still holds the database; a candidate's durability contract is that no journal or WAL file is
ever deleted to make the database look clean, and SQLite already does the right thing on a clean close.

### Conventions

**One resource lock, one transaction.** Every mutation holds the candidate database's exclusive file lock
(`kernel.file_lock.exclusive_file_lock`, reused rather than reimplemented) and runs inside one `BEGIN IMMEDIATE`
transaction, so a refusal can never leave a partial aggregate. A lock capability failure becomes
`lock_capability_unavailable`; an `apsw.BusyError` becomes `candidate_busy` rather than a hang.

**Insert-only.** There is no update or delete path for a revision, no upsert and no standalone predecessor-append
operation: a successor is a new revision naming its exact predecessors, and the database refuses the alternative
even if a future caller forgets. The one mutable field in the whole store is an identity row's `display_label`,
and even that edit names the row digest it expects (`labels.py`).

### Invariants And Boundaries

- **The store never accepts a caller-supplied `payload_digest`; it recomputes the seal (`create_revision` and
  `records.sealed_revision_from_draft`).**
- **Every write is scoped to the bound namespace: `scope_refusal` runs before any DML and returns
  `unauthorized_scope`.**
- **A refusal is inert: all checks that can refuse run before the first INSERT, and the transaction rolls back on
  any later failure, so the offending row counts do not move.**
- **The lineage guard's reach is the post-insert graph; a revision whose own lineage is acyclic can still be
  refused when it descends from a stored cycle. Raw cyclic state can only arise outside the operation, because
  admission accepts only existing predecessors and the vocabulary refuses a self-referencing payload.**
- **The lock and transaction helpers are package plumbing, not a private detail of the invariant operations.**
  The graph modules (`families`, `anchors`, `memberships`, `realizations`) call `exclusive_candidate_lock` and
  `within_immediate` on the opened store, which is what makes "one lock, one transaction" true for every
  mutation in the package rather than only for the ones defined here.
- **This store owns the invariant half only.** The family, anchor, membership and realization tables are written
  by their own modules; a new operation belongs in the module that owns its concept, not here.
- **`require_referential_integrity` is belt-and-braces: deferred composite-FK violations abort at `COMMIT` and
  immediate ones raise at the INSERT, so its `KnowledgeStorageError` path is defensive rather than the ordinary
  enforcement.**
- **The batch-facing helpers are published with no enforcement that a caller holds the lock and the transaction.**
  `write`, `within_immediate`'s sibling `immediate_transaction`, `insert_invariant_identity`,
  `insert_revision_aggregate`, the two module-level inserts and the three graph `insert_*`/`delete_*` helpers all
  assume the caller already owns both, which is what lets the batch span many commands without nesting a second
  `BEGIN IMMEDIATE` or re-taking the lock. Every shipped call site satisfies it — the single-record operations
  open their own transaction and the batch opens one for the whole request — and the private aliases
  (`_within_immediate`, `_write`, `_exclusive_candidate_lock`) keep the earlier spelling working. A future caller
  that invokes one of these outside a transaction would write an autocommitted row silently; that is the
  disclosed exposure, not a property this file enforces.
- **The per-write lineage cost is linear in the object's stored edges (`lineage.invariant_edges` loads the
  invariant's whole edge set); bounded today because one invariant's revision count is the only input, and worth a
  sizing check when bulk or imported revisions arrive (KS-R03/KS-R05).**

### Todos

None recorded for this leaf's slice. The six canonical tables this file does not write (`family`,
`family_revision`, `family_predecessor`, `source_anchor`, `family_member`, `realization_claim`) now have
operations, but they belong to the graph modules and are documented in their own cards; this store still writes
only `repository`, `invariant`, `invariant_revision` and `invariant_predecessor`.

One open item this leaf hands on: `require_referential_integrity` is skipped by `insert_revision` when the batch
declares pending predecessors, and the layer that enforces in that case is the batch's
`require_after_integrity` pass before `COMMIT`, with SQLite's own deferred constraints as the backstop. Do not
"restore" the immediate check without re-reading that decision — checking mid-batch would refuse a batch whose
command order is legal simply because another command's row is not visible yet.

One item this leaf **closes**: `close()` used to call `discard_closed_wal_peers` unconditionally. Do not
reintroduce a peer unlink on any close path in this package — the WAL/SHM files beside a candidate are SQLite's
own recovery state, a reader can block the checkpoint that would have made the unlink safe, and the durability
node that reaches the failure is
`mcp/tests/test_knowledge_candidate_workspace.py::test_a_live_reader_does_not_let_the_write_boundarys_close_lose_the_commit`.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The opened store: its bound namespace, validated schema, connection and lock path — re-cited against the working tree, where the class docstring now names the sibling graph owners. [1]
- **The close that unlinks nothing**, and the reason the peer unlink was removed rather than made conditional. [2]
- The read surface, including the seal-verifying single-revision read. [3]
- **The two enumerating reads the Intent Reviewer's entry list is built on: every recorded invariant and family identity, ordered by the identity's own column, with no filter and no count — because a reader that must be handed a subject cannot enumerate a candidate it was not pointed at.** [4]
- The one atomic insert-only revision operation and its ordered checks. [5]
- The two-caller identity contract: `confirm_repeat` decides whether a stored identity is a confirmation or a stale read. [6]
- The module-level revision aggregate insert, including the pending-predecessor skip of the immediate FK check. [7]
- The predecessor ownership rule with its batch-declared set, and the single-record lineage rule that can accept wider edges. [8]
- The batch-facing in-transaction helpers and the live identity read the whole snapshot half resolves against. [9]
- The membership query, which is not the write rule. [10]
- The transaction and lock boundary, with its required failure context and propagate-a-defect rule, now published with private aliases. [11]
- The write helper the batch and the single-record operations share. [12]
- The label-edit delegation and the module that owns the guard. [13]
- The graph modules that reuse this store's lock and transaction helpers. [14]
- The create-versus-reopen open functions. [15]
- The reused lock primitive this store does not reimplement. [16]
- The node that pins the two-caller identity contract on the single-record side. [17]
- The node that would fail if a close-time peer unlink came back. [18]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
