# mcp/src/agents_remember/memory/knowledge/lineage.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/lineage.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T08:24+02:00 |
| lastVerifiedCommitHash | `27242ecbefd79f2e8fbc6db32e02013fa8298ba3`|
| lastVerifiedCommitDate | 2026-09-16T08:41:27+02:00|
| governingOverview | `../../overview.md` |

## Governing Overview

[memory route overview](../../overview.md)

## Purpose

**One acyclic-lineage rule, shared by the invariant and the family lineage graphs.** Both graphs are
predecessor edges between revisions of one object, and both refuse a write that would leave *any*
revision of that object on a cycle. The rule therefore lives here once and is applied twice instead of
being re-derived per relation:

- `store.create_revision` applies it over the stored `invariant_predecessor` edges;
- `families.create_family_revision` applies it over the stored `family_predecessor` edges.

This module owns no table and writes no row. It owns the traversal and the two edge queries, and it is
the reason the two graphs cannot drift into describing different rules.

## Code Commentary

### Logic

- `find_cycle` is the write-path rule. It builds the post-insert graph for the candidate, finds every
  cycle vertex, and returns a `CycleFinding` in one of two branches: the candidate itself is on a
  cycle (`candidate_on_cycle=True`, every cycle vertex is named), or the candidate merely descends from
  a stored cycle (`candidate_on_cycle=False`, only the cycle vertices it reaches are named). The two
  branches exist because the remedies differ, not because the wording is being reused.
- **The reach is deliberately wider than adjacency.** A candidate is refused when inserting it would
  leave it on a cycle **or** when a retained revision reachable from it through predecessors is
  already on one. The second branch exists because a stored cycle is a fact about the object's past
  that a new successor must not silently inherit.
- `edges_on_cycle` is the *membership query*, not the write rule. Only edges actually on a cycle
  through the revision are members, so a revision that descends from a stored cycle without being on
  it reports an empty set here — the write path refuses it for a different reason and says so in its
  own words.
- `cycle_vertices` classifies with Tarjan's strongly-connected components: a vertex is on a cycle when
  it belongs to a component of more than one vertex, or has an edge to itself. `_CycleScan` keeps the
  traversal in one object with an explicit work stack rather than recursion, so a long lineage chain
  does not put the interpreter's recursion limit in the middle of a write.
- `invariant_edges` / `family_edges` are the two edge queries, each a single `SELECT` filtered by the
  repository and the owning object.

### Conventions

- The two edge statements are module constants keyed to their declared tables. Adding a third lineage
  graph means adding a statement and a thin accessor, not a third traversal.
- The traversal is written as Python rather than a recursive SQL CTE, and the docstring records why:
  SQLite's `UNION` deduplication changes which rows a recursive CTE revisits, so a traversal written
  that way does not close a cycle.
- `post_insert_graph` and `descendants` are exported so a caller can reason about the same graph the
  guard reasoned about, instead of rebuilding it.

### Invariants And Boundaries

- **The rule is evaluated over the post-insert graph and before any row is written**, so a refusal
  leaves the tables exactly as they were.
- **Raw cyclic state can only arise outside these operations.** Admission requires every declared
  predecessor to exist already and the vocabulary refuses a self-referencing payload, so no operation
  can build a cycle; that is why the guard is demonstrated against a graph written by hand.
- **Both branches must be worded for the branch they describe.** The descending branch must not claim
  self-reachability, because nothing points at that candidate.
- **Determinism.** Every iteration and every returned member set is sorted, so the refusal text and the
  membership tuple do not depend on dictionary or database row order.
- **Boundary.** This module decides acyclicity only. Whether a predecessor exists, whether it belongs to
  the same object, and whether the payload is well formed are the calling operation's checks; the
  refusal wording is `refusals.py`'s, not this module's.

### Todos

None recorded for this slice. The linear cost of loading one object's whole edge set is bounded by that
object's revision count and is noted in the route overview as worth a sizing check when bulk or
imported revisions arrive.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The two applications this one rule serves, stated in the module docstring. | "One acyclic-lineage rule, shared by the invariant and the family lineage graphs." | mcp/src/agents_remember/memory/knowledge/lineage.py:1-1 |
| The write-path rule and its two branches. | `find_cycle`; `CycleFinding` | mcp/src/agents_remember/memory/knowledge/lineage.py:71-86; mcp/src/agents_remember/memory/knowledge/lineage.py:41-52 |
| The membership query, which is not the write rule. | `edges_on_cycle` | mcp/src/agents_remember/memory/knowledge/lineage.py:89-109 |
| The post-insert graph construction the guard reasons over. | `post_insert_graph`; `descendants` | mcp/src/agents_remember/memory/knowledge/lineage.py:112-125; mcp/src/agents_remember/memory/knowledge/lineage.py:151-162 |
| The Tarjan classification and its reason for not being a recursive CTE. | `cycle_vertices`; `_CycleScan` | mcp/src/agents_remember/memory/knowledge/lineage.py:128-148; mcp/src/agents_remember/memory/knowledge/lineage.py:171-239 |
| The two edges queries, one per lineage graph. | `invariant_edges`; `family_edges` | mcp/src/agents_remember/memory/knowledge/lineage.py:55-61; mcp/src/agents_remember/memory/knowledge/lineage.py:63-68 |
| The invariant-side application and the rule it states once above the guard. | `_require_acyclic_lineage` | mcp/src/agents_remember/memory/knowledge/store.py:391-417 |
| The family-side application, which reuses this rule rather than restating it. | `_require_acyclic_family` | mcp/src/agents_remember/memory/knowledge/families.py:186-203 |
| The two-branch refusal wording, shared so the relations cannot describe different rules. | `_lineage_cycle_wording`; `lineage_cycle_refusal`; `family_lineage_cycle_refusal` | mcp/src/agents_remember/memory/knowledge/refusals.py:290-309; mcp/src/agents_remember/memory/knowledge/refusals.py:238-264; mcp/src/agents_remember/memory/knowledge/refusals.py:265-286 |
| The membership query the store still exposes, delegating to this module. | `lineage_cycle_members` | mcp/src/agents_remember/memory/knowledge/store.py:370-390 |
| The declared predecessor tables this module reads. | `invariant_predecessor`; `family_predecessor`; `family_predecessor_parent_endpoint` | mcp/src/agents_remember/memory/knowledge/schema.py:157-172; mcp/src/agents_remember/memory/knowledge/schema.py:202-217; mcp/src/agents_remember/memory/knowledge/schema.py:273-274 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-16T08:24+02:00 — 260915-KS-L2 curator (uncommitted change set on `ar/260915-ks-l02`, base `60e0820e`): created this one-to-one card for the extracted shared lineage rule. It records that the rule left `store.py` so one owner serves both graphs, the deliberate second branch whose reach is wider than adjacency, the distinction between the write-path rule and the membership query, and the recorded reason the traversal is Python rather than a recursive SQL CTE. Verification metadata remains empty until closeout stamps the code commit.
