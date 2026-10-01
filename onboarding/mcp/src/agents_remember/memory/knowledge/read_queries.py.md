# mcp/src/agents_remember/memory/knowledge/read_queries.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**The recorded-scope read queries: one statement per lookup, all addressed at one namespace.** Every
function takes the caller's connection and never opens one, so a selection's statements all run inside
whatever transaction the caller holds and therefore observe **one snapshot**.

## Code Commentary

### Logic

**Fifteen public readers** — ten the read half needed, five L8's comparison added — each one statement:

| Reader | What it returns |
| --- | --- |
| `fetch_revision_ids` | every retained revision id of one identity, in the table's **declared order** |
| `fetch_identity_rows` | the identity table's `display_label` rows, so a page can carry the authored label without a second query per item |
| `fetch_invariant_revisions` / `fetch_family_revisions` | the revision rows of the selected sets, decoded |
| `fetch_realizations_at_path` | the recorded claims at one repository/path — the path seed's entry point |
| `fetch_realizations_for_invariants` | the claims of every selected invariant revision, with their anchors |
| `fetch_memberships_of_invariants` | the membership rows that cite one of a set of invariant revisions — how `F0` is derived from recorded edges |
| `fetch_memberships_of_families` / `..._full` | the member revision ids of the frozen family set, and the same rows with their provenance |
| `fetch_family_ids_for_revisions` | the family identity each family revision belongs to |
| `invariant_revision_is_recorded` / `family_revision_is_recorded` | whether one snapshot holds one named revision of each kind, by exact identity |
| `membership_is_recorded` | whether one snapshot holds one named `member_id` |
| `realization_claim_is_recorded` | whether one snapshot holds one named claim — **looked up without its anchor**, because a comparison asks whether the *relationship* is still recorded and a claim whose anchor is a separate row is still that relationship |
| `fetch_predecessor_edges` | every `(successor_revision_id, predecessor_revision_id)` edge one snapshot records, as the `UNION ALL` of `invariant_predecessor` and `family_predecessor` |

**The five existence and predecessor readers are L8's addition, and they exist for one reason: a
comparison has to distinguish three states a single read never needs to tell apart** — a record the other
snapshot **does not hold**, a record it holds but the other side's declared selection **did not reach**,
and a record both sides selected. Only the first is absence; the second is a fact about the selection, and
reporting it as a deletion is the design's own named misreading. These lookups answer the first question
and nothing else, by exact identity, one statement each; the caller already holds the selected set that
answers the second. `_row_exists` is the shared shape: a `SELECT 1` whose row presence is the answer.

**`fetch_predecessor_edges` deliberately unions both predecessor tables**, because a comparison asks the
same question of either kind — and the union is why a consumer must **not** ask one table's probe about
the other table's endpoint: that was measured as a false alarm on a legal snapshot (one schema-valid
family edge made the pre-diff assertion fail at `test_knowledge_diff_scope.py:474`), and the fix was to
split the per-table question rather than to narrow the union. The edges returned are **authored**: they
are what an author declared when they wrote the successor, so a comparison pairs two revisions without
comparing labels, versions or insertion order — none of which an author guarantees.

**Two rules make these readers safe to compose, and both are contract rather than style:**

- **Table and column names come only from the declared manifest** in
  `agents_remember.memory.knowledge.schema`; a caller's text reaches a statement as a **bound parameter**
  and never as an identifier. `_require_order_column` refuses a table this reader does not own, so a
  name that is not in `_ORDER_COLUMNS` is an error rather than a silently interpolated string.
- **The typed JSON columns are decoded by `logical.py`, not by a second decoder here.** `logical.cell_value`
  is the public spelling of the decoder every reader of a stored row uses, so a read page and the logical
  digest cannot disagree about what a stored cell means. A second decoder would be a second definition of
  the dataset's identity.

**Ordering is by stored key, never by insertion order.** `_ORDER_COLUMNS` names each table's DDL primary
key — which is not every table's leading column list — so two datasets holding the same records read in
the same order and page identically. The selection layer's own final sort is a second, independent
statement of the item order (see `read.py`'s `_sort_key`).

**Five declared order columns for the appended tables.** `evidence_claim` and its two subject join tables are ordered by `claim_id`, the coverage table by its two-endpoint key in the order the DDL names them, and `verification_observation` by `observation_id`. The column named is the *second* of each key because the first is the namespace: a table keyed `(repository_id, identity)` is ordered by its identity. Ordering a read by a stored key rather than by insertion order is what makes two datasets holding the same records page identically, and the coverage table's pair key is why a relation's rows are ordered by the pair rather than by either half.

### Conventions

- Every function is `(connection, repository_id, …) -> tuple[...]`; nothing is cached between calls, so a
  selection cannot accidentally read a row from a different statement's snapshot.
- Rows come back as decoded mappings for the revision readers and as plain tuples for the edge readers,
  matching what the caller needs rather than one uniform shape.
- A table this reader does not declare an order for is a `KnowledgeStorageError` (a defect), not a
  refusal code: it is a programming error at the call site.

### Invariants And Boundaries

- **One connection, one snapshot.** Nothing here opens a connection, begins a transaction or commits; the
  caller's handle decides all three.
- **No writes.** Every statement is a `SELECT`.
- **The namespace is always bound.** `repository_id` is a parameter of every statement, so a selection
  cannot read a row belonging to another repository.
- **Boundary.** This module reads. It does not select (the policy is `read.py`'s), does not resolve an
  anchor, does not page and does not decide a refusal.

### Todos

None recorded. One carried limit touches this module's newest reader: `invariant_revision_is_recorded` is
called **0** times by one comparison on the leaf's fixture population (mutation `M23`), so it is a
**disclosed non-experiment with its reachability bound carried rather than resolved** (ledger-facing, with
its closing input named in `memory/knowledge/diff.py`'s card). That is a gap in the evidence, not a defect
in this reader: the statement is correct and is exercised by the comparison's other kinds.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- **The declared read order per table, and the refusal of a table this reader does not own.** [1]
- **The declared read order per table, and the refusal of a table this reader does not own.** [2]
- The identity-label reader and the identity's retained revisions. [3]
- The two revision readers, and the shared row fetcher their order column is checked by. [4]
- **The edge readers the frozen family set is derived from, and the family identity of a revision.** [5]
- The path seed's entry point and the claims of the selected invariant set. [6]
- **The shared existence shape, and the four probes that answer "does this snapshot hold this record, by this key".** [7]
- **The predecessor-edge union both tables feed, and the reason a consumer must ask each table with its own probe.** [8]
- **The one cell decoder a read page and the logical digest share, made public for exactly this reuse.** [9]
- The declarations these statements are built from. [10]
- **The node that asserts the union identity back against the two per-table edge sets, and the two dangling-edge failure lines.** [11]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
