# mcp/tests/test_knowledge_family_composition.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

The composition leaf's **unit-regression suite** for generation 5 and the authored record group:
eighteen cases covering the closed command union, the value-boundary policy validation, the appended
generation, a dataset that predates the composition tables, the authored edge and its immutability,
the declared unique tuple, the revision-altitude owning route, the explanatory context, and the one
shared cycle rule applied at both check levels.

Every case protects a clause of `KS-R17@v1` §1 through §6 and §9. The suite's load-bearing cases are
the ones that would catch a **silent widening** rather than a crash:

- an endpoint that could hold an invariant revision or an arbitrary record (**unrepresentable**, not
  merely rejected);
- a relationship inferred from a path, a label or a shared member;
- a silent second cycle rule beside the shared one;
- a policy that widens without a bound or a named scope;
- a context that rewrites the guarantee or is edited in place.

The module is registered as a **unit-regression** row in `mcp/tests/test-evidence-lanes.toml` and as
a **consumer** of three registered evidence contracts in `mcp/tests/evidence-lifecycle.toml`
(`knowledge-facet-cases`, `knowledge-generation-cases` and `knowledge-read-scope-cases`). It builds
its admitted candidate through the existing shared support modules — it adds **no** new fixture, no
new contract and no new artifact, so the catalogue's counts stay at **13 contracts / 54 artifacts**.

## Code Commentary

### Logic

- The **generation case** asserts `CURRENT_GENERATION is GENERATION_5`,
  `descends_from(GENERATION_5, GENERATION_4, GENERATION_4.tables)` and the six appended names **by
  name**, so a renumber is a rename in that case too rather than a rewrite.
- The **predating-dataset case** creates genuine generation-2 and generation-4 stores through their
  own recorded DDL and refuses a composition write against them; it uses
  `create_recorded_generation_store` with the registry's own constants, so the created-generation
  assertion follows the registry rather than a literal.
- The **union case** asserts the four command kinds and the six record tables from the leaf's own
  published constants, and that the six tables declare no content-address column.
- The **cycle cases** drive the shared rule at both check levels and assert that **no second walk and
  no `WITH RECURSIVE`** exists in any composition DDL.
- The **immutability case** drives three tables and five statements past the write path and proves the
  database refuses them.

### Conventions

- Hermetic: temporary directories and in-process APSW databases driven through the real admitted
  destination — no integration marker, no repository working tree, no subprocess — which is why the
  default unit lane is this module's behaviour-preserving classification.
- **Always run with `-o "filterwarnings=ignore"` on this host**: without it five modules fail to
  collect because `DeprecationWarning: The anyio.abc.BlockingPortal alias is deprecated` is raised as
  an error. That is a pre-existing, documented host condition, not this leaf's.
- Preservation comparisons are made **by value and by digest**, never by inspection.

### Invariants And Boundaries

- **No case deletes, skips, deselects or weakens a shipped assertion.** The two shipped assertions
  this leaf touched live in `test_knowledge_facets.py` and were re-scoped upward, not loosened.
- **The suite governs no durable artifact**: it creates no fixture, generator, recording or migration
  proof, and it carries no catalog row of its own.
- **Boundary.** The retrieval-read boundary and the projection cases are the sibling module's; this
  one owns the write shape and the generation.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- **The generation case: the six appended names, `descends_from` against generation 4, and the created generation.** [1]
- **The case that opens genuine generation-2 and generation-4 datasets and refuses a composition write against them — no migration path exists.** [2]
- **The case that proves a wrong endpoint kind is unrepresentable rather than merely rejected, and that the DDL carries exactly two family-revision keys and no target column.** [3]
- The case that pins the union's membership from the leaf's published constants. [4]
- **The case that drives three authored tables past the write path and proves the database refuses an update and a delete.** [5]
- **The case that proves the one shared rule judges the composition graph at both check levels, rolling back with its revision ids.** [6]
- **The case that asserts no second cycle walk and no recursive CTE exists beside the shared rule.** [7]
- The case that proves a context whose subject is not a family revision is refused. [8]
- The case that proves an edge with no declared policy is stored, readable and not traversable. [9]
- The lane row this module is registered under, and the unit ceiling it is measured against. [10]
- The one contract whose consumer list this module joined for its admitted candidate. [11]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
