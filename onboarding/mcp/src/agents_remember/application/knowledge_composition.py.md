# mcp/src/agents_remember/application/knowledge_composition.py

## Governing Overview

[application route overview](overview.md)

## Purpose

**The fifth read-only application seam**, beside `knowledge_read`, `knowledge_snapshot`,
`knowledge_merge` and `knowledge_export`. It admits a dataset path and a repository namespace, opens
the database **read-only**, and delegates to the two memory modules that own the acts:

- `follow_family_composition` — the declared-policy traversal, under one declared policy version,
  bounded by that version's declared depth bound;
- `family_view` — the Family projection, which reports the recorded links, the canonical owning route
  or the explicit ungoverned state, and the authored explanatory context.

**The traversal is a read, not a write, and it is not the retrieval read.** Following composition
edges is a different operation from `read_knowledge_scope`: this seam does not touch that function,
its selection policy or its advertised frontier. A caller that wants the recorded-scope selection
asks for that operation; a caller that wants declared composition edges followed asks for this one.

## Code Commentary

### Logic

- `follow_family_composition` — resolves the policy version, walks the declared edges and returns a
  `CompositionTraversalResult`. A traversal that cannot be reported as a **complete** scope — an
  unknown policy, a not-permitted edge, a step past the declared bound — returns the refusal rather
  than a truncated scope, because a truncated traversal reported as a scope would be a false
  statement about what was reached.
- `family_view` — returns a `FamilyViewResult` whose state is `reported` or `refused`. A family
  revision this namespace does not hold is **refused rather than reported empty**: an empty report
  would be indistinguishable from a revision that genuinely records nothing.
- `open_read_only_store` — the one open path. The connection is the shipped
  `open_read_only_database` handle, whose strongest available statement is a `SELECT`, and the schema
  is validated against the generation **the file declares**, exactly as every other open path does.
- `_as_refusal` — converts a modelled `KnowledgeRefused` into its typed refusal and lets anything
  else propagate, so a defect is never reported as an expected state.

### Conventions

- Every function opens through `open_read_only_store` inside a `with` block, so no read leaves a
  connection open and no caller can reach a writable handle by accident.
- **Every modelled failure is a typed refusal, not an exception**: an unknown policy identity or
  version, a not-permitted edge, a step past the declared bound and a family revision this namespace
  does not hold are all returned as `KnowledgeRefusal` values inside the result.
- `__all__` publishes the two operations and their two value types; nothing else in the module is
  part of the seam's surface.

### Invariants And Boundaries

- **Read-only, so a refusal persists nothing.** "A refused traversal changed nothing" is a property
  of the handle rather than a rollback this code remembers, and the boundary case asserts the file's
  bytes are identical before and after a refusal.
- **Two axes stay separate.** Axis A is the retrieval selection; axis B is the registered review
  scope. Conflating them is the defect this seam exists to prevent, and the case states the boundary
  as one measurement: running the traversal moves nothing about what the retrieval read selects.
- **The seam owns no semantics.** It carries values; the traversal and the projection own the rules.
- **Boundary.** Writing an edge, a policy, a route or a context is the candidate batch's path through
  `memory/knowledge/compositions.py`; this module is read-only and has no write path at all.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- **The read-only open path, whose handle is the shipped `open_read_only_database` connection and whose schema is the one the file declares.** [1]
- **The traversal seam: it carries `follow_family_composition` as its own operation and returns a refusal rather than a truncated scope.** [2]
- **The projection seam: a family revision this namespace does not hold is refused, not reported empty.** [3]
- The traversal result type carrying the state, the seed and the refusal or the scope. [4]
- The published seam surface: two operations and their two value types. [5]
- **The case that asserts the seam is read-only, carries its own operation, and moves no selection.** [6]
- The case that proves the shipped read never consults the composition table, which is the other half of the axis separation. [7]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
