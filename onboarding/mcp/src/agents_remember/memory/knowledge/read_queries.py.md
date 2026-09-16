# mcp/src/agents_remember/memory/knowledge/read_queries.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/read_queries.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T23:50+02:00 |
| lastVerifiedCommitHash | `1ff1893f44d875073d58af863238501a6be35288`|
| lastVerifiedCommitDate | 2026-09-16T23:58:57+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l07` uncommitted source; base `4eb2b1992f6183fba06e9f31aa664d9a93094c26` |
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**The recorded-scope read queries: one statement per lookup, all addressed at one namespace.** Every
function takes the caller's connection and never opens one, so a selection's statements all run inside
whatever transaction the caller holds and therefore observe **one snapshot**.

## Code Commentary

### Logic

Ten readers, each one statement:

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

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **The declared read order per table, and the refusal of a table this reader does not own.** | `_ORDER_COLUMNS`; `_require_order_column` | mcp/src/agents_remember/memory/knowledge/read_queries.py:26-43 |
| The identity-label reader and the identity's retained revisions. | `fetch_identity_rows`; `fetch_revision_ids` | mcp/src/agents_remember/memory/knowledge/read_queries.py:46-76 |
| The two revision readers. | `fetch_invariant_revisions`; `fetch_family_revisions` | mcp/src/agents_remember/memory/knowledge/read_queries.py:78-133 |
| **The edge readers the frozen family set is derived from, and the family identity of a revision.** | `fetch_memberships_of_families`; `fetch_memberships_of_families_full`; `fetch_family_ids_for_revisions`; `fetch_memberships_of_invariants` | mcp/src/agents_remember/memory/knowledge/read_queries.py:135-207 |
| The path seed's entry point and the claims of the selected invariant set. | `fetch_realizations_at_path`; `fetch_realizations_for_invariants` | mcp/src/agents_remember/memory/knowledge/read_queries.py:208-279 |
| **The one cell decoder a read page and the logical digest share, made public for exactly this reuse.** | `cell_value`; `_cell` | mcp/src/agents_remember/memory/knowledge/logical.py:224-232; mcp/src/agents_remember/memory/knowledge/logical.py:235-247 |
| The declarations these statements are built from. | `CANONICAL_TABLES`; `CANONICAL_COLUMNS` | mcp/src/agents_remember/memory/knowledge/schema.py:31-45; mcp/src/agents_remember/memory/knowledge/schema.py:47-112 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-16T23:50+02:00 — 260915-KS-l07 curator (uncommitted change set on `ar/260915-ks-l07`, base `4eb2b199`): created this one-to-one card for the read's query layer. It records the two rules that make the readers safe to compose — **table and column names come only from the declared schema manifest while a caller's text is always a bound parameter**, and **the typed JSON columns are decoded by `logical.py`'s one public `cell_value` rather than by a second decoder**, which is what keeps a read page and the logical digest from disagreeing about a stored cell — plus the ordering rule (each table's declared primary key, never insertion order) and the one-snapshot property (no function here opens a connection, begins a transaction or writes). Verification metadata remains empty until closeout stamps the code commit.
