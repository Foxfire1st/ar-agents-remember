# mcp/src/agents_remember/memory/knowledge/read_queries.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/read_queries.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-17T03:15+02:00 |
| lastVerifiedCommitHash | `b5a74aee6cdf671c9963f3aba4df6d44b856f697`|
| lastVerifiedCommitDate | 2026-09-18T09:42:44+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l08` uncommitted source; base `1ff1893f44d875073d58af863238501a6be35288` |
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **The declared read order per table, and the refusal of a table this reader does not own.** | `_ORDER_COLUMNS`; `_require_order_column` | mcp/src/agents_remember/memory/knowledge/read_queries.py:32-46; mcp/src/agents_remember/memory/knowledge/read_queries.py:49-55 |
| **The declared read order per table, and the refusal of a table this reader does not own.** | `_ORDER_COLUMNS`; `_require_order_column` | mcp/src/agents_remember/memory/knowledge/read_queries.py:26-55 |
| The identity-label reader and the identity's retained revisions. | `fetch_identity_rows`; `fetch_revision_ids` | mcp/src/agents_remember/memory/knowledge/read_queries.py:46-78 |
| The two revision readers, and the shared row fetcher their order column is checked by. | `fetch_invariant_revisions`; `fetch_family_revisions`; `_fetch_rows_by_ids` | mcp/src/agents_remember/memory/knowledge/read_queries.py:78-133 |
| **The edge readers the frozen family set is derived from, and the family identity of a revision.** | `fetch_memberships_of_families`; `fetch_memberships_of_families_full`; `fetch_family_ids_for_revisions`; `fetch_memberships_of_invariants` | mcp/src/agents_remember/memory/knowledge/read_queries.py:135-210 |
| The path seed's entry point and the claims of the selected invariant set. | `fetch_realizations_at_path`; `fetch_realizations_for_invariants` | mcp/src/agents_remember/memory/knowledge/read_queries.py:208-279 |
| **The shared existence shape, and the four probes that answer "does this snapshot hold this record, by this key".** | `_row_exists`; `invariant_revision_is_recorded`; `family_revision_is_recorded`; `membership_is_recorded`; `realization_claim_is_recorded` | mcp/src/agents_remember/memory/knowledge/read_queries.py:478-484; mcp/src/agents_remember/memory/knowledge/read_queries.py:335-341; mcp/src/agents_remember/memory/knowledge/read_queries.py:311-321; mcp/src/agents_remember/memory/knowledge/read_queries.py:323-331; mcp/src/agents_remember/memory/knowledge/read_queries.py:356-369 |
| **The predecessor-edge union both tables feed, and the reason a consumer must ask each table with its own probe.** | `fetch_predecessor_edges` | mcp/src/agents_remember/memory/knowledge/read_queries.py:455-461 |
| **The one cell decoder a read page and the logical digest share, made public for exactly this reuse.** | `cell_value`; `_cell` | mcp/src/agents_remember/memory/knowledge/logical.py:240-248; mcp/src/agents_remember/memory/knowledge/logical.py:251-263 |
| The declarations these statements are built from. | `CANONICAL_TABLES`; `CANONICAL_COLUMNS` | mcp/src/agents_remember/memory/knowledge/schema.py:31-45; mcp/src/agents_remember/memory/knowledge/schema.py:47-112 |
| **The node that asserts the union identity back against the two per-table edge sets, and the two dangling-edge failure lines.** | "test_a_record_the_other_snapshot_holds_but_the_selection_missed_is_not_an_absence" | mcp/tests/test_knowledge_diff_scope.py:424-530 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T05:00:00+00:00 — 260915-KS-L17 curator (uncommitted change set on `ar/260915-ks-l17`, base `e963a01c`): **re-read this card's claims against the source and re-cited the rows this leaf's additions moved.** The module is the package's one statement module, and this leaf added to it the six order-column registrations and the three projection lookups the Family view uses — beside, and not inside, the retrieval selection's own statements. The existence probes the comparison module consumes were re-cited to their own extents, because a single projected range for four anchors was evidence of nothing. Verification metadata is **not** advanced; the code commit does not exist yet and closeout owns that stamp.

- 2026-09-18T04:40:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **re-read every citation this card carries against the current source and repaired the ranges this leaf's addition moved.** This entry recorded the five declared order columns for the appended tables and why the coverage table orders by its two-endpoint pair. Verification metadata is unchanged and the code commit does not exist yet; closeout owns that stamp.

- 2026-09-17T01:15:00+00:00 — 260915-KS-L8 curator (uncommitted change set on `ar/260915-ks-l08`, base `1ff1893f`): **extended this card with the five readers L8 added and re-derived every citation range against the new bytes.** The module now carries **fifteen** public readers, ten the read half needed and five the comparison added: four existence probes (`invariant_revision_is_recorded`, `family_revision_is_recorded`, `membership_is_recorded`, `realization_claim_is_recorded`) and the predecessor-edge union (`fetch_predecessor_edges`). The card states the reason they exist — **a comparison must distinguish "the other snapshot does not hold this record" from "it holds it and the other side's selection did not reach it"**, and only the first is absence — plus the fact that a claim is looked up **without its anchor** (the comparison asks whether the relationship is still recorded). It records the trap the union creates and the fix the review forced: a consumer must ask each predecessor table with **its own** probe, because asking one table's probe about the other table's endpoint was measured as a false alarm on a legal snapshot (one schema-valid family edge failed the pre-fix assertion at `test_knowledge_diff_scope.py:474`). It also carries the one limit that touches the newest reader: `invariant_revision_is_recorded` is called **0** times on the fixture population (mutation `M23`), so it is a disclosed non-experiment with its bound carried rather than resolved — a gap in the evidence, not a defect in the statement. Verification metadata: lastUpdated advanced, the reviewed candidate moved to `ar/260915-ks-l08`, and the commit fields left at the last real commit because the code commit does not exist and closeout owns the stamp.

- 2026-09-16T21:50:00+00:00 — 260915-KS-l07 curator (uncommitted change set on `ar/260915-ks-l07`, base `4eb2b199`): created this one-to-one card for the read's query layer. It records the two rules that make the readers safe to compose — **table and column names come only from the declared schema manifest while a caller's text is always a bound parameter**, and **the typed JSON columns are decoded by `logical.py`'s one public `cell_value` rather than by a second decoder**, which is what keeps a read page and the logical digest from disagreeing about a stored cell — plus the ordering rule (each table's declared primary key, never insertion order) and the one-snapshot property (no function here opens a connection, begins a transaction or writes). Verification metadata remains empty until closeout stamps the code commit.
