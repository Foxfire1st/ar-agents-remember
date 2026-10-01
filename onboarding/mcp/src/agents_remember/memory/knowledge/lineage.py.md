# mcp/src/agents_remember/memory/knowledge/lineage.py

## Governing Overview

[memory route overview](../overview.md)

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
- `find_cycle` takes `extra_predecessors`: the declared edges of **other** revisions authored in the
  same batch. A batch may author several revisions at once, so the graph a candidate has to be judged
  against is the stored graph plus every edge the batch declares — including edges between two
  revisions that do not exist yet. Judging without them would let a batch write a cycle that neither
  revision could have written alone.
- `declared_cycle` is the batch-aware caller, and since `KS-R03` it is a real one. It gathers the edges
  a batch declares, judges each *declaring* revision with `find_cycle`, and supplies that revision's
  wider edge set through an `extras` callable. `batch_preconditions._require_declared_acyclic` calls it
  with `extras=_wider_edges`, which returns the other declared revisions' edges. **This call site is
  the only one that supplies `extra_predecessors`**: `store.require_acyclic_lineage` uses the default
  and is the single-record rule, so the parameter is wired rather than merely declared. The earlier
  account of this module said the mechanism existed while no caller passed a value; that claim was
  false and is corrected here.
- Only the declaring revisions are reported. A stored revision's position was settled when it was
  written, and a cycle that merely passes through one is already refusable by the single-record rule.
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
  guard reasoned about, instead of rebuilding it. `post_insert_graph` folds `extra_predecessors` into
  the graph exactly as stored edges, which is what makes an intra-batch cycle visible to the same rule.
- The batch path never grows a second cycle rule. `batch_preconditions` gathers the edge sets and asks
  this module; a local graph build there would be the drift this module exists to prevent.

### Invariants And Boundaries

- **The rule is evaluated over the post-insert graph and before any row is written**, so a refusal
  leaves the tables exactly as they were.
- **Raw cyclic state can only arise outside these operations.** Admission requires every declared
  predecessor to exist already and the vocabulary refuses a self-referencing payload, so no operation
  can build a cycle; that is why the guard is demonstrated against a graph written by hand.
- **A judgement must reach the shared rule to count as enforcement.** The batch's declared-edge
  exclusion is proven by neutering `find_cycle` and watching the refusal disappear and three named
  nodes fail; a docstring or a wrapper may not claim an enforcement no caller performs.
- **One caller supplies wider edges.** `declared_cycle` is that caller; `require_acyclic_lineage`'s
  default is the single-record rule. Adding a second supplier would be a second rule in disguise.
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

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The three applications this one rule serves, stated in the module docstring. [1]
- The write-path rule, its two branches and its `extra_predecessors` parameter. [2]
- The batch-aware caller that supplies the declared edges, and the only caller that does. [3]
- The membership query, which is not the write rule. [4]
- The post-insert graph construction the guard reasons over, which folds the wider edges in as stored ones. [5]
- The Tarjan classification and its reason for not being a recursive CTE. [6]
- The two edges queries, one per lineage graph. [7]
- The invariant-side application, which states the rule once above the guard and uses the default wider-edge set. [8]
- The family-side application, which reuses this rule rather than restating it. [9]
- The batch pass that gathers the declared edge sets and hands them to this module's rule. [10]
- The batch pass that gathers the declared edge sets and hands them to this module's rule. [11]
- The spy node that asserts the shared rule is reached carrying the batch's declared edges, and the nodes that fail when the rule is neutered or the wider edges are emptied. [12]
- The two-branch refusal wording, shared so the relations cannot describe different rules. [13]
- The membership query the store still exposes, delegating to this module. [14]
- The declared predecessor tables this module reads. [15]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
