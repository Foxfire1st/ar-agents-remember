# mcp/src/agents_remember/memory/knowledge/composition_traversal.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

The **read-side successor**: follow declared composition edges from one family revision under one
declared policy version, bounded by that version's declared depth bound, reporting the policy
identity and version it executed under.

**This is a different operation from the retrieval selection, not a flag on it.** The two live on
different axes:

- **Axis A** is the retrieval selection — what one snapshot read selects for a seed, its counts, its
  ordering, the revision groups it forms and the frontier it advertises. **This module does not touch
  it.** The shipped read does not consult the composition table at all, and a case in the boundary
  module asserts that no shipped read path does.
- **Axis B** is the registered review scope: declared edges followed under a versioned traversal
  policy. This module supplies the traversal semantics and the policy checks; the scope itself is
  built by a later leaf.

A card that describes composition edges as being followed **as part of the retrieval selection** is
false. Nothing here widens, reorders or reinterprets the selected set, and the selection policy is
unchanged by this leaf.

## Code Commentary

### Logic

- `follow_composition_scope` — the one traversal. It resolves the declared policy version first
  (through `composition_policies.require_declared_policy`, so an unknown identity and an unknown
  version are refused by name), then walks the declared edges in the declared direction up to the
  declared bound, and returns a `CompositionScope` carrying the reached set, the depth reached, and
  the policy identity and version.
- `TRAVERSAL_OPERATION` — the one operation name this module carries,
  `follow_family_composition`. It is **its own member of the operation vocabulary** because
  following declared edges under a versioned policy is not a retrieval selection; it is not a
  variant of `read_knowledge_scope`.
- `CompositionScope` — the value type. It reports what was reached under which declared policy
  version, so a result is never readable as one produced under another version.

**Four refusals are structural rather than incidental**, and each names the policy identity, its
version and the edge or bound it reached:

1. an **unknown policy identity or version** — never resolved to a default or to the only version
   stored;
2. a policy that **widens a scope this build does not register** — a policy may add scope to a
   *named* scope and nothing else;
3. an edge encountered under a policy that **does not permit following it** — an edge whose own
   declared policy is absent, of another identity, or of another version is not followable, and the
   traversal refuses rather than stepping around it silently;
4. a traversal that would **exceed its declared bound** — refused, never truncated, because a
   truncated traversal reported as a scope would be a false statement about what was reached.

### Conventions

- Widening is **monotone and additive by construction**: the walk only ever *adds* revisions to the
  reached set, in the declared direction, and it never removes, reorders or reinterprets anything a
  caller already held.
- Every modelled failure is a typed `KnowledgeRefusal` carrying the facts above; the caller reads a
  refusal rather than catching an exception.
- The module reads through `compositions` and `families` and never writes: it has no insert, no
  update and no delete.

### Invariants And Boundaries

- **One cycle rule, one walk.** This module contains no cycle check of its own. The composition
  graph is judged by the shipped shared lineage rule, fed by `lineages.composition_edges`; a case
  asserts that **no second cycle walk exists** beside it, and a second rule would make drift possible
  between three graphs instead of two.
- **The traversal is not the retrieval read, and it does not import it.** `family_view.py` never
  imports this module, and this module never touches the selection policy or the advertised frontier.
- **A refused traversal persists nothing.** The application seam opens the database read-only, so
  "a refusal changed nothing" is a fact about the handle rather than a rollback this code remembers.
- **Boundary.** This module follows edges; it does not decide which edges exist
  (`compositions.py`), what a policy is (`composition_policies.py`), or what the Family projection
  reports (`family_view.py`).

### Todos

None recorded. The registered-review-scope construction is a later leaf's; this module supplies the
traversal semantics that construction consumes.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- **The one traversal: policy resolved first, then the bounded declared-direction walk.** [1]
- **The traversal's own operation member, which is a different operation from the retrieval selection rather than a variant of it.** [2]
- The result value carrying the reached set, the depth reached and the policy identity and version it executed under. [3]
- The third edge source that feeds the shared cycle rule, so this module needs no walk of its own. [4]
- **The case that proves no second cycle walk or recursive CTE exists beside the shared rule.** [5]
- **The case that proves a traversal under a declared policy reports its version and widens nothing else.** [6]
- **The case that proves a traversal past its declared bound is refused, not truncated.** [7]
- **The case that proves the shipped read never consults the composition table.** [8]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
