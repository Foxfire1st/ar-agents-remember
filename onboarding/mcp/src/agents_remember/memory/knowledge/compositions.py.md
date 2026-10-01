# mcp/src/agents_remember/memory/knowledge/compositions.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

The **authored composition edge** between two exact family revisions, the **canonical owning route**
of a family *revision*, and the **authored explanatory context** with its append-only revision chain.
One module, three authored acts, all of them writes into generation 5's six tables.

The module owns the write path and the reads that answer "what did somebody author here". It does
**not** own the traversal policy (`composition_policies.py`), the declared-policy walk
(`composition_traversal.py`), the Family projection (`family_view.py`) or the cycle rule
(`lineages.py` supplies edges to the shared rule in `lineage.py`). That split is by protected
property, not by size: the edge, the route and the context share one preconditions-and-receipts
shape, while the policy and the traversal are different questions asked about the same edges.

**The edge is authored, never inferred.** There is no code here that derives a relationship from a
display label, a folder or path ancestry, a prefix, a symbol, a shared member, a shared anchor or a
prose sentence. Two endpoints are typed columns with repository-scoped composite foreign keys to
`family_revision(repository_id, revision_id)`, so a wrong endpoint kind is *unrepresentable* rather
than merely rejected, and there is deliberately no polymorphic `(target_kind, target_id)` column and
no `related_to` for an unchecked identity to land in.

## Code Commentary

### Logic

- `insert_composition` — the one write of an edge. It resolves both endpoints against the stored
  family revisions, refuses an endpoint this namespace does not hold **before any row is written and
  with the offending identity named**, and then inserts under the declared unique tuple. The
  duplicate lookup runs first, so a second bare edge is refused with a typed refusal before either
  partial unique index is reached.
- `find_composition_by_pair` and `composition_links_of_revision` — the two reads of the edge. The
  second returns every link of one revision *in declared order*, and it reports **both** rows when one
  pair carries two different declared policies: two separately authored meanings are two rows, and
  neither is silently preferred.
- `insert_family_revision_route` — records the canonical owning route of the revision aggregate.
  `require_route_endpoint` validates that the route is authored in this namespace, so a route that
  does not exist refuses **before** the association is written. This is the *revision* altitude, a
  different fact from generation 2's identity-level `family_route`.
- `owning_route_of_family_revision` — returns the recorded route, or `None` for the explicit
  **ungoverned** state. It never defaults to the repository root, to the identity's own route, or to
  a route derived from where the members live.
- `insert_context_revision`, `get_context_revision`, `context_of_family_revision` — the authored
  explanatory context. Its subject is bound exactly (both the family identity and the family
  revision), a successor's predecessor must already be stored, and `get_context_revision` is the read
  that returns the **earlier** text after a successor appends. The context is separable from the
  seal: no column here could hold a joint guarantee, and editing the context never rewrites one.
- `composition_row_digest`, `owning_route_row_digest`, `context_row_digest` — the row digests the
  receipt surfaces compare by value. They identify **authored rows**, not content: the context
  itself carries no content address, no logical fingerprint and no digest of its own.

### Conventions

- Every write goes through the batch path, and every modelled failure is returned as a typed
  `KnowledgeRefusal`, never raised as a bare exception for a caller to interpret.
- Authorship travels as an encoded provenance envelope on every row; a row with no provenance is not
  representable.
- Immutability is enforced twice on purpose: the operation's preconditions return the typed refusal,
  and generation 5's triggers raise `immutable_revision:` so a changeset, a repair script or a future
  code path that forgot the rule still cannot repoint or delete a row.

### Invariants And Boundaries

- **An authored row is immutable.** There is no update and no delete path here; a correction is a
  **new** edge, a new route record or a newly identified context revision. The earlier text survives
  the correction.
- **One pair under one declared policy version is stored once.** A second *policy* over the same pair
  is a second row and is reported as such. The unique tuple is two partial unique indexes rather than
  one table `UNIQUE`, because a table constraint over the nullable `policy_id` would not enforce
  uniqueness for `NULL`s.
- **The context is not a hiding place for an obligation.** A condition read as context is a review
  finding, and no read here performs that reading; the boundary is stated in the module and in
  `models/knowledge/composition.py`.
- **No row here carries task status, seat ownership, a lifecycle gate or approval authority**, so
  nothing in this module becomes an independently editable competing contract.
- **Boundary.** This module writes and reads authored rows. It does not decide whether the composition
  graph is acyclic — that is the shared rule's job, fed by `lineages.composition_edges` — and it does
  not walk edges under a policy.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The one composition-edge write, which resolves both endpoints and names the offending identity in its refusal. [1]
- **The duplicate lookup that refuses a second row for the same declared tuple before either partial unique index is reached.** [2]
- **The read that reports every stored link of one revision in declared order, including two policies over one pair.** [3]
- The revision-altitude owning-route write, which refuses a route this namespace does not hold. [4]
- **The owning-route read that returns the explicit ungoverned state rather than inferring a route.** [5]
- The context write, whose subject is bound to the exact family revision and whose predecessor must already be stored. [6]
- **The read that returns the earlier context text after a successor appends.** [7]
- The read the projection uses for one revision's recorded context. [8]
- The edge fingerprint the receipt surface compares, which is an authored-row identity and not a content address on the context. [9]
- **The case that drives three tables past the write path and proves no update and no delete exists.** [10]
- **The case that proves both policy rows over one pair are reported and neither is preferred.** [11]
- The case that proves a recorded route governs and the ungoverned state is reported rather than filled. [12]
- The case that proves the context is bound to the exact revision and a successor appends without rewriting the guarantee. [13]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
