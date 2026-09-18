# mcp/src/agents_remember/memory/knowledge/routes.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/routes.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-17T19:11+00:00 |
| lastVerifiedCommitHash | `7b1db4e0d73a321ee49df8725f5fe75846cf6c2b` |
| lastVerifiedCommitDate | 2026-09-18T13:43:14+02:00|
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**`Route` as an operable scope axis.** This module owns the two rules that make a route a real scope
rather than a table — the normalised confined path and the acyclic parent hierarchy — and the three
operations that author a route, attach a governed row to one, and read back which route governs it.

The entity is only the detection scope axis if records and anchors can actually be associated with the
route that governs them: a route with no attached rows names a scope nothing is in. Before this leaf
`Route` was generation-2 DDL plus a primary-key constraint and nothing could author one; this module
is the authored side, and `find_governing_route` is the read side.

## Code Commentary

### Logic

**Confinement — `normalize_route_path(path)` → the admitted path or a refusal.**
It accepts any object (a non-string is refused first), then walks `_CONFINEMENT_RULES`, a nine-entry
rule table of `(detail, predicate)` pairs, and returns a refusal for the **first** rule it breaches:
nonempty repository-relative POSIX path; no NUL; forward separators only; no drive letter; no UNC or
network form; not absolute; no trailing separator; already in normalised form; no empty or dot
segment and no traversal outside the repository. A path that satisfies every rule is returned
**unchanged**.

Normalisation is not repair. `posixpath.normpath` is used as a *comparison* against a path that is
already confined, and a path that would need normalising to become confined is refused rather than
silently rewritten — rewriting is how two spellings become one route while a caller believes it
authored two. The rule table is a table rather than an if-ladder because the rule *is* the reason, so
a new refused form is a new entry instead of a tenth branch through a guard sequence.

**Acyclicity — `require_acyclic_routes(connection, repository_id)` → `None` or one refusal.**
It runs a `UNION`-deduplicated recursive CTE over parent → child, anchored on the **edge**
`(route_id, parent_route_id)` and stepping node → parent, and returns `None` for an acyclic
hierarchy. The anchor is one row per *edge* and not per route: an anchor of `(route_id, route_id)`
would satisfy `start = node` for every route and report a cycle on a perfectly acyclic hierarchy —
that was the first implementation of this walk and it false-positived on a chain.

Two bounds are deliberate. The one-node cycle is caught by the table's own
`CHECK (parent_route_id <> route_id)`; this walk catches the longer one. And the walk runs **inside
the caller's transaction**, after the insertions and before the commit, so a cycle refuses the whole
batch rather than leaving a partial hierarchy.

**Authoring — `author_route(connection, repository_id, draft, authorship)` → the route id or a
refusal.** The order is the contract:

1. normalise the draft's path and return that refusal if it is refused;
2. look the admitted path up: if a route already exists for it, **return that existing id and write no
   second row** — this lookup is what keeps two spellings of one scope from producing two routes;
3. if a parent is named, require that the parent is authored in this repository, refusing
   `missing_expected_row` otherwise (an unauthored parent would join a hierarchy that does not exist);
4. insert the route with the caller's authorship as provenance;
5. run the acyclicity walk and **return** its refusal if there is one — the caller rolls back, this
   function does not;
6. otherwise return the draft's route id.

**Association — `set_governing_route(connection, repository_id, draft, authorship)` → `None` or one
refusal, and `find_governing_route(...)` → a route id or `None`.**
`_GOVERNED_TABLES` maps exactly three governed generation-1 entities to their join table and key
column: `source_anchor` → `source_anchor_route.anchor_id`, `invariant` → `invariant_route.invariant_id`,
`family` → `family_route.family_id`. The mapping is data rather than a branch, because the governed
row's key *is* the join table's primary key: "at most one governing route per governed row" is then a
constraint of the table rather than a check this function remembers to perform.

`set_governing_route` refuses, in order: a table that is not a governed entity (`invalid_reference`); a
route that is not authored (`missing_expected_row`); a governed row that is not stored
(`missing_expected_row`); and an already-governed row being pointed at a **different** route
(`relationship_constraint`). Re-stating the *same* association is idempotent and returns `None`.
`find_governing_route` returns the governing route's id, or `None` for an explicitly ungoverned row:
`None` is a fact, not a default, and it is never "the repository root".

**The existence question is public — `route_exists(connection, repository_id, route_id)` → `bool`.**
The private `_route_exists` this module already carried is the same function under its public name,
and `_route_exists` is kept as a one-line delegating alias so no existing caller moves. It is public
because the writer that needs it now lives in another module: a facet write that records a
*governing* route has to answer this question before it stores the governed row, where a named route
that does not exist is a dangling reference to refuse and `None` is the different fact —
the explicit ungoverned state requirement 4.4 permits. The body is the same `_ROUTE_BY_ID` lookup it
always was, so the rename publishes a question and adds no new way to decide membership.

### Conventions

- Expected failures are **returned `KnowledgeRefusal` values, never raised** — every guard in this
  module is a value the caller branches on. The `lineage_cycle` path in particular relies on the
  caller's rollback: the walk reports the cycle, the caller discards the batch.
- The operation name carried by a refusal is the operation that *failed*, and the wrapper's own
  refusals use `AUTHOR_ROUTE_OPERATION` / `GOVERNING_ROUTE_OPERATION`. The path-confinement and cycle
  refusals keep the module's base `ROUTE_OPERATION` because they describe the route rule rather than
  the wrapper call.
- Every refusal names a next action that a caller can act on (spell the path as a normalised
  repository-relative path; author the parent route first; author the governed row first; remove the
  existing association before naming another route).
- Request objects are frozen dataclasses — `RouteDraft(route_id, path, parent_route_id=None)` and
  `GoverningRouteDraft(governed_table, governed_id, route_id)` — so an authored route or association
  is a value rather than six positional arguments.
- `_GOVERNED_TABLES` and `_CONFINEMENT_RULES` are private rule/data tables; the module exposes the
  operations, not the tables.

### Invariants And Boundaries

- **Scope is never inferred.** Nothing here derives route membership from a name, a folder ancestry, a
  path prefix or a symbol string. The path is a declared input; comparing a stored anchor path against
  it is a resolution fact a caller may compute, and it is not authored membership. A path prefix is
  never a relationship.
- **Two spellings of one path must not produce two routes**, which is why the admitted-path lookup
  precedes the insert and why an unnormalised spelling is refused rather than repaired.
- **A cycle refuses the whole batch.** No partial hierarchy is stored, and this module never commits
  or rolls back on its own — the caller's transaction boundary owns that.
- **A governed row names at most one governing route**, enforced by the join table's primary key. A
  different route for an already-governed row is refused, never silently overwritten. The generation-2
  triggers (`*_route_no_repoint`) are the backstop that keeps a changeset or a repair script from
  bypassing this.
- **An unknown table is not silently associable.** The write side refuses a non-governed table by name.
- **Boundary.** This module does not own the `route` table's DDL or its triggers (`schema_v2.py`
  declares them), does not own generation selection (`schema_generations.py`), and does not decide
  which generation a dataset is. It does not create a route table, run a migration or alter any
  generation-1 table.
- **Known gap, recorded rather than implied.** Requirement 4.2's confinement rule names "no escaping
  symlink at resolution", and the module docstring repeats it, but no symlink resolution exists here:
  the refused forms are lexical. Whether resolution belongs at authoring time or at comparison time is
  open, and a reader must not assume the code checks it.

### Todos

- `find_governing_route` returns `None` both for "this row has no governing route" and for "this table
  is not a governed entity", so a caller cannot distinguish the two from the return value alone. The
  write side does distinguish them. Whether the read side should is an open question for the leaf that
  first consumes the read.
- The confinement rule's symlink clause has no implementation (see Invariants And Boundaries).

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The confinement rule table: nine refused forms, first breach wins, and an admitted path returned unchanged. | `normalize_route_path` | mcp/src/agents_remember/memory/knowledge/routes.py:75-89 |
| The recursive-CTE acyclicity walk, anchored on the edge rather than the route, returning `None` or one `lineage_cycle` refusal. | `require_acyclic_routes`; `lineage_cycle` | mcp/src/agents_remember/memory/knowledge/routes.py:93-145 |
| The write layer's two request objects. | `RouteDraft` | mcp/src/agents_remember/memory/knowledge/routes.py:171-179 |
| Route authoring: normalise, return an existing route for an already-authored path, refuse an unauthored parent, insert, then check the hierarchy inside the caller's transaction. | `author_route` | mcp/src/agents_remember/memory/knowledge/routes.py:225-279 |
| The read side of the association, and why `None` is a fact rather than a default. | `find_governing_route` | mcp/src/agents_remember/memory/knowledge/routes.py:306-352 |
| The governed-entity map — three generation-1 entities, one join table and key column each — and the four refusals plus the idempotent re-statement. | `_GOVERNED_TABLES` | mcp/src/agents_remember/memory/knowledge/routes.py:200-204 |
| The `route` table the walk reads: repository-relative `path`, self-referencing deferred parent, one-node cycle `CHECK`, rebind and delete triggers. | `path`; `CHECK` | mcp/src/agents_remember/memory/knowledge/schema_v2.py:103-204 |
| The three join tables whose primary keys make "at most one governing route per governed row" a constraint. | `APPENDED_PRIMARY_KEYS`; `source_anchor_route` | mcp/src/agents_remember/memory/knowledge/schema_v2.py:81-88 |
| The envelope's nullable governing route, so a record is scoped through the same route entity. | `knowledge_record` | mcp/src/agents_remember/memory/knowledge/schema_v2.py:53-62 |
| The shipped lineage-cycle technique this walk follows, and the confinement rule it implements. | `find_lineage_cycle` | mcp/src/agents_remember/memory/knowledge/store.py:665-680 |
| The authorship codec whose encoded value is stored as each route's and association's provenance. | `encode_authorship` | mcp/src/agents_remember/memory/knowledge/records.py:70-71 |
| The route operations in the shipped operation vocabulary. | `KnowledgeOperation` | mcp/src/agents_remember/models/knowledge/result.py:36-78 |
| The eighteen cases covering authoring, idempotence, refusal and the cycle rollback. | `test_a_confined_path_is_authored_and_its_identity_returned` | mcp/tests/test_knowledge_routes.py:1-199 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. A route's code-path scope is a
repository-relative scope, not a machine location: `Repository` remains the authority home, and a
local checkout path is environment configuration that never becomes portable identity.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T10:45:13+00:00: Generated citation repair: `_GOVERNED_TABLES` repointed to mcp/src/agents_remember/memory/knowledge/routes.py:200-204. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T01:18+02:00 — 260915-KS-L11 curator (uncommitted change set on `ar/260915-ks-l11`, base `4904e08f`): recorded the leaf's one change to this module: `_route_exists` became the public `route_exists` with the docstring that says why the question is asked from outside, and `_route_exists` remains as a one-line delegating alias. The body states what a reader must not infer from the rename — the lookup is the same `_ROUTE_BY_ID` statement, so the module publishes a question rather than new authority — and names the caller that needs it: the facet write path's governing-route reference check, which must answer it before storing a governed row while `None` stays the explicit ungoverned state. Verification metadata is **not** advanced: the code commit does not exist yet and closeout owns the stamp.
- 2026-09-17T19:11+00:00 — 260915-KS-L10 curator (uncommitted change set on `ar/260915-ks-l10`, base `420669c4`): created this one-to-one card for the route write layer. The leaf's first attempt delivered the `route` table and its constraint but no operation that could author a route or attach a governed row to one, which left `Route` as a constraint rather than a scope axis; this card records the authored side that closed that gap. It records the nine-entry confinement rule table with normalisation-as-comparison rather than repair, the acyclicity walk anchored on the edge (an anchor on the route false-positived on an acyclic chain), the ordering inside `author_route` that returns an existing route for an already-authored path, the three governed entities and why the join table's primary key makes "at most one governing route" a constraint, `None`-is-a-fact on the read side, and the two recorded gaps: the unimplemented symlink clause of the confinement rule and the read side's inability to distinguish "ungoverned" from "not a governed entity". Verification metadata stays at the last real commit: the code commit does not exist yet and closeout owns that stamp.
