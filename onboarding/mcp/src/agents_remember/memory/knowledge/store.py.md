# mcp/src/agents_remember/memory/knowledge/store.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/store.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T22:40+02:00 |
| lastVerifiedCommitHash | `27242ecbefd79f2e8fbc6db32e02013fa8298ba3`|
| lastVerifiedCommitDate | 2026-09-16T08:41:27+02:00|
| governingOverview | `../../overview.md` |

## Governing Overview

[memory route overview](../../overview.md)

## Purpose

The concrete APSW-backed knowledge store and its one atomic insert-only mutation. The store owns a connection
contract and a candidate mutation; it owns no transport, no approval decision and no Git resolution.

It is also the package's **shared plumbing**: the exclusive candidate lock and the one-immediate-transaction
wrapper live here and are reused by the sibling graph modules, which take the opened store as their first
argument instead of opening a transaction of their own.

## Code Commentary

### Logic

`OpenedKnowledgeStore` is a frozen dataclass holding the database path, the bound `repository_id`, the validated
`KnowledgeSchemaIdentity`, the live `apsw.Connection` and the resource-lock path. It is also a context manager
whose `__exit__` always closes and returns `False` (never suppressing a failure).

Reads: `get_repository`, `get_invariant`, `list_revision_ids` (ordered by revision id) and `get_revision`, which
loads the twelve declared columns and passes them to `records.decode_revision_row` with the predecessor set from
`_predecessors_of`, so every read re-derives the seal.

Mutations, each under `_exclusive_candidate_lock` and inside `_within_immediate`:

- `create_repository` inserts the namespace row; an existing identical row is `no_change`, an existing row with a
  different authority home is refused (`repository_rebind_refusal`).
- `create_invariant` checks scope, then treats a stored row with the same label as `no_change` and one with a
  different label as `duplicate_identity`.
- `create_revision` checks scope, seals the draft through `records.sealed_revision_from_draft` (a `ValueError`
  becomes `invalid_payload_refusal`), then `_insert_revision` performs, in order: identity reuse check
  (same digest → `no_change`; different digest → `duplicate_identity`), unknown-invariant check,
  `_require_same_invariant_predecessors` (dangling → `invalid_reference`, cross-invariant → `invalid_reference`
  naming both invariants), `_require_acyclic_lineage`, the revision INSERT, the predecessor edge INSERTs, and
  `_require_referential_integrity`.

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

### Conventions

**One resource lock, one transaction.** Every mutation holds the candidate database's exclusive file lock
(`kernel.file_lock.exclusive_file_lock`, reused rather than reimplemented) and runs inside one `BEGIN IMMEDIATE`
transaction, so a refusal can never leave a partial aggregate. A lock capability failure becomes
`lock_capability_unavailable`; an `apsw.BusyError` becomes `candidate_busy` rather than a hang.

**Insert-only.** There is no update or delete path for a revision, no upsert and no standalone predecessor-append
operation: a successor is a new revision naming its exact predecessors, and the database refuses the alternative
even if a future caller forgets.

### Invariants And Boundaries

- The store never accepts a caller-supplied `payload_digest`; it recomputes the seal (`create_revision` and
  `records.sealed_revision_from_draft`).
- Every write is scoped to the bound namespace: `scope_refusal` runs before any DML and returns
  `unauthorized_scope`.
- A refusal is inert: all checks that can refuse run before the first INSERT, and the transaction rolls back on
  any later failure, so the offending row counts do not move.
- The lineage guard's reach is the **post-insert graph**; a revision whose own lineage is acyclic can still be
  refused when it descends from a stored cycle. Raw cyclic state can only arise outside the operation, because
  admission accepts only existing predecessors and the vocabulary refuses a self-referencing payload.
- **The lock and transaction helpers are package plumbing, not a private detail of the invariant operations.**
  The graph modules (`families`, `anchors`, `memberships`, `realizations`) call `_exclusive_candidate_lock` and
  `_within_immediate` on the opened store, which is what makes "one lock, one transaction" true for every
  mutation in the package rather than only for the ones defined here.
- **This store owns the invariant half only.** The family, anchor, membership and realization tables are written
  by their own modules; a new operation belongs in the module that owns its concept, not here.
- `_require_referential_integrity` is belt-and-braces: deferred composite-FK violations abort at `COMMIT` and
  immediate ones raise at the INSERT, so its `KnowledgeStorageError` path is defensive rather than the ordinary
  enforcement.
- The per-write lineage cost is linear in the object's stored edges (`lineage.invariant_edges` loads the
  invariant's whole edge set); bounded today because one invariant's revision count is the only input, and worth a
  sizing check when bulk or imported revisions arrive (KS-R03/KS-R05).

### Todos

None recorded for this leaf's slice. The six canonical tables this file does not write (`family`,
`family_revision`, `family_predecessor`, `source_anchor`, `family_member`, `realization_claim`) now have
operations, but they belong to the graph modules and are documented in their own cards; this store still writes
only `repository`, `invariant`, `invariant_revision` and `invariant_predecessor`.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The opened store: its bound namespace, validated schema, connection and lock path — re-cited against the working tree, where the class docstring now names the sibling graph owners. | `OpenedKnowledgeStore` | mcp/src/agents_remember/memory/knowledge/store.py:86-104 |
| The read surface, including the seal-verifying single-revision read. | `get_revision`; `get_invariant`; `list_revision_ids`; `get_repository` | mcp/src/agents_remember/memory/knowledge/store.py:120-177 |
| The one atomic insert-only revision operation and its ordered checks. | `create_revision`; `_insert_revision` | mcp/src/agents_remember/memory/knowledge/store.py:224-259; mcp/src/agents_remember/memory/knowledge/store.py:296-344 |
| The lineage rule as stated once, including the post-insert scope and the before-any-write evaluation. | "The lineage rule, stated once" | mcp/src/agents_remember/memory/knowledge/store.py:315-326 |
| The renamed two-branch enforcement, which now delegates to the shared lineage module. | `_require_acyclic_lineage` | mcp/src/agents_remember/memory/knowledge/store.py:391-417 |
| The shared lineage traversal that left this file, and the family graph that applies the same rule. | `find_cycle`; `cycle_vertices`; `_CycleScan`; `_require_acyclic_family` | mcp/src/agents_remember/memory/knowledge/lineage.py:71-86; mcp/src/agents_remember/memory/knowledge/lineage.py:128-148; mcp/src/agents_remember/memory/knowledge/lineage.py:171-239; mcp/src/agents_remember/memory/knowledge/families.py:186-203 |
| The membership query, which is not the write rule. | `lineage_cycle_members` | mcp/src/agents_remember/memory/knowledge/store.py:370-390 |
| The transaction and lock boundary, with its required failure context and propagate-a-defect rule. | `_within_immediate`; `_exclusive_candidate_lock`; `SqliteFailureContext` | mcp/src/agents_remember/memory/knowledge/store.py:475-498; mcp/src/agents_remember/memory/knowledge/store.py:509-522; mcp/src/agents_remember/memory/knowledge/refusals.py:596-607 |
| The graph modules that reuse this store's lock and transaction helpers. | `create_family_revision`; `create_source_anchor`; `create_family_member`; `create_realization_claim` | mcp/src/agents_remember/memory/knowledge/families.py:112-141; mcp/src/agents_remember/memory/knowledge/anchors.py:49-70; mcp/src/agents_remember/memory/knowledge/memberships.py:59-80; mcp/src/agents_remember/memory/knowledge/realizations.py:61-83 |
| The create-versus-reopen open functions. | `open_knowledge_store`; `open_existing_knowledge_store` | mcp/src/agents_remember/memory/knowledge/store.py:523-542; mcp/src/agents_remember/memory/knowledge/store.py:543-556 |
| The reused lock primitive this store does not reimplement. | `exclusive_file_lock` | mcp/src/agents_remember/kernel/file_lock.py |
| The requirement packet the four properties belong to. | `KS-R01@v1` | ar-coordination/tasks/agents-remember/260915_knowledge-substrate/requirements/KS-R01-v1-immutable-knowledge-identity.md |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-16T08:24+02:00 — 260915-KS-L2 curator (uncommitted change set on `ar/260915-ks-l02`, base `60e0820e`): **superseded the L1 account of where the lineage rule lives.** The earlier card described `_require_no_lineage_cycle`, `_graph_cycle_vertices`, `_post_insert_lineage`, `_descendants` and `_CycleScan` as this file's own, and named the "seven canonical tables … have no operations". The traversal has left for `memory/knowledge/lineage.py` so one owner serves both the invariant and the new family lineage graph, the guard was renamed `_require_acyclic_lineage` and now delegates, and `_within_immediate` gained a required `SqliteFailureContext` so a mapped constraint failure can name the operation and table it came from. The card now also records this store's shared-plumbing role for the four graph modules and that it still writes only its own four tables. Verification metadata remains empty until closeout stamps the code commit.
- 2026-09-15T22:40+02:00 — 260915-KS-L1 curator (uncommitted change set on `ar/260915-ks-l01`, base `67b21aeb`): created this one-to-one card for the new concrete knowledge store. It records the one-lock/one-transaction rule, the insert-only contract, the post-insert reach of the lineage guard (the round-2/round-3 review outcome for sealed findings `RV-2` and `RV-4`), the defensive status of the deferred-FK check, and the linear lineage cost. Verification metadata remains empty until closeout stamps the code commit.
